import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import update_readme


class TestUpdateReadme(unittest.TestCase):
    def test_get_news_snapshot_iso_date_from_latest_heading(self):
        with tempfile.TemporaryDirectory() as td:
            docs = Path(td) / "docs"
            docs.mkdir(parents=True, exist_ok=True)
            news = docs / "NEWS.md"
            news.write_text(
                "# Anthropic News Feed\n\n## April 5, 2026\n\n### 🔥 Top Stories\n",
                encoding="utf-8",
            )
            with patch.object(update_readme, "DOCS_DIR", docs):
                self.assertEqual(update_readme.get_news_snapshot_iso_date(), "2026-04-05")

    def test_get_news_snapshot_iso_date_none_when_missing_or_unparseable(self):
        with tempfile.TemporaryDirectory() as td:
            docs = Path(td) / "docs"
            docs.mkdir(parents=True, exist_ok=True)
            with patch.object(update_readme, "DOCS_DIR", docs):
                self.assertIsNone(update_readme.get_news_snapshot_iso_date())

            news = docs / "NEWS.md"
            news.write_text("# Anthropic News Feed\n\n## Latest Snapshot\n", encoding="utf-8")
            with patch.object(update_readme, "DOCS_DIR", docs):
                self.assertIsNone(update_readme.get_news_snapshot_iso_date())

    def test_update_date_inline_uses_explicit_value(self):
        text = "> Last fetched: <!-- NEWS_DATE -->2026-04-04\n"
        updated = update_readme.update_date_inline(text, "NEWS", "2026-04-05")
        self.assertIn("<!-- NEWS_DATE -->2026-04-05", updated)


if __name__ == "__main__":
    unittest.main()
