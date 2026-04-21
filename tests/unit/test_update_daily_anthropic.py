import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts import update_daily_anthropic as daily


SAMPLE_NEWS = """# Anthropic News Feed

## February 27, 2026

### 🔥 Top Stories

| Score | Title | Source |
|------:|-------|--------|
| 111 | [Story One](https://example.com/1) | Hacker News |
| 99 | [Story Two](https://example.com/2) | r/ClaudeAI |
| 88 | [Story Three](https://example.com/3) | Anthropic Blog |
| 77 | [Story Four](https://example.com/4) | Anthropic Blog |

### 📰 Official Announcements

| Title | Source |
|-------|--------|
| [Official One](https://example.com/official-1) | Anthropic Blog |
| [Official Two](https://example.com/official-2) | Anthropic Blog |

### 🛠️ SDK & Tool Releases

| Release | Highlights |
|---------|------------|
| [claude-code v2.1.62](https://example.com/cc-262) | fixes |
| [anthropic-sdk-python v0.84.0](https://example.com/py-084) | update |
"""

EDITORIAL_SAMPLE_NEWS = """# Anthropic News Feed

## March 19, 2026

### 🔥 Top Stories

| Score | Title | Source |
|------:|-------|--------|
| 71 | [What 81,000 people want from AI](https://www.anthropic.com/features/81k-interviews) | Hacker News |
| 55 | [Story Two](https://example.com/2) | r/ClaudeAI |

### 🛠️ SDK & Tool Releases

| Release | Highlights |
|---------|------------|
| [claude-code v2.1.80](https://github.com/anthropics/claude-code/releases/tag/v2.1.80) | ## What's changed  - Added `rate_limits` field to statusline scripts for displaying Claude.ai rate limit usage |

---

## March 13, 2026

### 📰 Official Announcements

| Title | Source |
|-------|--------|
| [Anthropic invests $100 million into the Claude Partner Network](https://www.anthropic.com/news/claude-partner-network) | Anthropic Blog |

---

## March 12, 2026

### 📰 Official Announcements

| Title | Source |
|-------|--------|
| [Introducing The Anthropic Institute](https://www.anthropic.com/news/the-anthropic-institute) | Anthropic Blog |

---

## March 11, 2026

### 📰 Official Announcements

| Title | Source |
|-------|--------|
| [Sydney will become Anthropic’s fourth office in Asia-Pacific](https://www.anthropic.com/news/sydney-fourth-office-asia-pacific) | Anthropic Blog |
"""

RELEASE_FALLBACK_NEWS = """# Anthropic News Feed

## March 24, 2026

### 🛠️ SDK & Tool Releases

| Release | Highlights |
|---------|------------|
| [claude-code-action v1.0.77](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.77) | Subprocess environment scrubbing |

---

## March 21, 2026

### 🛠️ SDK & Tool Releases

| Release | Highlights |
|---------|------------|
| [claude-code v2.1.81](https://github.com/anthropics/claude-code/releases/tag/v2.1.81) | Added --bare and reliability fixes |
| [claude-code-action v1.0.76](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.76) | Maintenance release |
"""


class TestUpdateDailyAnthropic(unittest.TestCase):
    def test_is_anthropic_official_url_rejects_lookalike_domains(self):
        self.assertTrue(daily._is_anthropic_official_url("https://www.anthropic.com/news/claude-opus-4-7"))
        self.assertTrue(daily._is_anthropic_official_url("https://anthropic.com/news/claude-design"))
        self.assertFalse(daily._is_anthropic_official_url("https://bannedbyanthropic.com/"))
        self.assertFalse(daily._is_anthropic_official_url("https://example.com/anthropic.com/news"))

    def test_effective_section_date_prefers_carry_forward_note(self):
        section_text = (
            "> Carry-forward snapshot from **April 18, 2026** because DNS/network was unavailable during this run.\n"
        )
        self.assertEqual(daily._effective_section_date("April 19, 2026", section_text), "April 18, 2026")

    def test_read_news_date_uses_carry_forward_snapshot_date(self):
        carry_forward_news = """# Anthropic News Feed

## April 19, 2026

> Carry-forward snapshot from **April 18, 2026** because DNS/network was unavailable during this run.

### 🔥 Top Stories

| Score | Title | Source |
|------:|-------|--------|
| 100 | [Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/claude-design-anthropic-labs) | Anthropic Blog |
"""
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            news.write_text(carry_forward_news, encoding="utf-8")
            with patch.object(daily, "NEWS_PATH", news):
                self.assertEqual(daily.read_news_date(), "April 18, 2026")

    def test_read_top_stories_parses_markdown_links(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(daily, "NEWS_PATH", news):
                rows = daily.read_top_stories(limit=3)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0], "- [Story One](https://example.com/1)")
        self.assertEqual(rows[2], "- [Story Three](https://example.com/3)")

    def test_read_top_stories_empty_when_missing(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "missing.md"
            with patch.object(daily, "NEWS_PATH", news):
                rows = daily.read_top_stories(limit=3)
        self.assertEqual(rows, [])

    def test_read_section_links_parses_announcements(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(daily, "NEWS_PATH", news):
                rows = daily.read_section_links("📰 Official Announcements", title_col=0, limit=2)
        self.assertEqual(
            rows,
            [
                ("Official One", "https://example.com/official-1"),
                ("Official Two", "https://example.com/official-2"),
            ],
        )

    def test_unique_links_in_order_deduplicates_by_url(self):
        rows = [
            ("Official One", "https://example.com/official-1"),
            ("Official One duplicate", "https://example.com/official-1"),
            ("Official Two", "https://example.com/official-2"),
        ]
        self.assertEqual(
            daily.unique_links_in_order(rows, limit=3),
            [
                ("Official One", "https://example.com/official-1"),
                ("Official Two", "https://example.com/official-2"),
            ],
        )

    def test_ensure_file_creates_header_when_missing(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "DAILY_Anthropic.md"
            with patch.object(daily, "DAILY_PATH", target):
                text = daily.ensure_file()
            self.assertIn("# DAILY Anthropic Run Log", text)
            self.assertTrue(target.exists())

    def test_ensure_file_returns_existing_content(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "DAILY_Anthropic.md"
            target.write_text("custom text", encoding="utf-8")
            with patch.object(daily, "DAILY_PATH", target):
                text = daily.ensure_file()
            self.assertEqual(text, "custom text")

    def test_main_appends_entry_with_stories(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "DAILY_Anthropic.md"
            news = Path(td) / "NEWS.md"
            brief = Path(td) / "docs" / "DAILY_ANTHROPIC.md"
            blog = Path(td) / "docs" / "DAILY_BLOG.md"
            brief.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# DAILY Anthropic Run Log\n", encoding="utf-8")
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(daily, "DAILY_PATH", target), patch.object(daily, "NEWS_PATH", news), patch.object(
                daily, "DAILY_BRIEF_PATH", brief
            ), patch.object(
                daily, "DAILY_BLOG_PATH", blog
            ), patch("scripts.update_daily_anthropic.datetime") as dt_mock:
                dt_mock.now.return_value.strftime.return_value = "2026-02-27"
                dt_mock.now.return_value = dt_mock.now.return_value
                code = daily.main()
            content = target.read_text(encoding="utf-8")
            brief_content = brief.read_text(encoding="utf-8")
            blog_content = blog.read_text(encoding="utf-8")
            self.assertEqual(code, 0)
            self.assertIn("## 2026-02-27", content)
            self.assertIn("Story One", content)
            self.assertIn("# Daily Anthropic Brief", brief_content)
            self.assertIn("claude-code v2.1.62", brief_content)
            self.assertIn("# Daily Anthropic Blog Post", blog_content)
            self.assertIn("Executive Summary", blog_content)

    def test_main_is_idempotent_same_day(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "DAILY_Anthropic.md"
            news = Path(td) / "NEWS.md"
            brief = Path(td) / "docs" / "DAILY_ANTHROPIC.md"
            blog = Path(td) / "docs" / "DAILY_BLOG.md"
            brief.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# DAILY Anthropic Run Log\n\n## 2026-02-27\n", encoding="utf-8")
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(daily, "DAILY_PATH", target), patch.object(daily, "NEWS_PATH", news), patch.object(
                daily, "DAILY_BRIEF_PATH", brief
            ), patch.object(
                daily, "DAILY_BLOG_PATH", blog
            ), patch("scripts.update_daily_anthropic.datetime") as dt_mock:
                dt_mock.now.return_value.strftime.return_value = "2026-02-27"
                buf = io.StringIO()
                with redirect_stdout(buf):
                    code = daily.main()
            out = buf.getvalue()
            self.assertEqual(code, 0)
            self.assertIn("already exists", out)

    def test_main_fallback_when_news_table_missing(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "DAILY_Anthropic.md"
            news = Path(td) / "NEWS.md"
            brief = Path(td) / "docs" / "DAILY_ANTHROPIC.md"
            blog = Path(td) / "docs" / "DAILY_BLOG.md"
            brief.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# DAILY Anthropic Run Log\n", encoding="utf-8")
            news.write_text("no top stories section", encoding="utf-8")
            with patch.object(daily, "DAILY_PATH", target), patch.object(daily, "NEWS_PATH", news), patch.object(
                daily, "DAILY_BRIEF_PATH", brief
            ), patch.object(
                daily, "DAILY_BLOG_PATH", blog
            ), patch("scripts.update_daily_anthropic.datetime") as dt_mock:
                dt_mock.now.return_value.strftime.return_value = "2026-02-27"
                daily.main()
            content = target.read_text(encoding="utf-8")
            brief_content = brief.read_text(encoding="utf-8")
            self.assertIn("News table unavailable", content)
            self.assertIn("No new official announcements", brief_content)

    def test_write_daily_brief_includes_freshness_lag(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            brief = Path(td) / "docs" / "DAILY_ANTHROPIC.md"
            brief.parent.mkdir(parents=True, exist_ok=True)
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(daily, "NEWS_PATH", news), patch.object(daily, "DAILY_BRIEF_PATH", brief):
                daily.write_daily_brief("2026-03-01")
            brief_content = brief.read_text(encoding="utf-8")
            self.assertIn("Freshness Status", brief_content)
            self.assertIn("Snapshot lag: 2 day(s)", brief_content)

    def test_read_recent_section_links_walks_multiple_sections(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            news.write_text(EDITORIAL_SAMPLE_NEWS, encoding="utf-8")
            with patch.object(daily, "NEWS_PATH", news):
                rows = daily.read_recent_section_links("📰 Official Announcements", title_col=0, limit=3, max_sections=4)
        self.assertEqual(
            rows,
            [
                (
                    "Anthropic invests $100 million into the Claude Partner Network",
                    "https://www.anthropic.com/news/claude-partner-network",
                    "March 13, 2026",
                ),
                (
                    "Introducing The Anthropic Institute",
                    "https://www.anthropic.com/news/the-anthropic-institute",
                    "March 12, 2026",
                ),
                (
                    "Sydney will become Anthropic’s fourth office in Asia-Pacific",
                    "https://www.anthropic.com/news/sydney-fourth-office-asia-pacific",
                    "March 11, 2026",
                ),
            ],
        )

    def test_write_daily_blog_builds_article_deck(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            blog = Path(td) / "docs" / "DAILY_BLOG.md"
            blog.parent.mkdir(parents=True, exist_ok=True)
            news.write_text(EDITORIAL_SAMPLE_NEWS, encoding="utf-8")
            with patch.object(daily, "NEWS_PATH", news), patch.object(daily, "DAILY_BLOG_PATH", blog):
                daily.write_daily_blog("2026-03-19")
            blog_content = blog.read_text(encoding="utf-8")
            self.assertIn("### Latest News Articles", blog_content)
            self.assertIn("Article 1", blog_content)
            self.assertIn("Article 2", blog_content)
            self.assertIn("Article 3", blog_content)
            self.assertIn("Article 4", blog_content)
            self.assertIn("Article 5", blog_content)
            self.assertIn("### Source Trail", blog_content)
            self.assertIn("claude-code v2.1.80", blog_content)
            self.assertIn("rate_limits", blog_content)

    def test_find_latest_release_scans_recent_sections(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            news.write_text(RELEASE_FALLBACK_NEWS, encoding="utf-8")
            with patch.object(daily, "NEWS_PATH", news):
                row = daily.find_latest_release(prefix="claude-code ", max_sections=10)
        self.assertEqual(
            row,
            (
                "claude-code v2.1.81",
                "https://github.com/anthropics/claude-code/releases/tag/v2.1.81",
                "Added --bare and reliability fixes",
                "March 21, 2026",
            ),
        )

    def test_write_daily_blog_uses_latest_claude_code_across_sections(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            blog = Path(td) / "docs" / "DAILY_BLOG.md"
            blog.parent.mkdir(parents=True, exist_ok=True)
            news.write_text(RELEASE_FALLBACK_NEWS, encoding="utf-8")
            with patch.object(daily, "NEWS_PATH", news), patch.object(daily, "DAILY_BLOG_PATH", blog):
                daily.write_daily_blog("2026-03-25")
            blog_content = blog.read_text(encoding="utf-8")
            self.assertIn("Latest release tracked: claude-code v2.1.81.", blog_content)


if __name__ == "__main__":
    unittest.main()
