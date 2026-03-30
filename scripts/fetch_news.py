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
import socket
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
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


def has_network_connectivity() -> bool:
    """
    Fast DNS preflight for daily automation environments.

    When DNS is unavailable (common in sandboxed runs), we skip source fetches
    and avoid emitting noisy per-source resolver failures.
    """
    hosts = ("www.anthropic.com", "github.com", "www.reddit.com", "hn.algolia.com")
    for host in hosts:
        try:
            socket.getaddrinfo(host, 443, proto=socket.IPPROTO_TCP)
            return True
        except socket.gaierror:
            continue
    return False


# ---------------------------------------------------------------------------
# Source fetchers
# ---------------------------------------------------------------------------

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def fetch_anthropic_blog(since_hours: int = 48) -> list[NewsItem]:
    """Scrape https://www.anthropic.com/news for recent first-party posts."""
    import re as _re

    since = datetime.now(tz=timezone.utc) - timedelta(hours=since_hours)
    try:
        with httpx.Client(timeout=30, follow_redirects=True) as client:
            resp = client.get(
                "https://www.anthropic.com/news",
                headers={"User-Agent": "Mozilla/5.0 awesome-anthropic-bot/1.0"},
            )
            resp.raise_for_status()
        return extract_anthropic_items_from_html(resp.text, since)
    except Exception as e:
        print(f"[blog] Error: {e}", file=sys.stderr)
    return []


def extract_anthropic_items_from_html(html: str, since: datetime) -> list[NewsItem]:
    """Extract recent official Anthropic posts from newsroom HTML."""
    import re as _re

    date_pattern = _re.compile(
        r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
        r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
        r"\s+\d{1,2},\s+20\d\d"
    )
    official_paths = ("/news/", "/features/", "/research/", "/engineering/")

    items: list[NewsItem] = []
    soup = BeautifulSoup(html, "lxml")
    seen_hrefs: set[str] = set()
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href in seen_hrefs or not any(path in href for path in official_paths):
            continue
        seen_hrefs.add(href)

        raw_text = a_tag.get_text(" ", strip=True)
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
            raw_text = date_pattern.sub("", raw_text)

        for cat in ("Announcements", "Product", "Research", "Policy", "News", "Careers"):
            raw_text = raw_text.replace(cat, " ")
        title = " ".join(raw_text.split())[:120]
        if not title or len(title) < 5 or pub_dt < since:
            continue

        url = href if href.startswith("http") else f"https://www.anthropic.com{href}"
        items.append(
            NewsItem(
                title=title,
                url=url,
                source="Anthropic Blog",
                published_at=pub_dt.isoformat(),
                item_id=f"blog_{href.split('/')[-1]}",
            )
        )
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


def fetch_twitter_accounts(since_hours: int = 48) -> list[NewsItem]:
    """
    Fetch recent tweets from curated accounts via Nitter RSS (no API key needed).

    Tracks builders who regularly post informative Claude/Anthropic content.
    Falls back gracefully if Nitter instances are down.
    """
    import re as _re

    # Curated accounts: (handle, display_name)
    ACCOUNTS = [
        ("bcherny", "Boris Cherney"),     # Claude Code lead
        ("alexalbert__", "Alex Albert"),  # Anthropic Head of Developer Relations
        ("AnthropicAI", "Anthropic"),
    ]

    # Public Nitter instances (try in order until one works)
    NITTER_HOSTS = [
        "nitter.net",
        "nitter.privacydev.net",
        "nitter.poast.org",
    ]

    items: list[NewsItem] = []
    since = datetime.now(tz=timezone.utc) - timedelta(hours=since_hours)

    def _try_nitter(handle: str, display: str) -> list[NewsItem]:
        for host in NITTER_HOSTS:
            url = f"https://{host}/{handle}/rss"
            try:
                with httpx.Client(timeout=15, follow_redirects=True) as client:
                    resp = client.get(url, headers={"User-Agent": "awesome-anthropic-bot/1.0"})
                    if resp.status_code != 200:
                        continue
                    # Parse RSS XML
                    from xml.etree import ElementTree as ET
                    root = ET.fromstring(resp.text)
                    ns = {"dc": "http://purl.org/dc/elements/1.1/"}
                    channel = root.find("channel")
                    if channel is None:
                        continue
                    result = []
                    for item_el in channel.findall("item")[:20]:
                        title_el = item_el.find("title")
                        link_el  = item_el.find("link")
                        pub_el   = item_el.find("pubDate")
                        if title_el is None or link_el is None:
                            continue
                        raw_title = (title_el.text or "").strip()
                        # Skip retweets and replies (Nitter prefixes "RT @" and "R to @")
                        if _re.match(r"^(RT |R to @|@)", raw_title):
                            continue
                        # Strip "handle: " prefix Nitter sometimes adds
                        raw_title = _re.sub(r"^@?\w+:\s+", "", raw_title)
                        # Only keep tweets mentioning Claude/Anthropic (skip off-topic)
                        combined = raw_title.lower()
                        if not any(kw in combined for kw in ("claude", "anthropic", "llm", "ai ", "model", "agent", "code", "context")):
                            continue
                        # Normalise Nitter link → x.com, strip #m anchor
                        link = _re.sub(r"https?://[^/]+/", "https://x.com/", link_el.text or "")
                        link = link.split("#")[0]
                        pub_dt = datetime.now(tz=timezone.utc)
                        if pub_el is not None and pub_el.text:
                            try:
                                from email.utils import parsedate_to_datetime
                                pub_dt = parsedate_to_datetime(pub_el.text).astimezone(timezone.utc)
                            except Exception:
                                pass
                        if pub_dt < since:
                            continue
                        result.append(NewsItem(
                            title=raw_title[:200] or f"Tweet by {display}",
                            url=link,
                            source="X / Twitter",
                            published_at=pub_dt.isoformat(),
                            summary=display,
                            item_id=f"tweet_{handle}_{link.split('/')[-1]}",
                        ))
                    return result  # success — don't try other hosts
            except Exception as e:
                print(f"[twitter] {host}/{handle} failed: {e}", file=sys.stderr)
                continue
        return []

    for handle, display in ACCOUNTS:
        found = _try_nitter(handle, display)
        items.extend(found)
        print(f"[twitter] @{handle}: {len(found)} tweets", file=sys.stderr)

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

SIGNAL_KEYWORDS = {
    "anthropic",
    "claude",
    "sdk",
    "release",
    "policy",
    "model",
    "agent",
    "mcp",
    "security",
    "safety",
    "benchmark",
    "api",
}


def canonical_story_url(url: str) -> str:
    """Drop tracking params and normalize URL for duplicate detection."""
    try:
        parts = urlsplit((url or "").strip())
        if not parts.scheme or not parts.netloc:
            return url.strip()
        query_pairs = []
        for key, value in parse_qsl(parts.query, keep_blank_values=True):
            if key.lower().startswith("utm_"):
                continue
            if key.lower() in {"ref", "source", "s"}:
                continue
            query_pairs.append((key, value))
        query = urlencode(query_pairs, doseq=True)
        clean_path = parts.path.rstrip("/") or "/"
        return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), clean_path, query, ""))
    except Exception:
        return url.strip()


def title_fingerprint(title: str) -> str:
    """Normalize titles so near-identical reposts can be collapsed."""
    import re as _re

    cleaned = _re.sub(r"[^a-z0-9\s]", " ", title.lower())
    tokens = [t for t in cleaned.split() if t not in {"the", "a", "an", "and", "or", "to", "of"}]
    return " ".join(tokens)


def story_dedup_key(item: NewsItem) -> str:
    canonical = canonical_story_url(item.url)
    if canonical:
        return canonical
    return title_fingerprint(item.title)


def is_low_signal_story(item: NewsItem) -> bool:
    """
    Lightweight quality filter for community stories.

    We only apply this to Reddit sources to reduce low-information chatter
    while keeping official/product updates untouched.
    """
    import re as _re

    source = item.source.lower()
    if not source.startswith("r/"):
        return False

    title = item.title.strip()
    title_l = title.lower().strip(" .!?,")
    words = _re.findall(r"[a-z0-9']+", title_l)
    if not words:
        return True

    # Very short question-only headlines without domain keywords are noisy.
    if title.endswith("?") and len(words) <= 4 and not any(k in title_l for k in SIGNAL_KEYWORDS):
        return True

    # Short chatter lines with no Anthropic/Claude signal.
    if len(words) <= 3 and not any(k in title_l for k in SIGNAL_KEYWORDS):
        return True

    # Pure gratitude/reaction posts tend to be low signal for a daily digest.
    if _re.fullmatch(r"(thanks?|thank you|i m glad|i am glad)", title_l):
        return True

    # Meme-only reactions add noise unless they include concrete product signals.
    if _re.search(r"\b(yeah buddy|lightweight|lets go|we are so back)\b", title_l):
        if not any(k in title_l for k in SIGNAL_KEYWORDS):
            return True

    return False


def select_top_stories(stories: list[NewsItem], limit: int = 15, max_per_source: int = 4) -> list[NewsItem]:
    """
    Rank top stories with quality constraints:
      - remove low-signal Reddit chatter
      - collapse near-duplicate headlines across sources
      - keep source diversity by capping per-source items
    """
    ranked = sorted(stories, key=lambda x: x.score, reverse=True)
    selected: list[NewsItem] = []
    source_counts: dict[str, int] = {}
    seen_story_keys: set[str] = set()
    seen_title_fingerprints: set[str] = set()
    deferred_for_source_cap: list[NewsItem] = []

    for item in ranked:
        if is_low_signal_story(item):
            continue

        key = story_dedup_key(item)
        fp = title_fingerprint(item.title)
        if key and key in seen_story_keys:
            continue
        if fp and fp in seen_title_fingerprints:
            continue

        src_count = source_counts.get(item.source, 0)
        if src_count >= max_per_source:
            deferred_for_source_cap.append(item)
            continue

        selected.append(item)
        if key:
            seen_story_keys.add(key)
        if fp:
            seen_title_fingerprints.add(fp)
        source_counts[item.source] = src_count + 1
        if len(selected) >= limit:
            return selected

    # Backfill if strict source caps leave fewer than limit items.
    if len(selected) < limit:
        for item in deferred_for_source_cap:
            if is_low_signal_story(item):
                continue
            key = story_dedup_key(item)
            fp = title_fingerprint(item.title)
            if key and key in seen_story_keys:
                continue
            if fp and fp in seen_title_fingerprints:
                continue
            selected.append(item)
            if key:
                seen_story_keys.add(key)
            if fp:
                seen_title_fingerprints.add(fp)
            if len(selected) >= limit:
                break

    return selected


def build_primary_story_fallback(
    announcements: list[NewsItem],
    sdk_releases: list[NewsItem],
    limit: int = 5,
) -> list[NewsItem]:
    """
    Build a deterministic top-stories fallback from first-party announcements
    and SDK/tool releases when community stories are unavailable or filtered.
    """
    selected: list[NewsItem] = []
    seen_urls: set[str] = set()

    def _append(items: list[NewsItem], base_score: int, step: int) -> None:
        nonlocal selected
        rank = 0
        for item in sorted(items, key=lambda i: i.published_at, reverse=True):
            key = canonical_story_url(item.url)
            if not key or key in seen_urls:
                continue
            score = item.score if item.score > 0 else max(base_score - (rank * step), 1)
            selected.append(
                NewsItem(
                    title=item.title,
                    url=item.url,
                    source=item.source,
                    published_at=item.published_at,
                    summary=item.summary,
                    score=score,
                    item_id=item.item_id,
                )
            )
            seen_urls.add(key)
            rank += 1
            if len(selected) >= limit:
                return

    _append(announcements, base_score=100, step=5)
    if len(selected) < limit:
        _append(sdk_releases, base_score=85, step=5)
    return selected[:limit]


def upsert_news_date_section(existing: str, date_heading: str, section_markdown: str) -> str:
    """
    Ensure docs/NEWS.md contains exactly one section for `date_heading`.

    If the date already exists one or more times, remove all those sections and
    insert the latest section once at the top of the dated sections list.
    """
    import re as _re

    date_re = _re.compile(
        rf"(?ms)^##\s+{_re.escape(date_heading)}\n.*?(?=^##\s+|\Z)"
    )
    without_same_day = _re.sub(date_re, "", existing).rstrip() + "\n"
    new_section = section_markdown.rstrip() + "\n\n"

    first_section_match = _re.search(r"\n##\s+", without_same_day)
    if first_section_match:
        insert_pos = first_section_match.start() + 1
        return without_same_day[:insert_pos] + new_section + without_same_day[insert_pos:]
    return without_same_day + "\n" + new_section


def append_to_news_md(items: list[NewsItem]) -> None:
    """Write new items to NEWS.md using the section+table format the dashboard parser expects."""
    DOCS_DIR.mkdir(exist_ok=True)
    news_path = DOCS_DIR / "NEWS.md"

    # Human-readable date header (e.g. "February 26, 2026")
    today = datetime.now(tz=timezone.utc).strftime("%B %-d, %Y")

    # Categorise items
    SDK_SOURCES = {"GitHub Release", "github_release"}
    ANNOUNCE_SOURCES = {"Anthropic Blog"}
    RESEARCH_SOURCES = {"arXiv"}
    TWEET_SOURCES = {"X / Twitter"}

    stories = sorted(
        [i for i in items if i.source not in SDK_SOURCES | ANNOUNCE_SOURCES | RESEARCH_SOURCES | TWEET_SOURCES],
        key=lambda x: x.score, reverse=True,
    )
    announcements = [i for i in items if i.source in ANNOUNCE_SOURCES]
    research      = [i for i in items if i.source in RESEARCH_SOURCES]
    sdk           = [i for i in items if i.source in SDK_SOURCES]
    tweets        = [i for i in items if i.source in TWEET_SOURCES]
    stories = select_top_stories(stories, limit=15, max_per_source=4)
    if not stories:
        stories = build_primary_story_fallback(announcements=announcements, sdk_releases=sdk, limit=8)

    def _esc(s: str) -> str:
        return s.replace("|", "\\|")

    lines: list[str] = [f"## {today}", ""]

    if stories:
        lines += ["### 🔥 Top Stories", "",
                  "| Score | Title | Source |",
                  "|------:|-------|--------|"]
        for item in stories:
            lines.append(f"| {item.score} | [{_esc(item.title)}]({item.url}) | {_esc(item.source)} |")
        lines.append("")

    if announcements:
        lines += ["### 📰 Official Announcements", "",
                  "| Title | Source |",
                  "|-------|--------|"]
        for item in announcements:
            lines.append(f"| [{_esc(item.title)}]({item.url}) | {_esc(item.source)} |")
        lines.append("")

    if tweets:
        lines += ["### 🐦 From the Builders", "",
                  "| Tweet | Author |",
                  "|-------|--------|"]
        for item in tweets:
            lines.append(f"| [{_esc(item.title)}]({item.url}) | {_esc(item.summary or 'Boris Cherney')} |")
        lines.append("")

    if research:
        lines += ["### 🔬 Research", "",
                  "| Title | Source |",
                  "|-------|--------|"]
        for item in research:
            lines.append(f"| [{_esc(item.title)}]({item.url}) | {_esc(item.source)} |")
        lines.append("")

    if sdk:
        lines += ["### 🛠️ SDK & Tool Releases", "",
                  "| Release | Highlights |",
                  "|---------|------------|"]
        for item in sdk:
            notes = (item.summary or "").replace("\n", " ").replace("|", "\\|")[:100]
            lines.append(f"| [{_esc(item.title)}]({item.url}) | {notes} |")
        lines.append("")

    lines += ["---", ""]

    existing = news_path.read_text() if news_path.exists() else (
        "# Anthropic News Feed\n\n"
        "> **Updated daily** · Aggregated from Hacker News, Reddit, "
        "Anthropic Blog, arXiv, GitHub, and X/Twitter · Sorted by community engagement\n\n---\n\n"
    )
    section_text = "\n".join(lines)
    updated = upsert_news_date_section(existing, today, section_text)
    news_path.write_text(updated)


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", action="store_true", help="Print summary only, no file writes.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch but don't write.")
    args = parser.parse_args()

    print("Fetching news from all sources...", file=sys.stderr)
    if not has_network_connectivity():
        print(
            "[network] DNS/network unavailable. Skipping source fetches and keeping existing docs/NEWS.md unchanged.",
            file=sys.stderr,
        )
        if args.summary:
            print("- **Total fetched:** 0")
            print("- **New items:** 0")
            print("  - Network: unavailable")
        return

    all_items: list[NewsItem] = []
    all_items.extend(fetch_anthropic_blog())
    all_items.extend(fetch_hacker_news())
    all_items.extend(fetch_reddit())
    all_items.extend(fetch_arxiv())
    all_items.extend(fetch_github_releases())
    all_items.extend(fetch_twitter_accounts())

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
