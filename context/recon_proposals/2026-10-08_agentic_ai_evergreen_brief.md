# Evergreen Brief: agentic_ai — 2026-10-08
**Archetype:** evergreen
**Vertical:** agentic_ai
**Persona:** ai_architect
**Decision the reader is facing:** Where an agent's durable state should live — the prompt window itself (L1 scratchpad / L2 compacted summary), a retrieved vector store (L3), or a relational knowledge store (L4) — and what each tier boundary costs in tokens, latency and verifiability before a long-horizon agent is put in front of paying users.
**Durability:** The tier boundary is a structural property of the runtime, not a model-version artifact. Context rot is a measured property of long inputs (Chroma's report evaluated 18 LLMs, as of its 2025 context-rot writeup), cross-session recall collapse is measured (LongMemEval, 30% accuracy drop; v2 as of 2025-03-04), and the OS-inspired hierarchy of a fast prompt register in front of slower paged stores (MemGPT, as of 2023-10-12; Letta's file-backed agent at 74.0% LoCoMo as of 2025-08-12) still describes how production agents actually page state. Every time-bound figure is dated and re-checkable; the decision rule does not expire.
**De-dup:** 2026-09-24_maskills-multi-agent-skills-optimization argues the memory-vs-skills question (delete the validation gate and LoCoMo collapses 17.2 → 6.6); 2026-10-05_multi-agent-coordination-topology-cost argues coordination topology cost (fan-out vs. handoff vs. ensemble). Neither decides *where durable state belongs across tiers*. This brief settles the L1–L4 placement and its token/latency/verifiability trade-off, a distinct evergreen beat for this vertical.
**Thesis:** The context window is a working register, not storage: measured context degradation and a 30% cross-session recall drop mean the memory *tier* — not the model and not the memory tool — decides whether a long-horizon agent holds its task, and each tier trades tokens, latency and verifiability differently.

**Lead:** From the vertical's own `primary_angles` ("memory tiering topology L1-L4", "distributed microservices architecture") and the persona's `wants` in `context/personas.json` (`ai_architect`: "memory tiering topologies, MCP contracts, state recovery patterns, microservice RPC boundaries" — tiering is the declared number-one beat), reinforced by `context/growth_os/founder-voice.md` §3 ("Memory Tiering Topology": the explicit 4-tier L1–L4 hierarchy) and the field friction in `context/growth_os/customer-truth.md` (agentic_ai anecdote 3: a flat 12,000-token history degraded reasoning quality until a 4-tier hierarchy cut token overhead by 68%). Grounded against fetchable *measured* primaries, not asserted: the prior evergreen brief (2026-10-05) dropped this angle because its durable anchors were arXiv-only (a single host) — resolved here with measured evidence across four hosts. GSC (`scripts/gsc_analyzer.py --vertical agentic_ai`) is a bonus signal only; on a young site it never vetoes a good topic.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Chroma — "Context Rot: How Increasing Input Tokens Impacts LLM Performance" | https://research.trychroma.com/context-rot | 2026-10-08 | 18 LLMs — the report evaluates 18 models and finds performance varies significantly as input length changes even on simple tasks, so long context is not uniform capacity | measured |
| 2 | Wu et al. — "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory", arXiv:2410.10813 (v2 2025-03-04) | https://arxiv.org/abs/2410.10813 | 2026-10-08 | 30% — commercial chat assistants and long-context LLMs show a 30% accuracy drop on memorizing information across sustained interactions (500 curated questions) | measured |
| 3 | Chhikara et al. — "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory", arXiv:2504.19413 (2025-04-28) | https://arxiv.org/abs/2504.19413 | 2026-10-08 | 26% — an extracted-and-retrieved memory layer reports a 26% relative improvement in the LLM-as-judge metric over a full-context baseline, at 91% lower p95 latency | vendor claim |
| 4 | Letta — "Benchmarking AI Agent Memory: Is a Filesystem All You Need?" (2025-08-12) | https://www.letta.com/blog/benchmarking-ai-agent-memory | 2026-10-08 | 74.0% — a file-backed agent on gpt-4o-mini reached 74.0% on LoCoMo, above Mem0's reported 68.5%, i.e. the retrieval mechanism mattered less than how the agent managed context | measured |
| 5 | Anthropic Engineering — "Effective context engineering for AI agents" (2025-09-29) | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 2026-10-08 | 1,000-2,000 tokens — a subagent explores for tens of thousands of tokens but should return only a condensed 1,000-2,000-token summary; context is a finite resource with diminishing returns ("context rot") | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Memory tiering L1–L4: where agent state belongs (prompt vs. summary vs. vector vs. relational) | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| MCP protocol fabric: budgeting the agent's tool surface | 8 | 8 | 7 | 8 | 7.8 | dropped — the nearest corpus artifact is the published tool-count piece (2026-10-07_agent-tool-count-ceiling, multi_agent_enterprise_fabric), and the strongest tool-count anchors are secondary blogs, not fetchable primaries |
| Subagent cost optimization (the token multiplier) | 8 | 8 | 7 | 7 | 7.6 | dropped — a subset of the already-published 2026-10-05 topology-cost evergreen; no independent second measured anchor |
| Deterministic RPC boundaries & idempotent agent tool calls | 8 | 9 | 5 | 9 | 7.7 | dropped — durable and high-value, but the available sources are framework docs, not measured primaries with fetchable figures (the same reason it lost on 2026-10-05) |

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=5 hosts=4 decision="sha1:759d86e511" dedup="matched a prior artifact: 2026-09-24_maskills-multi-agent-sk" window_days=180 checked_at=2026-10-08T17:32:51+00:00 -->
<!-- evergreen-gate:end -->
