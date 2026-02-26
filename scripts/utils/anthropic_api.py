"""Thin wrapper around the Anthropic SDK for summarization tasks."""
from __future__ import annotations

import os


def is_api_available() -> bool:
    """Check if the Anthropic API key is configured."""
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


def summarize_news_item(title: str, url: str, body: str = "") -> str:
    """
    Return a one-sentence developer-oriented summary of a news item.
    Falls back to returning the title if the API is unavailable.
    """
    if not is_api_available():
        return title

    try:
        import anthropic

        client = anthropic.Anthropic()
        prompt = (
            f"Summarize the following news item in exactly one sentence for a developer audience. "
            f"Be specific and informative. Do not start with 'This article' or 'This post'.\n\n"
            f"Title: {title}\nURL: {url}\n"
            f"Content snippet: {body[:500] if body else 'N/A'}"
        )
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text.strip()
    except Exception:
        return title


def batch_summarize(items: list[dict]) -> list[str]:
    """
    Summarize multiple news items using the Messages Batches API.
    Each item should have 'title', 'url', and optionally 'body' keys.
    Falls back to returning titles if the API is unavailable.
    """
    if not is_api_available() or not items:
        return [item.get("title", "") for item in items]

    try:
        import anthropic

        client = anthropic.Anthropic()
        requests = []
        for i, item in enumerate(items):
            body = item.get("body", "")[:500]
            requests.append(
                anthropic.types.MessageCreateParamsNonStreaming(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=150,
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Summarize in one sentence for developers: "
                                f"Title: {item.get('title', '')}. Content: {body}"
                            ),
                        }
                    ],
                )
            )

        batch = client.messages.batches.create(
            requests=[
                {"custom_id": str(i), "params": req}
                for i, req in enumerate(requests)
            ]
        )

        # Poll until complete (for small batches this is quick)
        import time

        while batch.processing_status == "in_progress":
            time.sleep(5)
            batch = client.messages.batches.retrieve(batch.id)

        results = [""] * len(items)
        for result in client.messages.batches.results(batch.id):
            idx = int(result.custom_id)
            if result.result.type == "succeeded":
                results[idx] = result.result.message.content[0].text.strip()
            else:
                results[idx] = items[idx].get("title", "")
        return results

    except Exception:
        return [item.get("title", "") for item in items]
