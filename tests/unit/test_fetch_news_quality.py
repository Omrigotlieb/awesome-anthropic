import unittest
from datetime import datetime, timezone

from scripts.fetch_news import (
    NewsItem,
    build_primary_story_fallback,
    canonical_story_url,
    ensure_primary_signal_stories,
    extract_anthropic_items_from_html,
    is_low_signal_story,
    select_top_stories,
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
    def test_canonical_story_url_drops_tracking_params(self):
        url = "https://example.com/path/?utm_source=x&ref=y&id=7#frag"
        self.assertEqual(canonical_story_url(url), "https://example.com/path?id=7")

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


if __name__ == "__main__":
    unittest.main()
