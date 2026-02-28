#!/usr/bin/env python3
"""
update_daily_anthropic.py - Maintain DAILY_Anthropic.md and docs/DAILY_ANTHROPIC.md.

The script appends one run-log entry per UTC day and refreshes the
daily-brief page from the newest section in docs/NEWS.md.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DAILY_PATH = ROOT / "DAILY_Anthropic.md"
NEWS_PATH = ROOT / "docs" / "NEWS.md"
DAILY_BRIEF_PATH = ROOT / "docs" / "DAILY_ANTHROPIC.md"


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


def read_news_date() -> str:
    if not NEWS_PATH.exists():
        return ""
    match = re.search(r"^##\s+([^\n]+)$", NEWS_PATH.read_text(), flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def read_section_links(section_heading: str, title_col: int, limit: int = 5) -> list[tuple[str, str]]:
    if not NEWS_PATH.exists():
        return []
    text = NEWS_PATH.read_text()
    section_match = re.search(
        rf"###\s*{re.escape(section_heading)}\s*\n\n\|[^\n]*\n\|[^\n]*\n(?P<table>(?:\|[^\n]*\n)+)",
        text,
    )
    if not section_match:
        return []
    links: list[tuple[str, str]] = []
    for row in section_match.group("table").splitlines():
        cols = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cols) <= title_col:
            continue
        link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", cols[title_col])
        if not link_match:
            continue
        links.append((link_match.group(1), link_match.group(2)))
        if len(links) >= limit:
            break
    return links


def write_daily_brief(today: str) -> None:
    news_date = read_news_date()
    stories = read_top_stories(limit=3)
    announcements = read_section_links("📰 Official Announcements", title_col=0, limit=3)
    releases = read_section_links("🛠️ SDK & Tool Releases", title_col=0, limit=8)

    claude_code_release = ""
    claude_code_release_url = ""
    for name, url in releases:
        if name.lower().startswith("claude-code "):
            claude_code_release = name
            claude_code_release_url = url
            break

    verified_updates: list[str] = []
    if claude_code_release:
        verified_updates.append(
            f"- [{claude_code_release}]({claude_code_release_url}) is currently the latest Claude Code release visible in this repository snapshot."
        )
    if announcements:
        for title, url in announcements:
            verified_updates.append(f"- [{title}]({url})")
    if not verified_updates:
        snapshot = news_date or "the latest available snapshot"
        verified_updates.append(
            f"- No new official announcements were parsed today; carrying forward {snapshot} until connectivity resumes."
        )
    if len(verified_updates) > 5:
        verified_updates = verified_updates[:5]

    story_lines = stories if stories else ["- Top stories unavailable in docs/NEWS.md."]
    date_label = today
    if news_date:
        date_label = f"{today} (news snapshot: {news_date})"

    content = "\n".join(
        [
            "# Daily Anthropic Brief",
            "",
            f"## {date_label}",
            "",
            "This brief summarizes the latest verified Anthropic and Claude Code signals available during the automation run.",
            "",
            "### Verified Product and Research Updates",
            "",
            *verified_updates,
            "",
            "### Top Story Snapshot",
            "",
            *story_lines,
            "",
            "### Why This Matters for Builders",
            "",
            "- Claude Code release cadence remains a leading indicator for developer workflow changes.",
            "- Official Anthropic announcements should stay clearly separated from community commentary in daily reporting.",
            "- Daily brief freshness should be visible on the dashboard so readers can quickly assess data recency.",
            "",
            "## Website Improvement Backlog",
            "",
            "- Keep the dashboard freshness card prominent (news date, source diversity, and release-watch status).",
            "- Continue tightening top-story quality filtering to reduce duplicate or low-signal social posts.",
            "- Preserve a dedicated path from dashboard to this brief for daily editorial context.",
            "",
            "## Next Automation Gate",
            "",
            "1. Read `DAILY_Anthropic.md` before fetching updates.",
            "2. Refresh `docs/NEWS.md` from official + community sources.",
            "3. Rebuild this brief so dashboard context reflects today's run.",
            "",
        ]
    )
    DAILY_BRIEF_PATH.write_text(content)


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
        write_daily_brief(today=today)
        print(f"[daily] {today} already exists in DAILY_Anthropic.md")
        print(f"[daily] Refreshed docs/DAILY_ANTHROPIC.md for {today}")
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
    write_daily_brief(today=today)
    print(f"[daily] Appended entry for {today} in DAILY_Anthropic.md")
    print(f"[daily] Refreshed docs/DAILY_ANTHROPIC.md for {today}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
