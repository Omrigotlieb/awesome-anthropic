import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import MagicMock, patch

from scripts import email_digest as email


SAMPLE_NEWS = """# Anthropic News Feed

## February 27, 2026

### 🔥 Top Stories

| Score | Title | Source |
|------:|-------|--------|
| 500 | [Story One](https://example.com/1) | Hacker News |
| 450 | [Story Two](https://example.com/2) | r/ClaudeAI |
| 400 | [Story Three](https://example.com/3) | r/Anthropic |
| 350 | [Story Four](https://example.com/4) | Anthropic Blog |

### 📰 Official Announcements

| Title | Source |
|-------|--------|
| [Ann One](https://example.com/a1) | Anthropic Blog |
| [Ann Two](https://example.com/a2) | Anthropic Blog |
"""


class TestEmailDigest(unittest.TestCase):
    def test_parse_top_story_table(self):
        rows = email._parse_table(SAMPLE_NEWS, "🔥 Top Stories", max_rows=8)
        self.assertEqual(len(rows), 4)
        self.assertEqual(rows[0]["title"], "Story One")
        self.assertEqual(rows[1]["score"], 450)

    def test_parse_announcement_table(self):
        rows = email._parse_table(SAMPLE_NEWS, "Official Announcements", max_rows=4)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["title"], "Ann One")

    def test_get_news_date(self):
        self.assertEqual(email.get_news_date(SAMPLE_NEWS), "February 27, 2026")

    def test_build_markdown_contains_story_and_links(self):
        stories = email._parse_table(SAMPLE_NEWS, "🔥 Top Stories", max_rows=8)
        ann = email._parse_table(SAMPLE_NEWS, "Official Announcements", max_rows=4)
        md = email.build_markdown("February 27, 2026", stories, ann)
        self.assertIn("Top Stories", md)
        self.assertIn("Official Announcements", md)
        self.assertIn("Open Dashboard", md)
        self.assertIn("Story One", md)

    def test_mark_sent_and_already_sent(self):
        with tempfile.TemporaryDirectory() as td:
            sent_log = Path(td) / "last_email_sent.txt"
            with patch.object(email, "SENT_LOG", sent_log):
                self.assertFalse(email.already_sent("February 27, 2026"))
                email.mark_sent("February 27, 2026")
                self.assertTrue(email.already_sent("February 27, 2026"))

    def test_send_email_posts_to_buttondown(self):
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_client = MagicMock()
        mock_client.post.return_value = mock_resp
        with patch("scripts.email_digest.httpx.Client") as client_cls:
            client_cls.return_value.__enter__.return_value = mock_client
            email.send_email("api_key", "subject", "body")
        args, kwargs = mock_client.post.call_args
        self.assertIn("buttondown", args[0])
        self.assertEqual(kwargs["headers"]["Authorization"], "Token api_key")

    def test_main_dry_run_prints_subject_and_body(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            sent = Path(td) / "sent.txt"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(email, "NEWS_MD", news), patch.object(email, "SENT_LOG", sent), patch(
                "sys.argv", ["email_digest.py", "--dry-run"]
            ):
                buf = io.StringIO()
                with redirect_stdout(buf):
                    email.main()
            out = buf.getvalue()
            self.assertIn("DRY RUN", out)
            self.assertIn("Subject:", out)
            self.assertIn("Story One", out)

    def test_main_send_flow_marks_sent(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            sent = Path(td) / "sent.txt"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            env = dict(os.environ)
            env["BUTTONDOWN_API_KEY"] = "key"
            with patch.dict(os.environ, env, clear=True), patch.object(email, "NEWS_MD", news), patch.object(
                email, "SENT_LOG", sent
            ), patch("scripts.email_digest.send_email") as send_mock, patch("sys.argv", ["email_digest.py"]):
                email.main()
            send_mock.assert_called_once()
            self.assertTrue(sent.exists())


if __name__ == "__main__":
    unittest.main()
