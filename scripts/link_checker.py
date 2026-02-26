#!/usr/bin/env python3
"""
link_checker.py - Validate all Markdown links in the repository.

Usage:
  python scripts/link_checker.py
  python scripts/link_checker.py --output /tmp/broken_links.txt
  python scripts/link_checker.py --paths README.md docs/NEWS.md
"""
from __future__ import annotations

import argparse
import asyncio
import re
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).parent.parent

# URLs to skip (anchors, shields.io, localhost, placeholders)
SKIP_PATTERNS = [
    r"^#",
    r"^https://img\.shields\.io",
    r"^https://shields\.io",
    r"^https://licensebuttons\.net",
    r"^https://awesome\.re",
    r"^https?://localhost",
    r"^https?://127\.",
    r"^https?://0\.0\.0\.0",
    r"\.\.\..*",
]

SKIP_COMPILED = [re.compile(p) for p in SKIP_PATTERNS]
CONCURRENCY = 8
TIMEOUT = 15


def should_skip(url: str) -> bool:
    return any(p.match(url) for p in SKIP_COMPILED)


def extract_urls(path: Path) -> list[tuple[str, str]]:
    """Return list of (url, source_file) from a Markdown file."""
    text = path.read_text()
    # Match [text](url) patterns
    found = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)
    results = []
    for _text, url in found:
        url = url.strip().split(" ")[0]  # Remove title attribute if present
        if url and not should_skip(url):
            results.append((url, str(path.relative_to(ROOT))))
    return results


async def check_url(url: str, client: httpx.AsyncClient) -> tuple[str, bool, int]:
    """Return (url, is_ok, status_code)."""
    for attempt in range(3):
        try:
            resp = await client.head(
                url,
                follow_redirects=True,
                headers={"User-Agent": "awesome-anthropic-linkcheck/1.0"},
                timeout=TIMEOUT,
            )
            ok = resp.status_code < 400
            if not ok and resp.status_code == 405:
                # HEAD not allowed, try GET
                resp = await client.get(url, follow_redirects=True, timeout=TIMEOUT)
                ok = resp.status_code < 400
            return url, ok, resp.status_code
        except httpx.TimeoutException:
            if attempt == 2:
                return url, False, 408
            await asyncio.sleep(2 ** attempt)
        except Exception:
            return url, False, 0
    return url, False, 0


async def run_checks(urls: list[tuple[str, str]]) -> list[tuple[str, str, int]]:
    """Check all URLs concurrently. Returns broken (url, source_file, status)."""
    sem = asyncio.Semaphore(CONCURRENCY)
    broken = []

    async with httpx.AsyncClient() as client:
        async def bounded_check(url: str, src: str):
            async with sem:
                url_, ok, code = await check_url(url, client)
                if not ok:
                    broken.append((url_, src, code))
                    print(f"  BROKEN [{code}] {url_} (in {src})", file=sys.stderr)
                else:
                    print(f"  OK     [{code}] {url_}", file=sys.stderr)

        tasks = [bounded_check(url, src) for url, src in urls]
        await asyncio.gather(*tasks)

    return broken


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, help="File to write broken links to.")
    parser.add_argument("--paths", nargs="*", help="Specific files to check.")
    args = parser.parse_args()

    if args.paths:
        md_files = [ROOT / p for p in args.paths]
    else:
        md_files = list(ROOT.glob("README.md")) + list((ROOT / "docs").glob("*.md"))

    all_urls: list[tuple[str, str]] = []
    for f in md_files:
        if f.exists():
            all_urls.extend(extract_urls(f))

    # Deduplicate by URL
    seen = set()
    unique_urls = []
    for url, src in all_urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append((url, src))

    print(f"Checking {len(unique_urls)} unique URLs...", file=sys.stderr)
    broken = asyncio.run(run_checks(unique_urls))

    if broken:
        output_lines = [f"{code}\t{url}\t({src})" for url, src, code in broken]
        print("\nBroken links:")
        for line in output_lines:
            print(line)
        if args.output:
            Path(args.output).write_text("\n".join(output_lines))
        sys.exit(1)
    else:
        print("All links OK!")
        if args.output:
            Path(args.output).write_text("")


if __name__ == "__main__":
    main()
