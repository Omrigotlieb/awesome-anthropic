#!/usr/bin/env python3
"""
generate_rss.py — Generate RSS 2.0 feed from docs/NEWS.md

Reads the top stories table from NEWS.md and outputs a valid RSS feed at rss.xml.
Run after fetch_news.py to keep the feed in sync.

Usage:
  python scripts/generate_rss.py
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT   = Path(__file__).parent.parent
NEWS   = ROOT / "docs" / "NEWS.md"
OUTPUT = ROOT / "rss.xml"

FEED_TITLE = "Awesome Anthropic — Daily News"
FEED_LINK  = "https://omrigotlieb.github.io/awesome-anthropic/"
FEED_DESC  = "Daily-updated Claude & Anthropic community news aggregated from Hacker News, Reddit, arXiv, and Anthropic Blog."


def parse_top_stories(text: str) -> list[dict]:
    """Extract rows from the 🔥 Top Stories table."""
    lines = text.split("\n")
    found = False
    table_lines = []
    for line in lines:
        if not found:
            if "🔥 Top Stories" in line:
                found = True
            continue
        t = line.strip()
        if t.startswith("##") or t == "---":
            break
        table_lines.append(line)

    rows = []
    header_passed = False
    for line in table_lines:
        t = line.strip()
        if not t.startswith("|"):
            if header_passed:
                break
            continue
        if re.match(r"^[|\s:>\-]+$", t):
            header_passed = True
            continue
        if header_passed:
            cols = [c.strip() for c in t.split("|")[1:-1]]
            if len(cols) >= 3:
                score_str = cols[0]
                link_col  = cols[1]
                source    = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cols[2]).strip()

                m = re.match(r"\[([^\]]*)\]\(([^)]*)\)", link_col)
                if m:
                    title = m.group(1).strip()
                    href  = m.group(2).strip()
                else:
                    title = link_col.strip()
                    href  = ""

                try:
                    score = int(score_str)
                except ValueError:
                    score = 0

                if title and href:
                    rows.append({"title": title, "href": href, "source": source, "score": score})
    return rows[:20]


def get_news_date(text: str) -> str:
    """Extract the date header from NEWS.md."""
    m = re.search(r"## ([A-Za-z]+ \d+, \d{4})", text)
    return m.group(1) if m else datetime.now(tz=timezone.utc).strftime("%B %-d, %Y")


def xml_escape(s: str) -> str:
    return (str(s)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))


def build_item(item: dict, pub_date: str) -> str:
    title = xml_escape(item["title"])
    link  = xml_escape(item["href"])
    desc  = xml_escape(f"▲ {item['score']} points · {item['source']} · {item['title']}")
    return (
        "  <item>\n"
        f"    <title>{title}</title>\n"
        f"    <link>{link}</link>\n"
        f"    <guid isPermaLink=\"true\">{link}</guid>\n"
        f"    <description>{desc}</description>\n"
        f"    <source url=\"{xml_escape(FEED_LINK)}\">{xml_escape(item['source'])}</source>\n"
        f"    <pubDate>{pub_date}</pubDate>\n"
        "  </item>"
    )


def main() -> None:
    if not NEWS.exists():
        print(f"[rss] {NEWS} not found — skipping.", file=sys.stderr)
        return

    text   = NEWS.read_text(encoding="utf-8")
    items  = parse_top_stories(text)
    if not items:
        print("[rss] No stories parsed.", file=sys.stderr)
        return

    news_date = get_news_date(text)
    # Convert "February 26, 2026" to RFC-822
    try:
        dt = datetime.strptime(news_date, "%B %d, %Y").replace(tzinfo=timezone.utc)
    except ValueError:
        dt = datetime.now(tz=timezone.utc)
    pub_date_rfc = dt.strftime("%a, %d %b %Y 09:00:00 +0000")
    build_date   = datetime.now(tz=timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    items_xml = "\n".join(build_item(it, pub_date_rfc) for it in items)

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{xml_escape(FEED_TITLE)}</title>
    <link>{xml_escape(FEED_LINK)}</link>
    <description>{xml_escape(FEED_DESC)}</description>
    <language>en-us</language>
    <lastBuildDate>{build_date}</lastBuildDate>
    <atom:link href="{xml_escape(FEED_LINK)}rss.xml" rel="self" type="application/rss+xml"/>
    <image>
      <url>https://www.anthropic.com/images/index/og-anthropic-index.jpg</url>
      <title>{xml_escape(FEED_TITLE)}</title>
      <link>{xml_escape(FEED_LINK)}</link>
    </image>
{items_xml}
  </channel>
</rss>"""

    OUTPUT.write_text(rss, encoding="utf-8")
    print(f"[rss] Generated {OUTPUT} with {len(items)} items.", file=sys.stderr)


if __name__ == "__main__":
    main()
