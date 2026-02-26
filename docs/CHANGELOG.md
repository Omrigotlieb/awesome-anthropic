# Anthropic Changelog

> Auto-synced from [docs.anthropic.com/en/release-notes](https://docs.anthropic.com/en/release-notes/overview). Updated every 6 hours.

---

## February 19, 2026 — Automatic Caching + Model Retirements

**Automatic prompt caching** is now available on the Messages API. Add a single `cache_control` field and the system automatically caches the last cacheable block, moving the cache point forward as conversations grow. No manual breakpoint management required. Available on the Claude API and Azure AI Foundry (preview). [Learn more →](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

**Model retirements:**
- `claude-3-7-sonnet-20250219` (Sonnet 3.7) — retired, upgrade to **Claude Sonnet 4.6**
- `claude-3-5-haiku-20241022` (Haiku 3.5) — retired, upgrade to **Claude Haiku 4.5**
- `claude-3-haiku-20240307` (Haiku 3) — deprecation announced, retirement **April 19, 2026**, upgrade to **Claude Haiku 4.5**

---

## February 17, 2026 — Claude Sonnet 4.6 Launch

**Claude Sonnet 4.6** launched — improved agentic search performance, fewer tokens consumed. Supports extended thinking and 1M token context window (beta). [See Models & Pricing →](https://docs.anthropic.com/en/docs/about-claude/models)

**API updates (all GA, no beta header required):**
- Code execution is now **free when used with web search or web fetch**
- Web search tool + programmatic tool calling → generally available
- Web search now supports **dynamic filtering** via code execution
- Code execution, web fetch, tool search, tool use examples, memory tool → all GA

---

## February 7, 2026 — Fast Mode for Opus 4.6 (Research Preview)

**Fast mode** launched in research preview for Opus 4.6 — up to **2.5× faster** output token generation via the `speed` parameter, at premium pricing.

---

## February 5, 2026 — Claude Opus 4.6 Launch

**Claude Opus 4.6** — most intelligent model for complex agentic tasks and long-horizon work.
- Uses `thinking: {type: "adaptive"}` by default (manual `budget_tokens` deprecated)
- Does not support prefilling assistant messages
- [What's new in Claude 4.6 →](https://docs.anthropic.com/en/docs/about-claude/models)

**`effort` parameter** → now GA on all platforms, replaces `budget_tokens` for controlling thinking depth.

**Compaction API** (beta) — server-side context summarization for effectively infinite conversations.

**Data residency controls** — specify inference geography via `inference_geo` parameter. US-only inference available at 1.1× pricing.

---

## February 1, 2026 — 1M Token Context Window Beta

- **1M token context window** now in beta for Claude Opus 4.6, Sonnet 4.5, and Sonnet 4. Long context pricing applies above 200K input tokens.
- **Fine-grained tool streaming** → GA on all models and platforms.
- `output_format` parameter moved to `output_config.format`.

---

## January 29, 2026 — Structured Outputs GA

**Structured outputs** now generally available on the Claude API for Sonnet 4.5, Opus 4.5, and Haiku 4.5.
- Expanded schema support
- Improved grammar compilation latency
- No beta header required
- `output_format` moved to `output_config.format`
- Still in beta on Amazon Bedrock and Microsoft Foundry

---

## January 12, 2026 — Claude Console Moves to platform.claude.com

`console.anthropic.com` now redirects to `platform.claude.com`. Existing bookmarks and links continue working.

---

## January 5, 2026 — Claude Opus 3 Retired

`claude-3-opus-20240229` retired. All requests return an error. Upgrade to **Claude Opus 4.5** — significantly improved intelligence at one-third the cost. Researchers can request ongoing access via the External Researcher Access Program.

---

## December 19, 2025 — Claude Haiku 3.5 Deprecation Announced

`claude-3-5-haiku-20241022` deprecation announced. [Migration guide →](https://docs.anthropic.com/en/docs/resources/model-deprecations)

---

## November 24, 2025 — Claude Opus 4.5 Launch

**Claude Opus 4.5** — step-change improvements in vision, coding, and computer use at a more accessible price point than Opus 3.

New features launched same day:
- **Programmatic tool calling** (beta) — call tools from within code execution
- **Tool search tool** (beta) — dynamically discover tools from large catalogs
- **`effort` parameter** (beta) for Opus 4.5 — control token usage vs. thoroughness
- **Client-side compaction** in Python and TypeScript SDKs

---

[View full release notes on Anthropic Docs →](https://docs.anthropic.com/en/release-notes/overview)
