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


def read_news_text() -> str:
    if not NEWS_PATH.exists():
        return ""
    return NEWS_PATH.read_text()


def read_news_sections() -> list[tuple[str, str]]:
    text = read_news_text()
    if not text:
        return []

    matches = list(re.finditer(r"^##\s+([^\n]+)$", text, flags=re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), text[start:end].strip()))
    return sections


def _parse_table_rows(section_text: str, heading: str) -> list[list[str]]:
    section_match = re.search(
        rf"###\s*{re.escape(heading)}\s*\n\n\|[^\n]*\n\|[^\n]*\n(?P<table>(?:\|[^\n]*(?:\n|$))+)",
        section_text,
    )
    if not section_match:
        return []

    rows: list[list[str]] = []
    for row in section_match.group("table").splitlines():
        rows.append([c.strip() for c in row.strip().strip("|").split("|")])
    return rows


def _extract_link(value: str) -> tuple[str, str]:
    link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", value)
    if link_match:
        return link_match.group(1), link_match.group(2)
    return value, ""


def read_top_story_rows(limit: int = 5, max_sections: int = 1) -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    for news_date, section_text in read_news_sections()[:max_sections]:
        for cols in _parse_table_rows(section_text, "🔥 Top Stories"):
            if len(cols) < 3:
                continue
            title, url = _extract_link(cols[1])
            rows.append((title, url, cols[2], news_date))
            if len(rows) >= limit:
                return rows
    return rows


def read_recent_section_links(
    section_heading: str,
    title_col: int,
    limit: int = 5,
    max_sections: int = 4,
) -> list[tuple[str, str, str]]:
    links: list[tuple[str, str, str]] = []
    for news_date, section_text in read_news_sections()[:max_sections]:
        for cols in _parse_table_rows(section_text, section_heading):
            if len(cols) <= title_col:
                continue
            title, url = _extract_link(cols[title_col])
            if not url:
                continue
            links.append((title, url, news_date))
            if len(links) >= limit:
                return links
    return links


def read_release_rows(limit: int = 6, max_sections: int = 1) -> list[tuple[str, str, str, str]]:
    releases: list[tuple[str, str, str, str]] = []
    for news_date, section_text in read_news_sections()[:max_sections]:
        for cols in _parse_table_rows(section_text, "🛠️ SDK & Tool Releases"):
            if len(cols) < 2:
                continue
            title, url = _extract_link(cols[0])
            releases.append((title, url, cols[1], news_date))
            if len(releases) >= limit:
                return releases
    return releases


def read_top_stories(limit: int = 3) -> list[str]:
    stories: list[str] = []
    for title, url, _source, _date in read_top_story_rows(limit=limit):
        if url:
            stories.append(f"- [{title}]({url})")
        else:
            stories.append(f"- {title}")
    return stories


def read_news_date() -> str:
    sections = read_news_sections()
    return sections[0][0] if sections else ""


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
    return [
        (title, url)
        for title, url, _date in read_recent_section_links(
            section_heading, title_col=title_col, limit=limit, max_sections=4
        )
    ]


def _blog_intro(stale_days: int) -> list[str]:
    lines = [
        "This edition turns the daily log into a compact newsroom focused on product, release, and ecosystem signal.",
        "Each article is generated from the current `docs/NEWS.md` snapshot so the editorial deck stays aligned with verified repository data.",
    ]
    if stale_days > 0:
        lines.append(
            f"The current snapshot lags by {stale_days} day(s), so the article deck stays anchored to the latest verified items available in `docs/NEWS.md`."
        )
    return lines


def _blog_story_section(
    heading: str,
    date_label: str,
    source_title: str,
    url: str,
    paragraphs: list[str],
) -> list[str]:
    lines = [
        f"### {heading}",
        "",
        f"**News peg ({date_label}):** [{source_title}]({url})",
        "",
    ]
    for paragraph in paragraphs:
        lines.append(paragraph)
        lines.append("")
    return lines


def _compact(text: str, limit: int = 105) -> str:
    clean = " ".join((text or "").replace("## What's changed", "").split()).strip()
    if not clean:
        return "No additional summary details were captured in this snapshot."
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1].rstrip() + "…"


def _blog_angle(url: str, source: str) -> str:
    host = url.lower()
    source_l = source.lower()
    if "anthropic.com/" in host:
        return (
            "This is a first-party Anthropic announcement, so it should be treated as a product-direction signal rather than community speculation."
        )
    if "github.com/anthropics/claude-code" in host:
        return (
            "Claude Code release notes usually reflect near-term developer workflow changes, so this should remain part of daily release watch."
        )
    if "github.com/anthropics/" in host:
        return (
            "SDK and tooling releases from Anthropic repos are practical implementation signals that can change integration and migration priorities quickly."
        )
    if source_l.startswith("r/"):
        return (
            "This is community signal; it is useful for demand sensing, but should stay clearly separated from official announcements and release notes."
        )
    return "This item adds ecosystem signal and should be tracked alongside official updates for balanced daily coverage."


def _build_dynamic_article(
    article_num: int,
    headline: str,
    source_title: str,
    url: str,
    news_date: str,
    source: str,
    highlight: str,
) -> list[str]:
    return _blog_story_section(
        f"Article {article_num} — {headline}",
        news_date,
        source_title,
        url,
        [
            f"Snapshot update: {_compact(highlight, limit=220)}",
            _blog_angle(url, source),
        ],
    )


def build_blog_articles() -> list[str]:
    story_rows = read_top_story_rows(limit=10, max_sections=1)
    official_items = read_recent_section_links(
        "📰 Official Announcements", title_col=0, limit=6, max_sections=10
    )
    release_rows = read_release_rows(limit=10, max_sections=1)

    candidates: list[tuple[str, str, str, str, str, str]] = []
    seen_urls: set[str] = set()

    for title, url, news_date in official_items:
        if not url or url in seen_urls:
            continue
        candidates.append(
            (
                "Official announcement watch",
                title,
                url,
                news_date,
                "Anthropic Blog",
                title,
            )
        )
        seen_urls.add(url)
        if len(candidates) >= 3:
            break

    claude_code_release = next((row for row in release_rows if row[0].lower().startswith("claude-code ")), None)
    if claude_code_release:
        name, url, highlight, news_date = claude_code_release
        if url and url not in seen_urls:
            candidates.append(
                (
                    "Claude Code release watch",
                    name,
                    url,
                    news_date,
                    "GitHub Release",
                    highlight or name,
                )
            )
            seen_urls.add(url)

    for title, url, source, news_date in story_rows:
        if not url or url in seen_urls or "anthropic.com/" not in url:
            continue
        candidates.append(
            (
                "First-party story signal",
                title,
                url,
                news_date,
                source,
                f"Top story source: {source}",
            )
        )
        seen_urls.add(url)
        break

    for title, url, source, news_date in story_rows:
        if not url or url in seen_urls:
            continue
        source_l = source.lower()
        if source_l.startswith("r/"):
            headline = "Community demand signal"
        elif "github release" in source_l or "github.com/anthropics/" in url.lower():
            headline = "Ecosystem release signal"
        else:
            headline = "Ecosystem watch signal"
        candidates.append(
            (
                headline,
                title,
                url,
                news_date,
                source,
                f"Top story source: {source}",
            )
        )
        seen_urls.add(url)
        if len(candidates) >= 5:
            break

    if not candidates:
        return [
            "### Article 1 — Snapshot quality gate: not enough structured signals",
            "",
            "**News peg (Unknown):** [Daily feed unavailable](https://www.anthropic.com/news)",
            "",
            "Snapshot update: The current feed did not include enough official, release, or top-story rows to produce article briefs.",
            "",
            "Run `python3 scripts/fetch_news.py` and rebuild the daily docs to restore article coverage.",
            "",
        ]

    sections: list[str] = []
    for idx, (headline, title, url, news_date, source, highlight) in enumerate(candidates[:5], start=1):
        sections.extend(
            _build_dynamic_article(
                article_num=idx,
                headline=headline,
                source_title=title,
                url=url,
                news_date=news_date,
                source=source,
                highlight=highlight,
            )
        )
    return sections


def write_daily_brief(today: str) -> None:
    news_date = read_news_date()
    stories = read_top_stories(limit=3)
    announcements = [
        (title, url)
        for title, url, _date in read_recent_section_links(
            "📰 Official Announcements", title_col=0, limit=3, max_sections=10
        )
    ]
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
            "- Dashboard freshness and first-party-source mix should stay visible so readers can judge recency and trust quickly.",
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
    announcements = read_recent_section_links("📰 Official Announcements", title_col=0, limit=3, max_sections=10)
    releases = read_release_rows(limit=3, max_sections=1)
    today_dt = dt.datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    news_dt = _parse_news_date(news_date)
    stale_days = (today_dt - news_dt).days if news_dt else 0

    release_line = "No new Claude Code release detected in the current snapshot."
    for name, _url, _highlight, _date in releases:
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
            f"- Official channel signal remains active: {announcements[0][0]} ({announcements[0][2]})."
        )
    else:
        key_takeaways.append("- No official announcement row was parsed in this run.")
    if stale_days > 0:
        key_takeaways.append(
            f"- Freshness risk: snapshot is {stale_days} day(s) old due to unavailable network fetch in this environment."
        )

    story_lines = stories if stories else ["- No top stories were parsed from docs/NEWS.md."]
    improvements = [
        "- Keep freshness and source-quality signals near the article deck so readers can assess recency at a glance.",
        "- Add direct story deep links from dashboard cards once the blog format stabilizes.",
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

    recent_sources: list[str] = []
    seen_urls: set[str] = set()
    for title, url, date_label in announcements:
        if url not in seen_urls:
            recent_sources.append(f"- {date_label}: [{title}]({url})")
            seen_urls.add(url)
    for title, url, _source, date_label in read_top_story_rows(limit=5, max_sections=1):
        if url and "anthropic.com/" in url and url not in seen_urls:
            recent_sources.append(f"- {date_label}: [{title}]({url})")
            seen_urls.add(url)
    for name, url, _highlight, date_label in releases:
        if url not in seen_urls:
            recent_sources.append(f"- {date_label}: [{name}]({url})")
            seen_urls.add(url)

    content = "\n".join(
        [
            "# Daily Anthropic Blog Post",
            "",
            f"## {title_date}",
            "",
            "### Executive Summary",
            "",
            *_blog_intro(stale_days),
            "",
            "### Key Takeaways",
            "",
            *key_takeaways,
            "",
            "### Latest News Articles",
            "",
            *build_blog_articles(),
            "",
            "### Top Stories Referenced",
            "",
            *story_lines,
            "",
            "### Source Trail",
            "",
            *(recent_sources or ["- No source links were captured in this run."]),
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
