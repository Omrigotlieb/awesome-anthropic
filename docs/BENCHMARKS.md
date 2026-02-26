# Model Performance & Benchmarks

> Live rankings and benchmark scores for Claude models across major evaluation frameworks.
> **Live trackers:** [LMSYS Arena](https://lmarena.ai) · [SWE-bench](https://www.swebench.com) · [Artificial Analysis](https://artificialanalysis.ai) · [Vals.ai](https://www.vals.ai/benchmarks/mmlu_pro)

---

## 🏆 LMSYS Chatbot Arena (Elo Rankings)

Community-voted head-to-head battles — the most human signal for real-world quality.

| Model | Elo | Rank | Notes |
| --------------------- | ---- | ---- | ----------------------------------- |
| **Claude Opus 4.6** | ~1500+ | #1 | Current flagship |
| **Claude Opus 4.5** (thinking) | 1472 | #4 | #4 in Text & Code categories |
| **Claude Sonnet 4.5** (thinking) | ~1430 | #20 | Best value tier |
| Claude 3.5 Sonnet | ~1270 | — | Reference point (2024) |
| Claude 3 Opus | ~1247 | — | Legacy |

> [Live leaderboard →](https://lmarena.ai) · [Methodology →](https://lmsys.org/blog/2023-05-03-arena/)

---

## 💻 SWE-bench Verified (Real-World Coding)

Resolving real GitHub issues end-to-end — the gold standard for agentic coding ability.

| Model | Score | Notes |
| --------------------- | ------ | ---------------------------------------- |
| **Claude Opus 4.5** | **80.9%** | First model ever to break 80% |
| **Claude Sonnet 4.5** (parallel) | 82.0% | With parallel compute |
| **Claude Sonnet 4.5** | 77.2% | Standard inference |
| Claude Opus 4 | 72.5% | High-compute: 79.4% |
| Claude 3.5 Sonnet | 49.0% | Baseline reference |
| GPT-4o | ~33.0% | Competitor reference |

> [Live leaderboard →](https://www.swebench.com) · [Vals.ai tracker →](https://www.vals.ai/benchmarks/swebench) · [Scale leaderboard →](https://scale.com/leaderboard/swe_bench_pro_public)

---

## 🎓 GPQA Diamond (Graduate-Level Science)

PhD-level science questions in biology, chemistry, and physics. Human experts with PhDs score ~65%.

| Model | Score | vs. Human Expert |
| --------------------- | ------ | ---------------- |
| **Claude Opus 4.6** | **91.3%** | +26.3% above expert |
| **Claude Opus 4.5** | 87.0% | +22% above expert |
| **Claude Sonnet 4.5** | 83.4% | +18.4% above expert |
| Claude Opus 4 | 79.6% | High-compute: 83.3% |
| Claude 3.5 Sonnet | 59.4% | ~Expert level |
| Claude 3 Opus | 59.5% | ~Expert level |

> [Benchmark overview →](https://arxiv.org/abs/2311.12022) · [Intuition Labs analysis →](https://intuitionlabs.ai/articles/gpqa-diamond-ai-benchmark)

---

## 🧠 MMLU (Knowledge & Reasoning)

57 academic subjects from STEM to humanities. Broad general intelligence signal.

| Model | Score |
| --------------------- | ----- |
| **Claude Opus 4.6** | 91.0% |
| **Claude Opus 4.5** | 90.8% |
| **Claude Sonnet 4.5** | 89.1% |
| Claude 3.5 Sonnet | 90.4% |
| Claude Opus 4 | 87.4% |
| Claude 3 Opus | 86.8% |

> [MMLU-Pro tracker →](https://www.vals.ai/benchmarks/mmlu_pro)

---

## ⚡ HumanEval (Python Coding)

Classic pass@1 coding benchmark. Measures basic code generation accuracy.

| Model | HumanEval |
| --------------------- | --------- |
| **Claude Opus 4.6** | 95.0% |
| **Claude Sonnet 4.5** | ~93.0% |
| Claude 3.5 Sonnet | 92.0% |
| Claude 3 Opus | 55.0% |

---

## 💰 Price vs. Performance

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Context |
| --------------------- | --------------------- | ---------------------- | ------------ |
| **Claude Opus 4.6** | $15 | $75 | 1M (beta) |
| **Claude Opus 4.5** | $15 | $75 | 200K |
| **Claude Sonnet 4.6** | $3 | $15 | 1M (beta) |
| **Claude Haiku 4.5** | $0.80 | $4 | 200K |

> [Full pricing →](https://www.anthropic.com/pricing) · [Artificial Analysis comparison →](https://artificialanalysis.ai)

---

## 📊 Live Trackers

| Platform | What it tracks |
| ------------------------------------------ | ---------------------------------------------- |
| [LMSYS Chatbot Arena](https://lmarena.ai) | Human preference Elo rankings, live voting |
| [SWE-bench Leaderboard](https://www.swebench.com) | Real GitHub issue resolution rates |
| [Artificial Analysis](https://artificialanalysis.ai) | Speed, price, quality across providers |
| [Vals.ai](https://www.vals.ai/benchmarks/mmlu_pro) | MMLU-Pro, SWE-bench leaderboards |
| [Epoch AI](https://epochai.org/data/ai-benchmarks) | Historical benchmark tracking |
| [Scale AI HELM](https://crfm.stanford.edu/helm/) | Holistic evaluation framework |

---

*Benchmark scores sourced from official Anthropic model cards, LMSYS Arena, and third-party evaluations. Scores may vary by run configuration and date. Always check live trackers for the latest numbers.*
