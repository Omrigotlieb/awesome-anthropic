"""Markdown formatting utilities shared across scripts."""
from __future__ import annotations

from datetime import datetime


def date_header(date: datetime | str) -> str:
    """Return a level-2 Markdown date header."""
    if isinstance(date, datetime):
        date = date.strftime("%Y-%m-%d")
    return f"## {date}"


def news_item_to_md(title: str, url: str, source: str, summary: str = "", score: int = 0) -> str:
    """Format a news item as a Markdown list entry."""
    score_str = f" | Score: {score}" if score > 0 else ""
    lines = [f"- [{title}]({url}) — {source}{score_str}"]
    if summary:
        lines.append(f"  > {summary}")
    return "\n".join(lines)


def changelog_entry_to_md(date: str, title: str, content: str) -> str:
    """Format a changelog entry as Markdown."""
    lines = [f"### {date}: {title}", ""]
    lines.append(content.strip())
    return "\n".join(lines)


def section_divider() -> str:
    return "---"
