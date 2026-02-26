# Anthropic News Archive

## 2026-02-26

- [The Pentagon threatens Anthropic](https://www.astralcodexten.com/p/the-pentagon-threatens-anthropic) — Hacker News | Score: 173
  > The Pentagon threatens Anthropic
- [Launch HN: TeamOut (YC W22) – AI agent for planning company retreats](https://app.teamout.com/ai) — Hacker News | Score: 52
  > Launch HN: TeamOut (YC W22) – AI agent for planning company retreats
- [The Hater's Guide to Anthropic](https://www.wheresyoured.at/premium-the-haters-guide-to-anthropic/) — Hacker News | Score: 31
  > The Hater's Guide to Anthropic
- [Show HN: Sgai – Goal-driven multi-agent software dev (GOAL.md → working code)](https://github.com/sandgardenhq/sgai) — Hacker News | Score: 31
  > Show HN: Sgai – Goal-driven multi-agent software dev (GOAL.md → working code)
- [Show HN: OpenSwarm – Multi‑Agent Claude CLI Orchestrator for Linear/GitHub](https://github.com/Intrect-io/OpenSwarm) — Hacker News | Score: 28
  > Show HN: OpenSwarm – Multi‑Agent Claude CLI Orchestrator for Linear/GitHub
- [Anthropic and the Department of War](https://thezvi.substack.com/p/anthropic-and-the-department-of-war) — Hacker News | Score: 22
  > Anthropic and the Department of War
- [Hacker used Anthropic's Claude chatbot to attack government agencies in Mexico](https://www.engadget.com/ai/hacker-used-anthropics-claude-chatbot-to-attack-multiple-government-agencies-in-mexico-171237255.html) — Hacker News | Score: 17
  > Hacker used Anthropic's Claude chatbot to attack government agencies in Mexico
- [Hacker Used Anthropic's Claude to Steal Sensitive Mexican Data](https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data) — Hacker News | Score: 14
  > Hacker Used Anthropic's Claude to Steal Sensitive Mexican Data
- [Anthropic just released a mobile version of Claude Code called Remote Control](https://venturebeat.com/orchestration/anthropic-just-released-a-mobile-version-of-claude-code-called-remote) — Hacker News | Score: 13
  > Anthropic just released a mobile version of Claude Code called Remote Control
- [Show HN: CivBench a long-horizon AI benchmark for multi-agent games](https://clashai.live) — Hacker News | Score: 12
  > Show HN: CivBench a long-horizon AI benchmark for multi-agent games
- [Hegseth threatens to blacklist Anthropic over 'woke AI' concerns](https://www.npr.org/2026/02/24/nx-s1-5725327/pentagon-anthropic-hegseth-safety) — Hacker News | Score: 10
  > Hegseth threatens to blacklist Anthropic over 'woke AI' concerns
- [Anthropic acquires Vercept to advance Claude's computer use capabilities](https://www.anthropic.com/news/acquires-vercept) — Anthropic Blog
  > Anthropic acquires Vercept to advance Claude's computer use capabilities
- [Responsible Scaling](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy) — Anthropic Blog
  > Responsible Scaling
- [Red-Teaming Claude Opus and ChatGPT-based Security Advisors for Trusted Execution Environments](http://arxiv.org/abs/2602.19450v1) — arXiv
  > Trusted Execution Environments (TEEs) (e.g., Intel SGX and ArmTrustZone) aim to protect sensitive computation from a compromised operating system, yet real deployments remain vulnerable to microarchit
- [claude-code v2.1.59](https://github.com/anthropics/claude-code/releases/tag/v2.1.59) — GitHub Release
  > ## What's changed

- Claude automatically saves useful context to auto-memory. Manage with /memory
- Added `/copy` command to show an interactive picker when code blocks are present, allowing selection of individual code blocks or the full response.
- Improved "always allow" prefix suggestions for c
- [claude-code v2.1.58](https://github.com/anthropics/claude-code/releases/tag/v2.1.58) — GitHub Release
  > ## What's changed

- Expand Remote Control to more users

- [claude-code v2.1.56](https://github.com/anthropics/claude-code/releases/tag/v2.1.56) — GitHub Release
  > ## What's changed

- VS Code: Fixed another cause of "command 'claude-vscode.editor.openLast' not found" crashes

- [claude-code v2.1.55](https://github.com/anthropics/claude-code/releases/tag/v2.1.55) — GitHub Release
  > ## What's changed

- Fixed BashTool failing on Windows with EINVAL error

- [claude-code v2.1.53](https://github.com/anthropics/claude-code/releases/tag/v2.1.53) — GitHub Release
  > ## What's changed

- Fixed a UI flicker where user input would briefly disappear after submission before the message rendered
- Fixed bulk agent kill (ctrl+f) to send a single aggregate notification instead of one per agent, and to properly clear the command queue
- Fixed graceful shutdown sometimes
- [claude-agent-sdk-python v0.1.44](https://github.com/anthropics/claude-agent-sdk-python/releases/tag/v0.1.44) — GitHub Release
  > 
### Internal/Other Changes

- Updated bundled Claude CLI to version 2.1.59


---

**PyPI:** https://pypi.org/project/claude-agent-sdk/0.1.44/

```bash
pip install claude-agent-sdk==0.1.44
```

- [claude-agent-sdk-python v0.1.43](https://github.com/anthropics/claude-agent-sdk-python/releases/tag/v0.1.43) — GitHub Release
  > 
### Internal/Other Changes

- Updated bundled Claude CLI to version 2.1.56


---

**PyPI:** https://pypi.org/project/claude-agent-sdk/0.1.43/

```bash
pip install claude-agent-sdk==0.1.43
```

- [claude-agent-sdk-python v0.1.42](https://github.com/anthropics/claude-agent-sdk-python/releases/tag/v0.1.42) — GitHub Release
  > 
### Internal/Other Changes

- Updated bundled Claude CLI to version 2.1.55


---

**PyPI:** https://pypi.org/project/claude-agent-sdk/0.1.42/

```bash
pip install claude-agent-sdk==0.1.42
```

- [claude-agent-sdk-python v0.1.41](https://github.com/anthropics/claude-agent-sdk-python/releases/tag/v0.1.41) — GitHub Release
  > 
### Internal/Other Changes

- Updated bundled Claude CLI to version 2.1.52


---

**PyPI:** https://pypi.org/project/claude-agent-sdk/0.1.41/

```bash
pip install claude-agent-sdk==0.1.41
```

- [claude-agent-sdk-python v0.1.40](https://github.com/anthropics/claude-agent-sdk-python/releases/tag/v0.1.40) — GitHub Release
  > 
### Bug Fixes

- **Unknown message type handling**: Fixed an issue where unrecognized CLI message types (e.g., `rate_limit_event`) would crash the session by raising `MessageParseError`. Unknown message types are now silently skipped, making the SDK forward-compatible with future CLI message types 
- [claude-code-action v1.0.62](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.62) — GitHub Release
  > ## What's Changed
* Add gh.sh wrapper for gh CLI commands in issue triage workflows by @OctavianGuzu in https://github.com/anthropics/claude-code-action/pull/975


**Full Changelog**: https://github.com/anthropics/claude-code-action/compare/v1...v1.0.62
- [claude-code-action v1.0.61](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.61) — GitHub Release
  > **Full Changelog**: https://github.com/anthropics/claude-code-action/compare/v1...v1.0.61
- [claude-code-action v1.0.60](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.60) — GitHub Release
  > **Full Changelog**: https://github.com/anthropics/claude-code-action/compare/v1...v1.0.60
- [claude-code-action v1.0.59](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.59) — GitHub Release
  > **Full Changelog**: https://github.com/anthropics/claude-code-action/compare/v1...v1.0.59
- [anthropic-sdk-java v2.15.0](https://github.com/anthropics/anthropic-sdk-java/releases/tag/v2.15.0) — GitHub Release
  > ## 2.15.0 (2026-02-19)

Full Changelog: [v2.14.0...v2.15.0](https://github.com/anthropics/anthropic-sdk-java/compare/v2.14.0...v2.15.0)

### Features

* **api:** Add top-level cache control (automatic caching) ([836d140](https://github.com/anthropics/anthropic-sdk-java/commit/836d1404cc10991d4a2924f
- [anthropic-sdk-python v0.84.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.84.0) — GitHub Release
  > ## 0.84.0 (2026-02-25)

Full Changelog: [v0.83.0...v0.84.0](https://github.com/anthropics/anthropic-sdk-python/compare/v0.83.0...v0.84.0)

### Features

* **api:** change array_format to brackets ([925d2ad](https://github.com/anthropics/anthropic-sdk-python/commit/925d2ad6b76ad7c15de07b9b2768738775f
- [anthropic-sdk-python v0.83.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.83.0) — GitHub Release
  > ## 0.83.0 (2026-02-19)

Full Changelog: [v0.82.0...v0.83.0](https://github.com/anthropics/anthropic-sdk-python/compare/v0.82.0...v0.83.0)

### Features

* **api:** Add top-level cache control (automatic caching) ([a940123](https://github.com/anthropics/anthropic-sdk-python/commit/a940123da34ac33f0b6
- [claude-agent-sdk-typescript v0.2.59](https://github.com/anthropics/claude-agent-sdk-typescript/releases/tag/v0.2.59) — GitHub Release
  > ## What's changed

- Added `getSessionMessages()` function for reading a session's conversation history from its transcript file, with support for pagination via `limit` and `offset` options

## Update

```sh
npm install @anthropic-ai/claude-agent-sdk@0.2.59
# or
yarn add @anthropic-ai/claude-agent-
- [claude-agent-sdk-typescript v0.2.58](https://github.com/anthropics/claude-agent-sdk-typescript/releases/tag/v0.2.58) — GitHub Release
  > ## What's changed

- Updated to parity with Claude Code v2.1.58

## Update

```sh
npm install @anthropic-ai/claude-agent-sdk@0.2.58
# or
yarn add @anthropic-ai/claude-agent-sdk@0.2.58
# or
pnpm add @anthropic-ai/claude-agent-sdk@0.2.58
# or
bun add @anthropic-ai/claude-agent-sdk@0.2.58
```

- [claude-agent-sdk-typescript v0.2.56](https://github.com/anthropics/claude-agent-sdk-typescript/releases/tag/v0.2.56) — GitHub Release
  > ## What's changed

- Updated to parity with Claude Code v2.1.56

## Update

```sh
npm install @anthropic-ai/claude-agent-sdk@0.2.56
# or
yarn add @anthropic-ai/claude-agent-sdk@0.2.56
# or
pnpm add @anthropic-ai/claude-agent-sdk@0.2.56
# or
bun add @anthropic-ai/claude-agent-sdk@0.2.56
```

- [claude-agent-sdk-typescript v0.2.55](https://github.com/anthropics/claude-agent-sdk-typescript/releases/tag/v0.2.55) — GitHub Release
  > ## What's changed

- Updated to parity with Claude Code v2.1.55

## Update

```sh
npm install @anthropic-ai/claude-agent-sdk@0.2.55
# or
yarn add @anthropic-ai/claude-agent-sdk@0.2.55
# or
pnpm add @anthropic-ai/claude-agent-sdk@0.2.55
# or
bun add @anthropic-ai/claude-agent-sdk@0.2.55
```

- [claude-agent-sdk-typescript v0.2.53](https://github.com/anthropics/claude-agent-sdk-typescript/releases/tag/v0.2.53) — GitHub Release
  > ## What's changed

- Added `listSessions()` for discovering and listing past sessions with light metadata

## Update

```sh
npm install @anthropic-ai/claude-agent-sdk@0.2.53
# or
yarn add @anthropic-ai/claude-agent-sdk@0.2.53
# or
pnpm add @anthropic-ai/claude-agent-sdk@0.2.53
# or
bun add @anthropi
- [anthropic-sdk-csharp Anthropic-v12.8.0](https://github.com/anthropics/anthropic-sdk-csharp/releases/tag/Anthropic-v12.8.0) — GitHub Release
  > ## 12.8.0 (2026-02-19)

Full Changelog: [Anthropic-v12.7.0...Anthropic-v12.8.0](https://github.com/anthropics/anthropic-sdk-csharp/compare/Anthropic-v12.7.0...Anthropic-v12.8.0)

### Features

* **api:** Add top-level cache control (automatic caching) ([c294cb3](https://github.com/anthropics/anthrop
- [anthropic-sdk-ruby v1.23.0](https://github.com/anthropics/anthropic-sdk-ruby/releases/tag/v1.23.0) — GitHub Release
  > ## 1.23.0 (2026-02-19)

Full Changelog: [v1.22.0...v1.23.0](https://github.com/anthropics/anthropic-sdk-ruby/compare/v1.22.0...v1.23.0)

### Features

* **api:** Add top-level cache control (automatic caching) ([612806b](https://github.com/anthropics/anthropic-sdk-ruby/commit/612806bddee36afc3976fa6
- [anthropic-sdk-go v1.26.0](https://github.com/anthropics/anthropic-sdk-go/releases/tag/v1.26.0) — GitHub Release
  > ## 1.26.0 (2026-02-19)

Full Changelog: [v1.25.1...v1.26.0](https://github.com/anthropics/anthropic-sdk-go/compare/v1.25.1...v1.26.0)

### Features

* **api:** Add top-level cache control (automatic caching) ([75f9f70](https://github.com/anthropics/anthropic-sdk-go/commit/75f9f70045587c458ec2e3491b4
- [anthropic-sdk-go v1.25.1](https://github.com/anthropics/anthropic-sdk-go/releases/tag/v1.25.1) — GitHub Release
  > ## 1.25.1 (2026-02-19)

Full Changelog: [v1.25.0...v1.25.1](https://github.com/anthropics/anthropic-sdk-go/compare/v1.25.0...v1.25.1)

### Bug Fixes

* **client:** use correct format specifier for header serialization ([9115a61](https://github.com/anthropics/anthropic-sdk-go/commit/9115a6154d0b1ba94
- [anthropic-sdk-typescript vertex-sdk-v0.14.4](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/vertex-sdk-v0.14.4) — GitHub Release
  > ## 0.14.4 (2026-02-19)

Full Changelog: [vertex-sdk-v0.14.3...vertex-sdk-v0.14.4](https://github.com/anthropics/anthropic-sdk-typescript/compare/vertex-sdk-v0.14.3...vertex-sdk-v0.14.4)
- [anthropic-sdk-typescript sdk-v0.78.0](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.78.0) — GitHub Release
  > ## 0.78.0 (2026-02-19)

Full Changelog: [sdk-v0.77.0...sdk-v0.78.0](https://github.com/anthropics/anthropic-sdk-typescript/compare/sdk-v0.77.0...sdk-v0.78.0)

### Features

* **api:** Add top-level cache control (automatic caching) ([1e2f83d](https://github.com/anthropics/anthropic-sdk-typescript/co
- [anthropic-sdk-typescript bedrock-sdk-v0.26.4](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/bedrock-sdk-v0.26.4) — GitHub Release
  > ## 0.26.4 (2026-02-19)

Full Changelog: [bedrock-sdk-v0.26.3...bedrock-sdk-v0.26.4](https://github.com/anthropics/anthropic-sdk-typescript/compare/bedrock-sdk-v0.26.3...bedrock-sdk-v0.26.4)

### Bug Fixes

* **bedrock:** eliminate race condition in AWS credential resolution ([#901](https://github.co
- [anthropic-sdk-php v0.6.0](https://github.com/anthropics/anthropic-sdk-php/releases/tag/v0.6.0) — GitHub Release
  > ## 0.6.0 (2026-02-19)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/anthropics/anthropic-sdk-php/compare/v0.5.0...v0.6.0)

### Features

* add Bedrock client ([#273](https://github.com/anthropics/anthropic-sdk-php/issues/273)) ([cf8b733](https://github.com/anthropics/anthropic-sdk-php/commit

> Aggregated daily from Anthropic blog, Hacker News, Reddit, arXiv, and GitHub.
> Updated automatically by the [daily-news workflow](../.github/workflows/daily-news.yml).

To manually fetch today's news:

```bash
python scripts/fetch_news.py
```
