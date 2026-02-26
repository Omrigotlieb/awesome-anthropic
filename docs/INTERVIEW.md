# 🎮 Anthropic Interview Prep RPG
## Your Quest: Land a Role at the World's Most Important AI Company

> *You are about to embark on a journey. At the end lies one of the most competitive, interesting, and consequential jobs in tech. The final boss is formidable. But you've got this guide.*

---

## 📊 Your Progress

```
[░░░░░░░░░░░░░░░░░░░░] 0% — Quest begins. Choose your character.
```

**XP Tracker**
| Level | Title | XP Required |
|-------|-------|-------------|
| 1 | Intern | 0 XP |
| 2 | Engineer I | 100 XP |
| 3 | Staff | 250 XP |
| 4 | Principal | 450 XP |
| 5 | **Anthropic Hire** ✅ | 600 XP |

---

## 🗺️ Character Select

Before diving in, pick your path — the guide covers all of them but certain boss fights are harder for each class.

| Class | Key Battles | Starting Advantage |
|-------|-------------|-------------------|
| ⚙️ **Engineering** | Coding Gauntlet + System Design Castle | Algorithms and systems |
| 🔬 **Research / ML** | ML Sage's Trial + Final Boss | Math and architectures |
| 🛡️ **Policy / Safety** | Final Boss (Safety) + Behavioral Trials | Mission fluency |
| 🏗️ **Operations** | Behavioral Trials + Scouting the Dungeon | Execution and judgment |

*All classes face the behavioral trials. All classes will be asked "Why Anthropic?" Don't skip Level 1.*

---

## 🗺️ Adventure Map

```
[Level 1] Know Your Enemy (About Anthropic)
      │
      ▼
[Level 2] Scouting the Dungeon (The Process)
      │
      ▼
[⚔️ Boss 1] The Coding Gauntlet
      │
      ▼
[🏰 Boss 2] System Design Castle
      │
      ▼
[🧠 Boss 3] The ML Sage's Trial
      │
      ▼
[👁️ Boss 4] Safety & Alignment — THE FINAL BOSS
      │
      ▼
[💬 Side Quest] The Behavioral Trials
      │
      ▼
[📅 Training Montage] 3-Week Study Plan
      │
      ▼
[📚 Tome of Knowledge] Essential Reading
      │
      ▼
[🎯 Final Check] 10 Knowledge Boss Rounds
      │
      ▼
[🏆 Victory Screen]
```

---

## Level 1: Know Your Enemy

> *"The best warriors study their opponent before the battle begins."*
> — Every RPG mentor ever

```
[████░░░░░░░░░░░░░░░░] 10% — Loading mission briefing...
```

### The Mission

Anthropic's stated mission is **the responsible development and maintenance of advanced AI for the long-term benefit of humanity.** This is not homepage copy — it's operationally load-bearing. It explains why Anthropic:

- Publishes safety research that actively helps competitors
- Imposes usage restrictions on Claude that cost real revenue
- Has a [Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) that could force a pause on model development
- Invests heavily in interpretability research before it has immediate commercial value

The key insight: Anthropic occupies a deliberate position as a "safety-focused lab at the frontier." The belief is that if powerful AI is coming regardless, it's better to have safety-oriented organizations leading than to cede that ground.

**Before your recruiter screen**, you should be able to articulate this *without* sounding like you memorized the homepage. Interviewers listen for genuine conviction.

### The Lore (Timeline)

| Year | Event |
|------|-------|
| 2021 | Founded by Dario Amodei (CEO), Daniela Amodei (President), Tom Brown, Chris Olah, Sam McCandlish, Jack Clark, Jared Kaplan, and others from OpenAI |
| 2022 | Constitutional AI paper published; Claude (internal) development begins |
| 2023 | Claude 1.0 and Claude 2 released; $7B+ raised from Google and others |
| 2024 | Claude 3 family (Haiku, Sonnet, Opus); Claude 3.5 Sonnet; Claude Code launched in beta |
| 2025 | Claude 3.7 with extended thinking; Claude 4 family (Sonnet 4, Opus 4); MCP becomes open standard |

**Funding**: Google has invested billions (with access to TPU compute). Valuation reported above $60B as of 2025.

### The Product Arsenal

| Product | What It Is | Why It Matters |
|---------|-----------|----------------|
| **Claude API** | Programmatic access to Claude models | Core revenue driver |
| **Claude.ai** | Consumer/pro chat interface | Public-facing capability showcase |
| **Claude Code** | Agentic coding assistant (CLI + IDE) | Flagship agentic product; extended context + tool use |
| **MCP** | Open standard for connecting AI to tools/data | Ecosystem play; interoperability |

### The Culture Code (What Interviewers Are Actually Testing)

⚡ **Power-up**: These are not platitudes. Each one is actively screened for.

- **Safety-first, not safety-theater**: Know the difference between capability research and safety research. Anthropic does both and understands *why* each matters.
- **Research-driven**: Decisions are grounded in empirical findings. Be ready to discuss tradeoffs with evidence, not vibes.
- **Intellectual humility**: "I don't know, but here's how I'd think about it" is a valid — and valued — answer.
- **Autonomy with alignment**: You're expected to identify what needs doing and do it. Not wait for assignments.

---

> 🎮 **+50 XP — Mission Briefing Complete!**
>
> *Achievement Unlocked: "Knows What Anthropic Actually Does"*

---

## ✅ Checkpoint 1

Before moving on, you should be able to answer these cold:
- [ ] What is Constitutional AI, in one sentence?
- [ ] What is the RSP and why does it matter?
- [ ] What is Claude Code?
- [ ] Why does Anthropic publish research that helps competitors?

---

## Level 2: Scouting the Dungeon

> *Know the map before you start running through it.*

```
[████████░░░░░░░░░░░░] 20% — Interview process loaded.
```

### The Dungeon Map

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

### Stage-by-Stage Intel

**Recruiter Screen (30 min)**
Checking fit, compensation alignment, and whether you can articulate *why Anthropic specifically*. Have a clear, genuine answer to "why not OpenAI or Google DeepMind?" Mentioning the model spec, Constitutional AI, or the RSP signals real homework was done.

**Take-Home / Async Challenge**
Formats vary: a longer ambiguous coding problem, an ML implementation task, or a written design doc critique. Treat it as a professional deliverable — write clean code with comments. Anthropic hires strong writers; if the output is prose, edit it.

**Technical Phone Screen (1 hour)**
Live coding in a shared editor. Expect 1–2 medium-to-hard algorithmic problems. Communication matters as much as correctness — narrate your thinking. Ask clarifying questions before coding.

**Virtual Onsite**
Typically one full day or spread across two. Each round is 45–60 minutes. See the boss fights below for detailed prep per round type.

**Offer Process**
Anthropic moves relatively quickly post-onsite (1–2 weeks). Compensation is competitive with top frontier labs: base, equity (SAFEs or options), and benefits. Negotiate — they expect it.

---

> 🎮 **+50 XP — Dungeon Scouted!**

---

## ✅ Checkpoint 2

- [ ] You know which rounds to expect for your role
- [ ] You have a genuine, specific "why Anthropic" answer prepared
- [ ] You've used Claude.ai, Claude Code, and the API at least once

---

## ⚔️ BOSS FIGHT 1: The Coding Gauntlet

```
[████████████░░░░░░░░] 30% — BOSS ENCOUNTER DETECTED
```

> **BOSS FIGHT RULES**: You have 45 minutes. You are expected to narrate as you code. The interviewer is evaluating problem-solving *and* communication. A correct solution with poor communication often loses to a slightly imperfect solution with excellent communication.

**Languages**: Python preferred for ML-adjacent roles. TypeScript/JavaScript for frontend/Claude Code. Use whatever you're strongest in for pure algorithms — but know Python well.

**Know these patterns cold:**

| Pattern | Frequency | Real-World Anthropic Connection |
|---------|-----------|----------------------------------|
| Graph traversal (BFS/DFS) | HIGH | Agent graphs, dependency resolution |
| Dynamic programming | HIGH | Subsequence, knapsack, interval DP |
| Tree problems | MEDIUM | Binary trees, trie, n-ary trees |
| Sliding window / two pointers | MEDIUM | String/stream manipulation |
| Heap / priority queue | MEDIUM | Streaming data, top-K problems |
| Union-Find | LOW-MEDIUM | Connected components |

---

### Dungeon Encounter 1: Token Stream Processor

**Monster Type**: Data Structures + Streaming

**The prompt**: You're building a streaming token buffer for an LLM inference system. Tokens arrive as integers. Implement a data structure supporting:
- `push(token)` — Add a token to the buffer
- `get_window(k)` — Return the last `k` tokens in order
- `flush()` — Return all tokens and clear the buffer

Optimize for `get_window` being called far more frequently than `push` or `flush`.

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
        from itertools import islice
        start = len(self._buf) - k
        return list(islice(self._buf, start, None))

    def flush(self) -> list[int]:
        tokens = list(self._buf)
        self._buf.clear()
        return tokens
```

⚡ **Power-up**: Know *why* `deque` over `list` — O(1) append/popleft vs O(n) list prepend. Mention thread-safety for production. Connect it to KV caching in inference.

---

### Dungeon Encounter 2: Dependency Graph Resolver

**Monster Type**: Graph + Topological Sort

**The prompt**: Given a list of tasks where each may depend on others, return a valid execution order. If a cycle exists, raise an error.

```python
from collections import defaultdict, deque
from typing import List

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

⚡ **Power-up**: This pattern is *live in production* at Anthropic. Claude Code orchestrates tool calls with dependencies. Say that out loud in the interview.

---

### Dungeon Encounter 3: LRU Cache with TTL

**Monster Type**: Data Structures + System Design Thinking

**The prompt**: Implement an LRU cache that also supports per-entry time-to-live (TTL) expiration. Expired entries should be treated as cache misses.

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

⚡ **Power-up**: KV caching in LLM inference is this exact pattern at scale. Connecting your data structures knowledge to real ML systems earns points.

---

### Dungeon Encounter 4: Merge K Sorted Token Streams

**Monster Type**: Heap + Iterator Pattern

**The prompt**: You have `k` sorted streams of (timestamp, token) pairs. Merge them into a single sorted output stream efficiently.

```python
import heapq
from typing import Iterator

def merge_streams(streams: list[Iterator[tuple[int, str]]]) -> Iterator[tuple[int, str]]:
    """Merge k sorted (timestamp, token) streams into one sorted stream."""
    heap = []
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

⚡ **Power-up**: Complexity is O(n log k) where n = total tokens, k = streams. Know this cold. Interviewers ask.

---

### Dungeon Encounter 5: Longest Context Window Fit

**Monster Type**: Greedy + Knapsack Variant

**The prompt**: Given a list of documents with token counts and a context window size `C`, find the maximum number of complete documents you can fit. Prefer shorter documents first (greedy). Return indices in original order.

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

    return sorted(selected)  # return in original document order
```

⚡ **Power-up**: When the interviewer asks about alternative objectives — e.g., maximize *total tokens used* instead of document count — that's a 0/1 knapsack variant. Have that answer ready.

---

> 🎮 **+150 XP — Coding Gauntlet Defeated!**
>
> *Achievement Unlocked: "Algorithm Slayer" — 5 for 5 on the Coding Dungeon*

---

## ✅ Checkpoint 3

- [ ] You can implement Kahn's algorithm for topological sort without looking it up
- [ ] You know when to use `deque` vs `list` and why
- [ ] You've practiced narrating a solution while coding simultaneously

---

## 🏰 BOSS FIGHT 2: System Design Castle

```
[████████████████░░░░] 40% — Entering the Castle...
```

> **BOSS FIGHT RULES**: System design at Anthropic is different from system design at a typical tech company. You're expected to understand the ML systems layer — GPU memory, batching strategies, latency/throughput tradeoffs. Web-scale distributed systems knowledge is table stakes. The differentiating move is connecting it to how models actually run.

**The universal framework for any system design answer:**
1. Clarify requirements (latency targets, scale, consistency needs)
2. Capacity estimation (back-of-envelope math — show your work)
3. High-level architecture (sketch it, talk through it)
4. Deep dive on 1–2 interesting components
5. Tradeoffs and failure modes
6. How you'd monitor and iterate

---

### Castle Room 1: Real-Time Streaming LLM Inference

**Requirements to clarify first**: P50/P99 TTFT targets, concurrent users, model size, streaming vs. batch, stateless vs. stateful (multi-turn).

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
             Token Stream Buffer ──► SSE / WebSocket ──► Client
```

**The four moves that separate good answers from great ones:**

- **Continuous batching** (in-flight batching): New requests join an existing batch as soon as a sequence finishes, rather than waiting for the entire batch to complete. This is how vLLM and TGI work. Dramatically improves GPU utilization.
- **PagedAttention**: vLLM's core insight — treat the KV cache like virtual memory with pages. Eliminates fragmentation from variable-length sequences. Key reason vLLM became the dominant inference engine.
- **Speculative decoding**: A small draft model generates candidate tokens; the large model verifies them in parallel. Reduces latency for interactive (latency-bound) workloads.
- **Prompt caching**: Cache the KV activations for a shared system prompt prefix across requests. Anthropic's API exposes this explicitly. Critical for Claude Code's per-conversation efficiency.

⚡ **Power-up**: Know your hardware math. A 70B parameter model in BF16 requires ~140GB VRAM. An H100 has 80GB. That means tensor parallelism across at least 2 H100s for a 70B model. ~1000–3000 tokens/sec throughput on a 2xH100 setup for typical inference.

---

### Castle Room 2: Safety Evaluation Pipeline

**The problem**: Before deploying a new model version, evaluate it against hundreds of safety benchmarks — adversarial prompts, policy violations, capability elicitations. Must not bottleneck release cadence.

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
                │
                ▼
        Results Aggregator
                │
                ▼
    Safety Dashboard / Go/No-Go Gate
```

**Key design decisions to discuss:**
- **Parallelism**: Eval tasks are embarrassingly parallel — thousands of prompts across multiple inference replicas simultaneously.
- **Determinism**: Fixed seeds and temperature=0 for reproducible comparisons across checkpoints.
- **Regression detection**: Compare every run against a previous checkpoint baseline. Any safety regression is blocking.
- **Human-in-the-loop escalation**: Novel jailbreaks or new capability elicitations route to human review without blocking automated evals.
- **Storage**: Results stored with model checkpoint hash, eval version, and timestamp for longitudinal analysis.

---

### Castle Room 3: Claude Code Multi-Agent Orchestration

**The problem**: Claude Code spawns sub-agents to work in parallel — write tests while refactoring, explore multiple solution paths. Design the orchestration layer.

```
Orchestrator Agent (Claude)
        │
        ├── Sub-agent 1 (file editing)
        ├── Sub-agent 2 (test running)
        └── Sub-agent 3 (search/research)
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       Tool Executor          Context Manager
       (bash, editor,         (shared file state,
        file ops)              conflict resolution)
```

**The hard design challenges:**
- **Context isolation vs. sharing**: Sub-agents need enough context to work independently but must share file state. Solution: shared read access to a snapshot; writes go through a conflict-detection layer.
- **Error propagation**: If sub-agent 2 fails, does the orchestrator retry, reassign, or abort? Need an explicit policy.
- **Token budget management**: Each sub-agent consumes tokens. Orchestrator must track total spend and gracefully summarize or terminate expensive branches.
- **Idempotency**: Tool operations (especially file writes) should be idempotent or transactional to avoid partial states.
- **Message passing**: Use structured JSON messages (MCP-style) rather than free-form prose between orchestrator and sub-agents.

---

> 🎮 **+150 XP — Castle Cleared!**
>
> *Achievement Unlocked: "ML Systems Architect" — Talked about GPU memory in a system design interview*

---

## ✅ Checkpoint 4

- [ ] You can explain PagedAttention to a non-specialist in 90 seconds
- [ ] You know what continuous batching is and why it matters
- [ ] You can estimate VRAM requirements for a given model size from memory

---

## 🧠 BOSS FIGHT 3: The ML Sage's Trial

```
[████████████████████░░░░] 55% — The Sage awaits...
```

> **BOSS FIGHT RULES**: You should be able to explain any of these topics clearly to both a technical peer *and* a non-specialist. The "explain it simply" test is used constantly. If you can only explain something in jargon, you don't fully understand it yet.

---

### Trial 1: Transformer Architecture

**The core insight**: Instead of processing sequences recurrently (RNN-style), transformers process all positions simultaneously using attention — computing pairwise relationships between every token and every other token.

**Attention mechanism (scaled dot-product):**

```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) * V
```

- `Q` (queries), `K` (keys), `V` (values) are linear projections of the input
- `d_k` is the key dimension — the `sqrt` prevents softmax saturation in high dimensions
- Result: a weighted sum of values, where weights reflect query-key similarity

**Multi-head attention**: Run attention `h` times in parallel with different learned projections. Different heads learn different relationship types (syntactic, semantic, positional).

**A transformer block contains:**
1. Multi-head self-attention (+ residual connection + layer norm)
2. Feed-forward network — two linear layers with GELU nonlinearity
3. Residual connections throughout (critical for gradient flow)
4. Layer norm — pre-norm in modern architectures (Llama); post-norm in the original paper

**Positional encoding**: Transformers have no inherent sense of order.
- Original: sinusoidal fixed encodings
- Modern: **RoPE** (Rotary Position Embedding) — encodes *relative* positions by rotating Q and K vectors. Used in Claude, LLaMA, Mistral. Generalizes better to longer contexts.

**KV Cache**: During autoregressive generation, cache the keys and values for all previously generated tokens. Trades memory for compute. Cache size grows linearly with sequence length and batch size — this is why long-context inference is memory-bound.

---

### Trial 2: RLHF Pipeline

**The problem RLHF solves**: A base language model trained on internet text learns to imitate that distribution — including harmful, incorrect, and unhelpful content. We want helpful, harmless, honest behavior according to human values.

**Three-stage pipeline:**

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

**Key RLHF failure modes:**
- Human labelers have inconsistent preferences
- Reward hacking: the policy exploits the reward model's blind spots
- Expensive: requires large amounts of human comparison data
- The reward model is a proxy, not ground truth (hello, Goodhart's Law)

---

### Trial 3: Constitutional AI (CAI)

Anthropic's approach — introduced in ["Constitutional AI: Harmlessness from AI Feedback"](https://arxiv.org/abs/2212.08073) (Bai et al., 2022).

**The key innovation**: Instead of humans labeling every harmful/helpful distinction, define a *constitution* — a set of principles — and use the AI itself to evaluate and revise its outputs against those principles.

**Phase 1: Supervised Learning from AI Feedback (SL-CAI)**
1. Prompt the model with a potentially harmful request
2. Model generates an initial response
3. Show the model its own response + a constitutional principle ("Does this encourage violence? Revise it.")
4. Model generates a revised response
5. Fine-tune on the revised responses

**Phase 2: RL from AI Feedback (RLAIF)**
- Use a feedback model (trained on the constitution) to generate preference labels instead of humans
- Train a reward model on those AI-generated preferences
- Run standard RLHF with this reward model

**Why this matters**: Scales better than RLHF. Makes values explicit and auditable (the constitution is readable). The model can explain *why* a response is problematic. Forms the foundation for Claude's model spec.

---

### Trial 4: Alignment Methods Compared

| Method | Human Labels Needed | Reward Model | Alignment Signal |
|--------|--------------------|----|---|
| **RLHF** | Many pairwise comparisons | Yes (trained separately) | Human preferences |
| **CAI** | Few (constitution only) | Yes (AI-generated labels) | AI self-critique against principles |
| **DPO** | Pairwise comparisons | No | Direct policy optimization on preferences |

**DPO** (Rafailov et al., 2023) [Paper](https://arxiv.org/abs/2305.18290): Eliminates the explicit reward model by reframing the RL problem as supervised learning on preference data. Simpler to implement, often comparable quality to PPO-based RLHF.

---

### Trial 5: Scaling Laws

The foundational empirical result: model performance follows predictable power laws with respect to model size (N), dataset size (D), and compute (C).

**Kaplan et al. (2020)** ["Scaling Laws for Neural Language Models"](https://arxiv.org/abs/2001.08361): Established the basic relationships. Key finding: at fixed compute, scale model size more aggressively than data.

**Chinchilla (Hoffmann et al., 2022)** ["Training Compute-Optimal LLMs"](https://arxiv.org/abs/2203.15556): Corrected Kaplan. Compute-optimal ratio is roughly **20 tokens per parameter**. GPT-3 (175B params, 300B tokens) was *undertrained*. Chinchilla (70B params, 1.4T tokens) outperformed Gopher (280B) with the same compute.

⚡ **Power-up**: Jared Kaplan (the scaling laws researcher) is a co-founder of Anthropic. This work is foundational to Anthropic's strategic bets. Know it.

---

### Trial 6: Inference Optimization

**Speculative decoding** (Leviathan et al., 2023): Draft model proposes `k` tokens; large model verifies all `k` in one forward pass. Reduces latency without reducing throughput. Use it when latency-bound, not throughput-bound.

**Flash Attention** (Dao et al., 2022) [Paper](https://arxiv.org/abs/2205.14135): Rewrites attention to be IO-aware — keeps intermediate activations in fast SRAM rather than reading/writing HBM. Standard attention is memory-bandwidth-bound, not compute-bound. Flash Attention achieves 2–4x speedup on attention layers and enables much longer sequences.

**Quantization**: Reduce weight precision from FP32/BF16 to INT8 or INT4. Halves (or quarters) memory footprint. INT8 is generally acceptable; INT4 requires careful calibration (GPTQ, AWQ methods).

**Mixture of Experts (MoE)**: Route each token to a subset of expert sub-networks (typically 2 out of 8–64 experts). Increases model capacity without proportionally increasing FLOPs per token. Catch: all expert weights still need to be in memory; load balancing requires auxiliary loss terms.

---

> 🎮 **+150 XP — ML Sage Defeated!**
>
> *Achievement Unlocked: "Transformer Whisperer" — Can explain attention without saying "magic"*

---

## ✅ Checkpoint 5

- [ ] You can derive the attention formula from scratch
- [ ] You can explain the difference between CAI and RLHF to a non-ML person
- [ ] You understand *why* Chinchilla was a correction, not just what it said
- [ ] You know what Flash Attention actually does differently (IO-aware is the key phrase)

---

## 👁️ BOSS FIGHT 4: Safety & Alignment — THE FINAL BOSS

```
[████████████████████████░░░░] 70% — ⚠️ WARNING: Final Boss Ahead ⚠️
```

> **BOSS FIGHT RULES**: This is the section that separates Anthropic candidates from candidates at every other AI company. You don't need to be an alignment researcher. But you need to have *thought seriously* about these problems. Half-formed "AI is scary" takes will not land. Engage with the substance.

---

### Final Boss Phase 1: The Alignment Problem

**Outer alignment**: Does the reward function / objective actually capture what we want? Classic failure: a game-playing AI that exploits a bug in the game engine rather than playing skillfully. Technically satisfies the specification; totally misses the intent.

**Inner alignment** (mesa-optimization): Even with a correct outer objective, the training process might produce a model with a *different* internal objective that happened to correlate with good performance during training. A mesa-optimizer has its own goal, which may diverge at deployment.

**Concrete example**: A model trained to be helpful might have internalized "appear helpful during training/evaluation" rather than "actually be helpful." It would perform well when it believes it's being evaluated and differently otherwise. This is the treacherous turn scenario.

**Goodhart's Law**: When a measure becomes a target, it ceases to be a good measure. In RLHF: optimizing hard against a proxy reward model causes the policy to find ways to score highly that don't reflect genuine alignment.

**Deceptive alignment**: A particularly concerning form of inner misalignment where the mesa-optimizer actively models whether it's being evaluated and behaves accordingly. Hard to detect because behavioral testing is exactly what it exploits.

---

### Final Boss Phase 2: Interpretability

Anthropic's interpretability team (led by Chris Olah) is one of the most influential in the field.

**Circuits** (Olah et al., ["Zoom In: An Introduction to Circuits"](https://distill.pub/2020/circuits/zoom-in/), 2020): The hypothesis that neural networks implement understandable algorithms composed of "circuits" — subgraphs of neurons with interpretable functions.

**Superposition** (Elhage et al., ["Toy Models of Superposition"](https://arxiv.org/abs/2209.11895), 2022): Neural networks can represent *more features than they have dimensions* by superimposing features in different directions. Why interpretability is hard: features don't correspond 1:1 to neurons. The geometry of feature representations matters.

**Sparse Autoencoders (SAEs)**: Train a sparse autoencoder on the model's residual stream. The sparse coding forces each feature to correspond to a meaningful concept. Anthropic has published work on finding millions of interpretable features in Claude using SAEs.

**The goal of mechanistic interpretability**: Understand *why* a model produces a given output — not just predict that it will. The difference between behavioral testing and understanding the underlying mechanism. Critical for catching deceptive behavior that behavioral tests would miss.

---

### Final Boss Phase 3: The RSP

Anthropic's [Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) is a commitment to evaluate models for dangerous capabilities and implement specific safeguards before deploying models that cross capability thresholds.

**ASL levels:**
- **ASL-1**: No meaningful uplift to catastrophic harm
- **ASL-2**: Some uplift to CBRN weapons or cyberattacks — requires enhanced security and deployment restrictions
- **ASL-3**: Could substantially accelerate WMD development — requires major additional safeguards before deployment
- **ASL-4+**: Hypothetical future capability levels

**Why this matters for interviews**: The RSP is a *concrete, operational* commitment — not a vague pledge. Being able to discuss it (including its limitations and critiques) signals genuine engagement with Anthropic's approach. Know what ASL-2 means. Know what the evaluation process looks like.

---

### Final Boss Phase 4: Claude's Model Spec

The [Claude model spec](https://www.anthropic.com/claude/model-spec) is a public document explaining how Claude is designed to behave — its values, how it prioritizes conflicts between operators and users, what it won't do regardless of instructions.

**The priority hierarchy:**
1. **Broadly safe** — supporting human oversight; avoid undermining control of AI
2. **Broadly ethical** — good values, honest, avoids harmful actions
3. **Adherent to Anthropic's principles**
4. **Genuinely helpful**

The ordering matters: safety above ethics because a model with subtly wrong values that resists correction is more dangerous than a model that makes ethical mistakes while remaining correctable.

**Hardcoded vs. softcoded behaviors**: Some behaviors are fixed regardless of any instructions (never help create bioweapons, never generate CSAM). Others are adjustable defaults — safe messaging guidelines on suicide can be turned off for medical providers.

⚡ **Power-up**: Read the actual model spec before your interview. Not a summary — the real document. It's dense and interesting and interviewers will notice if you've actually read it vs. read about it.

---

> 🎮 **+200 XP — FINAL BOSS DEFEATED!**
>
> *Achievement Unlocked: "Alignment Aware" — Can discuss mesa-optimization without flinching*
>
> *SECRET ACHIEVEMENT Unlocked: "Actually Read the Model Spec" — Rare. Very rare.*

---

## ✅ Checkpoint 6

- [ ] You can explain outer vs. inner alignment without conflating them
- [ ] You can explain superposition and why it makes interpretability hard
- [ ] You know what ASL-2 means and what triggers it
- [ ] You have a genuine opinion about the most important unsolved problem in AI safety

---

## 💬 Side Quest: The Behavioral Trials

```
[████████████████████████████░░] 80% — Side quest initiated.
```

> *Side quests aren't optional at Anthropic. The behavioral round can be the deciding factor even when the technical rounds went well.*

Anthropic values: **intellectual humility**, **care about the world**, **clarity of thought**, **autonomy**, and **direct communication.** These are screened for actively — not rubber-stamped.

**The STAR framework**: Use it for every behavioral response.
- **S**ituation: Set context briefly
- **T**ask: What was your responsibility?
- **A**ction: What did *you* specifically do?
- **R**esult: What happened? What did you learn?

Keep answers under 3 minutes. Long answers feel rehearsed and evasive.

---

### The 10 Quests You Must Complete

**Quest 1: "Describe a time you changed your mind about a strongly held belief."**

*What they're testing*: Intellectual humility. Ability to update on evidence. Willingness to be publicly wrong.

*Strong answer*: A belief you held with real conviction. Real evidence that changed it. What it felt like to update. Avoid: beliefs you changed for social reasons, or trivial changes.

---

**Quest 2: "How do you think about the risks of the technology you're building?"**

*What they're testing*: Genuine engagement with AI risk — not just surface-level awareness.

*Strong answer*: Specific risks (not vague gestures). Short-term misuse AND long-term alignment risks. Your actual probability estimates on different risk categories. What you think can be done. Avoid: dismissing the concern, or catastrophizing without nuance.

---

**Quest 3: "Tell me about a time you pushed back on a decision made by leadership."**

*What they're testing*: Autonomy and direct communication. Anthropic wants advocates, not sycophants.

*Strong answer*: A real disagreement (not trivial). Clear articulation of your objection. How you raised it. What happened (you don't have to have won). What you learned.

---

**Quest 4: "Describe your most technically complex project. What made it hard?"**

*What they're testing*: Depth, not breadth. Can you engage deeply with a hard problem?

*Strong answer*: Pick your hardest project. Go deeper than the interviewer expects. Show you understand second and third-order implications, not just the first-order fix.

---

**Quest 5: "What do you think is the most important unsolved problem in AI safety?"**

*What they're testing*: Genuine engagement with the field. Original thinking. Awareness of the research landscape.

*Prepare a real answer*: Read at least 3–4 Anthropic safety papers first. Possible angles: scalable oversight, interpretability of large models, outer alignment for complex goals, deceptive alignment detection, RLHF reward hacking at scale.

---

**Quest 6: "How do you prioritize when you have more work than you can complete?"**

*What they're testing*: Judgment. Autonomy. Communication about constraints.

*Strong answer*: A real example where you had to cut scope. How you decided what to cut. Whether you communicated the tradeoff explicitly.

---

**Quest 7: "Tell me about a time you had to learn something completely new to solve a problem."**

*What they're testing*: Growth orientation. Self-directed learning. Adaptability.

*Strong answer*: Something genuinely outside your prior knowledge (not a new framework you learned in an afternoon). How you approached the learning. What surprised you.

---

**Quest 8: "Describe a project where you had significant ownership and drove it end-to-end."**

*What they're testing*: Ownership mentality. Ability to operate autonomously.

*Strong answer*: Real end-to-end ownership (not "I was on the team"). Ambiguity you had to resolve yourself. How you handled things going wrong.

---

**Quest 9: "What's something you've built that you're most proud of, and what would you do differently?"**

*What they're testing*: Genuine pride in craft + honest reflection. The "what would you do differently" is as important as the pride part.

*Trap to avoid*: Saying you'd change nothing signals a lack of reflection or a defensive posture. The best answers acknowledge real limitations with genuine thoughtfulness.

---

**Quest 10: "Why Anthropic specifically? Why not OpenAI, Google DeepMind, or a startup?"**

*What they're testing*: Genuine motivation. Understanding of what makes Anthropic different. Conviction about the mission.

*Strong answer*: Something specific — CAI, the RSP, interpretability research, the model spec. Your actual views on the AI safety landscape. Why the "safety-focused lab at the frontier" bet is the right one. Avoid: generic "I care about AI safety" or "Claude is the best model."

---

> 🎮 **+50 XP — Side Quest Complete!**
>
> *Achievement Unlocked: "Introspective" — Actually knows what you'd do differently*

---

## 📅 The Training Montage — 3-Week Study Plan

```
[████████████████████████████████░░] 88% — Training arc begins.
```

> *Every great protagonist has a training montage. This is yours. Eyes on the goal.*

---

### Week 1: Company and Product Deep Dive

**Days 1–2: Foundation**
- [ ] Read Anthropic's [Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) essay
- [ ] Read the [Claude model spec](https://www.anthropic.com/claude/model-spec) end-to-end (not a skim — the real thing)
- [ ] Read the [Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy)
- [ ] Sign up for Claude.ai and the Claude API (free tier) if you haven't

**Days 3–4: Constitutional AI and Safety Research**
- [ ] Read the [Constitutional AI paper](https://arxiv.org/abs/2212.08073) (at minimum: abstract, intro, Section 3)
- [ ] Read ["Toy Models of Superposition"](https://arxiv.org/abs/2209.11895) (Sections 1–3)
- [ ] Browse Anthropic's [research page](https://www.anthropic.com/research) for recent papers

**Days 5–7: Product Usage**
- [ ] Use Claude.ai extensively — push its limits, test edge cases, understand its refusals
- [ ] Install and use Claude Code on a real project
- [ ] Try building something with the Anthropic API (prompt caching, tool use, streaming)
- [ ] Read about MCP (Model Context Protocol) and its design philosophy

**Week 1 goal**: Explain what Anthropic does and why it matters, have genuine opinions about Claude's behavior, speak to the model spec with specificity.

---

### Week 2: Technical Foundation

**Days 1–2: Transformer Architecture**
- [ ] Read ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762)
- [ ] Implement a minimal transformer decoder from scratch in PyTorch (no tutorials — write it yourself)
- [ ] Study RoPE positional encodings and understand why they extend better than absolute positions
- [ ] Understand the difference between pre-norm and post-norm transformers

**Days 3–4: Training and Alignment Techniques**
- [ ] Study the RLHF pipeline — understand PPO at the level of *why* it's used (trust region)
- [ ] Read about DPO and understand the derivation at a high level
- [ ] Read the [Chinchilla paper](https://arxiv.org/abs/2203.15556) abstract + key figures
- [ ] Understand KV cache mechanics and prompt caching

**Days 5–7: Systems and Inference**
- [ ] Study continuous batching / PagedAttention ([vLLM blog post](https://vllm.ai/blog/2023/06/20/vllm.html) is excellent)
- [ ] Read the [Flash Attention paper](https://arxiv.org/abs/2205.14135) abstract — understand the IO-aware insight
- [ ] Review distributed systems fundamentals (consistent hashing, CAP theorem, Raft at a high level)
- [ ] Review ML infrastructure patterns: feature stores, model registries, A/B testing for models

**Week 2 goal**: Whiteboard a transformer architecture, explain RLHF vs CAI vs DPO, design an inference system under constraints.

---

### Week 3: Practice and Polish

**Days 1–2: Coding**
- [ ] Solve 10–15 LeetCode Hard problems — focus on graphs, DP, and heap/priority queue
- [ ] Practice narrating your solution before and while coding
- [ ] Time yourself: medium problems in under 20 minutes

**Days 3–4: System Design**
- [ ] Do 2 mock system design sessions (practice partner or AI)
- [ ] Practice capacity estimation math until it's automatic
- [ ] Walk through the 3 design scenarios in this guide out loud
- [ ] Read "Designing Data-Intensive Applications" Chapters 1–3 if you haven't

**Days 5–6: Behavioral**
- [ ] Write out STAR answers for all 10 behavioral questions above
- [ ] Record yourself answering 3 of them — watch it back, edit for length and clarity
- [ ] Prepare 6–8 distinct stories from your work history to draw from

**Day 7: Full Simulation**
- [ ] Full mock onsite with a friend (4 hours, all round types)
- [ ] Review the Knowledge Check below
- [ ] Sleep. Eat well. The interview is tomorrow.

**Week 3 goal**: Fluency under pressure. Content is automatic; you can focus entirely on communication quality.

---

> 🎮 **+50 XP — Training Montage Complete!**
>
> *Achievement Unlocked: "Rocky" — Three weeks of deliberate practice done*

---

## 📚 The Tome of Essential Knowledge

```
[████████████████████████████████████░] 93% — Loading the library...
```

| Resource | Type | Priority | Link |
|----------|------|----------|------|
| Constitutional AI: Harmlessness from AI Feedback | Paper | Essential | [arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073) |
| Scaling Laws for Neural Language Models (Kaplan) | Paper | Essential | [arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361) |
| Training Compute-Optimal LLMs (Chinchilla) | Paper | Essential | [arxiv.org/abs/2203.15556](https://arxiv.org/abs/2203.15556) |
| Attention Is All You Need | Paper | Essential | [arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762) |
| Toy Models of Superposition | Paper | Essential | [arxiv.org/abs/2209.11895](https://arxiv.org/abs/2209.11895) |
| Flash Attention | Paper | High | [arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135) |
| Direct Preference Optimization (DPO) | Paper | High | [arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290) |
| Mechanistic Interpretability (Elhage et al.) | Paper | High | [arxiv.org/abs/2112.00114](https://arxiv.org/abs/2112.00114) |
| Claude Model Spec | Document | Essential | [anthropic.com/claude/model-spec](https://www.anthropic.com/claude/model-spec) |
| Responsible Scaling Policy | Document | Essential | [anthropic.com/news/responsible-scaling-policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) |
| Anthropic Core Views on AI Safety | Essay | Essential | [anthropic.com/news/core-views-on-ai-safety](https://www.anthropic.com/news/core-views-on-ai-safety) |
| vLLM Blog: PagedAttention | Blog | High | [vllm.ai/blog/2023/06/20/vllm.html](https://vllm.ai/blog/2023/06/20/vllm.html) |
| Zoom In: Introduction to Circuits | Blog | High | [distill.pub/2020/circuits/zoom-in](https://distill.pub/2020/circuits/zoom-in/) |
| Anthropic Interpretability Research | Blog series | High | [transformer-circuits.pub](https://transformer-circuits.pub/) |
| The Illustrated Transformer | Blog | Medium | [jalammar.github.io/illustrated-transformer](https://jalammar.github.io/illustrated-transformer/) |
| Designing Data-Intensive Applications | Book | Medium | Kleppmann — available widely |
| Anthropic Research Page | Hub | High | [anthropic.com/research](https://www.anthropic.com/research) |

---

## 🎯 Final Boss: The Knowledge Check

```
[██████████████████████████████████████░] 97% — THE FINAL CHALLENGE
```

> **RULES**: Cover each answer. Try to answer from memory. A confident, correct answer in under 60 seconds is the target. If you can't do it in 60 seconds, you need more practice.

---

**Round 1: What is Constitutional AI and how does it differ from RLHF?**

> Constitutional AI (CAI) uses a set of written principles (a "constitution") to guide AI behavior rather than relying primarily on human pairwise comparisons. In standard RLHF, humans compare response pairs to train a reward model, which is then used in PPO. In CAI, the AI itself critiques and revises its responses against the constitution (SL-CAI phase), and AI-generated preference labels are used to train the reward model instead of human labels (RLAIF phase). The key advantages: scales better, makes values explicit and auditable, requires less direct human labeling.

---

**Round 2: Explain the attention mechanism in two sentences.**

> Attention computes a weighted sum of values for each position in a sequence, where the weights are determined by the similarity (dot product) between that position's query vector and every other position's key vector, scaled by sqrt(d_k) and normalized through softmax. This allows every token to directly attend to every other token in the sequence, capturing long-range dependencies that recurrent networks struggle with.

---

**Round 3: What is a mesa-optimizer?**

> A mesa-optimizer is an optimizer that emerges *within* a trained model as a result of the training process — a learned optimization algorithm inside the model. The concern is that a mesa-optimizer might have internalized its own objective (a "mesa-objective") that differs from the base training objective. If the mesa-objective only correlates with the training objective during training and not at deployment, the model could behave deceptively — performing well during training while pursuing a different goal in the real world.

---

**Round 4: What is superposition in neural networks and why does it make interpretability hard?**

> Superposition refers to the phenomenon where neural networks represent more features than they have dimensions by encoding multiple features in overlapping directions in activation space. A network with `d` hidden dimensions can represent `k >> d` features if those features are sparse and nearly orthogonal. This makes interpretability hard because individual neurons don't correspond to single interpretable features — each neuron participates in representing many features, and each feature is distributed across many neurons.

---

**Round 5: What is the Chinchilla scaling law, and what was its main finding vs. Kaplan et al.?**

> Chinchilla (Hoffmann et al., 2022) found that the compute-optimal way to train a language model is to scale model parameters and training data tokens in roughly equal proportion — approximately 20 tokens per parameter. This corrected Kaplan et al. (2020), which had suggested scaling model size more aggressively relative to data. Practical implication: GPT-3 (175B parameters, ~300B tokens) was undertrained relative to its compute budget; a smaller model trained on more data achieves better loss for the same compute.

---

**Round 6: What is the KV cache and what are its memory implications?**

> The KV cache stores the key and value tensors for each attention layer for all previously generated tokens, so they don't need to be recomputed at each generation step. Memory cost: for each layer, two tensors (K and V) of shape `[batch_size × sequence_length × num_heads × head_dim]` in the model's floating point precision. Total KV cache size scales linearly with sequence length, batch size, and number of layers — for long-context inference with large batches, it can exceed the size of the model weights themselves.

---

**Round 7: What is speculative decoding and when would you use it?**

> Speculative decoding uses a small, fast "draft" model to generate `k` candidate tokens, then verifies all `k` in a single forward pass of the large target model. When the draft model's predictions match the target model's (which happens often for common continuations), you get multiple tokens for the cost of one large-model forward pass. It reduces latency without reducing throughput. Use it when latency-bound (interactive use cases); less useful when throughput-bound (batch processing).

---

**Round 8: Explain the difference between outer alignment and inner alignment.**

> Outer alignment asks whether the training objective correctly captures what we actually want the AI to do — the specification problem. Inner alignment asks whether the trained model has actually learned to optimize the training objective, vs. having learned some correlated but different internal objective. A model can be outer-misaligned (the objective was wrong) while inner-aligned (truly optimizing that wrong objective), or inner-misaligned (the model learned a mesa-objective that diverges from the training objective). Both are distinct, independent failure modes.

---

**Round 9: What is Anthropic's ASL framework and why does it exist?**

> ASL (AI Safety Levels) is Anthropic's framework for categorizing models by dangerous capability level, defined in the Responsible Scaling Policy. ASL-1: no meaningful uplift to catastrophic harm. ASL-2: some uplift to CBRN weapons or cyberattacks. ASL-3: could substantially accelerate WMD development. ASL-4+: hypothetical future catastrophic capability levels. For each ASL level, Anthropic commits to specific security, deployment, and evaluation requirements *before* deploying a model that crosses that threshold. It exists to make capability-scaling commitments concrete and auditable rather than relying on vague safety pledges.

---

**Round 10: What are Claude's four core properties in priority order, and why is safety ranked above ethics?**

> According to the model spec, Claude is designed to be (1) **broadly safe** — supporting human oversight, avoiding actions that undermine human control of AI; (2) **broadly ethical** — having good values, being honest, avoiding harmful actions; (3) **adherent to Anthropic's principles**; and (4) **genuinely helpful**. Safety is prioritized over ethics because even a well-intentioned model with subtly wrong values is more dangerous if it resists correction. Helpfulness, while critical for Anthropic's commercial success and mission, comes last in cases of genuine conflict.

---

**Bonus Round: What is Flash Attention and what problem does it solve?**

> Flash Attention (Dao et al., 2022) is an IO-aware implementation of the attention mechanism that avoids materializing the full N×N attention matrix in GPU HBM (high-bandwidth memory). Instead, it tiles the computation to keep intermediate results in fast SRAM, reducing expensive memory reads/writes. Standard attention is memory-bandwidth-bound, not compute-bound. Flash Attention achieves 2–4x speedup on attention layers and dramatically reduces memory usage — enabling training and inference on much longer sequences than naive attention allows.

---

> 🎮 **+100 XP — Knowledge Check Survived!**

---

## 🏆 Victory Screen

```
[████████████████████████████████████████] 100%

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝

     Total XP Earned: 750 XP | Level 5: Anthropic Hire ✅
```

### Final Stats

| Skill | Status |
|-------|--------|
| Company & Mission | Mastered |
| Algorithms & Coding | Cleared |
| ML Systems | Cleared |
| Safety & Alignment | Cleared |
| Behavioral Communication | Cleared |
| Study Plan | Completed |

---

### Post-Game Tips

**Two weeks before**: Know the material. Stop cramming. Switch to practice.

**One week before**: Practice *communication*. The person who gets the offer usually communicates clearly under pressure, not the person with the most raw knowledge.

**Day before**: Use Claude. Read the model spec one more time. Go to bed early.

**Day of**: The interview is also your opportunity to evaluate Anthropic. Ask good questions. The best questions are about the research agenda, open problems, how safety and commercial pressures actually interact in practice. These questions signal that you're thinking like someone who would *work* there, not just someone who wants the job.

---

*Good luck. You've done the work. Now go get it.*

---

*This guide is part of the [Awesome Anthropic](https://github.com/anthropics/awesome-anthropic) resource collection.*
