# Awesome Anthropic [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

[![GitHub Stars](https://img.shields.io/github/stars/Omrigotlieb/awesome-anthropic?style=flat-square&logo=github&color=yellow)](https://github.com/Omrigotlieb/awesome-anthropic/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Omrigotlieb/awesome-anthropic?style=flat-square&color=green)](https://github.com/Omrigotlieb/awesome-anthropic/commits/main)
[![Daily Update](https://img.shields.io/badge/auto--updated-daily-blue?style=flat-square)](https://omrigotlieb.github.io/awesome-anthropic)
[![Contributors](https://img.shields.io/github/contributors/Omrigotlieb/awesome-anthropic?style=flat-square)](https://github.com/Omrigotlieb/awesome-anthropic/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![License: CC0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg?style=flat-square)](LICENSE)

![Awesome Anthropic preview](assets/img/og-awesome-anthropic.svg)

> A curated, daily-updated hub for Anthropic and Claude resources: official docs, SDKs, MCP tools, research, release notes, and community projects.

Human-curated, automation-assisted. The goal is simple: help builders find the best Anthropic resources fast and stay current without scraping half the internet themselves.

<p>
  <a href="https://omrigotlieb.github.io/awesome-anthropic"><strong>Open the live dashboard</strong></a> ·
  <a href="https://github.com/Omrigotlieb/awesome-anthropic/stargazers"><strong>Star on GitHub</strong></a> ·
  <a href="https://github.com/Omrigotlieb/awesome-anthropic/issues/new?template=add-resource.md"><strong>Suggest a resource</strong></a> ·
  <a href="https://omrigotlieb.github.io/awesome-anthropic/rss.xml"><strong>Subscribe via RSS</strong></a>
</p>

## Why Star This Repo

- Track Anthropic release notes, SDK updates, and ecosystem news from one place.
- Discover production tools, MCP servers, tutorials, and research without noisy general AI lists.
- Follow a live dashboard, RSS feed, and daily briefs that make the repo useful between stars.
- Contribute new resources quickly through issues or pull requests.

## Start Here

- [Live dashboard](https://omrigotlieb.github.io/awesome-anthropic) - Browse the curated feed, top stories, benchmarks, and changelog in one UI.
- [Official Resources](#official-resources) - Anthropic docs, blog, release notes, model spec, and prompt library.
- [Claude API & SDKs](#claude-api--sdks) - Official and community SDKs plus integration libraries.
- [Model Context Protocol (MCP)](#model-context-protocol-mcp) - Core MCP docs, SDKs, servers, and tools.
- [Projects & Applications](#projects--applications) - Popular Claude-powered products, agents, and workflows.
- [News Digest](#news-digest-auto-updated) - Daily snapshot of official launches, community buzz, and GitHub releases.

## Quick Facts

- Updated daily from official Anthropic release notes and ecosystem sources.
- Includes a GitHub Pages dashboard, RSS feed, contribution templates, and distribution tooling.
- Built for developers, researchers, founders, and operators following Claude closely.

---

## Contents

- [Official Resources](#official-resources)
- [Models](#models)
- [Claude API & SDKs](#claude-api--sdks)
- [Model Context Protocol (MCP)](#model-context-protocol-mcp)
- [Anthropic Research Papers](#anthropic-research-papers)
- [AI Safety & Alignment](#ai-safety--alignment)
- [Prompt Engineering](#prompt-engineering)
- [Projects & Applications](#projects--applications)
  - [Coding & Developer Tools](#coding--developer-tools)
  - [Productivity & Workflows](#productivity--workflows)
  - [Agent Frameworks](#agent-frameworks)
  - [Data & Analytics](#data--analytics)
  - [Creative & Media](#creative--media)
- [Learning Resources](#learning-resources)
  - [Tutorials & Guides](#tutorials--guides)
  - [Courses & Videos](#courses--videos)
- [Community](#community)
- [Comparisons & Benchmarks](#comparisons--benchmarks)
- [Changelog (Auto-updated)](#changelog-auto-updated)
- [News Digest (Auto-updated)](#news-digest-auto-updated)
- [Distribution & Growth](#distribution--growth)

---

## Official Resources

- [Anthropic Homepage](https://anthropic.com) - Official company website.
- [Anthropic Blog](https://anthropic.com/news) - Announcements, research, and product updates.
- [Claude.ai](https://claude.ai) - Consumer-facing Claude web and mobile interface.
- [Claude API Documentation](https://docs.anthropic.com) - Full API reference and guides.
- [Release Notes](https://docs.anthropic.com/en/release-notes/overview) - Official product changelog.
- [Anthropic Research](https://anthropic.com/research) - Published papers and technical reports.
- [Anthropic Responsible Scaling Policy (RSP)](https://anthropic.com/responsible-scaling-policy) - Commitments around safe model deployment.
- [Claude's Model Specification](https://anthropic.com/model-spec) - Claude's values, character, and guidelines.
- [Anthropic on GitHub](https://github.com/anthropics) - Official open-source repositories.
- [Anthropic on Hugging Face](https://huggingface.co/Anthropic) - Model cards and datasets.
- [Anthropic Careers](https://anthropic.com/careers) - Open roles at Anthropic.
- [Anthropic Prompt Library](https://anthropic.com/prompt-library) - Curated example prompts by Anthropic.
- [Claude on AWS Bedrock](https://aws.amazon.com/bedrock/claude/) - Claude via Amazon Bedrock.
- [Claude on Google Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) - Claude via Google Cloud.

---

## Models

### Claude 4 Family (2025–2026)

| Model                 | Context          | Best For                                                    |
| --------------------- | ---------------- | ----------------------------------------------------------- |
| **Claude Opus 4.6**   | 1M tokens (beta) | Most intelligent — complex agentic tasks, long-horizon work |
| **Claude Opus 4.5**   | 200K tokens      | Vision, coding, computer use at accessible price            |
| **Claude Sonnet 4.6** | 1M tokens (beta) | Balanced performance and cost — most popular for production |
| **Claude Haiku 4.5**  | 200K tokens      | Fastest and cheapest — real-time applications, high volume  |

### Claude 3 Family (2024)

| Model             | Context     | Notes                              |
| ----------------- | ----------- | ---------------------------------- |
| Claude Opus 3.5   | 200K tokens | Predecessor to Opus 4              |
| Claude Sonnet 3.5 | 200K tokens | Introduced computer use capability |
| Claude Haiku 3.5  | 200K tokens | Lightweight workhorse              |
| Claude Haiku 3    | 200K tokens | Original Haiku                     |

### Specialized Capabilities

- [Extended Thinking](https://docs.anthropic.com/en/docs/about-claude/models/extended-thinking) - Deep reasoning with visible thought chains (Opus 4.6, Opus 4.5, Sonnet 4.6+).
- [Computer Use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) - Autonomous GUI interaction across desktop applications.
- [Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) - Cache prefixes for cost and latency reduction.
- [Batch API](https://docs.anthropic.com/en/api/creating-message-batches) - Asynchronous large-scale inference at 50% cost.

---

## Claude API & SDKs

### Official SDKs

- [anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) - Official Python SDK.
- [anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript) - Official TypeScript/Node.js SDK.
- [anthropic-sdk-go](https://github.com/anthropics/anthropic-sdk-go) - Official Go SDK.
- [anthropic-sdk-java](https://github.com/anthropics/anthropic-sdk-java) - Official Java SDK.
- [anthropic-sdk-kotlin](https://github.com/anthropics/anthropic-sdk-kotlin) - Official Kotlin SDK.

### Community SDKs & Wrappers

- [anthropic-ruby](https://github.com/anthropics/anthropic-sdk-ruby) - Official Ruby SDK.
- [anthropic-php](https://github.com/anthropics/anthropic-sdk-php) - Community PHP SDK.
- [claudette](https://github.com/AnswerDotAI/claudette) - High-level Python API by Answer.AI.
- [instructor](https://github.com/instructor-ai/instructor) - Structured outputs for Claude and other LLMs.

### Framework Integrations

- [LangChain + Claude](https://python.langchain.com/docs/integrations/chat/anthropic/) - Claude in the LangChain ecosystem.
- [LlamaIndex + Claude](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/) - Claude for RAG pipelines.
- [Haystack + Claude](https://haystack.deepset.ai/integrations/anthropic-claude) - Claude in Haystack pipelines.
- [aisuite](https://github.com/andrewyng/aisuite) - Unified interface to Claude and other LLMs.
- [litellm](https://github.com/BerriAI/litellm) - Universal LLM proxy supporting Claude.
- [Vercel AI SDK](https://sdk.vercel.ai/providers/ai-sdk-providers/anthropic) - Claude in the Vercel AI SDK.

---

## Model Context Protocol (MCP)

MCP is Anthropic's open protocol for connecting AI assistants to data sources and tools.

### Official

- [MCP Specification](https://modelcontextprotocol.io) - Official MCP documentation and spec.
- [MCP GitHub Organization](https://github.com/modelcontextprotocol) - All official MCP repos.
- [mcp-python-sdk](https://github.com/modelcontextprotocol/python-sdk) - Python SDK for building MCP servers.
- [mcp-typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) - TypeScript SDK for MCP servers.
- [mcp-servers](https://github.com/modelcontextprotocol/servers) - Official reference MCP server implementations.

### Community MCP Servers

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Curated list of MCP server implementations.
- [mcp-server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) - GitHub MCP server.
- [mcp-server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) - PostgreSQL MCP server.
- [mcp-server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - Filesystem MCP server.
- [mcp-server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) - Web search MCP server.

### MCP Tools

- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) - Visual testing tool for MCP servers.

---

## Anthropic Research Papers

### Constitutional AI & RLHF

- [Constitutional AI: Harmlessness from AI Feedback (2022)](https://arxiv.org/abs/2212.08073) - Foundational paper on CAI training methodology.
- [Training a Helpful and Harmless Assistant with RLHF (2022)](https://arxiv.org/abs/2204.05862) - Core RLHF approach for Claude.
- [Reward Model Ensembles Help Mitigate Overoptimization (2023)](https://arxiv.org/abs/2310.02743) - Robustness in RLHF training.

### Interpretability & Mechanistic Analysis

- [Toy Models of Superposition (2022)](https://transformer-circuits.pub/2022/toy_model/index.html) - Foundational interpretability research.
- [In-context Learning and Induction Heads (2022)](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) - Mechanisms behind in-context learning.
- [Scaling Monosemanticity (2024)](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) - Dictionary learning at scale for feature extraction.
- [Interpretability in the Wild (2022)](https://arxiv.org/abs/2211.00593) - IOI circuit analysis in GPT-2.

### Scaling & Capabilities

- [Scaling Laws for Neural Language Models (2020)](https://arxiv.org/abs/2001.08361) - Original OpenAI scaling laws (Anthropic researchers co-authored).
- [Challenges in Evaluating AI Systems (2022)](https://anthropic.com/research/evaluating-ai-systems) - Evaluation methodology.
- [Measuring Progress on Scalable Oversight for Large Language Models (2022)](https://arxiv.org/abs/2211.03540) - Scalable oversight research.

### Safety & Alignment

- [Sleeper Agents: Training Deceptive LLMs (2024)](https://arxiv.org/abs/2401.05566) - Hidden backdoor behavior in LLMs.
- [Many-shot Jailbreaking (2024)](https://anthropic.com/research/many-shot-jailbreaking) - Long-context safety vulnerabilities.
- [Towards Monosemanticity (2023)](https://transformer-circuits.pub/2023/monosemantic-features/index.html) - Identifying interpretable features in neural networks.
- [Soft Prompting Might Be a Bug, Not a Feature (2022)](https://arxiv.org/abs/2210.01848) - Vulnerabilities in soft prompting.

### Claude-specific Technical Reports

- [Claude 3 Model Card (2024)](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) - Capabilities and safety evaluations.
- [Claude's Character (2023)](https://anthropic.com/research/claudes-character) - On authenticity and identity in AI assistants.
- [Core Views on AI Safety (2023)](https://anthropic.com/news/core-views-on-ai-safety) - Anthropic's safety philosophy.

---

## AI Safety & Alignment

### Frameworks & Policies

- [Anthropic's Long-Term Benefit Trust](https://anthropic.com/news/the-long-term-benefit-trust) - Governance structure for long-term benefit.
- [Claude's Constitution](https://www.anthropic.com/news/claudes-constitution) - Claude's constitutional principles and values.

### Safety Research Areas

- [Transformer Circuits Thread](https://transformer-circuits.pub) - Mechanistic interpretability research blog.
- [Alignment Forum](https://alignmentforum.org) - Broader AI alignment community (not Anthropic-specific, but relevant).

### Third-party Evaluations

- [METR Evals](https://metr.org) - Autonomous AI capabilities evaluations including Claude.
- [MLCommons AI Safety Benchmark](https://mlcommons.org/working-groups/ai-safety/ai-safety/) - Community safety benchmarks.

---

## Prompt Engineering

### Official Guides

- [Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) - Anthropic's official guide.
- [Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - How to use function calling effectively.
- [Vision Guide](https://docs.anthropic.com/en/docs/build-with-claude/vision) - Image prompting best practices.
- [Extended Thinking Guide](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) - Using reasoning/thinking modes.

### Community Resources

- [Prompt Hacking](https://learnprompting.org) - Open-source prompt engineering guide.
- [promptingguide.ai](https://promptingguide.ai) - Comprehensive prompting techniques.
- [fabric](https://github.com/danielmiessler/fabric) - Framework for system prompts and patterns.

---

## Projects & Applications

### Coding & Developer Tools

- [Claude Code](https://claude.ai/code) - Official Anthropic agentic coding CLI.
- [Cursor](https://cursor.sh) - AI code editor with Claude integration.
- [Cline](https://github.com/cline/cline) - Autonomous coding agent for VS Code with Claude support.
- [Aider](https://github.com/paul-gauthier/aider) - AI pair programming in the terminal.
- [Continue](https://github.com/continuedev/continue) - Open-source coding assistant with Claude backend.
- [Zed](https://zed.dev) - High-performance code editor with Claude integration.
- [Sourcegraph Cody](https://sourcegraph.com/cody) - Code search and AI assistant with Claude.

### Productivity & Workflows

- [Raycast AI](https://raycast.com/ai) - macOS launcher with Claude integration.
- [Superwhisper](https://superwhisper.com) - Voice-to-text with Claude for macOS.
- [Notion AI](https://notion.so/product/ai) - Notion's AI assistant powered by Claude.
- [Quip](https://quip.com) - Salesforce's document platform with Claude AI.
- [Perplexity](https://perplexity.ai) - AI search engine using Claude among other models.
- [Poe](https://poe.com) - Multi-model chatbot interface including Claude.

### Agent Frameworks

- [CrewAI](https://github.com/crewAIInc/crewAI) - Multi-agent orchestration supporting Claude.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful multi-actor applications with Claude.
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent conversation framework.
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - Open-source autonomous AI agent framework.
- [claude-agent-sdk](https://github.com/anthropics/claude-agent-sdk) - Official SDK for building agents with Claude.

### Data & Analytics

- [pandas-ai](https://github.com/Sinaptik-AI/pandas-ai) - Conversational data analysis with Claude backend.
- [datasette-llm](https://github.com/simonw/datasette-llm) - LLM integration for Datasette supporting Claude.
- [llm](https://github.com/simonw/llm) - CLI and Python library for running LLMs including Claude.

### Creative & Media

- [Claude for Sheets](https://workspace.google.com/marketplace/app/claude_for_sheets/909417792257) - Claude in Google Sheets.
- [Descript](https://descript.com) - AI-powered video/audio editing with Claude.

---

## Learning Resources

### Tutorials & Guides

- [Build with Claude](https://docs.anthropic.com/en/docs/build-with-claude) - Practical development guides.
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) - Code examples and recipes for Claude.
- [Claude API Quickstart](https://docs.anthropic.com/en/api/getting-started) - Getting started in minutes.
- [Prompt Engineering Interactive Tutorial](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial) - Official hands-on tutorial.

### Courses & Videos

- [Anthropic Courses on GitHub](https://github.com/anthropics/courses) - Official free courses by Anthropic.
- [Claude and the Claude API – Beginner's Course](https://www.deeplearning.ai/short-courses/anthropic-claude/) - Short course on DeepLearning.AI.
- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - Building agents using Claude.

---

## Community

- [Anthropic Discord](https://discord.gg/anthropic) - Official Anthropic community server.
- [r/ClaudeAI](https://reddit.com/r/ClaudeAI) - Reddit community for Claude users (~500k members).
- [r/Anthropic](https://reddit.com/r/Anthropic) - Reddit community for Anthropic news.
- [Hacker News: Anthropic stories](https://news.ycombinator.com/from?site=anthropic.com) - HN discussions on Anthropic posts.
- [Anthropic on X/Twitter](https://twitter.com/AnthropicAI) - Official Twitter/X account.
- [Dario Amodei on X](https://twitter.com/DarioAmodei) - Anthropic CEO.
- [Daniela Amodei on X](https://twitter.com/DanielaAmodei) - Anthropic President.
- [Chris Olah on X](https://twitter.com/ch402) - Interpretability research lead.
- [Amanda Askell on X](https://twitter.com/AmandaAskell) - Character and alignment lead.
- [Anthropic on LinkedIn](https://linkedin.com/company/anthropic-ai) - Professional network updates.

---

## Comparisons & Benchmarks

- [LMSYS Chatbot Arena](https://chat.lmsys.org) - Crowd-sourced model ranking (Claude consistently top-tier).
- [HumanEval](https://github.com/openai/human-eval) - Python coding benchmark.
- [MMLU](https://github.com/hendrycks/test) - Massive Multitask Language Understanding.
- [GPQA](https://github.com/idavidrein/gpqa) - Graduate-level science questions.
- [SWE-bench](https://www.swebench.com) - Real-world software engineering tasks.
- [BIG-Bench Hard](https://github.com/suzgunmirac/BIG-Bench-Hard) - Challenging reasoning tasks.
- [Scale AI HELM](https://crfm.stanford.edu/helm/) - Holistic evaluation framework.
- [Epoch AI Model Benchmarks](https://epochai.org/data/ai-benchmarks) - Historical benchmark tracking.

---

## Changelog (Auto-updated)

> Auto-synced from the official Anthropic release notes.
> Last synced: <!-- CHANGELOG_DATE -->2026-03-23

<!-- CHANGELOG_START -->
### March 18, 2026 — We've added model capability fields to the Models API . GET /v1/models and GET /

### March 16, 2026 — We've launched the display field for extended thinking, letting you omit thinkin

### March 13, 2026 — The 1M token context window is now generally available for Claude Opus 4.6 and S

[Full changelog →](docs/CHANGELOG.md)
<!-- CHANGELOG_END -->

---

## News Digest (Auto-updated)

> Aggregated from Anthropic blog, Hacker News, Reddit, arXiv, and GitHub.
> Last fetched: <!-- NEWS_DATE -->2026-03-23

<!-- NEWS_START -->
### Top Stories — March 23, 2026

- [Claude has overtaken ChatGPT in the Apple App Store](https://reddit.com/r/ClaudeAI/comments/1rhgsjz/claude_has_overtaken_chatgpt_in_the_apple_app/) - 3216 pts on r/ClaudeAI.
- [Looks like Anthropic's NO to the DOW has made it to Tumps twitter feed](https://reddit.com/r/ClaudeAI/comments/1rgivx2/looks_like_anthropics_no_to_the_dow_has_made_it/) - 2733 pts on r/ClaudeAI.
- [Outside Anthropic Office in SF "Thank You"](https://reddit.com/r/ClaudeAI/comments/1rgi8im/outside_anthropic_office_in_sf_thank_you/) - 2627 pts on r/ClaudeAI.
- [Why the majority of vibe coded projects fail](https://reddit.com/r/ClaudeAI/comments/1rt31th/why_the_majority_of_vibe_coded_projects_fail/) - 2596 pts on r/ClaudeAI.
- [Just picked up a new keyboard - can't wait to write a bunch of code with it](https://reddit.com/r/ClaudeAI/comments/1rru8zw/just_picked_up_a_new_keyboard_cant_wait_to_write/) - 2570 pts on r/ClaudeAI.

[Full news feed →](docs/NEWS.md)
<!-- NEWS_END -->

---

## Distribution & Growth

Use the built-in scripts to distribute the daily brief across owned channels:

- Generate social copy for X, LinkedIn, Reddit, and HN: `python3 scripts/generate_social_posts.py`
- Post to Telegram: `python3 scripts/notify_telegram.py`
- Post to Discord via webhook: `python3 scripts/notify_discord.py`
- Send email digest via Buttondown: `python3 scripts/email_digest.py`

Run the full daily workflow (news + website + distribution):

`bash scripts/run_daily.sh`

Every outbound post should point to both the live dashboard and the GitHub repo so visitors can browse and star without extra clicks.

See detailed setup and channel strategy in [docs/DISTRIBUTION.md](docs/DISTRIBUTION.md).

---

## Contributing

Contributions are welcome. Read the [contributing guidelines](https://github.com/Omrigotlieb/awesome-anthropic/blob/main/CONTRIBUTING.md), open a [pull request](https://github.com/Omrigotlieb/awesome-anthropic/compare), or [submit a resource issue](https://github.com/Omrigotlieb/awesome-anthropic/issues/new?template=add-resource.md). All list items must follow the format `- [Name](url) - Description.` Do not edit sections between `<!-- X_START -->` and `<!-- X_END -->` tags because they are auto-updated daily.

If this repo saves you time, [star it](https://github.com/Omrigotlieb/awesome-anthropic/stargazers) so more Anthropic builders can find it.

---
