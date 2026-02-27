import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import MagicMock, patch

from scripts import notify_telegram as telegram


SAMPLE_NEWS = """# Anthropic News Feed

## February 27, 2026

### 🔥 Top Stories

| Score | Title | Source |
|------:|-------|--------|
| 500 | [Story One](https://example.com/1) | Hacker News |
| 450 | [Story Two](https://example.com/2) | r/ClaudeAI |
| 400 | [Story Three](https://example.com/3) | r/Anthropic |
| 350 | [Story Four](https://example.com/4) | Anthropic Blog |
| 300 | [Story Five](https://example.com/5) | Anthropic Blog |
| 250 | [Story Six](https://example.com/6) | Anthropic Blog |
"""


class TestNotifyTelegram(unittest.TestCase):
    def test_parse_top_stories_respects_max(self):
        rows = telegram.parse_top_stories(SAMPLE_NEWS)
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0]["title"], "Story One")
        self.assertEqual(rows[4]["score"], 300)

    def test_get_news_date(self):
        self.assertEqual(telegram.get_news_date(SAMPLE_NEWS), "February 27, 2026")

    def test_build_message_contains_expected_sections(self):
        stories = telegram.parse_top_stories(SAMPLE_NEWS)
        msg = telegram.build_message("February 27, 2026", stories)
        self.assertIn("Top Stories", msg)
        self.assertIn("Full dashboard", msg)
        self.assertIn("Subscribe via RSS", msg)

    def test_mark_sent_and_already_sent(self):
        with tempfile.TemporaryDirectory() as td:
            sent_log = Path(td) / "last_telegram_sent.txt"
            with patch.object(telegram, "SENT_LOG", sent_log):
                self.assertFalse(telegram.already_sent("February 27, 2026"))
                telegram.mark_sent("February 27, 2026")
                self.assertTrue(telegram.already_sent("February 27, 2026"))

    def test_send_message_posts_with_html_mode(self):
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"ok": True}
        mock_client = MagicMock()
        mock_client.post.return_value = mock_resp
        with patch("scripts.notify_telegram.httpx.Client") as client_cls:
            client_cls.return_value.__enter__.return_value = mock_client
            telegram.send_message("token", "@channel", "hello")
        args, kwargs = mock_client.post.call_args
        self.assertIn("sendMessage", args[0])
        self.assertEqual(kwargs["json"]["parse_mode"], "HTML")

    def test_main_dry_run_prints_content(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            sent = Path(td) / "sent.txt"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(telegram, "NEWS_MD", news), patch.object(telegram, "SENT_LOG", sent), patch(
                "sys.argv", ["notify_telegram.py", "--dry-run"]
            ):
                buf = io.StringIO()
                with redirect_stdout(buf):
                    telegram.main()
            out = buf.getvalue()
            self.assertIn("DRY RUN", out)
            self.assertIn("Story One", out)

    def test_main_send_flow_marks_sent(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            sent = Path(td) / "sent.txt"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            env = dict(os.environ)
            env["TELEGRAM_BOT_TOKEN"] = "token"
            env["TELEGRAM_CHANNEL_ID"] = "@channel"
            with patch.dict(os.environ, env, clear=True), patch.object(telegram, "NEWS_MD", news), patch.object(
                telegram, "SENT_LOG", sent
            ), patch("scripts.notify_telegram.send_message") as send_mock, patch(
                "sys.argv", ["notify_telegram.py"]
            ):
                telegram.main()
            send_mock.assert_called_once()
            self.assertTrue(sent.exists())


if __name__ == "__main__":
    unittest.main()
