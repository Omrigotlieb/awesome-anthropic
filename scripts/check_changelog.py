#!/usr/bin/env python3
"""
check_changelog.py - Monitors the Anthropic changelog for new entries.

Fetches https://docs.anthropic.com/en/release-notes/overview, detects changes
using SHA-256 hashing, and writes new entries to docs/CHANGELOG.md.

Writes 'true' or 'false' to /tmp/changelog_changed.txt for GitHub Actions output.

Usage:
  python scripts/check_changelog.py
  python scripts/check_changelog.py --dry-run
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
CHANGELOG_URL = "https://docs.anthropic.com/en/release-notes/overview"


@dataclass
class ChangelogEntry:
    date: str
    title: str
    content: str

    def to_hash(self) -> str:
        payload = f"{self.date}|{self.title}|{self.content}"
        return hashlib.sha256(payload.encode()).hexdigest()[:16]


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def fetch_changelog_html() -> str:
    with httpx.Client(timeout=30, follow_redirects=True) as client:
        resp = client.get(
            CHANGELOG_URL,
            headers={"User-Agent": "awesome-anthropic-bot/1.0 (+https://github.com/Omrigotlieb/awesome-anthropic)"},
        )
        resp.raise_for_status()
        return resp.text


def parse_entries(html: str) -> list[ChangelogEntry]:
    """Extract changelog entries from the Anthropic docs page."""
    soup = BeautifulSoup(html, "lxml")
    entries = []

    # The Anthropic docs page uses heading elements for dates/versions
    # Try multiple selector strategies for robustness
    main = soup.find("main") or soup.find("article") or soup.body
    if not main:
        return entries

    # Look for date-like headings (h2, h3) followed by content
    headings = main.find_all(["h2", "h3"])
    for heading in headings:
        title = heading.get_text(strip=True)
        if not title:
            continue

        # Collect content until next heading
        content_parts = []
        sibling = heading.find_next_sibling()
        while sibling and sibling.name not in ("h2", "h3"):
            text = sibling.get_text(separator="\n", strip=True)
            if text:
                content_parts.append(text)
            sibling = sibling.find_next_sibling()

        content = "\n".join(content_parts)[:1000]
        if not content:
            continue

        # Try to extract a date from the title or surrounding context
        date = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
        # Simple heuristic: look for "Month DD, YYYY" pattern in the title
        import re
        date_match = re.search(
            r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}",
            title,
        )
        if date_match:
            try:
                date = datetime.strptime(date_match.group(), "%B %d, %Y").strftime("%Y-%m-%d")
            except ValueError:
                try:
                    date = datetime.strptime(date_match.group(), "%B %d %Y").strftime("%Y-%m-%d")
                except ValueError:
                    pass

        entries.append(ChangelogEntry(date=date, title=title, content=content))

    return entries[:20]  # Limit to most recent 20


def compute_page_hash(entries: list[ChangelogEntry]) -> str:
    combined = "".join(e.to_hash() for e in entries)
    return hashlib.sha256(combined.encode()).hexdigest()


def load_last_hash() -> str:
    path = DATA_DIR / "last_changelog_hash.txt"
    if path.exists():
        return path.read_text().strip()
    return ""


def save_hash(h: str) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    (DATA_DIR / "last_changelog_hash.txt").write_text(h)


def format_entry(entry: ChangelogEntry) -> str:
    lines = [f"### {entry.date}: {entry.title}", ""]
    lines.append(entry.content)
    lines.append("")
    return "\n".join(lines)


def write_changelog(entries: list[ChangelogEntry]) -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    path = DOCS_DIR / "CHANGELOG.md"
    synced_at = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    new_block = "\n".join(format_entry(e) for e in entries)

    if path.exists():
        existing = path.read_text()
        # Prepend new entries after the header
        header_end = existing.find("\n\n") + 2
        if header_end < 2:
            header_end = len(existing)
        content = existing[:header_end] + new_block + "\n---\n\n" + existing[header_end:]
    else:
        header = (
            "# Anthropic Changelog Mirror\n\n"
            f"> Auto-synced from [{CHANGELOG_URL}]({CHANGELOG_URL})\n"
            f"> Last sync: {synced_at}\n\n"
        )
        content = header + new_block

    path.write_text(content)


def update_readme_date() -> None:
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    text = readme.read_text()
    import re
    text = re.sub(r"<!-- CHANGELOG_DATE -->.*?(?=\n|$)", f"<!-- CHANGELOG_DATE -->{today}", text)
    readme.write_text(text)


def set_changed_output(changed: bool) -> None:
    Path("/tmp/changelog_changed.txt").write_text("true" if changed else "false")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("Fetching Anthropic changelog...", file=sys.stderr)
    try:
        html = fetch_changelog_html()
    except Exception as e:
        print(f"[changelog] Failed to fetch: {e}", file=sys.stderr)
        set_changed_output(False)
        return

    entries = parse_entries(html)
    if not entries:
        print("[changelog] No entries parsed.", file=sys.stderr)
        set_changed_output(False)
        return

    current_hash = compute_page_hash(entries)
    last_hash = load_last_hash()

    if current_hash == last_hash:
        print("[changelog] No changes detected.", file=sys.stderr)
        set_changed_output(False)
        return

    print(f"[changelog] Changes detected! {len(entries)} entries found.", file=sys.stderr)

    if not args.dry_run:
        write_changelog(entries)
        save_hash(current_hash)
        update_readme_date()

    set_changed_output(True)


if __name__ == "__main__":
    main()
