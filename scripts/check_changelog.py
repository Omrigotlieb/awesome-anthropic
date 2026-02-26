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
    """
    Extract changelog entries from the Anthropic docs page.

    Strategy: split the full text on date patterns (e.g. "February 19, 2026")
    and treat each block as one changelog entry. This is robust against
    JavaScript-rendered pages where the DOM structure may vary.
    """
    import re

    import re as _re

    soup = BeautifulSoup(html, "lxml")
    # Clean up inline elements to avoid word-splitting artifacts
    for tag in soup.find_all(["a", "code", "em", "strong", "span"]):
        tag.replace_with(tag.get_text())
    full_text = soup.get_text(" ")
    # Collapse excessive whitespace while preserving paragraph breaks
    full_text = _re.sub(r"[ \t]+", " ", full_text)
    full_text = _re.sub(r"\n{3,}", "\n\n", full_text)

    date_pattern = (
        r"((?:January|February|March|April|May|June|July|August|September|"
        r"October|November|December)\s+\d{1,2},\s+20\d\d)"
    )
    parts = re.split(date_pattern, full_text)

    entries = []
    for i in range(1, len(parts) - 1, 2):
        raw_date = parts[i].strip()
        content = parts[i + 1].strip()[:1200]

        # Skip blocks that are clearly navigation noise (short or no sentences)
        if len(content) < 50 or "." not in content[:200]:
            continue

        try:
            parsed_date = datetime.strptime(raw_date, "%B %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            parsed_date = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

        # Use the first sentence as the title
        first_line = content.split("\n")[0].strip()
        title = (first_line[:80] + "...") if len(first_line) > 80 else first_line

        entries.append(ChangelogEntry(date=parsed_date, title=title, content=content))

    return entries[:20]  # Most recent 20 entries


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
    """Format as '## Month D, YYYY — Title' to match the JS parseChangelog parser."""
    try:
        human_date = datetime.strptime(entry.date, "%Y-%m-%d").strftime("%B %-d, %Y")
    except ValueError:
        human_date = entry.date
    title = entry.title.rstrip(".")
    lines = [f"## {human_date} — {title}", ""]
    lines.append(entry.content.strip())
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def write_changelog(entries: list[ChangelogEntry]) -> None:
    """Fully replace changelog content (hash check ensures this only runs when changed)."""
    DOCS_DIR.mkdir(exist_ok=True)
    path = DOCS_DIR / "CHANGELOG.md"
    synced_at = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    header = (
        "# Anthropic Changelog\n\n"
        f"> Auto-synced from [{CHANGELOG_URL}]({CHANGELOG_URL})."
        f" Updated {synced_at}\n\n---\n\n"
    )
    body = "\n".join(format_entry(e) for e in entries)
    path.write_text(header + body)


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
