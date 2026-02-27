#!/usr/bin/env python3
"""
notify_discord.py - Post daily Awesome Anthropic digest to a Discord channel webhook.

Setup:
  1. Create a channel webhook in Discord server settings
  2. export DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
  3. python scripts/notify_discord.py

Usage:
  python scripts/notify_discord.py [--dry-run] [--force]
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

ROOT = Path(__file__).parent.parent
NEWS_MD = ROOT / "docs" / "NEWS.md"
SENT_LOG = ROOT / "data" / "last_discord_sent.txt"
MAX_STORIES = 5


def get_env(key: str) -> str:
    val = os.environ.get(key, "").strip()
    if not val:
        print(f"[discord] Missing env var: {key}. Skipping.", file=sys.stderr)
        sys.exit(0)
    return val


def parse_top_stories(text: str) -> list[dict]:
    section = re.search(
        r"###\s*🔥\s*Top Stories\s*\n\n\|[^\n]*\n\|[^\n]*\n(?P<table>(?:\|[^\n]*\n)+)",
        text,
    )
    if not section:
        return []

    rows = []
    for line in section.group("table").splitlines():
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 3:
            continue
        m = re.search(r"\[([^\]]+)\]\(([^)]+)\)", cols[1])
        if not m:
            continue
        rows.append(
            {
                "score": int(cols[0]) if cols[0].isdigit() else 0,
                "title": m.group(1).strip(),
                "href": m.group(2).strip(),
                "source": cols[2].strip(),
            }
        )
        if len(rows) >= MAX_STORIES:
            break
    return rows


def get_news_date(text: str) -> str:
    m = re.search(r"## ([A-Za-z]+ \d{1,2}, \d{4})", text)
    return m.group(1) if m else datetime.now(tz=timezone.utc).strftime("%B %-d, %Y")


def already_sent(date: str) -> bool:
    return SENT_LOG.exists() and SENT_LOG.read_text(encoding="utf-8").strip() == date


def mark_sent(date: str) -> None:
    SENT_LOG.parent.mkdir(exist_ok=True)
    SENT_LOG.write_text(date, encoding="utf-8")


def build_message(date: str, stories: list[dict]) -> str:
    lines = [
        f"**Awesome Anthropic — {date}**",
        "",
        "Top Stories:",
    ]
    for i, story in enumerate(stories, 1):
        lines.append(
            f"{i}. {story['title']} (▲ {story['score']} · {story['source']})\n{story['href']}"
        )
    lines.append("")
    lines.append("Dashboard: https://omrigotlieb.github.io/awesome-anthropic/")
    lines.append("RSS: https://omrigotlieb.github.io/awesome-anthropic/rss.xml")
    msg = "\n".join(lines)
    # Discord webhook content max is 2000 chars for plain messages.
    return msg[:1990]


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def send_message(webhook_url: str, text: str) -> None:
    with httpx.Client(timeout=20) as client:
        resp = client.post(webhook_url, json={"content": text})
        resp.raise_for_status()
    print("[discord] Message sent.", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if not NEWS_MD.exists():
        print(f"[discord] {NEWS_MD} not found.", file=sys.stderr)
        return

    text = NEWS_MD.read_text(encoding="utf-8")
    stories = parse_top_stories(text)
    date = get_news_date(text)

    if not stories:
        print("[discord] No stories found.", file=sys.stderr)
        return

    if not args.force and already_sent(date):
        print(f"[discord] Already sent for {date}. Use --force to resend.", file=sys.stderr)
        return

    msg = build_message(date, stories)
    if args.dry_run:
        print("=== DRY RUN — Would send to Discord ===")
        print(msg)
        return

    webhook = get_env("DISCORD_WEBHOOK_URL")
    try:
        send_message(webhook, msg)
        mark_sent(date)
    except Exception as e:
        print(f"[discord] Failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
