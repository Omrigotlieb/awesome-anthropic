import unittest
import socket
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

from scripts.fetch_news import (
    NewsItem,
    _collect_recent_primary_signal_rows,
    _ensure_carry_forward_official_announcements,
    _rebuild_carry_forward_top_stories,
    _strip_existing_carry_forward_note,
    build_primary_story_fallback,
    canonical_story_url,
    ensure_primary_signal_stories,
    extract_claude_code_changelog_items_from_html,
    extract_anthropic_items_from_html,
    has_network_connectivity,
    is_low_signal_story,
    select_top_stories,
    sort_stories_for_output,
    title_fingerprint,
    upsert_news_date_section,
)


def mk(
    title: str,
    source: str = "r/ClaudeAI",
    score: int = 100,
    url: str = "https://example.com/story",
    published_at: str = "2026-02-27T00:00:00+00:00",
) -> NewsItem:
    return NewsItem(
        title=title,
        url=url,
        source=source,
        score=score,
        published_at=published_at,
    )


class TestFetchNewsQuality(unittest.TestCase):
    class _FakeResponse:
        def __init__(self, text: str):
            self.text = text

        def raise_for_status(self):
            return None

    class _FakeClient:
        def __init__(self, html_by_url: dict[str, str]):
            self.html_by_url = html_by_url

        def get(self, url: str, **_kwargs):
            return TestFetchNewsQuality._FakeResponse(self.html_by_url.get(url, "<html></html>"))

    def test_canonical_story_url_drops_tracking_params(self):
        url = "https://example.com/path/?utm_source=x&ref=y&id=7#frag"
        self.assertEqual(canonical_story_url(url), "https://example.com/path?id=7")

    def test_has_network_connectivity_prefers_http_probe(self):
        client = MagicMock()
        client.__enter__.return_value = client
        client.get.return_value.status_code = 204

        with patch("scripts.fetch_news.httpx.Client", return_value=client):
            with patch("scripts.fetch_news.socket.getaddrinfo", side_effect=socket.gaierror()):
                self.assertTrue(has_network_connectivity(probe_urls=("https://example.com/ok",)))

    def test_has_network_connectivity_falls_back_to_dns(self):
        client = MagicMock()
        client.__enter__.return_value = client
        client.get.side_effect = RuntimeError("probe failed")

        def fake_getaddrinfo(host, *_args, **_kwargs):
            if host == "github.com":
                return [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", ("1.1.1.1", 443))]
            raise socket.gaierror()

        with patch("scripts.fetch_news.httpx.Client", return_value=client):
            with patch("scripts.fetch_news.socket.getaddrinfo", side_effect=fake_getaddrinfo):
                self.assertTrue(has_network_connectivity(probe_urls=("https://example.com/err",)))

    def test_has_network_connectivity_returns_false_when_all_checks_fail(self):
        client = MagicMock()
        client.__enter__.return_value = client
        client.get.side_effect = RuntimeError("probe failed")

        with patch("scripts.fetch_news.httpx.Client", return_value=client):
            with patch("scripts.fetch_news.socket.getaddrinfo", side_effect=socket.gaierror()):
                self.assertFalse(has_network_connectivity(probe_urls=("https://example.com/err",)))

    def test_title_fingerprint_normalizes_punctuation_and_articles(self):
        fp = title_fingerprint("The Claude, SDK: Release!")
        self.assertEqual(fp, "claude sdk release")

    def test_low_signal_not_applied_to_non_reddit(self):
        item = mk("Thank you", source="Hacker News")
        self.assertFalse(is_low_signal_story(item))

    def test_low_signal_short_question_without_keywords(self):
        item = mk("Thoughts?")
        self.assertTrue(is_low_signal_story(item))

    def test_not_low_signal_when_keywords_present(self):
        item = mk("Claude memory feature?", source="r/ClaudeAI")
        self.assertFalse(is_low_signal_story(item))

    def test_low_signal_gratitude_reaction(self):
        item = mk("thank you")
        self.assertTrue(is_low_signal_story(item))

    def test_low_signal_meme_without_keywords(self):
        item = mk("Yeah buddy... Lightweight!!!")
        self.assertTrue(is_low_signal_story(item))

    def test_select_top_stories_collapses_duplicate_titles(self):
        stories = [
            mk("Claude 4.6 released", source="Hacker News", score=500, url="https://a"),
            mk("Claude 4.6 released", source="r/ClaudeAI", score=450, url="https://b"),
            mk("Anthropic security update", source="Hacker News", score=400, url="https://c"),
        ]
        selected = select_top_stories(stories, limit=10, max_per_source=4)
        self.assertEqual(len(selected), 2)
        self.assertEqual(selected[0].source, "Hacker News")
        self.assertEqual(selected[1].title, "Anthropic security update")

    def test_select_top_stories_collapses_duplicate_urls(self):
        stories = [
            mk("Release note thread", source="r/ClaudeAI", score=600, url="https://example.com/r?id=1&utm_source=reddit"),
            mk("Release note thread on HN", source="Hacker News", score=700, url="https://example.com/r?id=1"),
            mk("Another unique item", source="Hacker News", score=500, url="https://example.com/u?id=2"),
        ]
        selected = select_top_stories(stories, limit=10, max_per_source=4)
        self.assertEqual(len(selected), 2)
        self.assertEqual(selected[0].title, "Release note thread on HN")

    def test_select_top_stories_applies_source_cap_with_backfill(self):
        stories = [
            mk("Claude release S1", source="r/ClaudeAI", score=500, url="https://1"),
            mk("Claude release S2", source="r/ClaudeAI", score=490, url="https://2"),
            mk("Claude release S3", source="r/ClaudeAI", score=480, url="https://3"),
            mk("Claude release S4", source="r/ClaudeAI", score=470, url="https://4"),
            mk("Claude release S5", source="r/ClaudeAI", score=460, url="https://5"),
            mk("Unique HN", source="Hacker News", score=450, url="https://6"),
        ]
        selected = select_top_stories(stories, limit=6, max_per_source=2)
        # cap keeps top 2 from source first, then backfill allows additional if needed
        self.assertEqual(len(selected), 6)
        self.assertEqual(selected[0].title, "Claude release S1")
        self.assertEqual(selected[1].title, "Claude release S2")
        self.assertTrue(any(s.source == "Hacker News" for s in selected))

    def test_select_top_stories_filters_low_signal(self):
        stories = [
            mk("thank you", source="r/ClaudeAI", score=900, url="https://1"),
            mk("Claude Code release notes", source="r/ClaudeAI", score=800, url="https://2"),
            mk("Anthropic policy update", source="Hacker News", score=700, url="https://3"),
        ]
        selected = select_top_stories(stories, limit=5, max_per_source=4)
        titles = [s.title for s in selected]
        self.assertNotIn("thank you", titles)
        self.assertIn("Claude Code release notes", titles)
        self.assertIn("Anthropic policy update", titles)

    def test_sort_stories_for_output_orders_by_score_then_date(self):
        stories = [
            mk(
                "Older high score",
                source="r/ClaudeAI",
                score=500,
                url="https://example.com/1",
                published_at="2026-04-01T00:00:00+00:00",
            ),
            mk(
                "Newer high score",
                source="r/ClaudeAI",
                score=500,
                url="https://example.com/2",
                published_at="2026-04-02T00:00:00+00:00",
            ),
            mk(
                "Lower score",
                source="Hacker News",
                score=300,
                url="https://example.com/3",
                published_at="2026-04-03T00:00:00+00:00",
            ),
        ]
        ordered = sort_stories_for_output(stories)
        self.assertEqual([s.title for s in ordered], ["Newer high score", "Older high score", "Lower score"])

    def test_primary_story_fallback_prefers_announcements_then_releases(self):
        announcements = [
            mk(
                "What 81,000 people want from AI",
                source="Anthropic Blog",
                score=0,
                url="https://www.anthropic.com/features/81k-interviews",
                published_at="2026-03-18T00:00:00+00:00",
            )
        ]
        releases = [
            mk(
                "claude-code v2.1.87",
                source="GitHub Release",
                score=0,
                url="https://github.com/anthropics/claude-code/releases/tag/v2.1.87",
                published_at="2026-03-29T00:00:00+00:00",
            )
        ]
        selected = build_primary_story_fallback(announcements, releases, limit=3)
        self.assertEqual(len(selected), 2)
        self.assertEqual(selected[0].source, "Anthropic Blog")
        self.assertEqual(selected[1].source, "GitHub Release")
        self.assertGreater(selected[0].score, selected[1].score)

    def test_primary_story_fallback_prefers_newer_claude_code_versions(self):
        announcements = []
        releases = [
            mk(
                "claude-code v2.1.109",
                source="GitHub Release",
                score=0,
                url="https://github.com/anthropics/claude-code/releases/tag/v2.1.109",
                published_at="2026-04-15T00:00:00+00:00",
            ),
            mk(
                "claude-code v2.1.110",
                source="GitHub Release",
                score=0,
                url="https://github.com/anthropics/claude-code/releases/tag/v2.1.110",
                published_at="2026-04-15T00:00:00+00:00",
            ),
            mk(
                "claude-code-action v1.0.97",
                source="GitHub Release",
                score=0,
                url="https://github.com/anthropics/claude-code-action/releases/tag/v1.0.97",
                published_at="2026-04-15T00:00:00+00:00",
            ),
        ]
        selected = build_primary_story_fallback(announcements, releases, limit=3)
        self.assertEqual(
            [item.title for item in selected],
            ["claude-code v2.1.110", "claude-code-action v1.0.97"],
        )

    def test_primary_story_fallback_dedupes_same_title_across_sources(self):
        announcements = [
            mk(
                "Introducing Claude Opus 4.7",
                source="Anthropic Blog",
                score=0,
                url="https://www.anthropic.com/news/claude-opus-4-7",
                published_at="2026-04-17T00:00:00+00:00",
            )
        ]
        releases = [
            mk(
                "Introducing Claude Opus 4.7",
                source="GitHub Release",
                score=0,
                url="https://example.com/mirror/claude-opus-4-7",
                published_at="2026-04-17T00:00:00+00:00",
            ),
            mk(
                "claude-code v2.1.116",
                source="GitHub Release",
                score=0,
                url="https://github.com/anthropics/claude-code/releases/tag/v2.1.116",
                published_at="2026-04-21T00:00:00+00:00",
            ),
        ]
        selected = build_primary_story_fallback(announcements, releases, limit=5)
        self.assertEqual([item.title for item in selected].count("Introducing Claude Opus 4.7"), 1)
        self.assertIn("claude-code v2.1.116", [item.title for item in selected])

    def test_ensure_primary_signal_stories_injects_release_when_missing(self):
        stories = [
            mk("Community story 1", source="r/ClaudeAI", score=900, url="https://example.com/s1"),
            mk("Community story 2", source="r/ClaudeAI", score=800, url="https://example.com/s2"),
            mk("Community story 3", source="Hacker News", score=700, url="https://example.com/s3"),
        ]
        announcements = []
        releases = [
            mk(
                "claude-code v2.1.90",
                source="GitHub Release",
                score=0,
                url="https://github.com/anthropics/claude-code/releases/tag/v2.1.90",
                published_at="2026-04-02T00:00:00+00:00",
            )
        ]
        selected = ensure_primary_signal_stories(
            stories=stories,
            announcements=announcements,
            sdk_releases=releases,
            min_count=1,
            max_total=3,
        )
        self.assertEqual(len(selected), 3)
        self.assertTrue(any(s.source == "GitHub Release" for s in selected))

    def test_ensure_primary_signal_stories_keeps_existing_primary(self):
        stories = [
            mk(
                "Australian government and Anthropic sign MOU for AI safety and research",
                source="Anthropic Blog",
                score=120,
                url="https://www.anthropic.com/news/australia-MOU",
                published_at="2026-03-31T00:00:00+00:00",
            ),
            mk("Community story", source="r/ClaudeAI", score=100, url="https://example.com/s1"),
        ]
        selected = ensure_primary_signal_stories(
            stories=stories,
            announcements=[],
            sdk_releases=[],
            min_count=1,
            max_total=2,
        )
        self.assertEqual([s.url for s in selected], [s.url for s in stories])

    def test_upsert_news_date_section_inserts_when_missing(self):
        existing = (
            "# Anthropic News Feed\n\n"
            "> Intro\n\n"
            "---\n\n"
            "## March 22, 2026\n\n"
            "A\n"
        )
        section = "## March 23, 2026\n\nB\n\n---"
        updated = upsert_news_date_section(existing, "March 23, 2026", section)
        self.assertIn("## March 23, 2026", updated)
        self.assertEqual(updated.count("## March 23, 2026"), 1)
        self.assertLess(updated.find("## March 23, 2026"), updated.find("## March 22, 2026"))

    def test_upsert_news_date_section_replaces_duplicate_same_day_sections(self):
        existing = (
            "# Anthropic News Feed\n\n"
            "---\n\n"
            "## March 23, 2026\n\nOld A\n\n---\n\n"
            "## March 22, 2026\n\nOlder\n\n---\n\n"
            "## March 23, 2026\n\nOld B\n\n---\n"
        )
        section = "## March 23, 2026\n\nFresh block\n\n---"
        updated = upsert_news_date_section(existing, "March 23, 2026", section)
        self.assertEqual(updated.count("## March 23, 2026"), 1)
        self.assertIn("Fresh block", updated)
        self.assertNotIn("Old A", updated)
        self.assertNotIn("Old B", updated)

    def test_extract_anthropic_items_includes_features_posts(self):
        html = """
        <html><body>
          <a href="/features/81k-interviews">Product Mar 21, 2026 What 81,000 people want from AI</a>
          <a href="/news/claude-partner-network">Announcements Mar 12, 2026 Anthropic invests $100 million into the Claude Partner Network</a>
          <a href="https://example.com/off-topic">Mar 21, 2026 unrelated link</a>
        </body></html>
        """
        since = datetime(2026, 3, 1, tzinfo=timezone.utc)
        items = extract_anthropic_items_from_html(html, since=since)
        urls = [item.url for item in items]

        self.assertIn("https://www.anthropic.com/features/81k-interviews", urls)
        self.assertIn("https://www.anthropic.com/news/claude-partner-network", urls)
        self.assertNotIn("https://example.com/off-topic", urls)

    def test_extract_anthropic_items_includes_event_posts(self):
        html = """
        <html><body>
          <a href="/events/anthropic-at-google-cloud-next-2026">Events Apr 22, 2026 Anthropic at Google Cloud Next 2026</a>
          <a href="/careers/jobs">Careers Apr 22, 2026 Join us</a>
        </body></html>
        """
        since = datetime(2026, 4, 1, tzinfo=timezone.utc)
        items = extract_anthropic_items_from_html(html, since=since)
        urls = [item.url for item in items]
        event_sources = {item.url: item.source for item in items}

        self.assertIn("https://www.anthropic.com/events/anthropic-at-google-cloud-next-2026", urls)
        self.assertEqual(
            event_sources["https://www.anthropic.com/events/anthropic-at-google-cloud-next-2026"],
            "Anthropic Events",
        )
        self.assertNotIn("https://www.anthropic.com/careers/jobs", urls)

    def test_extract_anthropic_items_respects_since_filter(self):
        html = """
        <html><body>
          <a href="/news/old-item">Announcements Feb 10, 2026 Older post</a>
          <a href="/news/new-item">Announcements Mar 12, 2026 Newer post</a>
        </body></html>
        """
        since = datetime(2026, 3, 1, tzinfo=timezone.utc)
        items = extract_anthropic_items_from_html(html, since=since)
        urls = [item.url for item in items]

        self.assertNotIn("https://www.anthropic.com/news/old-item", urls)
        self.assertIn("https://www.anthropic.com/news/new-item", urls)

    def test_extract_anthropic_items_includes_glasswing_page(self):
        html = """
        <html><body>
          <a href="/glasswing">Announcements Apr 7, 2026 Project Glasswing: Securing critical software for the AI era</a>
          <a href="/about">About Anthropic</a>
        </body></html>
        """
        since = datetime(2026, 4, 1, tzinfo=timezone.utc)
        items = extract_anthropic_items_from_html(html, since=since)
        urls = [item.url for item in items]

        self.assertIn("https://www.anthropic.com/glasswing", urls)
        self.assertNotIn("https://www.anthropic.com/about", urls)

    def test_extract_anthropic_items_prefers_official_page_metadata_title(self):
        html = """
        <html><body>
          <a href="/glasswing">
            Announcements Apr 7, 2026
            Project Glasswing A new initiative that brings together Amazon Web Services and others
          </a>
        </body></html>
        """
        client = self._FakeClient(
            {
                "https://www.anthropic.com/glasswing": (
                    "<html><head>"
                    "<meta property='og:title' content='Project Glasswing: Securing critical software for the AI era'/>"
                    "</head><body></body></html>"
                )
            }
        )
        since = datetime(2026, 4, 1, tzinfo=timezone.utc)
        items = extract_anthropic_items_from_html(html, since=since, client=client)

        self.assertEqual(items[0].title, "Project Glasswing: Securing critical software for the AI era")

    def test_extract_claude_code_changelog_items_parses_recent_versions(self):
        html = """
        <html><body>
          <h2>2.1.105</h2>
          <p>April 13, 2026</p>
          <ul><li>Fixed issue A</li></ul>
          <h2>2.1.101</h2>
          <p>April 10, 2026</p>
          <h2>2.1.90</h2>
          <p>March 31, 2026</p>
        </body></html>
        """
        since = datetime(2026, 4, 1, tzinfo=timezone.utc)
        items = extract_claude_code_changelog_items_from_html(html, since=since)
        self.assertEqual([item.title for item in items], ["claude-code v2.1.105", "claude-code v2.1.101"])
        self.assertEqual(items[0].source, "Claude Code Changelog")
        self.assertTrue(items[0].url.startswith("https://code.claude.com/docs/en/changelog?version=2.1.105"))

    def test_ensure_primary_signal_stories_accepts_claude_code_changelog_source(self):
        stories = [
            mk("Community story 1", source="r/ClaudeAI", score=900, url="https://example.com/s1"),
            mk("Community story 2", source="r/ClaudeAI", score=800, url="https://example.com/s2"),
            mk("Community story 3", source="Hacker News", score=700, url="https://example.com/s3"),
        ]
        releases = [
            mk(
                "claude-code v2.1.105",
                source="Claude Code Changelog",
                score=0,
                url="https://code.claude.com/docs/en/changelog?version=2.1.105",
                published_at="2026-04-13T00:00:00+00:00",
            )
        ]
        selected = ensure_primary_signal_stories(
            stories=stories,
            announcements=[],
            sdk_releases=releases,
            min_count=1,
            max_total=3,
        )
        self.assertEqual(len(selected), 3)
        self.assertTrue(any(s.source == "Claude Code Changelog" for s in selected))

    def test_strip_existing_carry_forward_note(self):
        body = (
            "> Carry-forward snapshot from **April 9, 2026** because DNS/network was unavailable during this run.\n\n"
            "### 🔥 Top Stories\n\n"
            "| Score | Title | Source |\n"
        )
        cleaned = _strip_existing_carry_forward_note(body)
        self.assertTrue(cleaned.startswith("### 🔥 Top Stories"))
        self.assertNotIn("Carry-forward snapshot", cleaned)

    def test_rebuild_carry_forward_top_stories_prefers_primary_signal(self):
        body = (
            "### 🔥 Top Stories\n\n"
            "| Score | Title | Source |\n"
            "|------:|-------|--------|\n"
            "| 999 | [Rumor headline](https://reddit.com/r/ClaudeAI/comments/x) | r/ClaudeAI |\n\n"
            "### 📰 Official Announcements\n\n"
            "| Title | Source |\n"
            "|-------|--------|\n"
            "| [Project Glasswing](https://www.anthropic.com/glasswing) | Anthropic Blog |\n\n"
            "### 🛠️ SDK & Tool Releases\n\n"
            "| Release | Highlights |\n"
            "|---------|------------|\n"
            "| [claude-code v2.1.100](https://github.com/anthropics/claude-code/releases/tag/v2.1.100) | Stable update |\n"
        )
        rebuilt = _rebuild_carry_forward_top_stories(body, "April 10, 2026")
        self.assertIn("Project Glasswing", rebuilt)
        self.assertIn("claude-code v2.1.100", rebuilt)
        self.assertNotIn("Rumor headline", rebuilt)

    def test_rebuild_carry_forward_top_stories_no_primary_signal_keeps_original(self):
        body = (
            "### 🔥 Top Stories\n\n"
            "| Score | Title | Source |\n"
            "|------:|-------|--------|\n"
            "| 100 | [Community thread](https://reddit.com/r/ClaudeAI/comments/y) | r/ClaudeAI |\n"
        )
        rebuilt = _rebuild_carry_forward_top_stories(body, "April 10, 2026")
        self.assertEqual(rebuilt, body)

    def test_rebuild_carry_forward_top_stories_uses_recent_section_fallback(self):
        body = (
            "### 🔥 Top Stories\n\n"
            "| Score | Title | Source |\n"
            "|------:|-------|--------|\n"
            "| 100 | [Community thread](https://reddit.com/r/ClaudeAI/comments/y) | r/ClaudeAI |\n"
        )
        existing_news = (
            "## April 11, 2026\n\n"
            "### 📰 Official Announcements\n\n"
            "| Title | Source |\n"
            "|-------|--------|\n"
            "| [Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents-in-practice) | Anthropic Blog |\n\n"
            "### 🛠️ SDK & Tool Releases\n\n"
            "| Release | Highlights |\n"
            "|---------|------------|\n"
            "| [claude-code v2.1.101](https://github.com/anthropics/claude-code/releases/tag/v2.1.101) | Added team onboarding command |\n\n"
            "---\n\n"
            "## April 10, 2026\n\n"
            "Older section\n"
        )
        announcements, releases = _collect_recent_primary_signal_rows(existing_news, max_sections=3)
        rebuilt = _rebuild_carry_forward_top_stories(
            body,
            "April 12, 2026",
            fallback_announcements=announcements,
            fallback_releases=releases,
        )
        self.assertIn("Trustworthy agents in practice", rebuilt)
        self.assertIn("claude-code v2.1.101", rebuilt)
        self.assertNotIn("Community thread", rebuilt)

    def test_rebuild_carry_forward_top_stories_keeps_latest_per_release_family(self):
        body = (
            "### 🔥 Top Stories\n\n"
            "| Score | Title | Source |\n"
            "|------:|-------|--------|\n"
            "| 100 | [Community thread](https://reddit.com/r/ClaudeAI/comments/y) | r/ClaudeAI |\n\n"
            "### 🛠️ SDK & Tool Releases\n\n"
            "| Release | Highlights |\n"
            "|---------|------------|\n"
            "| [claude-code v2.1.118](https://github.com/anthropics/claude-code/releases/tag/v2.1.118) | Latest |\n"
            "| [claude-code v2.1.117](https://github.com/anthropics/claude-code/releases/tag/v2.1.117) | Previous |\n"
            "| [claude-code-action v1.0.104](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.104) | Latest action |\n"
            "| [claude-code-action v1.0.103](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.103) | Previous action |\n"
        )
        rebuilt = _rebuild_carry_forward_top_stories(body, "April 23, 2026")
        top_stories_block = rebuilt.split("### 🛠️ SDK & Tool Releases", 1)[0]
        self.assertIn("claude-code v2.1.118", rebuilt)
        self.assertIn("claude-code-action v1.0.104", rebuilt)
        self.assertNotIn("claude-code v2.1.117", top_stories_block)
        self.assertNotIn("claude-code-action v1.0.103", top_stories_block)

    def test_rebuild_carry_forward_top_stories_preserves_section_divider(self):
        body = (
            "### 🔥 Top Stories\n\n"
            "| Score | Title | Source |\n"
            "|------:|-------|--------|\n"
            "| 999 | [Rumor headline](https://reddit.com/r/ClaudeAI/comments/x) | r/ClaudeAI |\n\n"
            "### 📰 Official Announcements\n\n"
            "| Title | Source |\n"
            "|-------|--------|\n"
            "| [Project Glasswing](https://www.anthropic.com/glasswing) | Anthropic Blog |\n\n"
            "### 🛠️ SDK & Tool Releases\n\n"
            "| Release | Highlights |\n"
            "|---------|------------|\n"
            "| [claude-code v2.1.100](https://github.com/anthropics/claude-code/releases/tag/v2.1.100) | Stable update |\n\n"
            "---\n"
        )
        rebuilt = _rebuild_carry_forward_top_stories(body, "April 10, 2026")
        self.assertIn("---", rebuilt)
        self.assertTrue(rebuilt.rstrip().endswith("---"))

    def test_ensure_carry_forward_official_announcements_inserts_when_missing(self):
        body = (
            "### 🔥 Top Stories\n\n"
            "| Score | Title | Source |\n"
            "|------:|-------|--------|\n"
            "| 90 | [claude-code v2.1.101](https://github.com/anthropics/claude-code/releases/tag/v2.1.101) | GitHub Release |\n\n"
            "### 🛠️ SDK & Tool Releases\n\n"
            "| Release | Highlights |\n"
            "|---------|------------|\n"
            "| [claude-code v2.1.101](https://github.com/anthropics/claude-code/releases/tag/v2.1.101) | Added team onboarding command |\n"
        )
        fallback_announcements = [
            mk(
                "Anthropic’s Long-Term Benefit Trust appoints Vas Narasimhan to Board of Directors",
                source="Anthropic Blog",
                score=100,
                url="https://www.anthropic.com/news/narasimhan-board",
                published_at="2026-04-14T00:00:00+00:00",
            )
        ]
        updated = _ensure_carry_forward_official_announcements(
            body,
            fallback_announcements=fallback_announcements,
        )
        self.assertIn("### 📰 Official Announcements", updated)
        self.assertIn("narasimhan-board", updated)

    def test_ensure_carry_forward_official_announcements_keeps_existing_block(self):
        body = (
            "### 🔥 Top Stories\n\n"
            "| Score | Title | Source |\n"
            "|------:|-------|--------|\n"
            "| 90 | [Project Glasswing](https://www.anthropic.com/glasswing) | Anthropic Blog |\n\n"
            "### 📰 Official Announcements\n\n"
            "| Title | Source |\n"
            "|-------|--------|\n"
            "| [Project Glasswing](https://www.anthropic.com/glasswing) | Anthropic Blog |\n"
        )
        fallback_announcements = [
            mk(
                "Anthropic’s Long-Term Benefit Trust appoints Vas Narasimhan to Board of Directors",
                source="Anthropic Blog",
                score=100,
                url="https://www.anthropic.com/news/narasimhan-board",
                published_at="2026-04-14T00:00:00+00:00",
            )
        ]
        updated = _ensure_carry_forward_official_announcements(
            body,
            fallback_announcements=fallback_announcements,
        )
        self.assertEqual(updated.count("### 📰 Official Announcements"), 1)
        self.assertNotIn("narasimhan-board", updated)


if __name__ == "__main__":
    unittest.main()
