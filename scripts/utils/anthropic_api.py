"""Thin wrapper around the Anthropic SDK for summarization tasks.

Authentication priority:
  1. ANTHROPIC_API_KEY env var (standard API key from console.anthropic.com)
  2. Claude Code OAuth credentials from ~/.claude/credentials.json (Max subscription)
"""
from __future__ import annotations

import json
import os
from pathlib import Path


def _get_claude_code_token() -> str | None:
    """Read the OAuth access token from Claude Code credentials."""
    creds_path = Path.home() / ".claude" / "credentials.json"
    if not creds_path.exists():
        return None
    try:
        data = json.loads(creds_path.read_text())
        return data.get("claudeAiOauth", {}).get("accessToken")
    except Exception:
        return None


def _resolve_key() -> tuple[str, str]:
    """
    Return (api_key, method) where method is 'api_key', 'session_token', or 'oauth'.
    Raises RuntimeError if no credentials are found.
    """
    # 1. Standard API key from console.anthropic.com
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        return api_key, "api_key"

    # 2. Claude Code session token (injected automatically when running inside Claude Code)
    session_token = os.environ.get("CLAUDE_CODE_SESSION_ACCESS_TOKEN")
    if session_token:
        return session_token, "session_token"

    # 3. Claude Code OAuth token from credentials file
    oauth_token = _get_claude_code_token()
    if oauth_token:
        return oauth_token, "oauth"

    raise RuntimeError(
        "No Anthropic credentials found. Set ANTHROPIC_API_KEY or run inside Claude Code."
    )


def _make_client():
    """Create an Anthropic client using available credentials."""
    import anthropic

    key, method = _resolve_key()
    if method == "api_key":
        return anthropic.Anthropic(api_key=key)
    # Session tokens and OAuth tokens use Bearer auth
    return anthropic.Anthropic(auth_token=key)


def is_api_available() -> bool:
    """Check if any Anthropic credentials are available."""
    try:
        _resolve_key()
        return True
    except RuntimeError:
        return False


def _default_model() -> str:
    """Pick the summarization model."""
    return "claude-haiku-4-5-20251001"


def summarize_news_item(title: str, url: str, body: str = "") -> str:
    """
    Return a one-sentence developer-oriented summary of a news item.
    Falls back to returning the title if no credentials are available.
    """
    if not is_api_available():
        return title

    try:
        client = _make_client()
        prompt = (
            "Summarize the following news item in exactly one sentence for a developer audience. "
            "Be specific and informative. Do not start with 'This article' or 'This post'.\n\n"
            f"Title: {title}\nURL: {url}\n"
            f"Content snippet: {body[:500] if body else 'N/A'}"
        )
        message = client.messages.create(
            model=_default_model(),
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text.strip()
    except Exception:
        return title


def batch_summarize(items: list[dict]) -> list[str]:
    """
    Summarize multiple news items.
    When using Claude Code OAuth, summarizes sequentially (batches API not available via claude.ai).
    Falls back to returning titles if no credentials are available.
    """
    if not is_api_available() or not items:
        return [item.get("title", "") for item in items]

    # If we have a standard API key, use the efficient Batches API
    if os.environ.get("ANTHROPIC_API_KEY"):
        return _batch_via_api(items)

    # Claude Code OAuth: sequential summarization
    results = []
    for item in items:
        summary = summarize_news_item(
            title=item.get("title", ""),
            url=item.get("url", ""),
            body=item.get("body", ""),
        )
        results.append(summary)
    return results


def _batch_via_api(items: list[dict]) -> list[str]:
    """Use the Messages Batches API (requires standard API key)."""
    import time
    import anthropic

    try:
        client = anthropic.Anthropic()
        model = "claude-haiku-4-5-20251001"

        batch = client.messages.batches.create(
            requests=[
                {
                    "custom_id": str(i),
                    "params": {
                        "model": model,
                        "max_tokens": 150,
                        "messages": [
                            {
                                "role": "user",
                                "content": (
                                    f"Summarize in one sentence for developers: "
                                    f"Title: {item.get('title', '')}. "
                                    f"Content: {item.get('body', '')[:500]}"
                                ),
                            }
                        ],
                    },
                }
                for i, item in enumerate(items)
            ]
        )

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
