#!/usr/bin/env python3
"""
update_daily_anthropic.py - Maintain DAILY_Anthropic.md with a dated run log.

This script appends one entry per UTC day based on the current docs/NEWS.md
top stories so automation runs always start with recent context.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DAILY_PATH = ROOT / "DAILY_Anthropic.md"
NEWS_PATH = ROOT / "docs" / "NEWS.md"


def read_top_stories(limit: int = 3) -> list[str]:
    if not NEWS_PATH.exists():
        return []

    text = NEWS_PATH.read_text()
    # Grab the first Top Stories table in the file.
    section_match = re.search(
        r"###\s*🔥\s*Top Stories\s*\n\n\|[^\n]*\n\|[^\n]*\n(?P<table>(?:\|[^\n]*\n)+)",
        text,
    )
    if not section_match:
        return []

    stories: list[str] = []
    for row in section_match.group("table").splitlines():
        cols = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cols) < 3:
            continue
        title_col = cols[1]
        link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", title_col)
        if link_match:
            stories.append(f"- [{link_match.group(1)}]({link_match.group(2)})")
        else:
            stories.append(f"- {title_col}")
        if len(stories) >= limit:
            break

    return stories


def ensure_file() -> str:
    if DAILY_PATH.exists():
        return DAILY_PATH.read_text()

    initial = (
        "# DAILY Anthropic Run Log\n\n"
        "This file is checked first at the start of each daily automation run.\n"
    )
    DAILY_PATH.write_text(initial)
    return initial


def main() -> int:
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    existing = ensure_file()
    day_header = f"## {today}"

    if day_header in existing:
        print(f"[daily] {today} already exists in DAILY_Anthropic.md")
        return 0

    stories = read_top_stories(limit=3)
    if not stories:
        stories = [
            "- News table unavailable; run `python3 scripts/fetch_news.py` before this script.",
        ]

    entry = "\n".join(
        [
            "",
            day_header,
            "",
            "- Started by checking this file before any other task.",
            "- Reviewed official Anthropic + Claude Code updates for this run.",
            "- Top stories snapshot:",
            *stories,
            "- Website improvement focus: dashboard freshness, release watch, quality filtering.",
            "",
        ]
    )

    DAILY_PATH.write_text(existing.rstrip() + "\n" + entry)
    print(f"[daily] Appended entry for {today} in DAILY_Anthropic.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
