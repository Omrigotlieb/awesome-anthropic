#!/usr/bin/env python3
"""
email_digest.py — Send daily Awesome Anthropic digest via Buttondown newsletter.

Buttondown (buttondown.email) — free tier, no credit card required.

Setup:
  1. Sign up at https://buttondown.email (free)
  2. Settings → API Keys → create a key
  3. export BUTTONDOWN_API_KEY=your_key_here
  4. python scripts/email_digest.py

Usage:
  python scripts/email_digest.py [--dry-run] [--force]
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
SENT_LOG = ROOT / "data" / "last_email_sent.txt"

BUTTONDOWN_API = "https://api.buttondown.email/v1/emails"
SITE_URL = "https://omrigotlieb.github.io/awesome-anthropic/"
RSS_URL  = f"{SITE_URL}rss.xml"
MAX_STORIES   = 8
MAX_ANNOUNCES = 4


def get_env(key: str) -> str:
    val = os.environ.get(key, "").strip()
    if not val:
        print(f"[email] Missing env var: {key}. Skipping.", file=sys.stderr)
        sys.exit(0)
    return val


def _parse_table(text: str, heading: str, max_rows: int) -> list[dict]:
    lines = text.split("\n")
    found, header_passed, rows = False, False, []
    for line in lines:
        if not found:
            if heading in line:
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
            if cols:
                m = re.match(r"\[([^\]]*)\]\(([^)]*)\)", cols[0] if len(cols) == 1 else cols[1] if len(cols) > 1 else "")
                if m:
                    rows.append({
                        "score": int(cols[0]) if len(cols) > 1 and cols[0].isdigit() else 0,
                        "title": m.group(1).strip(),
                        "href":  m.group(2).strip(),
                        "source": cols[2].strip() if len(cols) > 2 else (cols[1].strip() if len(cols) > 1 else ""),
                    })
    return rows[:max_rows]


def get_news_date(text: str) -> str:
    m = re.search(r"## ([A-Za-z]+ \d+, \d{4})", text)
    return m.group(1) if m else datetime.now(tz=timezone.utc).strftime("%B %-d, %Y")


def already_sent(date: str) -> bool:
    return SENT_LOG.exists() and SENT_LOG.read_text().strip() == date


def mark_sent(date: str) -> None:
    SENT_LOG.parent.mkdir(exist_ok=True)
    SENT_LOG.write_text(date)


def build_markdown(date: str, stories: list[dict], announces: list[dict]) -> str:
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]
    lines = [f"# ⚡ Awesome Anthropic — {date}\n\n## 🔥 Top Stories\n"]
    for i, s in enumerate(stories):
        medal = medals[i] if i < len(medals) else f"{i+1}."
        lines.append(f"{medal} **[{s['title']}]({s['href']})** — ▲ {s['score']} pts · {s['source']}")
    if announces:
        lines.append("\n## 📢 Official Announcements\n")
        for a in announces:
            lines.append(f"- [{a['title']}]({a['href']})")
    lines.append(f"\n---\n[Open Dashboard →]({SITE_URL}) · [Subscribe via RSS]({RSS_URL})")
    return "\n".join(lines)


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def send_email(api_key: str, subject: str, body: str) -> None:
    with httpx.Client(timeout=30) as client:
        resp = client.post(
            BUTTONDOWN_API,
            headers={"Authorization": f"Token {api_key}"},
            json={"subject": subject, "body": body, "email_type": "public", "status": "sent"},
        )
        resp.raise_for_status()
    print(f"[email] Sent: {subject}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force",   action="store_true")
    args = parser.parse_args()

    if not NEWS_MD.exists():
        print(f"[email] {NEWS_MD} not found.", file=sys.stderr)
        return

    text      = NEWS_MD.read_text(encoding="utf-8")
    stories   = _parse_table(text, "🔥 Top Stories", MAX_STORIES)
    announces = _parse_table(text, "Official Announcements", MAX_ANNOUNCES)
    date      = get_news_date(text)

    if not stories:
        print("[email] No stories found.", file=sys.stderr)
        return

    if not args.force and already_sent(date):
        print(f"[email] Already sent for {date}. Use --force to resend.", file=sys.stderr)
        return

    subject = f"⚡ Awesome Anthropic — {date}"
    body    = build_markdown(date, stories, announces)

    if args.dry_run:
        print("=== DRY RUN ===")
        print(f"Subject: {subject}\n")
        print(body)
        return

    api_key = get_env("BUTTONDOWN_API_KEY")
    try:
        send_email(api_key, subject, body)
        mark_sent(date)
    except Exception as e:
        print(f"[email] Failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
