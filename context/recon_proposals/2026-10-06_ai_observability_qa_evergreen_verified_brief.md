# Verified Brief: ai_observability_qa — 2026-10-06 (EVERGREEN track)

**Archetype:** evergreen
**Vertical:** ai_observability_qa
**Persona:** evals_infra_eng
**Brief:** context/recon_proposals/2026-10-06_ai_observability_qa_evergreen_brief.md (evergreen gate PASS — 4 sources, 3 hosts)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | A — τ-bench reliability | The best function-calling agents (gpt-4o class) solve fewer than half of τ-bench tasks in a single run | VERIFIED | https://arxiv.org/abs/2406.12045 | "Our experiments show that even state-of-the-art function calling agents (like gpt-4o) succeed on <50% of the tasks" |
| 2 | A — τ-bench reliability | On the repeat-trial metric, the same agents fall below 25% in the retail domain (pass^8) | VERIFIED | https://arxiv.org/abs/2406.12045 | "and are quite inconsistent (pass^8 <25% in retail)" |
| 3 | A — τ-bench metric | pass^k is proposed precisely to measure reliability of an agent's behaviour across multiple trials, not one run | VERIFIED | https://arxiv.org/abs/2406.12045 | "We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials." |
| 4 | B — MAST failure taxonomy | The taxonomy was built from 150 analysed traces with high annotator agreement (kappa = 0.88) | VERIFIED | https://arxiv.org/abs/2503.13657 | "We develop MAST through rigorous analysis of 150 traces, guided closely by expert human annotators and validated by high inter-annotator agreement (kappa = 0.88)." |
| 5 | B — MAST failure taxonomy | The analysis identifies 14 unique failure modes in 3 categories: system design, inter-agent misalignment, and task verification — i.e. failures are design/verification, not model capability | VERIFIED | https://arxiv.org/abs/2503.13657 | "This process identifies 14 unique modes, clustered into 3 categories: (i) system design issues, (ii) inter-agent misalignment, and (iii) task verification." |
| 6 | C — production adoption | About 51% of surveyed respondents already use agents in production; tracing/observability top the must-have controls | VERIFIED | https://www.langchain.com/stateofaiagents | "About 51% of respondents are using agents in production today." / "Tracing and observability tools top the list of must-have controls, helping developers get visibility into agent behaviors and performance." |
| 7 | D — retry attribution in traces | The standard itself frames an unexplained slow agent as three candidate causes — the model, a slow tool call, or a retry loop — and the fix is per-call GenAI spans | VERIFIED | https://opentelemetry.io/blog/2026/genai-observability | "Your AI agent just took 45 seconds to answer a simple question. Was it the model? A slow tool call? A retry loop?" |
| 8 | D — retry attribution in traces | The GenAI semantic conventions standardise the per-call attributes that expose model, token counts and tool invocations | VERIFIED | https://opentelemetry.io/blog/2026/genai-observability | "The span details show GenAI semantic convention attributes: gen_ai.request.model — the model used (for example, gpt-4o). gen_ai.usage.input_tokens and gen_ai.usage.output_tokens — token counts for each LLM call. gen_ai.response.finish_reasons — why the model…" |

**Gate rules:** 8/8 VERIFIED, 0 FLAGGED, 0 REMOVED. Single-signal evergreen topic (no synthesis, no dual-anchor requirement). Only VERIFIED figures survive into drafting: **<50% pass@1**, **25% pass^8 (retail)**, **150 traces / 14 modes / 3 categories / kappa 0.88**, **51% in production**, **45 seconds**.
