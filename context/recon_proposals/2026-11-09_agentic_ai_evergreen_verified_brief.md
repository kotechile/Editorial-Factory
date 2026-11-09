# Verified Brief: agentic_ai — 2026-11-09 (EVERGREEN)

Companion to `2026-11-09_agentic_ai_evergreen_brief.md` (marker rows=7, fetched=7, sources=4, hosts=2,
checked_at 2026-11-09T17:34:59+00:00). The news track's `2026-11-09_agentic_ai_verified_brief.md` is a
different artifact and is left untouched (filename rule, `skills/evergreen_topics.md` §4).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | State-selection | Chat-history-only recovery restores 8–13% of Terminal-Bench tasks; chat+filesystem 28–42%; capturing process state reaches 100% | VERIFIED | https://arxiv.org/html/2604.28138v1 | "Crab achieves 100% recovery correctness, compared with 8–13% for chat-only and 28–42% for chat+filesystem baselines on Terminal-Bench." |
| 2 | Checkpoint cost at density | Every-turn full checkpointing slows execution up to 3.78x at 96 co-located sandboxes per host (3.06x at 64) from host storage contention | VERIFIED | https://arxiv.org/html/2604.28138v1 | "every-turn full checkpointing adds up to 3.78 × on Terminal-Bench at 96-sandbox density due to host I/O contention"; "FullCkpt for Claude-code slows execution by 3.06 × and 3.78 ×" |
| 3 | Sparsity | Up to 87% of agent turns change neither process nor filesystem state and can skip the checkpoint | VERIFIED | https://arxiv.org/html/2604.28138v1 | "Crab classifies up to 87% of turns as requiring no checkpoint, eliminating corresponding C/R works entirely."; abstract: "over 75% of agent turns produce no recovery-relevant state" |
| 4 | Overlap cost | Overlapping checkpoint work with the model wait kept p95 exposed checkpoint delay at 0.44% of task time at 64 sandboxes per host | VERIFIED | https://arxiv.org/html/2604.28138v1 | "asynchronous overlap keeps the p95 exposed checkpoint delay to 0.44% of task time at a density of 64 co-located sandboxes" |
| 5 | Journal bound | A workflow execution's event history is limited to 51,200 events or 50 MB, warning at 10,240 events or 10 MB | VERIFIED | https://docs.temporal.io/workflow-execution/limits | "the Workflow Execution's Event History is limited to 51,200 Events or 50 MB and will warn you after 10,240 Events or 10 MB." |
| 6 | Cheap write | Diff-based checkpoint completes in 14 ms and rollback in 5 ms, against hundreds of milliseconds to seconds for full duplication | VERIFIED | https://arxiv.org/html/2605.22781v1 | "DeltaBox completes checkpoint and rollback in millisecond-level latency (14 ms and 5 ms, respectively)"; "Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R" |
| 7 | Long horizon | Long-horizon baseline traces average up to 337.2 recorded LLM and tool events per task; baseline success 28.0%–73.2% across seven models on MettleBench | VERIFIED | https://arxiv.org/html/2608.14380v1 | Table 1: "GPT-5.4 62.2 … Qwen3.7-Max 73.2 … Kimi K2.5 28.0 … DeepSeek-V4-Flash 37.8 … GLM-5.1 59.8"; "task success rates range from 28.0% to 73.2% and no model saturates MettleBench" |

## Provenance rulings (what the drafter may and may not say)

1. **3.78x is density- and workload-specific.** The same paper reports FullCkpt performing well on SWE-bench,
   where turns almost exclusively modify files. The article must not generalise the figure to all workloads.
2. **8–13% is the Terminal-Bench (shell-heavy) number.** On SWE-bench the chat+filesystem baseline reaches 100%.
   The article carries that split explicitly.
3. **Affiliation:** Crab — Hong Kong University of Science and Technology (all authors). DeltaBox — Shanghai Jiao
   Tong University (with Huawei). AgentRewind — University of Chinese Academy of Sciences / IIIS Tsinghua /
   Zhongguancun Academy / Institute of Automation, CAS; the draft line was corrected from "from Tsinghua" to
   "from a team at Tsinghua and the Chinese Academy of Sciences" for that reason.
4. **Temporal's numbers are a documented platform limit, not a measured benchmark** — labelled vendor claim in
   the brief and written as documentation in the article, never as an experiment.
5. **eBPF is expanded in place** ("a Linux tracing layer ... extended Berkeley Packet Filter") and **p95 glossed**
   ("the point where the slowest 5% of turns begin") — `check_accessibility` hard-fails unglossed terms.
6. **No derived arithmetic in the article** beyond the table's plain comparison; no payback, percentage or ratio
   was computed by the rewrite, so the recompute-after-Loop-3 rule had nothing to catch.
7. **REMOVED:** none. **FLAGGED:** none. Seven claims, all VERIFIED against the fetched page.
