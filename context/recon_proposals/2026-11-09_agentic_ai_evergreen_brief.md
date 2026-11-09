# Evergreen Brief: agentic_ai — 2026-11-09
**Archetype:** evergreen
**Vertical:** agentic_ai
**Persona:** ai_architect
**Decision the reader is facing:** What a long-horizon agent runtime must write down after every turn so a crashed run resumes correctly — the chat history, a filesystem snapshot, or only the OS-visible state the turn actually changed — and at what co-location density a per-turn full checkpoint stops paying for itself.
**Durability:** The hierarchy is structural, not a vendor preference: a chat log records what the agent said, not what its tools did to the environment, and the cost of writing sandbox state scales with how many sandboxes share a host. As of the 2026 measurements used here (Crab, 30 Apr 2026; DeltaBox, 21 May 2026; AgentRewind, 14 Aug 2026) the 8–13% chat-only recovery rate, the 87% of turns that change no durable state, and the 3.06–3.78× dense-colocation checkpoint tax are properties of Linux containers, microVMs and shared storage bandwidth, not of one model generation; Temporal's 51,200-event / 50 MB journal ceiling as of its 2026 documentation is the same class of bound. Nothing in the article depends on a price or a model score, so it stays true while agents are still executed in sandboxes and durable engines still replay a journal.
**De-dup:** `2026-10-07_durable-execution-not-a-transaction` (multi_agent_enterprise_fabric) is the nearest artifact by mechanism and is refused only after being read: it argues that a durable journal records that a step ran but not what state it touched, and asks for declared effect semantics at the MCP tool contract. This piece measures what a resume actually restores (8–13% chat-only, 28–42% filesystem, 100% with process state) and what the checkpoint write costs at 64–96 sandboxes per host, which decides the runtime's snapshot substrate and cadence rather than the contract's metadata. Within this vertical, `2026-10-29_your-sandbox-boot-tax-110x-then-nothing` prices provisioning a sandbox once per run, not persisting its state per turn, and `2026-11-05_agentic_ai_evergreen_brief.md` (A2A task state) asks where a hop's state lives between agents, not how a single run survives a process death.
**Thesis:** A crashed agent run resumes correctly only if the runtime captured the state its tools actually touched — chat history alone restores 8–13% of shell-heavy tasks and a filesystem snapshot 28–42%, while checkpointing everything every turn costs up to 3.78× at 96 sandboxes per host — so checkpointing is a classification problem (up to 87% of turns change nothing durable; a diff-based write of the turns that do takes 14 ms) and the durable journal has to stay a pointer log under its 51,200-event / 50 MB ceiling rather than become the state store.

**Lead:** The persona's own `wants` — "state recovery patterns" for `ai_architect` in `context/personas.json` — plus the vertical's `primary_angles` ("distributed microservices architecture", "deterministic RPC boundaries") and the checkpointing pillar in `context/growth_os/founder-voice.md` §3. Material: three 2026 systems measurements of agent-sandbox checkpoint/restore on SWE-bench and Terminal-Bench, plus the documented event-history ceiling of the durable-execution engine most teams reach for.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Wu et al., HKUST — "Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes" (arXiv:2604.28138v1) | https://arxiv.org/html/2604.28138v1 | 2026-11-09 | 3.78x — every-turn full checkpointing slows Terminal-Bench execution 3.78x at 96 co-located sandboxes per host (3.06x at 64) because host storage bandwidth saturates | measured |
| 2 | Crab (arXiv:2604.28138v1) — checkpoint sparsity | https://arxiv.org/html/2604.28138v1 | 2026-11-09 | 87% — up to 87% of agent turns change neither process nor filesystem state and can skip the checkpoint entirely | measured |
| 3 | Crab (arXiv:2604.28138v1) — recovery correctness by state captured | https://arxiv.org/html/2604.28138v1 | 2026-11-09 | 28–42% — chat-history-only recovery restores 8–13% of Terminal-Bench tasks and a filesystem snapshot 28–42%, against 100% when process state is checkpointed too | measured |
| 4 | Crab (arXiv:2604.28138v1) — overhead of overlapping the write | https://arxiv.org/html/2604.28138v1 | 2026-11-09 | 0.44% — overlapping checkpoint work with the model wait window kept p95 exposed checkpoint delay at 0.44% of task time at 64 sandboxes per host | measured |
| 5 | Temporal — "Workflow Execution limits" (platform documentation) | https://docs.temporal.io/workflow-execution/limits | 2026-11-09 | 51,200 — a workflow execution's event history is limited to 51,200 events or 50 MB, with warnings from 10,240 events or 10 MB | vendor claim |
| 6 | Dong et al., SJTU — "DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback" (arXiv:2605.22781v1) | https://arxiv.org/html/2605.22781v1 | 2026-11-09 | 14 ms — a diff-based checkpoint completes in 14 ms and rollback in 5 ms, against hundreds of milliseconds to seconds for full duplication | measured |
| 7 | Zhuang et al. — "AgentRewind: Recoverable Execution for Long-Horizon LLM Agents" (arXiv:2608.14380v1), MettleBench baselines | https://arxiv.org/html/2608.14380v1 | 2026-11-09 | 337.2 — long-horizon baseline traces average up to 337.2 recorded LLM and tool events per task, the horizon a checkpoint has to survive | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Checkpoint what the tools touched: state selection and cadence for a crashed long-horizon run | 9 | 9 | 9 | 9 | 9.0 | **winner** |
| How many standing rules one agent can carry (the instruction-density ceiling) | 8 | 9 | 8 | 7 | 8.1 | dropped — same context-budget mechanism already argued in `published/2026-10-07_agent-tool-count-ceiling.md` (multi_agent_enterprise_fabric) |
| Re-embedding a live vector tier: migration cost and cutover | 8 | 7 | 6 | 7 | 7.1 | dropped — no fetchable measured re-embed cost or index-drift harm; every candidate anchor was vendor marketing |
| Per-server MCP topology: one process per tool vs one tool fabric | 7 | 8 | 7 | 7 | 7.2 | dropped — retread of `published/2026-10-26_your-tool-boundary-costs-3-engineers.md` |

## Notes (verbatim anchors for the drafting pass)
- Crab abstract: "over 75% of agent turns produce no recovery-relevant state, so most checkpoints are unnecessary"; result sentence: "raises recovery correctness from 8% (chat-only) to 100%, cuts checkpoint traffic by up to 87%, and stays within 1.9% of fault-free execution time".
- Crab evaluation: "Chat+FS reaches 100% on SWE-bench, but only 28% and 42% on Terminal-Bench"; "restart … increasing completion time by up to 1.52× on Terminal-Bench and 1.67× on SWE-bench"; "median turn duration of 3.34 s and 117 expected turns per task", "17 requests/s and a p90 of 26 requests/s" at 100 sandboxes per host.
- DeltaBox abstract: "completes checkpoint and rollback in millisecond-level latency (14 ms and 5 ms, respectively)"; motivation sentence: "Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R".
- Temporal limits page: "the Workflow Execution's Event History is limited to 51,200 Events or 50 MB and will warn you after 10,240 Events or 10 MB".
- The writing trap to avoid: do not present the 3.78× figure as "full checkpointing is always wrong" — the same paper shows FullCkpt performs well on SWE-bench, where turns only modify files. The rule is density- and workload-dependent, and the article has to say so.

## Gate result

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=4 hosts=2 decision="sha1:d3bd46386e" dedup="matched a prior artifact: 2026-10-07_durable-execution-not-a" window_days=180 checked_at=2026-11-09T17:34:59+00:00 -->
<!-- evergreen-gate:end -->
