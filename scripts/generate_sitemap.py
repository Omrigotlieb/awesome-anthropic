#!/usr/bin/env python3
"""
generate_sitemap.py — Generate sitemap.xml for the Awesome Anthropic GitHub Pages site.

Produces an XML sitemap covering all main pages.
Run after content updates to keep sitemap fresh.

Usage:
  python scripts/generate_sitemap.py
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT   = Path(__file__).parent.parent
OUTPUT = ROOT / "sitemap.xml"

BASE_URL = "https://omrigotlieb.github.io/awesome-anthropic"

# Static pages with their relative hash-route equivalents
# Priority: 1.0 = most important, 0.5 = standard
PAGES: list[dict[str, str | float]] = [
    {"loc": f"{BASE_URL}/",              "route": "/",                     "changefreq": "daily",   "priority": 1.0},
    {"loc": f"{BASE_URL}/#/docs/NEWS",   "route": "/#/docs/NEWS",          "changefreq": "daily",   "priority": 0.9},
    {"loc": f"{BASE_URL}/#/docs/CHANGELOG", "route": "/#/docs/CHANGELOG",  "changefreq": "daily",   "priority": 0.8},
    {"loc": f"{BASE_URL}/#/README",      "route": "/#/README",             "changefreq": "weekly",  "priority": 0.8},
    {"loc": f"{BASE_URL}/#/docs/BENCHMARKS", "route": "/#/docs/BENCHMARKS","changefreq": "weekly",  "priority": 0.7},
    {"loc": f"{BASE_URL}/#/docs/CLAUDE_CODE","route": "/#/docs/CLAUDE_CODE","changefreq": "weekly",  "priority": 0.7},
    {"loc": f"{BASE_URL}/#/docs/INTERVIEW",  "route": "/#/docs/INTERVIEW",  "changefreq": "monthly", "priority": 0.6},
    {"loc": f"{BASE_URL}/#/docs/PROMPTS",    "route": "/#/docs/PROMPTS",    "changefreq": "weekly",  "priority": 0.7},
    {"loc": f"{BASE_URL}/#/docs/TOOLS",      "route": "/#/docs/TOOLS",      "changefreq": "weekly",  "priority": 0.7},
]

# Auto-discover doc files to catch new pages
DOCS_DIR = ROOT / "docs"
KNOWN_ROUTES = {p["route"] for p in PAGES}


def discover_docs() -> list[dict[str, str | float]]:
    """Add any docs/*.md files not already in the static list."""
    extra = []
    for md in sorted(DOCS_DIR.glob("*.md")):
        route = f"/#/docs/{md.stem}"
        if route not in KNOWN_ROUTES and not md.stem.startswith("_"):
            extra.append({
                "loc": f"{BASE_URL}/{route}",
                "route": route,
                "changefreq": "monthly",
                "priority": 0.5,
            })
    return extra


def build_sitemap(pages: list[dict[str, str | float]], lastmod: str) -> str:
    items = []
    for page in pages:
        items.append(
            f"  <url>\n"
            f"    <loc>{page['loc']}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            f"    <changefreq>{page['changefreq']}</changefreq>\n"
            f"    <priority>{page['priority']}</priority>\n"
            f"  </url>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(items)
        + "\n</urlset>\n"
    )


def main() -> None:
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    all_pages = PAGES + discover_docs()
    xml = build_sitemap(all_pages, today)
    OUTPUT.write_text(xml, encoding="utf-8")
    print(f"[sitemap] Generated {OUTPUT} with {len(all_pages)} URLs.", file=sys.stderr)


if __name__ == "__main__":
    main()
