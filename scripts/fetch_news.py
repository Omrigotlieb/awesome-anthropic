#!/usr/bin/env python3
"""
fetch_news.py - Multi-source Anthropic news aggregator.

Sources:
  1. Anthropic blog (scrape)
  2. Hacker News Algolia API
  3. Reddit (r/ClaudeAI, r/Anthropic, r/MachineLearning, r/LocalLLaMA)
  4. arXiv (Anthropic-authored papers)
  5. GitHub releases (anthropics org)

Usage:
  python scripts/fetch_news.py            # Full run, writes to docs/NEWS.md
  python scripts/fetch_news.py --summary  # Print count summary only
  python scripts/fetch_news.py --dry-run  # Fetch but don't write files
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"


@dataclass
class NewsItem:
    title: str
    url: str
    source: str
    published_at: str  # ISO format
    summary: str = ""
    score: int = 0
    item_id: str = field(default="")

    def __post_init__(self):
        if not self.item_id:
            self.item_id = hashlib.sha256(self.url.encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Source fetchers
# ---------------------------------------------------------------------------

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def fetch_anthropic_blog(since_hours: int = 48) -> list[NewsItem]:
    """Scrape https://www.anthropic.com/news for recent posts."""
    import re as _re

    items = []
    since = datetime.now(tz=timezone.utc) - timedelta(hours=since_hours)
    date_pattern = _re.compile(
        r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
        r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
        r"\s+\d{1,2},\s+20\d\d"
    )
    try:
        with httpx.Client(timeout=30, follow_redirects=True) as client:
            resp = client.get(
                "https://www.anthropic.com/news",
                headers={"User-Agent": "Mozilla/5.0 awesome-anthropic-bot/1.0"},
            )
            resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")

        seen_hrefs: set[str] = set()
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if "/news/" not in href or href in seen_hrefs:
                continue
            seen_hrefs.add(href)

            raw_text = a_tag.get_text(" ", strip=True)
            # Extract date from text if present
            date_match = date_pattern.search(raw_text)
            pub_dt = datetime.now(tz=timezone.utc)
            if date_match:
                try:
                    pub_dt = datetime.strptime(date_match.group(), "%b %d, %Y").replace(tzinfo=timezone.utc)
                except ValueError:
                    try:
                        pub_dt = datetime.strptime(date_match.group(), "%B %d, %Y").replace(tzinfo=timezone.utc)
                    except ValueError:
                        pass
                # Remove date and categories from text to get title
                raw_text = date_pattern.sub("", raw_text)

            # Strip known category words
            for cat in ("Announcements", "Product", "Research", "Policy", "News", "Careers"):
                raw_text = raw_text.replace(cat, " ")
            title = " ".join(raw_text.split())[:120]
            if not title or len(title) < 5:
                continue

            url = href if href.startswith("http") else f"https://www.anthropic.com{href}"
            if pub_dt >= since:
                items.append(
                    NewsItem(
                        title=title,
                        url=url,
                        source="Anthropic Blog",
                        published_at=pub_dt.isoformat(),
                        item_id=f"blog_{href.split('/')[-1]}",
                    )
                )
    except Exception as e:
        print(f"[blog] Error: {e}", file=sys.stderr)
    return items


def fetch_hacker_news(since_hours: int = 24, min_score: int = 10) -> list[NewsItem]:
    """Fetch Anthropic-related posts from HN via Algolia API."""
    items = []
    since_unix = int((datetime.now(tz=timezone.utc) - timedelta(hours=since_hours)).timestamp())
    queries = ["anthropic", "claude AI model"]

    seen_ids = set()
    with httpx.Client(timeout=20) as client:
        for query in queries:
            try:
                resp = client.get(
                    "https://hn.algolia.com/api/v1/search",
                    params={
                        "query": query,
                        "tags": "story",
                        "numericFilters": f"created_at_i>{since_unix},points>={min_score}",
                        "hitsPerPage": 20,
                    },
                )
                resp.raise_for_status()
                for hit in resp.json().get("hits", []):
                    hn_id = hit.get("objectID", "")
                    if hn_id in seen_ids:
                        continue
                    seen_ids.add(hn_id)
                    items.append(
                        NewsItem(
                            title=hit.get("title", ""),
                            url=hit.get("url") or f"https://news.ycombinator.com/item?id={hn_id}",
                            source="Hacker News",
                            published_at=datetime.fromtimestamp(
                                hit.get("created_at_i", 0), tz=timezone.utc
                            ).isoformat(),
                            score=hit.get("points", 0),
                            item_id=f"hn_{hn_id}",
                        )
                    )
            except Exception as e:
                print(f"[hn] Error for query '{query}': {e}", file=sys.stderr)
    return items


def fetch_reddit(since_hours: int = 24, min_score: int = 50) -> list[NewsItem]:
    """Fetch Anthropic-related posts from Reddit using PRAW if credentials available."""
    items = []
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")

    if not client_id or not client_secret:
        # Fallback: use Reddit JSON API (no auth, rate limited)
        return _fetch_reddit_json(since_hours, min_score)

    try:
        import praw

        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="awesome-anthropic-bot/1.0",
        )
        subreddits = ["ClaudeAI", "Anthropic", "MachineLearning", "LocalLLaMA"]
        since = datetime.now(tz=timezone.utc) - timedelta(hours=since_hours)
        keywords = {"anthropic", "claude"}

        for sub_name in subreddits:
            try:
                sub = reddit.subreddit(sub_name)
                for post in sub.hot(limit=25):
                    if post.score < min_score:
                        continue
                    title_lower = post.title.lower()
                    if sub_name not in ("ClaudeAI", "Anthropic") and not any(
                        kw in title_lower for kw in keywords
                    ):
                        continue
                    created = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)
                    if created < since:
                        continue
                    items.append(
                        NewsItem(
                            title=post.title,
                            url=f"https://reddit.com{post.permalink}",
                            source=f"r/{sub_name}",
                            published_at=created.isoformat(),
                            score=post.score,
                            item_id=f"reddit_{post.id}",
                        )
                    )
            except Exception as e:
                print(f"[reddit] Error for r/{sub_name}: {e}", file=sys.stderr)
    except ImportError:
        return _fetch_reddit_json(since_hours, min_score)
    return items


def _fetch_reddit_json(since_hours: int = 24, min_score: int = 50) -> list[NewsItem]:
    """Fallback Reddit fetch using public JSON API."""
    items = []
    subreddits = ["ClaudeAI", "Anthropic"]
    since = datetime.now(tz=timezone.utc) - timedelta(hours=since_hours)

    with httpx.Client(timeout=20, follow_redirects=True) as client:
        for sub in subreddits:
            try:
                resp = client.get(
                    f"https://www.reddit.com/r/{sub}/hot.json",
                    params={"limit": 25},
                    headers={"User-Agent": "awesome-anthropic-bot/1.0"},
                )
                resp.raise_for_status()
                for post in resp.json()["data"]["children"]:
                    d = post["data"]
                    if d.get("score", 0) < min_score:
                        continue
                    created = datetime.fromtimestamp(d.get("created_utc", 0), tz=timezone.utc)
                    if created < since:
                        continue
                    items.append(
                        NewsItem(
                            title=d.get("title", ""),
                            url=f"https://reddit.com{d.get('permalink', '')}",
                            source=f"r/{sub}",
                            published_at=created.isoformat(),
                            score=d.get("score", 0),
                            item_id=f"reddit_{d.get('id', '')}",
                        )
                    )
            except Exception as e:
                print(f"[reddit_json] Error for r/{sub}: {e}", file=sys.stderr)
    return items


def fetch_arxiv(since_days: int = 7) -> list[NewsItem]:
    """Fetch recent Anthropic-affiliated arXiv papers."""
    items = []
    try:
        import arxiv

        search = arxiv.Search(
            query="au:anthropic OR ti:claude AND (cat:cs.AI OR cat:cs.LG OR cat:cs.CL)",
            max_results=10,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )
        since = datetime.now(tz=timezone.utc) - timedelta(days=since_days)
        client = arxiv.Client()
        for result in client.results(search):
            if result.published and result.published.replace(tzinfo=timezone.utc) >= since:
                items.append(
                    NewsItem(
                        title=result.title,
                        url=result.entry_id,
                        source="arXiv",
                        published_at=result.published.isoformat(),
                        summary=result.summary[:200],
                        item_id=f"arxiv_{result.entry_id.split('/')[-1]}",
                    )
                )
    except ImportError:
        print("[arxiv] arxiv package not installed, skipping.", file=sys.stderr)
    except Exception as e:
        print(f"[arxiv] Error: {e}", file=sys.stderr)
    return items


def fetch_github_releases() -> list[NewsItem]:
    """Fetch recent releases from the anthropics GitHub org."""
    import sys as _sys
    _sys.path.insert(0, str(ROOT))
    from scripts.utils.github_api import get_org_releases

    items = []
    try:
        for rel in get_org_releases(org="anthropics", since_days=7):
            items.append(
                NewsItem(
                    title=rel["title"],
                    url=rel["url"],
                    source="GitHub Release",
                    published_at=rel["published_at"].isoformat(),
                    summary=rel.get("body", ""),
                )
            )
    except Exception as e:
        print(f"[github] Error: {e}", file=sys.stderr)
    return items


# ---------------------------------------------------------------------------
# Deduplication & persistence
# ---------------------------------------------------------------------------

def load_seen_ids() -> set[str]:
    path = DATA_DIR / "last_news_fetch.json"
    if path.exists():
        try:
            data = json.loads(path.read_text())
            return set(data.get("seen_ids", []))
        except Exception:
            pass
    return set()


def save_seen_ids(seen: set[str]) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / "last_news_fetch.json"
    # Keep only last 2000 IDs to prevent unbounded growth
    trimmed = list(seen)[-2000:]
    path.write_text(json.dumps({"seen_ids": trimmed}, indent=2))


def deduplicate(items: list[NewsItem], seen: set[str]) -> list[NewsItem]:
    new_items = []
    for item in items:
        if item.item_id not in seen:
            new_items.append(item)
            seen.add(item.item_id)
    return new_items


# ---------------------------------------------------------------------------
# Writing output
# ---------------------------------------------------------------------------

def append_to_news_md(items: list[NewsItem]) -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    news_path = DOCS_DIR / "NEWS.md"
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

    lines = [f"## {today}\n"]
    for item in sorted(items, key=lambda x: x.score, reverse=True):
        score_str = f" | Score: {item.score}" if item.score else ""
        lines.append(f"- [{item.title}]({item.url}) — {item.source}{score_str}")
        if item.summary:
            lines.append(f"  > {item.summary}")
    lines.append("")

    existing = news_path.read_text() if news_path.exists() else "# Anthropic News Archive\n\n"
    # Insert after the top-level header
    header_end = existing.find("\n\n") + 2
    if header_end < 2:
        header_end = 0
    new_content = existing[:header_end] + "\n".join(lines) + "\n" + existing[header_end:]
    news_path.write_text(new_content)


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", action="store_true", help="Print summary only, no file writes.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch but don't write.")
    args = parser.parse_args()

    print("Fetching news from all sources...", file=sys.stderr)
    all_items: list[NewsItem] = []
    all_items.extend(fetch_anthropic_blog())
    all_items.extend(fetch_hacker_news())
    all_items.extend(fetch_reddit())
    all_items.extend(fetch_arxiv())
    all_items.extend(fetch_github_releases())

    seen = load_seen_ids()
    new_items = deduplicate(all_items, seen)

    if args.summary:
        print(f"- **Total fetched:** {len(all_items)}")
        print(f"- **New items:** {len(new_items)}")
        by_source: dict[str, int] = {}
        for item in new_items:
            by_source[item.source] = by_source.get(item.source, 0) + 1
        for src, count in sorted(by_source.items()):
            print(f"  - {src}: {count}")
        return

    print(f"Found {len(new_items)} new items out of {len(all_items)} total.", file=sys.stderr)

    if not new_items:
        print("No new items. Exiting.", file=sys.stderr)
        return

    # Optionally summarize with Claude
    try:
        from scripts.utils.anthropic_api import batch_summarize, is_api_available
        if is_api_available():
            print("Summarizing with Claude...", file=sys.stderr)
            summaries = batch_summarize([asdict(i) for i in new_items])
            for item, summary in zip(new_items, summaries):
                if not item.summary:
                    item.summary = summary
    except Exception as e:
        print(f"[summarize] Skipped: {e}", file=sys.stderr)

    if not args.dry_run:
        append_to_news_md(new_items)
        save_seen_ids(seen)
        print(f"Wrote {len(new_items)} items to docs/NEWS.md", file=sys.stderr)


if __name__ == "__main__":
    main()
