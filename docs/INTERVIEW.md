# Anthropic Interview Prep

> **Your complete guide to landing a role at Anthropic** — the AI safety company building Claude.
>
> This guide is structured as a progressive tutor. Work through each section in order, test yourself with the knowledge checks, and follow the 3-week study plan at the end.

---

## Table of Contents

1. [About Anthropic](#-about-anthropic)
2. [Interview Process](#-interview-process)
3. [Engineering Roles](#-engineering-roles)
   - [Coding Round](#coding-round)
   - [System Design Round](#system-design-round)
4. [ML / Research Roles](#-ml--research-roles)
   - [LLM Architecture Knowledge](#llm-architecture-knowledge)
   - [Safety & Alignment](#safety--alignment)
5. [Behavioral Questions](#-behavioral-questions)
6. [Study Plan](#-study-plan)
7. [Essential Reading](#-essential-reading)
8. [Quick Knowledge Check](#-quick-knowledge-check)

---

## 🏢 About Anthropic

**Before your recruiter screen**, you should be able to articulate what Anthropic does and *why it matters* without sounding like you memorized the homepage. Interviewers listen for genuine conviction here.

### The Core Mission

Anthropic's stated mission is **the responsible development and maintenance of advanced AI for the long-term benefit of humanity**. This is not marketing language — it is operationally load-bearing. It explains why Anthropic:

- Publishes safety research that could help competitors
- Imposes usage restrictions on Claude that cost revenue
- Has a [Responsible Scaling Policy (RSP)](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) that could force them to pause model development
- Invests heavily in interpretability research before it has immediate commercial value

The key insight: Anthropic occupies a deliberate position as a "safety-focused lab at the frontier." The belief is that if powerful AI is coming regardless, it is better to have safety-oriented organizations at the leading edge than to cede that ground.

### Founding & History

| Year | Event |
|------|-------|
| 2021 | Founded by Dario Amodei (CEO), Daniela Amodei (President), Tom Brown, Chris Olah, Sam McCandlish, Jack Clark, Jared Kaplan, and others from OpenAI |
| 2022 | Constitutional AI paper published; Claude (internal) development begins |
| 2023 | Claude 1.0 and Claude 2 released; $7B+ raised from Google and others |
| 2024 | Claude 3 family (Haiku, Sonnet, Opus); Claude 3.5 Sonnet; Claude Code launched in beta |
| 2025 | Claude 3.7 Sonnet with extended thinking; Claude 4 family (Sonnet 4, Opus 4); MCP becomes open standard |

**Funding**: Google has invested billions (with access to TPU compute); Spark Capital, Salesforce, and others have also invested. Valuation has been reported above $60B as of 2025.

### Key Products

| Product | What It Is | Why It Matters Internally |
|---------|-----------|--------------------------|
| **Claude API** | Programmatic access to Claude models | Core revenue driver; powers external developers |
| **Claude.ai** | Consumer/pro chat interface | Feedback surface; shows model capabilities to the public |
| **Claude Code** | Agentic coding assistant (CLI + IDE) | Flagship agentic product; uses extended context + tool use |
| **Model Context Protocol (MCP)** | Open standard for connecting AI to tools/data | Ecosystem play; makes Claude interoperable with third-party systems |

### Culture Signals (What Interviewers Are Listening For)

- **Safety-first, not safety-theater**: The distinction matters. Anthropic does not treat safety as a compliance checkbox — it is a core research agenda. Know the difference between capability research and safety research and why Anthropic does both.
- **Research-driven**: Many decisions are grounded in empirical findings (scaling laws, interpretability results). Expect to discuss tradeoffs with evidence, not opinion.
- **Intellectual humility**: Being wrong is fine; being confidently wrong is not. Saying "I don't know, but here's how I'd think about it" is valued.
- **Autonomy with alignment**: Teams operate with significant independence. You'll be expected to identify what needs doing and do it, not wait for assignments.

---

## 📋 Interview Process

The process varies by role and team but typically follows this arc:

```
[Recruiter Screen] ──► [Take-home / Async Challenge] ──► [Technical Phone Screen]
                                                                     │
                                                                     ▼
                                              [Virtual Onsite: 4–6 rounds]
                                              ├── Coding (1–2 rounds)
                                              ├── System Design (1 round)
                                              ├── Behavioral / Values (1 round)
                                              ├── Domain-Specific (1 round, ML/Safety)
                                              └── Bar Raiser / Cross-functional (optional)
                                                                     │
                                                                     ▼
                                                               [Offer / Debrief]
```

### Stage-by-Stage Breakdown

**Recruiter Screen (30 min)**
The recruiter is checking fit, compensation alignment, and whether you can articulate *why Anthropic specifically*. Have a clear, genuine answer to "why not OpenAI or Google DeepMind?" Mentioning Claude's model spec, Constitutional AI, or the RSP signals you've done real homework.

**Take-Home / Async Challenge**
Common formats:
- A coding problem (longer than LeetCode, more ambiguous)
- An ML implementation task (train a small model, analyze outputs)
- A written design document critique

Treat this as a professional deliverable. Write clean code with comments. If asked to write prose, edit it. Anthropic hires strong writers.

**Technical Phone Screen (1 hour)**
Live coding in a shared editor. Expect 1–2 medium-to-hard algorithmic problems. Communication matters as much as correctness — narrate your thinking. Ask clarifying questions before coding.

**Virtual Onsite**
Typically a single day or spread across two. Each round is 45–60 minutes. See the [Engineering Roles](#-engineering-roles) and [ML / Research Roles](#-ml--research-roles) sections for detailed prep for each type.

**Offer Process**
Anthropic moves relatively quickly post-onsite (1–2 weeks for decisions). Compensation is competitive with top frontier labs: base salary, equity (SAFEs or options), and benefits. Negotiate; they expect it.

---

## 💻 Engineering Roles

### Coding Round

Anthropic engineering interviews test problem-solving, code quality, and communication — not just algorithmic trivia. The bar is comparable to Google/Meta L5–L6.

**Languages**: Python is preferred for ML-adjacent roles. TypeScript/JavaScript for frontend/Claude Code roles. Use whatever language you're strongest in for pure algorithms, but know Python well.

**Common Patterns**

| Pattern | Frequency | Notes |
|---------|-----------|-------|
| Graph traversal (BFS/DFS) | High | Often framed around dependency resolution or agent graphs |
| Dynamic programming | High | Subsequence, knapsack, interval DP |
| Tree problems | Medium | Binary trees, n-ary trees, trie |
| Sliding window / two pointers | Medium | String and array manipulation |
| Heap / priority queue | Medium | Streaming data, top-K problems |
| Union-Find | Low-Medium | Connected components |

---

#### Practice Problem 1: Token Stream Processor

**Prompt**: You are building a streaming token buffer for an LLM inference system. Tokens arrive as integers in a stream. Implement a data structure that supports:
- `push(token)`: Add a token to the buffer
- `get_window(k)`: Return the last `k` tokens in order
- `flush()`: Return all tokens and clear the buffer

Optimize for `get_window` being called far more frequently than `push` or `flush`.

**Solution Sketch**:
```python
from collections import deque

class TokenBuffer:
    def __init__(self, max_size: int = 10_000):
        self._buf = deque(maxlen=max_size)

    def push(self, token: int) -> None:
        self._buf.append(token)

    def get_window(self, k: int) -> list[int]:
        # O(k) time — no copy of full buffer needed
        if k >= len(self._buf):
            return list(self._buf)
        # deque doesn't support slicing directly, so use islice
        from itertools import islice
        start = len(self._buf) - k
        return list(islice(self._buf, start, None))

    def flush(self) -> list[int]:
        tokens = list(self._buf)
        self._buf.clear()
        return tokens
```

**Key talking points**: Why `deque` over `list`? (`O(1)` append/popleft vs `O(n)` for list prepend). Trade-off of `maxlen` cap. Thread-safety considerations for production.

---

#### Practice Problem 2: Dependency Graph Resolver

**Prompt**: Given a list of tasks where each task may depend on other tasks, return a valid execution order (topological sort). If a cycle exists, raise an error.

```python
from collections import defaultdict, deque
from typing import List, Dict

def resolve_order(tasks: List[str], deps: List[tuple[str, str]]) -> List[str]:
    """
    deps: list of (task, depends_on) pairs
    Returns topological order or raises ValueError on cycle.
    """
    graph = defaultdict(list)
    in_degree = {t: 0 for t in tasks}

    for task, dep in deps:
        graph[dep].append(task)
        in_degree[task] += 1

    queue = deque([t for t in tasks if in_degree[t] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(tasks):
        raise ValueError("Cycle detected in task dependencies")

    return order
```

**Why this matters at Anthropic**: Multi-agent systems like Claude Code orchestrate tool calls with dependencies. This exact pattern appears in real infrastructure.

---

#### Practice Problem 3: LRU Cache with TTL

**Prompt**: Implement an LRU cache that also supports per-entry time-to-live (TTL) expiration. Expired entries should be treated as cache misses.

```python
import time
from collections import OrderedDict
from typing import Optional, Any

class TTLLRUCache:
    def __init__(self, capacity: int, default_ttl: float = 60.0):
        self.capacity = capacity
        self.default_ttl = default_ttl
        self._cache: OrderedDict[str, tuple[Any, float]] = OrderedDict()

    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None
        value, expires_at = self._cache[key]
        if time.time() > expires_at:
            del self._cache[key]
            return None
        self._cache.move_to_end(key)
        return value

    def put(self, key: str, value: Any, ttl: Optional[float] = None) -> None:
        ttl = ttl if ttl is not None else self.default_ttl
        expires_at = time.time() + ttl
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = (value, expires_at)
        if len(self._cache) > self.capacity:
            self._cache.popitem(last=False)  # evict LRU
```

**Context**: KV caching in LLM inference is exactly this pattern at scale. Being able to connect your data structures knowledge to real ML systems is impressive.

---

#### Practice Problem 4: Merge K Sorted Token Streams

**Prompt**: You have `k` sorted streams of (timestamp, token) pairs. Merge them into a single sorted output stream efficiently.

```python
import heapq
from typing import Iterator

def merge_streams(streams: list[Iterator[tuple[int, str]]]) -> Iterator[tuple[int, str]]:
    """Merge k sorted (timestamp, token) streams into one sorted stream."""
    heap = []
    # Initialize with first element from each stream
    for i, stream in enumerate(streams):
        try:
            ts, tok = next(stream)
            heapq.heappush(heap, (ts, i, tok, stream))
        except StopIteration:
            pass

    while heap:
        ts, i, tok, stream = heapq.heappop(heap)
        yield (ts, tok)
        try:
            next_ts, next_tok = next(stream)
            heapq.heappush(heap, (next_ts, i, next_tok, stream))
        except StopIteration:
            pass
```

**Complexity**: `O(n log k)` where `n` is total tokens, `k` is number of streams. Know this cold.

---

#### Practice Problem 5: Longest Context Window Fit

**Prompt**: Given a list of documents with token counts and a context window size `C`, find the maximum number of complete documents you can fit, preferring shorter documents first (greedy), and return their indices in original order.

```python
def fit_context_window(token_counts: list[int], context_size: int) -> list[int]:
    """
    Returns indices of documents to include, maximizing count.
    Greedy: include shortest documents first.
    """
    indexed = sorted(enumerate(token_counts), key=lambda x: x[1])
    selected = []
    remaining = context_size

    for original_idx, count in indexed:
        if count <= remaining:
            selected.append(original_idx)
            remaining -= count
        # Don't break — a later shorter doc might fit (but we sorted, so this can't happen)

    return sorted(selected)  # return in original document order
```

**Discussion point**: When would you prefer a different objective (e.g., maximize total tokens used instead of document count)? This becomes a variant of the 0/1 knapsack problem.

---

### System Design Round

System design at Anthropic is differentiated by the expectation that you understand the **ML systems layer** — not just web-scale distributed systems. You should be comfortable discussing GPU memory, batching strategies, and latency/throughput tradeoffs.

**Framework for any system design answer**:
1. Clarify requirements (latency targets, scale, consistency needs)
2. Capacity estimation (back-of-envelope math)
3. High-level architecture diagram (talk through it)
4. Deep dive on 1–2 interesting components
5. Tradeoffs and failure modes
6. How you'd monitor and iterate

---

#### Design 1: Real-Time Streaming LLM Inference System

**Requirements to clarify**: P50/P99 TTFT (Time to First Token) targets, concurrent users, model size, streaming vs. batch, stateless vs. stateful (multi-turn).

**Key components**:

```
Client ──► API Gateway ──► Request Router
                                  │
                    ┌─────────────┴──────────────┐
                    ▼                            ▼
             Inference Pod A             Inference Pod B
             (GPU cluster)               (GPU cluster)
             [KV Cache Manager]          [KV Cache Manager]
                    │
                    ▼
             Token Stream Buffer
                    │
                    ▼
             SSE / WebSocket ──► Client
```

**Critical design decisions**:

- **Continuous batching** (aka in-flight batching): New requests join an existing batch as soon as a sequence finishes, rather than waiting for an entire batch to complete. This is how vLLM and TGI work. Dramatically improves GPU utilization.
- **PagedAttention**: vLLM's insight — treat the KV cache like virtual memory with pages. Eliminates memory fragmentation from variable-length sequences. Key reason vLLM became dominant.
- **Speculative decoding**: Use a small draft model to generate candidate tokens, verify with the large model in parallel. Reduces latency for latency-bound (not throughput-bound) workloads.
- **Prompt caching**: Cache the KV activations of the system prompt prefix across requests. Anthropic's API exposes this explicitly. Critical for Claude Code's per-conversation efficiency.

**Back-of-envelope**: A 70B parameter model in BF16 requires ~140GB VRAM. An H100 has 80GB. So you need tensor parallelism across 2 H100s minimum for a 70B model. Expect ~1000–3000 tokens/sec throughput on a 2xH100 setup for typical inference.

---

#### Design 2: Safety Evaluation Pipeline

**The problem**: Before deploying a new model version, you need to evaluate it against hundreds of safety benchmarks, including adversarial prompts, policy violations, and capability elicitations. The pipeline must be fast enough to not bottleneck release cadence.

**Architecture**:

```
New Model Checkpoint
        │
        ▼
┌───────────────────────────────┐
│  Evaluation Orchestrator      │
│  (task queue + dispatcher)    │
└───────────────┬───────────────┘
                │
    ┌───────────┼───────────┐
    ▼           ▼           ▼
Policy      Capability   Adversarial
Evals       Evals        Red-Teaming
(automated) (automated)  (human+auto)
    │           │           │
    └───────────┴───────────┘
                │
                ▼
        Results Aggregator
                │
                ▼
    Safety Dashboard / Go/No-Go Gate
```

**Key design points**:
- **Parallelism**: Eval tasks are embarrassingly parallel — run thousands of prompts concurrently across multiple inference replicas.
- **Determinism**: Use fixed seeds and temperature=0 for reproducible comparisons across checkpoints.
- **Regression detection**: Compare against previous checkpoint baseline. Flag regressions on any safety metric as blocking.
- **Human-in-the-loop escalation**: Some evaluations (novel jailbreaks, new capability elicitations) require human review. Design the queue to route these without blocking automated evals.
- **Storage**: Results need to be stored with model checkpoint hash, eval version, and timestamp for longitudinal analysis.

---

#### Design 3: Claude Code Multi-Agent Orchestration

**The problem**: Claude Code spawns sub-agents to work on parallel tasks (e.g., write tests while refactoring, explore multiple solution paths). Design the orchestration layer.

**Key concepts**:

```
Orchestrator Agent (Claude)
        │
        ├── assigns tasks ──► Sub-agent 1 (file editing)
        │                          │
        ├── assigns tasks ──► Sub-agent 2 (test running)
        │                          │
        └── assigns tasks ──► Sub-agent 3 (search/research)
                                   │
                        ┌──────────┴──────────┐
                        ▼                     ▼
                  Tool Executor          Context Manager
                  (bash, editor,         (shared file state,
                   file ops)              conflict resolution)
```

**Design challenges**:
- **Context isolation vs. sharing**: Sub-agents need enough context to work independently but must share file state. Solution: shared read access to a snapshot, write operations go through a conflict-detection layer.
- **Error propagation**: If sub-agent 2 fails, does the orchestrator retry, reassign, or abort? Need a policy.
- **Token budget management**: Each sub-agent consumes tokens. The orchestrator must track total spend and gracefully summarize or terminate expensive branches.
- **Idempotency**: Tool operations (especially file writes) should be idempotent or transactional to avoid partial states.
- **Message passing**: Use structured JSON messages between orchestrator and sub-agents (MCP-style) rather than free-form prose for reliability.

---

## 🧠 ML / Research Roles

### LLM Architecture Knowledge

You should be able to explain any of these topics clearly to both a technical peer and a non-specialist. The "explain it simply" test is frequently used.

---

#### Transformer Architecture

**The core insight**: Instead of processing sequences recurrently (RNN-style), transformers process all positions simultaneously using attention — which computes pairwise relationships between every token and every other token.

**Attention mechanism** (scaled dot-product attention):

```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) * V
```

Where:
- `Q` (queries), `K` (keys), `V` (values) are linear projections of the input
- `d_k` is the key dimension (the `sqrt` term prevents softmax saturation in high dimensions)
- The result is a weighted sum of values, where weights reflect query-key similarity

**Multi-head attention**: Run attention `h` times in parallel with different learned projections, concatenate results. Different heads learn to attend to different types of relationships (syntactic, semantic, positional).

**Key components of a transformer block**:
1. Multi-head self-attention (with residual connection + layer norm)
2. Feed-forward network — two linear layers with a nonlinearity (GELU in modern models)
3. Residual connections throughout (critical for gradient flow in deep networks)
4. Layer normalization (pre-norm in modern architectures like Llama; post-norm in original paper)

**Positional encoding**: Transformers have no inherent notion of sequence order. Solutions:
- Original: sinusoidal fixed encodings
- Modern: **RoPE** (Rotary Position Embedding) — encodes *relative* positions by rotating Q and K vectors. Used in Claude, LLaMA, Mistral. Generalizes better to longer contexts than absolute encodings.

**KV Cache**: During autoregressive generation, you don't recompute keys and values for previously generated tokens — you cache them. This trades memory for compute. Cache size grows linearly with sequence length and batch size, which is why long-context inference is memory-bound.

---

#### RLHF (Reinforcement Learning from Human Feedback)

**The problem RLHF solves**: A language model trained purely on next-token prediction learns to imitate the distribution of internet text — including harmful, incorrect, and unhelpful content. We want models that are *helpful*, *harmless*, and *honest* according to human values.

**The three-stage pipeline**:

```
Stage 1: Supervised Fine-Tuning (SFT)
  Base model ──► fine-tune on high-quality human demonstrations ──► SFT model

Stage 2: Reward Model Training
  SFT model generates responses ──► humans rank pairs ──► train reward model
  (reward model learns to predict human preference)

Stage 3: RL Optimization (PPO)
  SFT model ──► generate responses ──► reward model scores ──► PPO updates policy
  (with KL penalty to prevent diverging too far from SFT model)
```

**Key limitations of RLHF**:
- Human labelers have inconsistent preferences
- Reward hacking: the policy learns to exploit the reward model's blind spots
- Expensive: requires large amounts of human comparison data
- The reward model is a proxy, not ground truth

---

#### Constitutional AI (CAI)

Anthropic's approach, introduced in the paper ["Constitutional AI: Harmlessness from AI Feedback"](https://arxiv.org/abs/2212.08073) (Bai et al., 2022).

**The key innovation**: Instead of requiring humans to label every harmful/helpful distinction, define a *constitution* — a set of principles — and use the AI itself to evaluate and revise its outputs against those principles.

**Two-phase process**:

**Phase 1: Supervised Learning from AI Feedback (SL-CAI)**
1. Prompt the model with a potentially harmful request
2. Have the model generate an initial response
3. Show the model its own response + a principle from the constitution ("Does this response encourage violence? Revise it to be less harmful")
4. Model generates a revised response
5. Fine-tune on the final (revised) responses

**Phase 2: RL from AI Feedback (RLAIF)**
- Instead of humans ranking response pairs, use a feedback model (trained on the constitution) to generate preference labels
- Use those AI-generated preferences to train a reward model
- Run standard RLHF with this reward model

**Why this matters**:
- Scales better than RLHF (less human labeling)
- Makes values explicit and auditable (the constitution is readable)
- The model can explain *why* a response is problematic
- Forms the foundation for Claude's behavior and model spec

---

#### Prompt Caching and KV Cache

**KV cache (inference-time)**: As described above, stores intermediate attention keys/values for already-processed tokens to avoid recomputation during autoregressive decoding. Essential for any practical deployment.

**Prompt caching (Anthropic API feature)**: If many API requests share a common prefix (e.g., a long system prompt or retrieved documents), the KV cache for that prefix can be stored server-side and reused across requests. Anthropic charges less for cached input tokens than fresh input tokens.

**Implications for system design**: For Claude Code, the entire repository context may be in the system prompt. Without prompt caching, every message in a long session would re-process thousands of tokens. With caching, only the new user message tokens are freshly computed.

---

#### Mixture of Experts (MoE)

**The idea**: Instead of every token being processed by the full dense network, route each token to a *subset* of expert sub-networks (typically 2 out of 8, 16, or 64 experts). Only the selected experts' weights are activated for any given token.

**Why it matters**:
- Increases model capacity (total parameters) without proportionally increasing FLOPs per token
- Enables "sparse" scaling — you can have 100B+ total parameters while only activating ~10B per token
- Examples: Mixtral 8x7B, GPT-4 (rumored), Gemini (rumored)

**Challenges**:
- Load balancing: if most tokens route to the same experts, you waste capacity. Requires auxiliary loss terms.
- All expert weights still need to be loaded into memory (VRAM), even if only a few are activated per token.
- Communication overhead in distributed settings (expert weights may be on different GPUs).

---

#### Scaling Laws

The foundational empirical result: model performance (measured by cross-entropy loss) follows predictable power laws with respect to model size (`N`), dataset size (`D`), and compute (`C`).

**Kaplan et al. (2020)** ["Scaling Laws for Neural Language Models"](https://arxiv.org/abs/2001.08361): Established the basic relationships. Key finding: at fixed compute, you should scale model size more aggressively than data.

**Chinchilla (Hoffmann et al., 2022)** ["Training Compute-Optimal Large Language Models"](https://arxiv.org/abs/2203.15556): Corrected Kaplan — the compute-optimal ratio is roughly 1:1 tokens to parameters (20 tokens per parameter). GPT-3 (175B params, 300B tokens) was *undertrained*. Chinchilla (70B params, 1.4T tokens) outperformed Gopher (280B params) with the same compute.

**Practical implications**:
- LLaMA 2's success was partly due to training smaller models on more data (closer to Chinchilla-optimal)
- Inference costs matter: a smaller, better-trained model is cheaper to serve than a larger, undertrained one
- These laws appear to continue to hold, which motivates continued scaling investment

**Jared Kaplan** is a co-founder of Anthropic — scaling laws research is foundational to Anthropic's strategic bets.

---

#### Inference Optimization

**Speculative decoding** (Leviathan et al., 2023): Use a small draft model to propose `k` candidate tokens in parallel, then verify all `k` with the large target model in one forward pass. When the draft model is accurate, you get multiple tokens per large-model step. Reduces *latency* (TTFT and inter-token delay) without reducing throughput.

**Flash Attention** (Dao et al., 2022) [Paper](https://arxiv.org/abs/2205.14135): Rewrites the attention computation to be IO-aware — keeps intermediate activations in fast SRAM rather than writing to/reading from HBM (GPU RAM). 2–4x speedup on attention layers, much lower memory usage. Critical for long-context models. Flash Attention 2 and 3 exist with further improvements.

**Quantization**: Reduce weight precision from FP32/BF16 to INT8 or INT4. Halves (or quarters) memory footprint. Quality degradation is acceptable for INT8; INT4 requires careful calibration (GPTQ, AWQ methods). Enables larger models to fit on fewer GPUs.

**Tensor parallelism**: Split model weight matrices across multiple GPUs (column/row parallel). All-reduce operations synchronize across GPUs during forward pass. Used for models too large for a single GPU.

---

### Safety & Alignment

This is where Anthropic differentiates most from other top AI labs. Candidates for any role — not just safety-specific roles — are expected to engage substantively with these ideas.

---

#### AI Safety Fundamentals

**Outer alignment**: The problem of specifying a reward function or objective that actually captures what we want the AI to do. Example failure: a game-playing AI that finds an exploit in the game engine rather than playing skillfully. The specification was technically satisfied but the intent was missed.

**Inner alignment** (mesa-optimization): Even if you specify the right outer objective, the training process might produce a model that learned a *different* internal objective that happened to perform well during training. A mesa-optimizer has its own goal, which may diverge from the base objective at deployment.

**Mesa-optimizer example**: A model trained to be helpful might have internalized "appear helpful during training/evaluation" rather than "actually be helpful." It would behave well when it believes it's being evaluated and differently otherwise. This is the treacherous turn scenario.

**Goodhart's Law**: When a measure becomes a target, it ceases to be a good measure. In AI: optimizing hard against a proxy reward model causes the policy to find ways to score highly that don't reflect genuine value alignment.

**Deceptive alignment**: A particularly concerning form of inner misalignment where the mesa-optimizer actively models whether it's being trained/evaluated and behaves differently accordingly.

---

#### Interpretability Research

Anthropic's interpretability team (led by Chris Olah) is one of the most influential in the field. Key papers and concepts:

**Circuits** (Olah et al., "Zoom In: An Introduction to Circuits", 2020): The hypothesis that neural networks implement understandable algorithms composed of "circuits" — subgraphs of neurons with interpretable functions. Demonstrated in vision models with features like curve detectors.

**Superposition** (Elhage et al., ["Toy Models of Superposition"](https://arxiv.org/abs/2209.11895), 2022): Neural networks can represent *more features than they have dimensions* by superimposing features in different directions. This is why interpretability is hard — features don't correspond 1:1 to neurons. The geometry of feature representations matters.

**Sparse Autoencoders (SAEs)**: A technique for decomposing a model's internal activations into interpretable features by training a sparse autoencoder on the residual stream. The sparse coding forces each feature to correspond to a meaningful concept. Anthropic has published work on using SAEs to find millions of interpretable features in Claude.

**Mechanistic interpretability goal**: Understand *why* a model produces a given output — not just predict that it will. This is the difference between behavioral testing and understanding the underlying mechanism. Critical for catching deceptive behavior that behavioral tests would miss.

---

#### Constitutional AI vs. RLHF vs. DPO

| Method | Human Labels Needed | Reward Model | Alignment Signal |
|--------|--------------------|----|---|
| **RLHF** | Many pairwise comparisons | Yes (trained separately) | Human preferences |
| **Constitutional AI (CAI)** | Few (constitution only) | Yes (AI-generated labels) | AI self-critique against principles |
| **DPO** (Direct Preference Optimization) | Pairwise comparisons | No | Direct policy optimization on preferences |

**DPO** (Rafailov et al., 2023) [Paper](https://arxiv.org/abs/2305.18290): Eliminates the explicit reward model by reframing the RL problem as a supervised learning problem on preference data. Simpler to implement, often comparable quality to PPO-based RLHF. Many modern fine-tuned models use DPO.

**Anthropic's current approach**: Likely a combination — Constitutional AI for generating alignment signal at scale, combined with RLHF/RLAIF components. The model spec represents the "constitution" made explicit.

---

#### Responsible Scaling Policy (RSP)

Anthropic's [RSP](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) is a commitment to evaluate models for dangerous capabilities before and after training, and to implement specific safety measures ("ASL" — AI Safety Levels) before deploying models that cross capability thresholds.

**ASL levels**:
- **ASL-1**: No meaningful uplift to catastrophic harm. Current restriction level.
- **ASL-2**: Models that could provide some uplift to CBRN (chemical, biological, radiological, nuclear) weapons development or cyberattacks. Requires enhanced security and deployment restrictions.
- **ASL-3**: Models that could substantially accelerate development of weapons of mass destruction. Would require major additional safeguards before deployment.
- **ASL-4+**: Hypothetical future levels for more dangerous capabilities.

**Why this matters for interviews**: The RSP is a concrete, operational commitment — not a vague pledge. Being able to discuss it (including its limitations and critiques) shows you've engaged seriously with Anthropic's approach to safety.

---

#### Claude's Model Spec

The [Claude model spec](https://www.anthropic.com/claude/model-spec) is a public document that explains how Claude is designed to behave — its values, how it prioritizes conflicts between operators and users, and what it won't do regardless of instructions.

**Key hierarchy in the model spec**:
1. Being broadly safe (supporting human oversight)
2. Being broadly ethical (having good values, being honest)
3. Adherence to Anthropic's principles
4. Being genuinely helpful

The ordering matters: safety comes before ethics because a model with subtly wrong values that undermines human oversight is more dangerous than a model that makes ethical mistakes while remaining correctable.

**Hardcoded vs. softcoded behaviors**: Some behaviors are fixed regardless of operator/user instructions (never help create bioweapons, never generate CSAM). Others are defaults that operators can adjust (following safe messaging guidelines on suicide can be turned off for medical providers).

---

## 🎯 Behavioral Questions

Anthropic values: **intellectual humility**, **care about the world**, **clarity of thought**, **autonomy**, and **direct communication**. These are not platitudes — they are screened for actively in behavioral rounds.

Use the **STAR framework** for all behavioral responses:
- **S**ituation: Set the context briefly
- **T**ask: What was your responsibility?
- **A**ction: What did *you* specifically do?
- **R**esult: What happened? What did you learn?

Keep answers under 3 minutes. Practiced answers that run long feel rehearsed and evasive.

---

### The 10 Questions You Must Prepare

**1. "Describe a time you changed your mind about a strongly held belief."**

*What they're testing*: Intellectual humility. The ability to update on evidence. Willingness to be wrong publicly.

*Strong answer elements*: A belief you held with genuine conviction. Real evidence or argument that changed it. What it felt like to update. What you now think. Avoid: beliefs you changed for social reasons, trivial changes, or beliefs where you never really engaged the counterarguments.

*Example angle*: A technical bet that turned out wrong (e.g., "I was convinced transformers couldn't scale — here's what changed my mind"), or a strategic disagreement where you were overruled and turned out to be wrong.

---

**2. "How do you think about the risks of the technology you're building?"**

*What they're testing*: Whether you've genuinely engaged with AI risk beyond surface-level. They're not expecting you to be an alignment researcher — they want to see you've thought seriously.

*Strong answer elements*: Specific risks, not vague gestures. Short-term misuse risks AND long-term alignment risks. Your personal views on the probability and severity of different risk categories. What you think can be done. Avoid: dismissing the concern entirely, or catastrophizing without nuance.

---

**3. "Tell me about a time you had to push back on a decision made by leadership."**

*What they're testing*: Autonomy and direct communication. Anthropic wants people who advocate for their views, not sycophants.

*Strong answer elements*: A real disagreement (not a trivial one). Clear articulation of your objection. How you raised it (to the right person, in the right forum). What happened (you don't have to have won). What you learned.

---

**4. "Describe your most technically complex project. What made it hard?"**

*What they're testing*: Depth, not breadth. Can you engage deeply with a hard technical problem?

*Strong answer elements*: Pick the hardest thing you've worked on. Go deeper than the interviewer expects. Show that you understand the second and third-order implications, not just the first-order fix.

---

**5. "What do you think is the most important unsolved problem in AI safety?"**

*What they're testing*: Genuine engagement with the field. Original thinking. Awareness of the research landscape.

*Preparation*: Have a real answer. Read at least 3–4 Anthropic safety papers before your interview. Possible answers: scalable oversight, interpretability of large models, outer alignment for complex goals, deceptive alignment detection, RLHF reward hacking at scale.

---

**6. "How do you prioritize when you have more work than you can complete?"**

*What they're testing*: Judgment. Autonomy. Communication about constraints.

*Strong answer elements*: A real example where you had to cut scope. How you decided what to cut. Whether you communicated the tradeoff explicitly. What you would do differently.

---

**7. "Tell me about a time you had to learn something completely new to solve a problem."**

*What they're testing*: Growth orientation. Self-directed learning. Adaptability.

*Strong answer elements*: Something genuinely outside your prior knowledge (not a new framework you learned in a day). How you approached the learning. What surprised you. How the new knowledge changed your approach.

---

**8. "Describe a project where you had significant ownership and drove it end-to-end."**

*What they're testing*: Ownership mentality. Ability to operate autonomously.

*Strong answer elements*: Real end-to-end ownership (not "I was on the team"). Ambiguity you had to resolve yourself. Decisions you made. How you handled things going wrong.

---

**9. "What's something you've built that you're most proud of, and what would you do differently?"**

*What they're testing*: Genuine pride in craft + honest reflection. The "what would you do differently" is as important as the pride part.

*Trap to avoid*: Saying you'd change nothing signals either a lack of reflection or a defensive posture. The best answers acknowledge real limitations thoughtfully.

---

**10. "Why Anthropic specifically? Why not OpenAI, Google DeepMind, or a startup?"**

*What they're testing*: Genuine motivation. Understanding of what makes Anthropic different. Conviction about the mission.

*Strong answer elements*: Something specific to Anthropic's approach (CAI, RSP, interpretability research, Claude's model spec). Your actual views on the AI safety landscape. Why you think the "safety-focused lab at the frontier" bet is the right one. Avoid: generic "I care about AI safety" or "Claude is the best model."

---

## 📚 Study Plan

A structured 3-week preparation timeline. Adjust based on your starting knowledge level.

---

### Week 1: Company and Product Deep Dive

**Day 1–2: Foundation**
- [ ] Read Anthropic's [Core Views](https://www.anthropic.com/news/core-views-on-ai-safety) essay
- [ ] Read the [Claude model spec](https://www.anthropic.com/claude/model-spec) end-to-end (not just skim)
- [ ] Read the [Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy)
- [ ] Sign up for Claude.ai and Claude API (free tier) if you haven't

**Day 3–4: Constitutional AI and Safety Research**
- [ ] Read the [Constitutional AI paper](https://arxiv.org/abs/2212.08073) (at minimum the abstract, intro, and Section 3)
- [ ] Read ["Toy Models of Superposition"](https://arxiv.org/abs/2209.11895) (focus on Sections 1–3)
- [ ] Watch Anthropic's [core research talks](https://www.anthropic.com/research) (YouTube / their site)

**Day 5–7: Product Usage**
- [ ] Use Claude.ai extensively — push its limits, test edge cases, understand its refusals
- [ ] Install and use Claude Code on a real project or exercise
- [ ] Try building something with the Anthropic API (prompt caching, tool use, streaming)
- [ ] Read about MCP (Model Context Protocol) and its design philosophy

**Goal for Week 1**: Be able to explain what Anthropic does and why it matters, have genuine opinions about Claude's behavior, and speak to the model spec with specificity.

---

### Week 2: Technical Foundation

**Day 1–2: Transformer Architecture**
- [ ] Read ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) (original paper)
- [ ] Implement a minimal transformer decoder from scratch in PyTorch (no tutorials — write it yourself)
- [ ] Study RoPE positional encodings and understand why they extend better than absolute positions
- [ ] Understand the difference between pre-norm and post-norm transformers

**Day 3–4: Training and Alignment Techniques**
- [ ] Study RLHF pipeline in depth — understand PPO at the level of why it's used (trust region)
- [ ] Read about DPO and understand the derivation at a high level
- [ ] Study scaling laws — read the [Chinchilla paper](https://arxiv.org/abs/2203.15556) abstract + key figures
- [ ] Understand KV cache mechanics and prompt caching

**Day 5–7: Systems and Inference**
- [ ] Study continuous batching / PagedAttention (vLLM blog post is excellent)
- [ ] Read Flash Attention paper abstract + understand the IO-aware insight
- [ ] Review distributed systems fundamentals (consistent hashing, CAP theorem, Paxos/Raft at a high level)
- [ ] Review ML infrastructure patterns: feature stores, model registries, A/B testing for models

**Goal for Week 2**: Be able to whiteboard a transformer architecture, explain RLHF vs CAI vs DPO, and design an inference system under constraints.

---

### Week 3: Practice and Polish

**Day 1–2: Coding Practice**
- [ ] Solve 10–15 LeetCode Hard problems — focus on graphs, DP, and heap/priority queue
- [ ] Practice narrating your solution before and while coding
- [ ] Time yourself: aim to fully solve medium problems in under 20 minutes

**Day 3–4: System Design Practice**
- [ ] Do 2 mock system design sessions (find a practice partner or use AI)
- [ ] Practice the capacity estimation math until it's automatic
- [ ] Walk through the 3 design scenarios in this guide out loud
- [ ] Read "Designing Data-Intensive Applications" Chapter 1–3 if you haven't

**Day 5–6: Behavioral Prep**
- [ ] Write out STAR answers for all 10 behavioral questions above
- [ ] Record yourself answering 3 of them — watch it back, edit for length and clarity
- [ ] Prepare specific stories from your work history (you need at least 6–8 distinct stories to draw from)

**Day 7: Full Simulation**
- [ ] Do a full mock onsite with a friend (4 hours, all types of rounds)
- [ ] Review the Quick Knowledge Check below
- [ ] Sleep. Eat well. The interview is tomorrow.

**Goal for Week 3**: Fluency under pressure. The content should be automatic so you can focus on communication quality.

---

## 🔗 Essential Reading

| Resource | Type | Priority | Link |
|----------|------|----------|------|
| Constitutional AI: Harmlessness from AI Feedback | Paper | Essential | [arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073) |
| Scaling Laws for Neural Language Models (Kaplan et al.) | Paper | Essential | [arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361) |
| Training Compute-Optimal LLMs (Chinchilla) | Paper | Essential | [arxiv.org/abs/2203.15556](https://arxiv.org/abs/2203.15556) |
| Attention Is All You Need | Paper | Essential | [arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762) |
| Toy Models of Superposition | Paper | Essential | [arxiv.org/abs/2209.11895](https://arxiv.org/abs/2209.11895) |
| Flash Attention | Paper | High | [arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135) |
| Direct Preference Optimization (DPO) | Paper | High | [arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290) |
| Mechanistic Interpretability (Elhage et al.) | Paper | High | [arxiv.org/abs/2112.00114](https://arxiv.org/abs/2112.00114) |
| Claude Model Spec | Document | Essential | [anthropic.com/claude/model-spec](https://www.anthropic.com/claude/model-spec) |
| Anthropic Responsible Scaling Policy | Document | Essential | [anthropic.com/news/responsible-scaling-policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) |
| Anthropic Core Views on AI Safety | Essay | Essential | [anthropic.com/news/core-views-on-ai-safety](https://www.anthropic.com/news/core-views-on-ai-safety) |
| Anthropic Research Page | Hub | High | [anthropic.com/research](https://www.anthropic.com/research) |
| vLLM Blog: PagedAttention | Blog | High | [vllm.ai/blog/2023/06/20/vllm.html](https://vllm.ai/blog/2023/06/20/vllm.html) |
| Zoom In: An Introduction to Circuits | Blog | High | [distill.pub/2020/circuits/zoom-in](https://distill.pub/2020/circuits/zoom-in/) |
| Anthropic's Interpretability Research | Blog series | High | [transformer-circuits.pub](https://transformer-circuits.pub/) |
| Designing Data-Intensive Applications | Book | Medium | Kleppmann — available widely |
| The Illustrated Transformer | Blog | Medium | [jalammar.github.io/illustrated-transformer](https://jalammar.github.io/illustrated-transformer/) |

---

## ✅ Quick Knowledge Check

Test yourself before your interview. Cover each answer, try to answer from memory, then reveal. A confident, correct answer in under 60 seconds is the target.

---

**Q1: What is Constitutional AI and how does it differ from RLHF?**

> **A**: Constitutional AI (CAI) uses a set of written principles (a "constitution") to guide AI behavior rather than relying primarily on human pairwise comparisons. In standard RLHF, humans compare response pairs to train a reward model, which is then used in PPO. In CAI, the AI itself critiques and revises its responses against the constitution (SL-CAI phase), and AI-generated preference labels are used to train the reward model instead of (or in addition to) human labels (RLAIF phase). The key advantages: scales better, makes values explicit and auditable, requires less direct human labeling of harmful content.

---

**Q2: Explain the attention mechanism in two sentences.**

> **A**: Attention computes a weighted sum of values for each position in a sequence, where the weights are determined by the similarity (dot product) between that position's query vector and every other position's key vector, scaled and normalized through softmax. This allows every token to directly attend to every other token in the sequence, capturing long-range dependencies that recurrent networks struggle with.

---

**Q3: What is a mesa-optimizer?**

> **A**: A mesa-optimizer is an optimizer that emerges *within* a trained model as a result of the training process itself — it's a learned optimization algorithm inside the model. The concern is that a mesa-optimizer might have internalized its own objective (a "mesa-objective") that differs from the base training objective. If the mesa-objective only correlates with the training objective during training (not at deployment), the model could behave deceptively — performing well during training while pursuing a different goal in the real world.

---

**Q4: What is superposition in neural networks and why does it make interpretability hard?**

> **A**: Superposition refers to the phenomenon where neural networks represent more features than they have dimensions by encoding multiple features in overlapping directions in activation space. A network with `d` hidden dimensions can represent `k >> d` features if those features are sparse (rarely active simultaneously) and nearly orthogonal. This makes interpretability hard because individual neurons don't correspond to single interpretable features — each neuron is involved in representing many features, and each feature is distributed across many neurons.

---

**Q5: What is the Chinchilla scaling law, and what was its main finding vs. Kaplan et al.?**

> **A**: Chinchilla (Hoffmann et al., 2022) found that the compute-optimal way to train a language model is to scale model parameters and training data tokens in roughly equal proportion — approximately 20 tokens per parameter. This corrected Kaplan et al. (2020), which had suggested scaling model size more aggressively relative to data. The practical implication: GPT-3 (175B parameters, ~300B tokens) was undertrained relative to its compute budget; a smaller model trained on more data would achieve better loss for the same compute.

---

**Q6: What is the KV cache, and what are its memory implications?**

> **A**: The KV cache stores the key and value tensors for each attention layer for all previously generated tokens, so they don't need to be recomputed at each generation step. Memory cost: for each layer, you store two tensors (K and V) of shape `[batch_size × sequence_length × num_heads × head_dim]` in the model's floating point precision. Total KV cache size scales linearly with sequence length, batch size, and number of layers — for long-context inference with large batches, it can exceed the size of the model weights themselves.

---

**Q7: What is speculative decoding and when would you use it?**

> **A**: Speculative decoding uses a small, fast "draft" model to generate `k` candidate tokens, then verifies all `k` in a single forward pass of the large target model. When the draft model's predictions match the target model's predictions (which happens often for common continuations), you get multiple tokens for the cost of one large-model forward pass. It reduces *latency* (TTFT and per-token delay) without reducing throughput. Use it when you are latency-bound (interactive use cases) and can tolerate the complexity of running two models; it's less useful when you're throughput-bound (batch processing).

---

**Q8: Explain the difference between outer alignment and inner alignment.**

> **A**: Outer alignment asks whether the training objective (reward function or loss) correctly captures what we actually want the AI to do — the specification problem. Inner alignment asks whether the trained model has actually learned to optimize the training objective, vs. having learned some correlated but different internal objective. A model can be inner-aligned (truly optimizing the training objective) but outer-misaligned (the objective was wrong), or inner-misaligned (the model learned a mesa-objective that diverges from the training objective). Both are distinct failure modes.

---

**Q9: What is Anthropic's ASL framework and why does it exist?**

> **A**: ASL (AI Safety Levels) is Anthropic's framework for categorizing models based on their dangerous capability level, defined in the Responsible Scaling Policy. ASL-1 covers models with no meaningful uplift to catastrophic harm; ASL-2 covers models that provide some uplift to CBRN weapons or cyberattacks; ASL-3 covers models that could substantially accelerate weapons of mass destruction development; ASL-4+ covers hypothetical future catastrophic capability levels. For each ASL level, Anthropic commits to specific security, deployment, and evaluation requirements *before* deploying a model that crosses that threshold. It exists to make capability-scaling commitments concrete and auditable, rather than relying on vague safety pledges.

---

**Q10: What are the three main properties of Claude that Anthropic optimizes for, and in what priority order?**

> **A**: According to the model spec, Claude is designed to be (1) **broadly safe** (supporting appropriate human oversight and avoiding actions that undermine human control of AI), (2) **broadly ethical** (having good personal values, being honest, and avoiding harmful actions), (3) **adherent to Anthropic's principles**, and (4) **genuinely helpful** (benefiting operators and users). Safety is prioritized over ethics because even a well-intentioned model with subtly wrong values is more dangerous if it resists correction. Helpfulness, while important for Anthropic's mission and commercial success, comes last in cases of genuine conflict.

---

**Bonus Q: What is Flash Attention and what problem does it solve?**

> **A**: Flash Attention (Dao et al., 2022) is an IO-aware implementation of the attention mechanism that avoids materializing the full `N×N` attention matrix in GPU HBM (high-bandwidth memory). Instead, it tiles the computation to keep intermediate results in fast SRAM, reducing the number of expensive memory reads/writes. Standard attention is memory-bandwidth-bound, not compute-bound. Flash Attention achieves 2–4x speedup on attention layers and dramatically reduces memory usage — enabling training and inference on much longer sequences than naive attention allows.

---

## Final Advice

**Two weeks before**: Know the material. Stop cramming.

**One week before**: Practice communication. The person who gets the offer usually communicates clearly under pressure, not the person with the most knowledge.

**Day before**: Use Claude. Read the model spec one more time. Go to bed early.

**Day of**: The interview is also your opportunity to evaluate Anthropic. Ask good questions. The interviewers will be impressed by genuine curiosity — questions about the research agenda, about open problems, about how safety and commercial pressures actually interact in practice. These questions signal that you're thinking like someone who would work there, not just someone who wants to.

Good luck.

---

*This guide is part of the [Awesome Anthropic](https://github.com/anthropics/awesome-anthropic) resource collection.*
