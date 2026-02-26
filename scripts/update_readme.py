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
    news_path = DOCS_DIR / "NEWS.md"
    if not news_path.exists():
        return "_No news items yet. Run `python scripts/fetch_news.py` to populate._"

    lines = news_path.read_text().splitlines()
    preview_lines = []
    item_count = 0
    in_section = False

    for line in lines:
        if line.startswith("## ") and not in_section:
            in_section = True
            preview_lines.append(line)
            continue
        if in_section:
            if line.startswith("## ") and item_count >= NEWS_MAX_ITEMS:
                break
            if line.startswith("- "):
                item_count += 1
            if item_count > NEWS_MAX_ITEMS:
                break
            preview_lines.append(line)

    if not preview_lines:
        return "_No recent news items found._"

    preview = "\n".join(preview_lines).strip()
    preview += f"\n\n[View all news →](docs/NEWS.md)"
    return preview


def get_changelog_preview() -> str:
    cl_path = DOCS_DIR / "CHANGELOG.md"
    if not cl_path.exists():
        return "_Changelog not yet synced. Run `python scripts/check_changelog.py` to populate._"

    lines = cl_path.read_text().splitlines()
    preview_lines = []
    entry_count = 0

    for line in lines:
        if line.startswith("### "):
            entry_count += 1
            if entry_count > CHANGELOG_MAX_ENTRIES:
                break
        if entry_count > 0:
            preview_lines.append(line)
        if line.startswith("---") and entry_count >= CHANGELOG_MAX_ENTRIES:
            break

    if not preview_lines:
        return "_No changelog entries yet._"

    preview = "\n".join(preview_lines).strip()
    preview += f"\n\n[Full changelog history →](docs/CHANGELOG.md)"
    return preview


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
