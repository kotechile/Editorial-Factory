# Evergreen Brief: agentic_ai — 2026-10-05
**Archetype:** evergreen
**Vertical:** agentic_ai
**Persona:** ai_architect
**Decision the reader is facing:** Which multi-agent coordination topology to wire into a production agent runtime — parallel fan-out (orchestrator + subagents), sequential handoff, or a deliberative ensemble/debate — and what each mode actually costs in tokens and added failure modes before committing engineering time.
**Durability:** Coordination topology is a structural choice, not a model-version artifact: the three modes (parallel fan-out, sequential handoff, deliberative ensemble/debate) still describe how production runtimes are wired, and every load-bearing figure is a dated snapshot a reader can re-check — the 90.2% capability gain and ~15× token multiplier are Anthropic's own published measurements (as of its 2025 multi-agent research write-up), the 14 failure modes are MAST's taxonomy (arXiv 2503.13657, v1 2025-03-17), and the 65.1% ensemble score is MoA (arXiv 2406.04692, 2024-06-07). The decision framework does not expire; only the multipliers drift, and each is dated.
**De-dup:** 2026-10-01_planner-as-router-plan-time-routing (routing the model inside one plan) and 2026-09-24_maskills-multi-agent-skills-optimization (what agents learn — peer/central/tiered teams appear only as a side finding) are this vertical's nearest prior artifacts; neither is a topology-selection framework with a cost curve. This brief decides *which coordination mode to wire and what it costs*, a distinct evergreen beat, and no evergreen brief exists for agentic_ai yet.
**Thesis:** Multi-agent coordination is a cost-and-verifiability decision, not a capability flex: parallel fan-out buys breadth at roughly 15× the tokens of a single chat, a deliberative ensemble buys factual reliability at the cost of latency, and sequential handoffs keep the bill flat — so the topology should be chosen from the decision the task actually needs, and the dominant risk is system-design failure (14 catalogued modes), not a weak model.

**Lead:** From the vertical's own `primary_angles` ("multi-agent coordination modes", "subagent cost optimization") and the persona's `wants` in `context/personas.json` (`ai_architect`: "memory tiering topologies, MCP contracts, state recovery patterns, microservice RPC boundaries" — the coordination-mode beat is the vertical's declared angle), reinforced by `context/growth_os/founder-voice.md` §3 ("Multi-Agent Coordination Modes": don't default to open-ended agent chat rooms — compare competitive debate, sequential handoffs, and centralized blackboard). The founder's three-mode taxonomy had no fetchable *measured* anchor in the corpus, so it was grounded against primary sources found by search rather than asserted. GSC (`scripts/gsc_analyzer.py --vertical agentic_ai`) returned 0 opportunities — bonus signal only on a young site, never a veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Anthropic Engineering — "How we built our multi-agent research system" (2025 multi-agent research write-up) | https://www.anthropic.com/engineering/multi-agent-research-system | 2026-10-05 | A multi-agent system (Opus 4 lead + Sonnet 4 subagents) outperformed single-agent Claude Opus 4 by 90.2% on an internal research eval — the capability upside of parallel fan-out | measured |
| 2 | Anthropic Engineering — "How we built our multi-agent research system" (same write-up) | https://www.anthropic.com/engineering/multi-agent-research-system | 2026-10-05 | Multi-agent systems use about 15× more tokens than chats (and agents about 4× more than chat) — the cost side of fan-out, and why it needs high-value tasks | measured |
| 3 | Cemri et al. — "Why Do Multi-Agent LLM Systems Fail?" (MAST), arXiv:2503.13657, v1 2025-03-17 | https://arxiv.org/abs/2503.13657 | 2026-10-05 | Analysis of 150 traces identifies 14 unique failure modes clustered into 3 categories (system design, inter-agent misalignment, task verification) — the failure risk is design, not model capability | measured |
| 4 | Wang et al. — "Mixture-of-Agents Enhances Large Language Model Capabilities", arXiv:2406.04692, 2024-06-07 | https://arxiv.org/abs/2406.04692 | 2026-10-05 | Layered ensemble aggregation (a deliberative mode) reached 65.1% on AlpacaEval 2.0 vs 57.5% for GPT-4 Omni — what a debate/ensemble topology buys on verifiable outputs | measured |
| 5 | Microsoft Research — AutoGen multi-agent conversation framework (AutoGen 0.4 release) | https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/ | 2026-10-05 | A coordinated multi-agent conversation framework reached top results on the GAIA benchmark by about 8 points — a sequential/conversational handoff topology that ships today | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Multi-agent coordination modes: picking the topology that pays (fan-out vs sequential handoff vs deliberative ensemble) | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Memory tiering topology L1–L4 (which tier holds what) | 8 | 9 | 6 | 7 | 7.6 | dropped — nearest prior article (2026-09-24_maskills…) already argues the memory-vs-skill question, and the durable anchors are arxiv-only (single host), so it de-dups ambiguously and under-spreads evidence |
| Subagent cost ceilings: budgeting the token multiplier | 8 | 9 | 7 | 6 | 7.7 | dropped — a subset of the winner's cost leg; no independent second host beyond the same Anthropic measurement |
| Deterministic RPC boundaries & idempotency for agent tool calls | 8 | 8 | 5 | 9 | 7.4 | dropped — strong and durable, but the available sources are framework docs, not measured primaries with fetchable figures |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=4 hosts=3 decision="sha1:1d074393fb" dedup="matched a prior artifact: 2026-10-01_planner-as-router-plan-" window_days=180 checked_at=2026-10-05T17:33:23+00:00 -->
<!-- evergreen-gate:end -->
