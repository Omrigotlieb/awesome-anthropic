# GitHub Growth Backlog

`gh auth status` currently reports an invalid token for `Omrigotlieb`, so these are prepared as issue-ready follow-ups for when GitHub auth is fixed.

## P0: Configure GitHub repo metadata for discovery

**Suggested issue title:** Configure About metadata, topics, website, and custom social preview

**Why:** The repo now has stronger on-page packaging, but GitHub discovery still depends on metadata configured in the repository UI. Topics, About text, website URL, and a custom social preview improve searchability and click-through.

**Checklist**

- Set About description to a short one-line value proposition.
- Add the website URL: `https://omrigotlieb.github.io/awesome-anthropic/`
- Add relevant topics such as `anthropic`, `claude`, `claude-code`, `awesome-list`, `mcp`, `llm`, `prompt-engineering`
- Upload a custom social preview image based on `assets/img/og-awesome-anthropic.svg`
- Verify the repo card unfurl looks branded and not generic

## P0: Seed contributor-friendly GitHub issues

**Suggested issue title:** Seed `good first issue` and `help wanted` backlog for contributors

**Why:** The repo benefits from visible activity. A curated repo with no open issues looks inactive even when content updates daily.

**Checklist**

- Create 5 to 8 concrete improvement issues
- Add `good first issue` to the easiest items
- Add `help wanted` to larger follow-ups
- Include clear acceptance criteria in each issue
- Link contributors back to `CONTRIBUTING.md`

**Suggested issue candidates**

- Tighten README top stories so official launches outrank low-signal community posts
- Add a small featured resources panel above the fold on the homepage
- Add a stale-data indicator when sources lag
- Improve changelog parsing to avoid truncated entries
- Add a lightweight release cadence or monthly roundup

## P1: Pin and cross-promote the repo from the GitHub profile

**Suggested issue title:** Pin `awesome-anthropic` on the maintainer profile and cross-link from profile README

**Why:** GitHub profile traffic is high intent traffic. Pinning the repo makes it easier for visitors to discover the project and star it.

**Checklist**

- Pin the repo on the maintainer profile
- If a profile README exists, add a short callout and link
- Reuse the same one-line description as the repo About section

## P1: Create a weekly promotion cadence outside the repo

**Suggested issue title:** Publish a weekly roundup post that links back to the repo

**Why:** Daily social copy is now repo-aware, but a weekly roundup is a better format for earning attention on Hacker News, Reddit, X, and LinkedIn without looking repetitive.

**Checklist**

- Pick one weekly roundup day
- Include the best official launch, one standout builder project, one SDK release, and one research link
- Link both the dashboard and the repo
- Track which channel drives the most stars
