import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import generate_social_posts as social


SAMPLE_NEWS = """# Anthropic News Feed

## February 27, 2026

### 🔥 Top Stories

| Score | Title | Source |
|------:|-------|--------|
| 100 | [Story One](https://example.com/1) | Hacker News |
| 90 | [Story Two](https://example.com/2) | r/ClaudeAI |
| 80 | [Story Three](https://example.com/3) | r/Anthropic |
| 70 | [Story Four](https://example.com/4) | Anthropic Blog |

### 📰 Official Announcements

| Title | Source |
|-------|--------|
| [Ann One](https://example.com/a1) | Anthropic Blog |
| [Ann Two](https://example.com/a2) | Anthropic Blog |
| [Ann Three](https://example.com/a3) | Anthropic Blog |
"""


class TestGenerateSocialPosts(unittest.TestCase):
    def test_parse_date_from_heading(self):
        got = social.parse_date(SAMPLE_NEWS)
        self.assertEqual(got, "February 27, 2026")

    def test_parse_date_fallback(self):
        got = social.parse_date("# no heading")
        self.assertRegex(got, r"^[A-Za-z]+ \d{1,2}, \d{4}$")

    def test_parse_top_stories_respects_limit(self):
        rows = social.parse_top_stories(SAMPLE_NEWS, max_rows=3)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0]["title"], "Story One")
        self.assertEqual(rows[1]["score"], 90)

    def test_parse_top_stories_empty_without_section(self):
        rows = social.parse_top_stories("no table", max_rows=3)
        self.assertEqual(rows, [])

    def test_parse_announcements_respects_limit(self):
        rows = social.parse_announcements(SAMPLE_NEWS, max_rows=2)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["title"], "Ann One")
        self.assertEqual(rows[1]["url"], "https://example.com/a2")

    def test_parse_announcements_empty_without_section(self):
        rows = social.parse_announcements("no announcements", max_rows=2)
        self.assertEqual(rows, [])

    def test_build_markdown_contains_all_channels(self):
        stories = social.parse_top_stories(SAMPLE_NEWS, max_rows=3)
        ann = social.parse_announcements(SAMPLE_NEWS, max_rows=2)
        out = social.build_markdown("February 27, 2026", stories, ann)
        self.assertIn("## X / Twitter", out)
        self.assertIn("## LinkedIn", out)
        self.assertIn("## Reddit", out)
        self.assertIn("## Hacker News", out)
        self.assertIn("Story One", out)
        self.assertIn(social.REPO_URL, out)

    def test_build_markdown_fallback_text_when_empty(self):
        out = social.build_markdown("February 27, 2026", [], [])
        self.assertIn("Top Claude + Anthropic story", out)
        self.assertIn("Official Anthropic announcement", out)

    def test_main_writes_expected_output_files(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            news = tmp / "NEWS.md"
            out_root = tmp / "distribution"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(social, "NEWS_MD", news), patch.object(social, "OUT_ROOT", out_root):
                code = social.main()
            self.assertEqual(code, 0)
            self.assertTrue((out_root / "latest_social_posts.md").exists())
            day_dirs = [p for p in out_root.iterdir() if p.is_dir()]
            self.assertEqual(len(day_dirs), 1)
            self.assertTrue((day_dirs[0] / "social_posts.md").exists())

    def test_main_skips_when_news_missing(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            news = tmp / "missing.md"
            out_root = tmp / "distribution"
            with patch.object(social, "NEWS_MD", news), patch.object(social, "OUT_ROOT", out_root):
                code = social.main()
            self.assertEqual(code, 0)
            self.assertFalse(out_root.exists())


if __name__ == "__main__":
    unittest.main()
