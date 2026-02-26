# Claude & Anthropic Tools Directory

> 50+ curated tools, SDKs, and integrations for building with Claude.
> Community-maintained. Updated regularly.

---

## 🔧 Official SDKs & APIs

| Tool | Install / Link | Description | Best For |
|------|---------------|-------------|----------|
| **Anthropic Python SDK** | `pip install anthropic` · [GitHub](https://github.com/anthropic/anthropic-sdk-python) | Official Python SDK for the Claude API | Server-side Python apps, scripts, agents |
| **Anthropic TypeScript SDK** | `npm install @anthropic-ai/sdk` · [GitHub](https://github.com/anthropic/anthropic-sdk-typescript) | Official TypeScript/Node.js SDK | Frontend integrations, Node.js servers |
| **Claude Agent SDK (Python)** | [GitHub](https://github.com/anthropic/claude-code) | Agentic framework for building multi-step AI workflows | Orchestrating autonomous agents in Python |
| **Claude Agent SDK (TypeScript)** | [GitHub](https://github.com/anthropic/claude-code) | TypeScript agentic framework matching Python counterpart | Orchestrating autonomous agents in TypeScript |
| **Anthropic Java SDK** | [GitHub](https://github.com/anthropic/anthropic-sdk-java) | Official Java SDK for the Claude API | Enterprise Java apps, Android development |
| **Anthropic Go SDK** | [GitHub](https://github.com/anthropic/anthropic-sdk-go) | Official Go SDK for the Claude API | High-performance Go microservices |
| **Anthropic Kotlin SDK** | [GitHub](https://github.com/anthropic/anthropic-sdk-kotlin) | Official Kotlin SDK | Android apps, Kotlin backend services |
| **Anthropic Swift SDK** | [GitHub](https://github.com/anthropic/anthropic-sdk-swift) | Official Swift SDK | iOS and macOS native apps |
| **Anthropic Ruby SDK** | [GitHub](https://github.com/anthropic/anthropic-sdk-ruby) | Official Ruby SDK | Rails apps, Ruby scripts |
| **Claude Code** | `npm install -g @anthropic-ai/claude-code` · [Docs](https://docs.anthropic.com/claude-code) | Agentic CLI for Claude — runs in your terminal, reads and edits code | AI-assisted development from the command line |

---

## ⚡ Claude Code Extensions & Integrations

| Tool | Link | Description | Best For |
|------|------|-------------|----------|
| **Claude Code VS Code Extension** | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) | Run Claude Code directly inside VS Code | In-editor agentic coding |
| **Claude Code JetBrains Plugin** | [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/anthropic-claude-code) | Claude Code integration for IntelliJ, PyCharm, WebStorm, etc. | JetBrains IDE users |
| **MCP Server for GitHub** | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github) | Gives Claude Code read/write access to GitHub repos, PRs, and issues | Automating GitHub workflows |
| **MCP Server for Filesystem** | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Exposes local filesystem operations to Claude via MCP | Safe, sandboxed file access |
| **MCP Server for Slack** | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) | Read and send Slack messages from Claude Code sessions | Integrating Claude into team workflows |
| **MCP Server for Google Calendar** | [GitHub](https://github.com/modelcontextprotocol/servers) | Read and create Google Calendar events | Calendar-aware agents and scheduling |
| **MCP Server for Gmail** | [GitHub](https://github.com/modelcontextprotocol/servers) | Read, search, and draft Gmail messages | Email automation and research |
| **Context7** | [context7.com](https://context7.com) · [GitHub](https://github.com/upstash/context7) | MCP server that provides up-to-date library documentation to Claude | Keeping Claude current on library APIs |
| **Figma MCP** | [GitHub](https://github.com/GLips/Figma-Context-MCP) | Gives Claude access to Figma designs and components | Design-to-code workflows |

---

## 🌐 Web Apps & Interfaces

| Tool | Link | Description | Best For |
|------|------|-------------|----------|
| **Claude.ai** | [claude.ai](https://claude.ai) | The main Claude web interface — chat, files, vision, tools | General use, day-to-day tasks |
| **Claude.ai Projects** | [claude.ai](https://claude.ai) | Persistent context across conversations in a shared project | Long-running work with consistent context |
| **Anthropic Console** | [console.anthropic.com](https://console.anthropic.com) | API key management, Workbench playground, usage monitoring | API exploration and prototyping |
| **Claude API Workbench** | [console.anthropic.com/workbench](https://console.anthropic.com/workbench) | Browser-based prompt testing and evaluation environment | Prompt iteration and API experimentation |

---

## 🤖 Agent Frameworks

| Tool | Link | Description | Best For |
|------|------|-------------|----------|
| **OpenHands** (formerly OpenDevin) | [GitHub](https://github.com/All-Hands-AI/OpenHands) | Open-source coding agent platform that can browse the web, run code, and edit files | Autonomous software engineering tasks |
| **CrewAI** | [crewai.com](https://crewai.com) · [GitHub](https://github.com/crewAIInc/crewAI) | Framework for orchestrating multi-agent workflows with role-based agents | Multi-agent automation pipelines |
| **LangGraph** | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/) · [GitHub](https://github.com/langchain-ai/langgraph) | Build stateful, cyclical agent graphs with fine-grained control | Complex stateful agent architectures |
| **AutoGen** | [microsoft.github.io/autogen](https://microsoft.github.io/autogen/) · [GitHub](https://github.com/microsoft/autogen) | Multi-agent conversation framework by Microsoft | Conversational multi-agent systems |
| **Agentless** | [GitHub](https://github.com/OpenAutoCoder/Agentless) | Minimalist framework for repo-level automated code repair | Automated bug fixing and code generation |
| **Cursor IDE** | [cursor.com](https://cursor.com) | AI-first code editor with deep Claude integration for tab completion, chat, and Composer | Daily coding with AI inline assistance |
| **Windsurf** | [codeium.com/windsurf](https://codeium.com/windsurf) | Agentic code editor from Codeium with multi-file awareness | Codeium-powered agentic development |

---

## 📊 Evaluation & Testing

| Tool | Link | Description | Best For |
|------|------|-------------|----------|
| **Promptfoo** | [promptfoo.dev](https://promptfoo.dev) · [GitHub](https://github.com/promptfoo/promptfoo) | Open-source LLM testing framework — define test cases, run evals, compare models | Regression testing prompts across model versions |
| **Braintrust** | [braintrustdata.com](https://www.braintrustdata.com) | AI eval platform with logging, scoring, and human review | Production eval with a managed platform |
| **Evals (Anthropic)** | [GitHub](https://github.com/anthropics/evals) | Anthropic's internal evaluation harness and benchmark suite | Model capability benchmarking |
| **PromptLayer** | [promptlayer.com](https://promptlayer.com) | Prompt versioning, logging, and analytics for LLM apps | Tracking prompt changes over time |
| **Weights & Biases** | [wandb.ai](https://wandb.ai) | Experiment tracking, model evaluation, and artifact management | ML experiment tracking with LLM support |

---

## 🛡️ Safety & Monitoring

| Tool | Link | Description | Best For |
|------|------|-------------|----------|
| **LangFuse** | [langfuse.com](https://langfuse.com) · [GitHub](https://github.com/langfuse/langfuse) | Open-source LLM observability — traces, spans, evaluations, and dashboards | Production monitoring and debugging |
| **LangSmith** | [smith.langchain.com](https://smith.langchain.com) | LangChain's debugging, testing, and monitoring platform | Teams already using LangChain |
| **Patronus AI** | [patronus.ai](https://www.patronus.ai) | Automated LLM testing with hallucination detection and safety checks | Automated quality gates before deployment |
| **Giskard** | [giskard.ai](https://giskard.ai) · [GitHub](https://github.com/Giskard-AI/giskard) | Open-source vulnerability scanning for LLM applications | Security and bias testing for AI apps |

---

## 📚 Prompt & Knowledge Management

| Tool | Link | Description | Best For |
|------|------|-------------|----------|
| **LlamaIndex** | [llamaindex.ai](https://www.llamaindex.ai) · [GitHub](https://github.com/run-llama/llama_index) | RAG framework for connecting LLMs to external data sources | Document Q&A and knowledge base retrieval |
| **LangChain** | [langchain.com](https://langchain.com) · [GitHub](https://github.com/langchain-ai/langchain) | Comprehensive LLM tooling for chains, agents, and retrieval | Rapid prototyping of LLM-powered apps |
| **Instructor** | [python.useinstructor.com](https://python.useinstructor.com) · [GitHub](https://github.com/jxnl/instructor) | Structured output extraction from LLMs using Pydantic models | Reliable JSON/typed output from Claude |
| **Guardrails AI** | [guardrailsai.com](https://www.guardrailsai.com) · [GitHub](https://github.com/guardrails-ai/guardrails) | Output validation and correction for LLM responses | Enforcing output schemas and safety policies |

---

## 🎯 Specialty Tools

| Tool | Link | Description | Best For |
|------|------|-------------|----------|
| **Continue.dev** | [continue.dev](https://continue.dev) · [GitHub](https://github.com/continuedev/continue) | Open-source VS Code and JetBrains AI coding assistant — supports Claude | Configurable AI code assistant in any IDE |
| **Aider** | [aider.chat](https://aider.chat) · [GitHub](https://github.com/paul-gauthier/aider) | Terminal-based AI pair programmer that edits files and commits changes | Git-integrated coding sessions in the terminal |
| **Composio** | [composio.dev](https://composio.dev) | Pre-built tool integrations (100+ apps) for LLM agents | Connecting agents to SaaS tools without custom code |
| **E2B** | [e2b.dev](https://e2b.dev) · [GitHub](https://github.com/e2b-dev/e2b) | Secure sandboxed code execution environments for AI agents | Running agent-generated code safely in the cloud |
| **PDFChat** | [pdfgear.com/chat](https://www.pdfgear.com/pdf-reader-chat/) | Document Q&A for PDF files using Claude | Reading and analyzing PDFs via natural language |
| **Cursor Rules** | [cursor.directory](https://cursor.directory) | Community repository of `.cursorrules` files for different frameworks | Sharing and discovering IDE prompting conventions |

---

> Last updated: February 2026 · [Suggest a tool](https://github.com/Omrigotlieb/awesome-anthropic/issues/new) · [View on GitHub](https://github.com/Omrigotlieb/awesome-anthropic)
