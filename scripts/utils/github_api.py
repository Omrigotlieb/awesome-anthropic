"""GitHub API helpers for fetching Anthropic org activity."""
from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Any

import httpx


BASE_URL = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def _auth_headers() -> dict:
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return {**HEADERS, "Authorization": f"Bearer {token}"}
    return HEADERS


def get_org_releases(org: str = "anthropics", since_days: int = 7) -> list[dict[str, Any]]:
    """Fetch recent releases from all repos in an org."""
    since = datetime.now(tz=timezone.utc) - timedelta(days=since_days)
    releases = []

    with httpx.Client(timeout=30, headers=_auth_headers()) as client:
        # Get all repos
        resp = client.get(f"{BASE_URL}/orgs/{org}/repos", params={"per_page": 100, "sort": "updated"})
        if resp.status_code != 200:
            return releases
        repos = resp.json()

        for repo in repos:
            if repo.get("archived") or repo.get("fork"):
                continue
            rel_resp = client.get(
                f"{BASE_URL}/repos/{org}/{repo['name']}/releases",
                params={"per_page": 5},
            )
            if rel_resp.status_code != 200:
                continue
            for rel in rel_resp.json():
                published = rel.get("published_at")
                if not published:
                    continue
                pub_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
                if pub_dt >= since:
                    releases.append(
                        {
                            "title": f"{repo['name']} {rel['tag_name']}",
                            "url": rel["html_url"],
                            "published_at": pub_dt,
                            "source": "github_release",
                            "body": (rel.get("body") or "")[:300],
                        }
                    )
    return releases
