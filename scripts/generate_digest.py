#!/usr/bin/env python3
"""
generate_digest.py - Create a human-readable digest from accumulated news.

Reads docs/NEWS.md and docs/CHANGELOG.md, summarizes with Claude,
and prepends a "Weekly Digest" section to docs/NEWS.md.

Usage:
  python scripts/generate_digest.py
  python scripts/generate_digest.py --dry-run  # Print only, don't write
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS_DIR = ROOT / "docs"


def read_recent_news(max_items: int = 20) -> str:
    """Read recent items from NEWS.md as raw text."""
    path = DOCS_DIR / "NEWS.md"
    if not path.exists():
        return ""
    lines = path.read_text().splitlines()
    result, count = [], 0
    for line in lines:
        if line.startswith("- "):
            count += 1
            if count > max_items:
                break
        result.append(line)
    return "\n".join(result)


def read_recent_changelog(max_entries: int = 3) -> str:
    """Read recent entries from CHANGELOG.md."""
    path = DOCS_DIR / "CHANGELOG.md"
    if not path.exists():
        return ""
    lines = path.read_text().splitlines()
    result, count = [], 0
    for line in lines:
        if line.startswith("### "):
            count += 1
            if count > max_entries:
                break
        if count > 0:
            result.append(line)
    return "\n".join(result)


def generate_with_claude(news: str, changelog: str) -> str:
    """Use Claude to generate a structured weekly digest."""
    try:
        import anthropic
        import os
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise ValueError("No API key")

        client = anthropic.Anthropic()
        prompt = f"""You are maintaining an "awesome-anthropic" GitHub repository that tracks Anthropic news.

Based on the following recent news and changelog entries, write a concise weekly digest in Markdown format.

Structure your response as:
## Weekly Digest — {datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")}

### Top Stories
(3-5 bullet points of the most significant news)

### Product Changes
(What changed in Anthropic's products this week, from changelog)

### Community Highlights
(Notable community projects or discussions)

---

RECENT NEWS:
{news[:3000]}

RECENT CHANGELOG:
{changelog[:1500]}

Write the digest now. Be concise and developer-focused."""

        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text.strip()
    except Exception as e:
        print(f"[digest] Claude unavailable: {e}", file=sys.stderr)
        return generate_simple_digest(news, changelog)


def generate_simple_digest(news: str, changelog: str) -> str:
    """Fallback digest without Claude."""
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    lines = [f"## Weekly Digest — {today}", ""]
    if news:
        lines += ["### Recent News", "", news[:1000], ""]
    if changelog:
        lines += ["### Recent Changelog", "", changelog[:500], ""]
    return "\n".join(lines)


def prepend_digest(digest: str) -> None:
    path = DOCS_DIR / "NEWS.md"
    DOCS_DIR.mkdir(exist_ok=True)
    if path.exists():
        existing = path.read_text()
        header_end = existing.find("\n\n") + 2
        content = existing[:header_end] + digest + "\n\n---\n\n" + existing[header_end:]
    else:
        content = "# Anthropic News Archive\n\n" + digest + "\n"
    path.write_text(content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    news = read_recent_news()
    changelog = read_recent_changelog()

    if not news and not changelog:
        print("[digest] No content to digest.", file=sys.stderr)
        return

    print("[digest] Generating digest...", file=sys.stderr)
    digest = generate_with_claude(news, changelog)

    if args.dry_run:
        print(digest)
        return

    prepend_digest(digest)
    print("[digest] Digest written to docs/NEWS.md", file=sys.stderr)


if __name__ == "__main__":
    main()
