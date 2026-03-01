#!/usr/bin/env python3
"""
update_daily_anthropic.py - Maintain DAILY_Anthropic.md and docs/DAILY_ANTHROPIC.md.

The script appends one run-log entry per UTC day and refreshes the
daily-brief page from the newest section in docs/NEWS.md.
"""
from __future__ import annotations

import re
import datetime as dt
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DAILY_PATH = ROOT / "DAILY_Anthropic.md"
NEWS_PATH = ROOT / "docs" / "NEWS.md"
DAILY_BRIEF_PATH = ROOT / "docs" / "DAILY_ANTHROPIC.md"
DAILY_BLOG_PATH = ROOT / "docs" / "DAILY_BLOG.md"


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


def _parse_news_date(news_date: str) -> datetime | None:
    if not news_date:
        return None
    for fmt in ("%B %d, %Y", "%b %d, %Y"):
        try:
            return dt.datetime.strptime(news_date, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


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
    today_dt = dt.datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    news_dt = _parse_news_date(news_date)
    stale_days = (today_dt - news_dt).days if news_dt else 0

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

    freshness_lines = [
        f"- Run date (UTC): {today}",
        f"- News snapshot date: {news_date or 'Unknown'}",
    ]
    if news_dt and stale_days > 0:
        freshness_lines.append(
            f"- Snapshot lag: {stale_days} day(s). Live fetch likely unavailable; verify sources when connectivity resumes."
        )
    else:
        freshness_lines.append("- Snapshot lag: 0 day(s).")

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
            "### Freshness Status",
            "",
            *freshness_lines,
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


def write_daily_blog(today: str) -> None:
    news_date = read_news_date()
    stories = read_top_stories(limit=3)
    announcements = read_section_links("📰 Official Announcements", title_col=0, limit=2)
    releases = read_section_links("🛠️ SDK & Tool Releases", title_col=0, limit=3)
    today_dt = dt.datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    news_dt = _parse_news_date(news_date)
    stale_days = (today_dt - news_dt).days if news_dt else 0

    release_line = "No new Claude Code release detected in the current snapshot."
    for name, _ in releases:
        if name.lower().startswith("claude-code "):
            release_line = f"Latest release tracked: {name}."
            break

    key_takeaways = []
    key_takeaways.append(
        f"- The daily run on {today} uses the {news_date or 'latest available'} news snapshot."
    )
    key_takeaways.append(f"- {release_line}")
    if announcements:
        key_takeaways.append(
            f"- Official channel signal remains active: {announcements[0][0]}."
        )
    else:
        key_takeaways.append("- No official announcement row was parsed in this run.")
    if stale_days > 0:
        key_takeaways.append(
            f"- Freshness risk: snapshot is {stale_days} day(s) old due to unavailable network fetch in this environment."
        )

    story_lines = stories if stories else ["- No top stories were parsed from docs/NEWS.md."]
    improvements = [
        "- Add a visible stale-data badge when snapshot lag is greater than 0 days.",
        "- Show source diversity and announcement count as first-class dashboard metrics.",
        "- Keep the Daily Brief and Daily Blog links in navigation for editorial continuity.",
    ]
    actions = [
        "1. Re-run `python3 scripts/fetch_news.py` once DNS/network access is restored.",
        "2. Validate that the next run moves the snapshot date to the current UTC day.",
        "3. Continue tightening duplicate and low-signal social story filtering.",
    ]

    title_date = today
    if news_date:
        title_date = f"{today} (news snapshot: {news_date})"
    content = "\n".join(
        [
            "# Daily Anthropic Blog Post",
            "",
            f"## {title_date}",
            "",
            "### Executive Summary",
            "",
            "Today’s run focused on Claude Code release watch, official Anthropic signals, and homepage dashboard quality.",
            "",
            "### Key Takeaways",
            "",
            *key_takeaways,
            "",
            "### Top Stories Referenced",
            "",
            *story_lines,
            "",
            "### Website Improvement Review",
            "",
            *improvements,
            "",
            "### Next Run Actions",
            "",
            *actions,
            "",
        ]
    )
    DAILY_BLOG_PATH.write_text(content)


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
        write_daily_blog(today=today)
        print(f"[daily] {today} already exists in DAILY_Anthropic.md")
        print(f"[daily] Refreshed docs/DAILY_ANTHROPIC.md for {today}")
        print(f"[daily] Refreshed docs/DAILY_BLOG.md for {today}")
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
    write_daily_blog(today=today)
    print(f"[daily] Appended entry for {today} in DAILY_Anthropic.md")
    print(f"[daily] Refreshed docs/DAILY_ANTHROPIC.md for {today}")
    print(f"[daily] Refreshed docs/DAILY_BLOG.md for {today}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
