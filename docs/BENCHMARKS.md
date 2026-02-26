# Model Performance & Benchmarks

> Live rankings and benchmark scores across all major AI providers.
> Numbers marked with `~` are approximate estimates; verify against live trackers before relying on them.
> **Live trackers:** [LMSYS Arena](https://lmarena.ai) · [SWE-bench](https://www.swebench.com) · [Aider Leaderboard](https://aider.chat/docs/leaderboards/) · [Claude Code Tracker](https://marginlab.ai/trackers/claude-code/) · [Artificial Analysis](https://artificialanalysis.ai) · [LiveCodeBench](https://livecodebench.github.io) · [Scale AI](https://scale.com/leaderboard)

---

## LMSYS Chatbot Arena (Elo Rankings)

Community-voted head-to-head battles — the most human signal for real-world quality.
Top 15 models as of early 2026. Claude models shown in **bold**.

| Rank | Model | Provider | Elo | Notes |
| ---- | ----- | -------- | ---- | ----- |
| #1 | **Claude Opus 4.6** | Anthropic | ~1510 | Current overall leader |
| #2 | o3 | OpenAI | ~1500 | Reasoning-focused flagship |
| #3 | **Claude Opus 4.5** (thinking) | Anthropic | ~1475 | #4 in Text & Code categories |
| #4 | GPT-4.1 | OpenAI | ~1460 | Latest GPT-4 series |
| #5 | Gemini 2.0 Flash (thinking) | Google | ~1450 | Fast reasoning model |
| #6 | o1 | OpenAI | ~1445 | Chain-of-thought reasoning |
| #7 | **Claude Sonnet 4.5** (thinking) | Anthropic | ~1435 | Best value thinking tier |
| #8 | Gemini 1.5 Pro | Google | ~1415 | Long-context specialist |
| #9 | GPT-4o | OpenAI | ~1400 | Multimodal flagship |
| #10 | Grok 2 | xAI | ~1390 | Real-time knowledge |
| #11 | DeepSeek R1 | DeepSeek | ~1385 | Open-weights reasoning |
| #12 | DeepSeek V3 | DeepSeek | ~1370 | General open-weights |
| #13 | Llama 3.1 405B | Meta | ~1345 | Largest open-weights model |
| #14 | Qwen 2.5 72B | Alibaba | ~1330 | Strong multilingual model |
| #15 | Mistral Large 2 | Mistral | ~1310 | European frontier model |

> [Live leaderboard →](https://lmarena.ai) · [Methodology →](https://lmsys.org/blog/2023-05-03-arena/)

---

## SWE-bench Verified (Real-World Coding)

Resolving real GitHub issues end-to-end — the gold standard for agentic coding ability.
Includes both AI model baselines and coding agent / product results.

### AI Model Baselines

| Model | Provider | Score | Notes |
| ----- | -------- | ----- | ----- |
| **Claude Sonnet 4.5** (parallel) | Anthropic | 82.0% | With parallel compute |
| **Claude Opus 4.5** | Anthropic | 80.9% | First model to break 80% |
| **Claude Sonnet 4.5** | Anthropic | 77.2% | Standard inference |
| **Claude Opus 4** | Anthropic | 72.5% | High-compute: 79.4% |
| o3 | OpenAI | ~71.7% | Reasoning model |
| o1 | OpenAI | ~48.9% | Earlier reasoning model |
| DeepSeek R1 | DeepSeek | ~49.2% | Open-weights reasoning |
| DeepSeek V3 | DeepSeek | ~42.0% | General open-weights |
| GPT-4o | OpenAI | ~33.0% | Multimodal baseline |
| Gemini 2.0 Flash | Google | ~35.0% | Fast inference model |
| Llama 3.1 405B | Meta | ~27.0% | Open-weights reference |
| **Claude 3.5 Sonnet** | Anthropic | 49.0% | 2024 reference point |

### Coding Agents & Products

| Agent / Product | Score | Notes |
| --------------- | ----- | ----- |
| Devin 2.0 | ~53.6% | Autonomous software engineer |
| GitHub Copilot Workspace | ~45.0% | Agentic IDE integration |
| SWE-agent (GPT-4o) | ~23.7% | Research scaffold |
| Cursor (Composer) | ~38.0% | IDE-native agent; varies by model |

> [Live leaderboard →](https://www.swebench.com) · [Vals.ai tracker →](https://www.vals.ai/benchmarks/swebench) · [Scale leaderboard →](https://scale.com/leaderboard/swe_bench_pro_public)

---

## GPQA Diamond (Graduate-Level Science)

PhD-level science questions in biology, chemistry, and physics.
Human experts with PhDs score ~65%.

| Model | Provider | Score | vs. Human Expert |
| ----- | -------- | ----- | ---------------- |
| **Claude Opus 4.6** | Anthropic | **91.3%** | +26.3% above expert |
| o3 | OpenAI | ~87.7% | +22.7% above expert |
| **Claude Opus 4.5** | Anthropic | 87.0% | +22.0% above expert |
| **Claude Sonnet 4.5** | Anthropic | 83.4% | +18.4% above expert |
| o1 | OpenAI | ~78.0% | +13.0% above expert |
| **Claude Opus 4** | Anthropic | 79.6% | +14.6% above expert |
| Gemini 2.0 Flash (thinking) | Google | ~80.9% | +15.9% above expert |
| Gemini 1.5 Pro | Google | ~72.0% | +7.0% above expert |
| GPT-4o | OpenAI | ~53.6% | Below expert |
| DeepSeek R1 | DeepSeek | ~71.5% | +6.5% above expert |
| DeepSeek V3 | DeepSeek | ~59.1% | ~Expert level |
| Grok 2 | xAI | ~56.0% | ~Expert level |
| Llama 3.1 405B | Meta | ~51.1% | Below expert |
| **Claude 3.5 Sonnet** | Anthropic | 59.4% | ~Expert level |
| Human expert (PhD) | — | ~65% | Baseline |

> [Benchmark overview →](https://arxiv.org/abs/2311.12022) · [Intuition Labs analysis →](https://intuitionlabs.ai/articles/gpqa-diamond-ai-benchmark)

---

## MMLU (Knowledge & Reasoning)

57 academic subjects from STEM to humanities. Broad general intelligence signal.
5-shot accuracy reported unless noted.

| Model | Provider | Score | Notes |
| ----- | -------- | ----- | ----- |
| **Claude Opus 4.6** | Anthropic | ~91.0% | |
| o3 | OpenAI | ~91.6% | Chain-of-thought reasoning |
| **Claude Opus 4.5** | Anthropic | 90.8% | |
| **Claude 3.5 Sonnet** | Anthropic | 90.4% | 2024 reference |
| **Claude Sonnet 4.5** | Anthropic | 89.1% | |
| GPT-4o | OpenAI | 88.7% | |
| GPT-4.1 | OpenAI | ~90.0% | |
| Gemini 1.5 Pro | Google | 85.9% | |
| Gemini 2.0 Flash | Google | ~89.0% | |
| DeepSeek R1 | DeepSeek | ~90.8% | |
| DeepSeek V3 | DeepSeek | ~88.5% | |
| Llama 3.1 405B | Meta | 88.6% | |
| Qwen 2.5 72B | Alibaba | ~86.0% | |
| Mistral Large 2 | Mistral | ~84.0% | |
| Grok 2 | xAI | ~87.5% | |
| **Claude Opus 4** | Anthropic | 87.4% | |
| **Claude 3 Opus** | Anthropic | 86.8% | Legacy |

> [MMLU-Pro tracker →](https://www.vals.ai/benchmarks/mmlu_pro)

---

## HumanEval / LiveCodeBench (Coding)

**HumanEval** is the classic Python pass@1 benchmark.
**LiveCodeBench** uses recent contest problems to prevent data contamination and is a stronger signal.

### HumanEval (pass@1)

| Model | Provider | Score |
| ----- | -------- | ----- |
| **Claude Opus 4.6** | Anthropic | ~95.0% |
| o3 | OpenAI | ~95.8% |
| **Claude Sonnet 4.5** | Anthropic | ~93.0% |
| GPT-4o | OpenAI | 90.2% |
| GPT-4.1 | OpenAI | ~92.0% |
| DeepSeek R1 | DeepSeek | ~92.6% |
| DeepSeek V3 | DeepSeek | ~89.9% |
| Gemini 1.5 Pro | Google | 84.1% |
| Gemini 2.0 Flash | Google | ~89.0% |
| Llama 3.1 405B | Meta | 89.0% |
| **Claude 3.5 Sonnet** | Anthropic | 92.0% |
| **Claude 3 Opus** | Anthropic | 55.0% | Legacy |

### LiveCodeBench (recent problems, harder signal)

| Model | Provider | Score | Notes |
| ----- | -------- | ----- | ----- |
| o3 | OpenAI | ~69.8% | Best performer |
| **Claude Opus 4.6** | Anthropic | ~68.0% | |
| o1 | OpenAI | ~59.3% | |
| **Claude Opus 4.5** | Anthropic | ~63.0% | |
| **Claude Sonnet 4.5** | Anthropic | ~57.0% | |
| DeepSeek R1 | DeepSeek | ~57.5% | |
| GPT-4o | OpenAI | ~42.0% | |
| Gemini 2.0 Flash (thinking) | Google | ~56.0% | |
| DeepSeek V3 | DeepSeek | ~43.4% | |
| Llama 3.1 405B | Meta | ~29.0% | |

> [LiveCodeBench leaderboard →](https://livecodebench.github.io)

---

## Aider Polyglot Coding Leaderboard

The **Aider Polyglot** benchmark is one of the most respected real-world coding evaluations.
It tests models on editing existing codebases across multiple languages (Python, JavaScript, TypeScript, Go, Rust, Java, etc.) — much closer to day-to-day engineering work than HumanEval.

Key features:
- Uses a diverse polyglot corpus of real files
- Tests whole-file and diff-based editing, not just code generation
- Results correlate well with practical coding agent performance
- Regularly updated with new problems to reduce contamination

| Model | Provider | Score | Notes |
| ----- | -------- | ----- | ----- |
| o3 | OpenAI | ~79.6% | Top overall |
| **Claude Opus 4.5** | Anthropic | ~74.0% | |
| **Claude Sonnet 4.5** | Anthropic | ~72.0% | |
| GPT-4.1 | OpenAI | ~73.0% | |
| DeepSeek R1 | DeepSeek | ~62.0% | |
| GPT-4o | OpenAI | ~60.0% | |
| Gemini 2.0 Flash | Google | ~58.0% | |
| DeepSeek V3 | DeepSeek | ~55.0% | |
| Llama 3.1 405B | Meta | ~44.0% | |
| Mistral Large 2 | Mistral | ~37.0% | |

> All numbers above are approximate — **always check the live leaderboard for the latest results.**
> [Aider Polyglot Leaderboard (live) →](https://aider.chat/docs/leaderboards/)

---

## Claude Code Performance Tracker (marginlab.ai)

[**marginlab.ai/trackers/claude-code**](https://marginlab.ai/trackers/claude-code/) is a dedicated daily tracker for Claude Code's pass rate on a curated **SWE-Bench-Pro** subset.
This is the most granular publicly available signal for Claude Code's real-world coding performance over time.

**Current stats (as of Feb 2026):**

| Metric | Value |
| ------ | ----- |
| 30-day pass rate | ~56% |
| Total instances tested | 1,050 |
| Daily evaluation batch | N=50 instances |
| Tracking started | February 2026 |

**What is tracked per evaluation run:**

- Pass rate (primary signal)
- Token usage (input + output)
- Cost per run
- Runtime / latency

This tracker is especially valuable because:

1. It runs daily, so short-term regressions or improvements surface quickly.
2. The SWE-Bench-Pro subset is curated to be harder and more representative than standard SWE-bench Verified.
3. It provides cost and token data alongside pass rate, enabling price-efficiency analysis.

> [Live tracker →](https://marginlab.ai/trackers/claude-code/)

---

## Price vs. Performance

Pricing as of early 2026. All prices per 1M tokens unless noted.

### Anthropic

| Model | Input | Output | Context | Tier |
| ----- | ----- | ------ | ------- | ---- |
| **Claude Opus 4.6** | $15 | $75 | 1M (beta) | Frontier |
| **Claude Opus 4.5** | $15 | $75 | 200K | Frontier |
| **Claude Sonnet 4.6** | $3 | $15 | 1M (beta) | Mid |
| **Claude Sonnet 4.5** | $3 | $15 | 200K | Mid |
| **Claude Haiku 4.5** | $0.80 | $4 | 200K | Fast/cheap |

### OpenAI

| Model | Input | Output | Context | Tier |
| ----- | ----- | ------ | ------- | ---- |
| o3 | ~$10 | ~$40 | 200K | Frontier reasoning |
| o1 | $15 | $60 | 200K | Reasoning |
| GPT-4.1 | ~$2 | ~$8 | 1M | Frontier |
| GPT-4o | $2.50 | $10 | 128K | Frontier |
| GPT-4o mini | $0.15 | $0.60 | 128K | Fast/cheap |

### Google

| Model | Input | Output | Context | Tier |
| ----- | ----- | ------ | ------- | ---- |
| Gemini 2.0 Flash (thinking) | ~$3.50 | ~$14 | 1M | Reasoning |
| Gemini 1.5 Pro | $3.50 | $10.50 | 2M | Frontier |
| Gemini 2.0 Flash | $0.10 | $0.40 | 1M | Fast/cheap |
| Gemini 1.5 Flash | $0.075 | $0.30 | 1M | Fast/cheap |

### Meta (Llama — open weights, hosted API pricing varies)

| Model | Hosted Input | Hosted Output | Context | Notes |
| ----- | ------------ | ------------- | ------- | ----- |
| Llama 3.1 405B | ~$5 | ~$5 | 128K | Self-hostable |
| Llama 3.1 70B | ~$0.90 | ~$0.90 | 128K | Self-hostable |
| Llama 3.1 8B | ~$0.20 | ~$0.20 | 128K | Self-hostable |

### Mistral

| Model | Input | Output | Context | Notes |
| ----- | ----- | ------ | ------- | ----- |
| Mistral Large 2 | $3 | $9 | 128K | Flagship |
| Mistral Small | $0.20 | $0.60 | 32K | Efficient |

### DeepSeek

| Model | Input | Output | Context | Notes |
| ----- | ----- | ------ | ------- | ----- |
| DeepSeek R1 | ~$0.55 | ~$2.19 | 64K | Open weights, reasoning |
| DeepSeek V3 | ~$0.27 | ~$1.10 | 64K | Open weights, general |

> Prices fluctuate — always verify at [Anthropic](https://www.anthropic.com/pricing) · [OpenAI](https://openai.com/pricing) · [Google](https://ai.google.dev/pricing) · [Artificial Analysis](https://artificialanalysis.ai)

---

## Live Trackers

| Platform | URL | What it tracks |
| -------- | --- | -------------- |
| LMSYS Chatbot Arena | [lmarena.ai](https://lmarena.ai) | Human preference Elo rankings, live voting |
| SWE-bench Leaderboard | [swebench.com](https://www.swebench.com) | Real GitHub issue resolution rates |
| **Claude Code Tracker** | [marginlab.ai/trackers/claude-code](https://marginlab.ai/trackers/claude-code/) | Daily Claude Code pass rate, tokens, cost, runtime |
| Aider Polyglot Leaderboard | [aider.chat/docs/leaderboards](https://aider.chat/docs/leaderboards/) | Polyglot real-code editing across languages |
| LiveCodeBench | [livecodebench.github.io](https://livecodebench.github.io) | Contamination-resistant coding benchmark |
| Scale AI Leaderboard | [scale.com/leaderboard](https://scale.com/leaderboard) | SWE-bench Pro and other evaluations |
| Artificial Analysis | [artificialanalysis.ai](https://artificialanalysis.ai) | Speed, price, quality across providers |
| Vals.ai | [vals.ai](https://www.vals.ai/benchmarks/mmlu_pro) | MMLU-Pro, SWE-bench leaderboards |
| Epoch AI | [epochai.org/data/ai-benchmarks](https://epochai.org/data/ai-benchmarks) | Historical benchmark tracking |
| Stanford HELM | [crfm.stanford.edu/helm](https://crfm.stanford.edu/helm/) | Holistic evaluation framework |

---

*Benchmark scores sourced from official model cards, LMSYS Arena, and third-party evaluations. Numbers marked `~` are approximate estimates based on available data as of early 2026. Scores vary by run configuration, prompt format, and date. Always verify against the live trackers above before citing specific numbers.*
