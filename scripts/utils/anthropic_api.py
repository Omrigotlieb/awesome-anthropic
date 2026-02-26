"""
AI summarization utilities.

Priority order:
  1. ANTHROPIC_API_KEY env var → use Python SDK directly
  2. `claude` CLI in PATH (not nested inside Claude Code) → use subprocess
  3. No credentials → skip summarization, use item title as fallback

This means:
  - Local runs (outside Claude Code): uses `claude` CLI with your Max subscription
  - GitHub Actions with claude installed: uses `claude` CLI
  - GitHub Actions without claude: gracefully skips (titles used as summaries)
  - Inside Claude Code sessions: skips (nested sessions are blocked by design)
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys


def _inside_claude_code() -> bool:
    """True when running as a subprocess of Claude Code."""
    return bool(os.environ.get("CLAUDECODE"))


def _claude_cli_available() -> bool:
    """True if `claude` CLI is in PATH and we're not inside a Claude Code session."""
    return not _inside_claude_code() and shutil.which("claude") is not None


def _api_key_available() -> bool:
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


def is_api_available() -> bool:
    """Return True if any summarization method is available."""
    return _api_key_available() or _claude_cli_available()


def summarize_news_item(title: str, url: str, body: str = "") -> str:
    """
    Return a one-sentence developer-oriented summary.
    Falls back to the title if no summarization method is available.
    """
    if not is_api_available():
        return title

    if _api_key_available():
        return _summarize_via_sdk(title, url, body)

    return _summarize_via_cli(title, url, body)


def batch_summarize(items: list[dict]) -> list[str]:
    """
    Summarize multiple items. Falls back to titles if nothing is available.
    """
    if not is_api_available() or not items:
        return [item.get("title", "") for item in items]

    if _api_key_available():
        return _batch_via_sdk(items)

    # CLI: summarize sequentially (batching not applicable)
    results = []
    for item in items:
        summary = _summarize_via_cli(
            title=item.get("title", ""),
            url=item.get("url", ""),
            body=item.get("body", ""),
        )
        results.append(summary)
    return results


# ---------------------------------------------------------------------------
# Implementation: Python SDK
# ---------------------------------------------------------------------------

def _summarize_via_sdk(title: str, url: str, body: str) -> str:
    try:
        import anthropic

        client = anthropic.Anthropic()
        prompt = (
            "Summarize the following news item in exactly one sentence for a developer audience. "
            "Be specific and informative. Do not start with 'This article' or 'This post'.\n\n"
            f"Title: {title}\nURL: {url}\n"
            f"Content: {body[:500] if body else 'N/A'}"
        )
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text.strip()
    except Exception:
        return title


def _batch_via_sdk(items: list[dict]) -> list[str]:
    """Use the Messages Batches API for efficient batch summarization."""
    import time

    try:
        import anthropic

        client = anthropic.Anthropic()
        batch = client.messages.batches.create(
            requests=[
                {
                    "custom_id": str(i),
                    "params": {
                        "model": "claude-haiku-4-5-20251001",
                        "max_tokens": 150,
                        "messages": [
                            {
                                "role": "user",
                                "content": (
                                    "Summarize in one sentence for developers: "
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


# ---------------------------------------------------------------------------
# Implementation: claude CLI subprocess
# ---------------------------------------------------------------------------

def _summarize_via_cli(title: str, url: str, body: str) -> str:
    """Use the `claude` CLI to summarize a single item."""
    prompt = (
        f"Summarize in one sentence for developers (be specific, no filler):\n"
        f"Title: {title}\n"
        f"URL: {url}\n"
        f"Content: {body[:400] if body else 'N/A'}\n\n"
        f"Reply with only the one-sentence summary."
    )
    try:
        result = subprocess.run(
            ["claude", "--print", "--no-notifications", "-p", prompt],
            capture_output=True,
            text=True,
            timeout=30,
            env={**os.environ, "FORCE_COLOR": "0"},
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().split("\n")[0]
    except Exception as e:
        print(f"[cli] summarize error: {e}", file=sys.stderr)
    return title
