#!/usr/bin/env python3
"""
notify_telegram.py — Post daily Awesome Anthropic digest to a Telegram channel.

Setup:
  1. Create a bot via @BotFather → get TELEGRAM_BOT_TOKEN
  2. Create a channel, add bot as admin → get TELEGRAM_CHANNEL_ID (e.g. @yourchannel)
  3. export TELEGRAM_BOT_TOKEN=xxx TELEGRAM_CHANNEL_ID=yyy
  4. python scripts/notify_telegram.py

Usage:
  python scripts/notify_telegram.py [--dry-run] [--force]
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

ROOT     = Path(__file__).parent.parent
NEWS_MD  = ROOT / "docs" / "NEWS.md"
SENT_LOG = ROOT / "data" / "last_telegram_sent.txt"

TELEGRAM_API = "https://api.telegram.org/bot{token}/sendMessage"
MAX_STORIES  = 5


def get_env(key: str) -> str:
    val = os.environ.get(key, "").strip()
    if not val:
        print(f"[telegram] Missing env var: {key}. Skipping.", file=sys.stderr)
        sys.exit(0)
    return val


def parse_top_stories(text: str) -> list[dict]:
    lines = text.split("\n")
    found, header_passed, rows = False, False, []
    for line in lines:
        if not found:
            if "🔥 Top Stories" in line:
                found = True
            continue
        t = line.strip()
        if t.startswith("##") or t == "---":
            break
        if not t.startswith("|"):
            continue
        if re.match(r"^[|\s:>\-]+$", t):
            header_passed = True
            continue
        if header_passed:
            cols = [c.strip() for c in t.split("|")[1:-1]]
            if len(cols) >= 2:
                m = re.match(r"\[([^\]]*)\]\(([^)]*)\)", cols[1])
                if m:
                    rows.append({
                        "score": int(cols[0]) if cols[0].isdigit() else 0,
                        "title": m.group(1).strip(),
                        "href":  m.group(2).strip(),
                        "source": cols[2].strip() if len(cols) > 2 else "",
                    })
    return rows[:MAX_STORIES]


def get_news_date(text: str) -> str:
    m = re.search(r"## ([A-Za-z]+ \d+, \d{4})", text)
    return m.group(1) if m else datetime.now(tz=timezone.utc).strftime("%B %-d, %Y")


def already_sent(date: str) -> bool:
    return SENT_LOG.exists() and SENT_LOG.read_text().strip() == date


def mark_sent(date: str) -> None:
    SENT_LOG.parent.mkdir(exist_ok=True)
    SENT_LOG.write_text(date)


def build_message(date: str, stories: list[dict]) -> str:
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
    lines = [
        f"⚡ <b>Awesome Anthropic — {date}</b>",
        "",
        "🔥 <b>Top Stories</b>",
        "",
    ]
    for i, s in enumerate(stories):
        lines.append(f'{medals[i]} <a href="{s["href"]}">{s["title"]}</a>')
        lines.append(f'    ▲ {s["score"]} pts · {s["source"]}')
        lines.append("")
    lines.append('🌐 <a href="https://omrigotlieb.github.io/awesome-anthropic/">Full dashboard →</a>')
    lines.append('📡 <a href="https://omrigotlieb.github.io/awesome-anthropic/rss.xml">Subscribe via RSS →</a>')
    return "\n".join(lines)


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def send_message(token: str, channel: str, text: str) -> None:
    url = TELEGRAM_API.format(token=token)
    with httpx.Client(timeout=20) as client:
        resp = client.post(url, json={
            "chat_id": channel,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": False,
        })
        resp.raise_for_status()
        result = resp.json()
        if not result.get("ok"):
            raise RuntimeError(f"Telegram API error: {result}")
    print(f"[telegram] Message sent to {channel}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if not NEWS_MD.exists():
        print(f"[telegram] {NEWS_MD} not found.", file=sys.stderr)
        return

    text    = NEWS_MD.read_text(encoding="utf-8")
    stories = parse_top_stories(text)
    date    = get_news_date(text)

    if not stories:
        print("[telegram] No stories found.", file=sys.stderr)
        return

    if not args.force and already_sent(date):
        print(f"[telegram] Already sent for {date}. Use --force to resend.", file=sys.stderr)
        return

    msg = build_message(date, stories)

    if args.dry_run:
        print("=== DRY RUN — Would send to Telegram ===")
        print(msg)
        return

    token   = get_env("TELEGRAM_BOT_TOKEN")
    channel = get_env("TELEGRAM_CHANNEL_ID")

    try:
        send_message(token, channel, msg)
        mark_sent(date)
    except Exception as e:
        print(f"[telegram] Failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
