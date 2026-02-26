"""RSS/Atom feed parser utilities."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def fetch_feed(url: str) -> list[dict[str, Any]]:
    """
    Fetch and parse an RSS or Atom feed.
    Returns a list of dicts with keys: title, url, published_at, summary.
    """
    import xml.etree.ElementTree as ET

    with httpx.Client(timeout=30, follow_redirects=True) as client:
        resp = client.get(url, headers={"User-Agent": "awesome-anthropic-bot/1.0"})
        resp.raise_for_status()

    root = ET.fromstring(resp.text)
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "dc": "http://purl.org/dc/elements/1.1/",
    }

    items = []

    # RSS 2.0
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub_date = item.findtext("pubDate") or item.findtext("dc:date", namespaces=ns) or ""
        summary = (item.findtext("description") or "").strip()[:300]

        if not title or not link:
            continue

        try:
            from email.utils import parsedate_to_datetime
            pub_dt = parsedate_to_datetime(pub_date) if pub_date else datetime.now(tz=timezone.utc)
        except Exception:
            pub_dt = datetime.now(tz=timezone.utc)

        items.append({"title": title, "url": link, "published_at": pub_dt, "summary": summary})

    # Atom
    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        link_el = entry.find("atom:link", ns)
        updated_el = entry.find("atom:updated", ns)
        summary_el = entry.find("atom:summary", ns) or entry.find("atom:content", ns)

        title = (title_el.text or "").strip() if title_el is not None else ""
        link = (link_el.get("href") or "").strip() if link_el is not None else ""
        updated = (updated_el.text or "").strip() if updated_el is not None else ""
        summary = (summary_el.text or "").strip()[:300] if summary_el is not None else ""

        if not title or not link:
            continue

        try:
            pub_dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
        except Exception:
            pub_dt = datetime.now(tz=timezone.utc)

        items.append({"title": title, "url": link, "published_at": pub_dt, "summary": summary})

    return items
