#!/usr/bin/env python3
"""
generate_social_posts.py - Build daily multi-channel social copy from docs/NEWS.md.

Outputs:
  - data/distribution/<YYYY-MM-DD>/social_posts.md
  - data/distribution/latest_social_posts.md

Usage:
  python scripts/generate_social_posts.py
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
NEWS_MD = ROOT / "docs" / "NEWS.md"
OUT_ROOT = ROOT / "data" / "distribution"

SITE_URL = "https://omrigotlieb.github.io/awesome-anthropic/"
NEWS_URL = f"{SITE_URL}#/docs/NEWS"
RSS_URL = f"{SITE_URL}rss.xml"
REPO_URL = "https://github.com/Omrigotlieb/awesome-anthropic"


def parse_date(text: str) -> str:
    m = re.search(r"## ([A-Za-z]+ \d{1,2}, \d{4})", text)
    if m:
        return m.group(1)
    return datetime.now(tz=timezone.utc).strftime("%B %-d, %Y")


def parse_top_stories(text: str, max_rows: int = 3) -> list[dict[str, str | int]]:
    section = re.search(
        r"###\s*🔥\s*Top Stories\s*\n\n\|[^\n]*\n\|[^\n]*\n(?P<table>(?:\|[^\n]*\n)+)",
        text,
    )
    if not section:
        return []

    rows: list[dict[str, str | int]] = []
    for line in section.group("table").splitlines():
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 3:
            continue
        link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", cols[1])
        if not link_match:
            continue
        rows.append(
            {
                "score": int(cols[0]) if cols[0].isdigit() else 0,
                "title": link_match.group(1).strip(),
                "url": link_match.group(2).strip(),
                "source": cols[2].strip(),
            }
        )
        if len(rows) >= max_rows:
            break
    return rows


def parse_announcements(text: str, max_rows: int = 2) -> list[dict[str, str]]:
    section = re.search(
        r"###\s*📰\s*Official Announcements\s*\n\n\|[^\n]*\n\|[^\n]*\n(?P<table>(?:\|[^\n]*\n)+)",
        text,
    )
    if not section:
        return []

    rows: list[dict[str, str]] = []
    for line in section.group("table").splitlines():
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 2:
            continue
        link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", cols[0])
        if not link_match:
            continue
        rows.append({"title": link_match.group(1).strip(), "url": link_match.group(2).strip()})
        if len(rows) >= max_rows:
            break
    return rows


def build_markdown(date: str, stories: list[dict[str, str | int]], ann: list[dict[str, str]]) -> str:
    top = stories[0] if stories else {}
    s1 = stories[0]["title"] if len(stories) > 0 else "Top Claude + Anthropic story"
    s2 = stories[1]["title"] if len(stories) > 1 else "Fresh product and ecosystem updates"
    s3 = stories[2]["title"] if len(stories) > 2 else "Community and release signals"
    a1 = ann[0]["title"] if len(ann) > 0 else "Official Anthropic announcement"

    x_post = (
        f"Claude + Anthropic daily pulse ({date}):\n"
        f"1) {s1}\n"
        f"2) {s2}\n"
        f"3) {s3}\n\n"
        f"Track it here:\n"
        f"Repo: {REPO_URL}\n"
        f"Dashboard: {SITE_URL}"
    )

    linkedin_post = (
        f"We published today’s Awesome Anthropic brief ({date}).\n\n"
        f"Highlights:\n"
        f"• {s1}\n"
        f"• {s2}\n"
        f"• {a1}\n\n"
        f"For builders tracking Claude Code and Anthropic product movement:\n"
        f"{NEWS_URL}\n\n"
        f"Repository: {REPO_URL}"
    )

    reddit_post = (
        f"Daily Anthropic + Claude Code brief ({date})\n\n"
        f"Top signals:\n"
        f"- {s1}\n"
        f"- {s2}\n"
        f"- {s3}\n\n"
        f"Full feed: {NEWS_URL}\n"
        f"Repo: {REPO_URL}\n"
        f"RSS: {RSS_URL}"
    )

    hn_title = f"Daily Claude + Anthropic digest ({date}): {str(top.get('title', s1))[:80]}"
    hn_body = (
        f"Tracking daily product, release, and community signals here: {SITE_URL} "
        f"Repository: {REPO_URL}"
    )

    lines = [
        f"# Daily Social Distribution Copy — {date}",
        "",
        "Use and adapt these drafts for channel distribution.",
        "",
        "## X / Twitter",
        "",
        "```text",
        x_post,
        "```",
        "",
        "## LinkedIn",
        "",
        "```text",
        linkedin_post,
        "```",
        "",
        "## Reddit",
        "",
        "```text",
        reddit_post,
        "```",
        "",
        "## Hacker News",
        "",
        "```text",
        f"Title: {hn_title}",
        f"Text: {hn_body}",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    if not NEWS_MD.exists():
        print(f"[social] {NEWS_MD} not found; skipping.")
        return 0

    text = NEWS_MD.read_text(encoding="utf-8")
    date = parse_date(text)
    day_key = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    stories = parse_top_stories(text, max_rows=3)
    ann = parse_announcements(text, max_rows=2)

    out_day_dir = OUT_ROOT / day_key
    out_day_dir.mkdir(parents=True, exist_ok=True)

    content = build_markdown(date, stories, ann)
    day_file = out_day_dir / "social_posts.md"
    latest_file = OUT_ROOT / "latest_social_posts.md"
    day_file.write_text(content, encoding="utf-8")
    latest_file.write_text(content, encoding="utf-8")

    print(f"[social] Wrote {day_file}")
    print(f"[social] Wrote {latest_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
