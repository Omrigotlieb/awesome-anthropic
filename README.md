# Awesome Anthropic [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

[![GitHub Stars](https://img.shields.io/github/stars/Omrigotlieb/awesome-anthropic?style=flat-square&logo=github&color=yellow)](https://github.com/Omrigotlieb/awesome-anthropic/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Omrigotlieb/awesome-anthropic?style=flat-square&color=green)](https://github.com/Omrigotlieb/awesome-anthropic/commits/main)
[![Daily Update](https://img.shields.io/badge/auto--updated-daily-blue?style=flat-square&logo=github-actions)](https://github.com/Omrigotlieb/awesome-anthropic/actions)
[![Contributors](https://img.shields.io/github/contributors/Omrigotlieb/awesome-anthropic?style=flat-square)](https://github.com/Omrigotlieb/awesome-anthropic/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![License: CC0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg?style=flat-square)](LICENSE)
[![Changelog Sync](https://img.shields.io/github/actions/workflow/status/Omrigotlieb/awesome-anthropic/changelog-check.yml?label=changelog%20sync&style=flat-square)](https://github.com/Omrigotlieb/awesome-anthropic/actions/workflows/changelog-check.yml)
[![Link Check](https://img.shields.io/github/actions/workflow/status/Omrigotlieb/awesome-anthropic/link-checker.yml?label=links&style=flat-square)](https://github.com/Omrigotlieb/awesome-anthropic/actions/workflows/link-checker.yml)

> A curated, **daily-updated** list of awesome resources, tools, SDKs, research papers, and community projects related to [Anthropic](https://anthropic.com) and the Claude AI family.

Anthropic is an AI safety company building reliable, interpretable, and steerable AI systems. Claude is their flagship family of AI assistants, used by millions of developers and deployed across enterprise, research, and consumer applications worldwide.

This list is **automatically updated every day** — changelog synced from the official Anthropic docs, news aggregated from blogs, Hacker News, Reddit, arXiv, and GitHub.

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
- [Contributing](#contributing)

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

| Model | Context | Best For |
|-------|---------|----------|
| **Claude Opus 4.6** | 1M tokens (beta) | Most intelligent — complex agentic tasks, long-horizon work |
| **Claude Opus 4.5** | 200K tokens | Vision, coding, computer use at accessible price |
| **Claude Sonnet 4.6** | 1M tokens (beta) | Balanced performance and cost — most popular for production |
| **Claude Haiku 4.5** | 200K tokens | Fastest and cheapest — real-time applications, high volume |

### Claude 3 Family (2024)

| Model | Context | Notes |
|-------|---------|-------|
| Claude Opus 3.5 | 200K tokens | Predecessor to Opus 4 |
| Claude Sonnet 3.5 | 200K tokens | Introduced computer use capability |
| Claude Haiku 3.5 | 200K tokens | Lightweight workhorse |
| Claude Haiku 3 | 200K tokens | Original Haiku |

### Specialized Capabilities

- **Extended Thinking** — Deep reasoning with visible thought chains (Opus 4.6, Opus 4.5, Sonnet 4.6+).
- **Computer Use** — Autonomous GUI interaction (Sonnet 3.5+).
- **Tool Use / Function Calling** — Structured JSON tool integration across all models.
- **Vision** — Image understanding across all current models.
- **Prompt Caching** — Cache prefixes for cost and latency reduction.
- **Batch API** — Asynchronous large-scale inference at 50% cost.

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
- [vercel/ai](https://sdk.vercel.ai/providers/ai-sdk-providers/anthropic) - Claude in Vercel AI SDK.

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

- [Responsible Scaling Policy (RSP)](https://anthropic.com/responsible-scaling-policy) - Anthropic's commitment to safe model deployment.
- [Claude's Model Specification](https://anthropic.com/model-spec) - Full behavioral guidelines for Claude.
- [Anthropic's Long-Term Benefit Trust](https://anthropic.com/news/the-long-term-benefit-trust) - Governance structure.

### Safety Research Areas

- [AI Safety Research at Anthropic](https://anthropic.com/research) - Overview of safety research pillars.
- [Transformer Circuits Thread](https://transformer-circuits.pub) - Mechanistic interpretability research blog.
- [Alignment Forum](https://alignmentforum.org) - Broader AI alignment community (not Anthropic-specific, but relevant).

### Third-party Evaluations

- [METR Evals](https://metr.org) - Autonomous AI capabilities evaluations including Claude.
- [MLCommons AI Safety Benchmark](https://mlcommons.org/working-groups/ai-safety/ai-safety/) - Community safety benchmarks.

---

## Prompt Engineering

### Official Guides

- [Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) - Anthropic's official guide.
- [Anthropic Prompt Library](https://anthropic.com/prompt-library) - Curated prompt templates.
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

- [Anthropic Documentation](https://docs.anthropic.com) - Official comprehensive documentation.
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

> Auto-synced from [docs.anthropic.com/en/release-notes](https://docs.anthropic.com/en/release-notes/overview).
> Last synced: <!-- CHANGELOG_DATE -->2026-02-26

<!-- CHANGELOG_START -->
### Feb 19, 2026 — Automatic Caching + Model Retirements

**Automatic prompt caching** is now available on the Messages API — add a single `cache_control` field and the system auto-caches without manual breakpoints. Available on Claude API and Azure AI Foundry (preview).

**Model retirements:** `claude-3-7-sonnet-20250219` and `claude-3-5-haiku-20241022` retired. Upgrade to **Claude Sonnet 4.6** and **Claude Haiku 4.5** respectively.

### Feb 17, 2026 — Claude Sonnet 4.6 Launch

**Claude Sonnet 4.6** — improved agentic search, fewer tokens consumed, extended thinking support, 1M token context window (beta). Code execution now **free when used with web search or web fetch**. Web search + programmatic tool calling now GA (no beta header required).

### Feb 5, 2026 — Claude Opus 4.6 Launch

**Claude Opus 4.6** — most intelligent model for complex agentic tasks. Uses `thinking: {type: "adaptive"}` by default. New **`effort` parameter** (GA), **Compaction API** (beta), **data residency controls** via `inference_geo`.

[Full changelog →](docs/CHANGELOG.md)
<!-- CHANGELOG_END -->

---

## News Digest (Auto-updated)

> Aggregated from Anthropic blog, Hacker News, Reddit, arXiv, and GitHub.
> Last fetched: <!-- NEWS_DATE -->2026-02-26

<!-- NEWS_START -->
### Top Stories — Feb 26, 2026

| ⭐ | Story | Source |
|---:|-------|--------|
| 1682 | [They’re shipping so fast](https://reddit.com/r/ClaudeAI/comments/1rep29w/theyre_shipping_so_fast/) | r/ClaudeAI |
| 1227 | [Pentagon, Claude and the military use](https://reddit.com/r/ClaudeAI/comments/1recva7/pentagon_claude_and_the_military_use/) | r/ClaudeAI |
| 631 | [Anthropic Drops Flagship Safety Pledge](https://www.astralcodexten.com/p/the-pentagon-threatens-anthropic) | Hacker News |
| 497 | [Update on model deprecation commitments for Claude Opus 3](https://reddit.com/r/ClaudeAI/comments/1req1ad/official_an_update_on_model_deprecation/) | r/ClaudeAI |
| 299 | [Claude Code subagents built a 3D renderer from scratch in 3 days](https://reddit.com/r/ClaudeAI/comments/1rerl6w/claude_code_with_subagents_inside_subagents/) | r/ClaudeAI |

**Official:** [Anthropic acquires Vercept AI](https://www.anthropic.com/news/acquires-vercept) · [RSP v3.0](https://www.anthropic.com/news/responsible-scaling-policy-v3) · [Claude Code Security](https://www.anthropic.com/news/claude-code-security)

[Full news feed →](docs/NEWS.md)
<!-- NEWS_END -->

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

- **Add a resource**: Open a PR with your addition following the format `- [Name](url) - Description.`
- **Report broken link**: Open an issue using the broken link template.
- **Automated sections**: Do not edit sections between `<!-- X_START -->` and `<!-- X_END -->` tags — they are auto-updated.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work. See [LICENSE](LICENSE).
