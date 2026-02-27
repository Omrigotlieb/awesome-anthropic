import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import MagicMock, patch

from scripts import notify_discord as discord


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


class TestNotifyDiscord(unittest.TestCase):
    def test_parse_top_stories_max_five(self):
        rows = discord.parse_top_stories(SAMPLE_NEWS)
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0]["title"], "Story One")
        self.assertEqual(rows[4]["score"], 300)

    def test_parse_top_stories_empty_when_missing(self):
        self.assertEqual(discord.parse_top_stories("no section"), [])

    def test_get_news_date_parses_heading(self):
        self.assertEqual(discord.get_news_date(SAMPLE_NEWS), "February 27, 2026")

    def test_get_news_date_fallback_format(self):
        got = discord.get_news_date("missing date")
        self.assertRegex(got, r"^[A-Za-z]+ \d{1,2}, \d{4}$")

    def test_mark_sent_and_already_sent(self):
        with tempfile.TemporaryDirectory() as td:
            sent_log = Path(td) / "last_discord_sent.txt"
            with patch.object(discord, "SENT_LOG", sent_log):
                self.assertFalse(discord.already_sent("February 27, 2026"))
                discord.mark_sent("February 27, 2026")
                self.assertTrue(discord.already_sent("February 27, 2026"))

    def test_build_message_contains_links(self):
        stories = discord.parse_top_stories(SAMPLE_NEWS)
        msg = discord.build_message("February 27, 2026", stories)
        self.assertIn("Dashboard:", msg)
        self.assertIn("RSS:", msg)
        self.assertIn("Story One", msg)

    def test_build_message_truncates_to_discord_limit(self):
        long_story = {
            "score": 1,
            "title": "A" * 3000,
            "href": "https://example.com/long",
            "source": "Hacker News",
        }
        msg = discord.build_message("February 27, 2026", [long_story] * 5)
        self.assertLessEqual(len(msg), 1990)

    def test_send_message_posts_via_httpx(self):
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_client = MagicMock()
        mock_client.post.return_value = mock_resp
        with patch("scripts.notify_discord.httpx.Client") as client_cls:
            client_cls.return_value.__enter__.return_value = mock_client
            discord.send_message("https://discord.example/hook", "hello")
        mock_client.post.assert_called_once()

    def test_main_dry_run_prints_message(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            sent = Path(td) / "sent.txt"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            with patch.object(discord, "NEWS_MD", news), patch.object(discord, "SENT_LOG", sent), patch(
                "sys.argv", ["notify_discord.py", "--dry-run"]
            ):
                buf = io.StringIO()
                with redirect_stdout(buf):
                    discord.main()
            out = buf.getvalue()
            self.assertIn("DRY RUN", out)
            self.assertIn("Story One", out)

    def test_main_skips_when_news_missing(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "missing.md"
            sent = Path(td) / "sent.txt"
            with patch.object(discord, "NEWS_MD", news), patch.object(discord, "SENT_LOG", sent), patch(
                "sys.argv", ["notify_discord.py"]
            ):
                discord.main()
            self.assertFalse(sent.exists())

    def test_main_send_flow_marks_sent(self):
        with tempfile.TemporaryDirectory() as td:
            news = Path(td) / "NEWS.md"
            sent = Path(td) / "sent.txt"
            news.write_text(SAMPLE_NEWS, encoding="utf-8")
            env = dict(os.environ)
            env["DISCORD_WEBHOOK_URL"] = "https://discord.example/hook"
            with patch.dict(os.environ, env, clear=True), patch.object(discord, "NEWS_MD", news), patch.object(
                discord, "SENT_LOG", sent
            ), patch("scripts.notify_discord.send_message") as send_mock, patch("sys.argv", ["notify_discord.py"]):
                discord.main()
            send_mock.assert_called_once()
            self.assertTrue(sent.exists())


if __name__ == "__main__":
    unittest.main()
