#!/usr/bin/env python3
"""
update_readme.py - Injects auto-generated content into README.md placeholder zones.

Zones in README.md:
  <!-- NEWS_START --> ... <!-- NEWS_END -->
  <!-- CHANGELOG_START --> ... <!-- CHANGELOG_END -->
  <!-- NEWS_DATE -->
  <!-- CHANGELOG_DATE -->

Usage:
  python scripts/update_readme.py --section NEWS
  python scripts/update_readme.py --section CHANGELOG
  python scripts/update_readme.py --section ALL
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
README = ROOT / "README.md"
DOCS_DIR = ROOT / "docs"

NEWS_MAX_ITEMS = 5
CHANGELOG_MAX_ENTRIES = 3


def inject_zone(text: str, section: str, content: str) -> str:
    pattern = rf"(<!-- {section}_START -->).*?(<!-- {section}_END -->)"
    replacement = rf"\1\n{content}\n\2"
    new_text, count = re.subn(pattern, replacement, text, flags=re.DOTALL)
    if count == 0:
        print(f"[update_readme] Warning: zone <!-- {section}_START --> not found in README.", file=sys.stderr)
    return new_text


def get_news_preview() -> str:
    """Extract top items from the score table in NEWS.md as an awesome-lint-compliant list."""
    news_path = DOCS_DIR / "NEWS.md"
    if not news_path.exists():
        return "_No news items yet. Run `python scripts/fetch_news.py` to populate._"

    text = news_path.read_text()

    # Extract date heading (first ## heading)
    date_heading = ""
    for line in text.splitlines():
        if line.startswith("## "):
            date_heading = line.lstrip("# ").strip()
            break

    # Extract rows only from the first "🔥 Top Stories" table (newest section).
    table_lines: list[str] = []
    found_top = False
    for line in text.splitlines():
        if not found_top:
            if "🔥 Top Stories" in line:
                found_top = True
            continue
        stripped = line.strip()
        if stripped.startswith("## ") or stripped == "---":
            break
        table_lines.append(line)

    rows: list[tuple[str, str, str]] = []
    header_passed = False
    for line in table_lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if header_passed:
                break
            continue
        if re.match(r"^[|\s:>\-]+$", stripped):
            header_passed = True
            continue
        if not header_passed:
            continue

        cols = [c.strip() for c in stripped.split("|")[1:-1]]
        if len(cols) < 3:
            continue
        score = cols[0]
        link = cols[1]
        source = cols[2]
        if re.match(r"^\d+$", score):
            rows.append((score, link, source))

    if not rows:
        return "_No recent news items found._"

    # Sort by score descending, take top N
    rows_sorted = sorted(rows, key=lambda r: int(r[0]), reverse=True)[:NEWS_MAX_ITEMS]

    heading = f"### Top Stories — {date_heading}" if date_heading else "### Top Stories"
    lines = [heading, ""]
    for score, link, source in rows_sorted:
        source = source.strip()
        lines.append(f"- {link} - {score} pts on {source}.")

    lines.append("")
    lines.append("[Full news feed →](docs/NEWS.md)")
    return "\n".join(lines)


def get_changelog_preview() -> str:
    """Extract entry titles as bold text — no bullets, no links, no h2 headings."""
    cl_path = DOCS_DIR / "CHANGELOG.md"
    if not cl_path.exists():
        return "_Changelog not yet synced. Run `python scripts/check_changelog.py` to populate._"

    titles: list[str] = []
    for line in cl_path.read_text().splitlines():
        if line.startswith("## "):
            titles.append(line[3:].strip())
            if len(titles) >= CHANGELOG_MAX_ENTRIES:
                break

    if not titles:
        return "_No changelog entries yet._"

    lines: list[str] = []
    for title in titles:
        lines.append(f"### {title}")
        lines.append("")
    lines.append("[Full changelog →](docs/CHANGELOG.md)")
    return "\n".join(lines)


def update_date_inline(text: str, zone: str) -> str:
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    return re.sub(
        rf"<!-- {zone}_DATE -->.*?(?=\n|$)",
        f"<!-- {zone}_DATE -->{today}",
        text,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--section", choices=["NEWS", "CHANGELOG", "ALL"], default="ALL")
    args = parser.parse_args()

    if not README.exists():
        print(f"[update_readme] README.md not found at {README}", file=sys.stderr)
        sys.exit(1)

    text = README.read_text()

    if args.section in ("NEWS", "ALL"):
        content = get_news_preview()
        text = inject_zone(text, "NEWS", content)
        text = update_date_inline(text, "NEWS")

    if args.section in ("CHANGELOG", "ALL"):
        content = get_changelog_preview()
        text = inject_zone(text, "CHANGELOG", content)
        text = update_date_inline(text, "CHANGELOG")

    README.write_text(text)
    print(f"[update_readme] README.md updated (section={args.section}).", file=sys.stderr)


if __name__ == "__main__":
    main()
