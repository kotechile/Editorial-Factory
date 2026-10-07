# Evergreen Brief: ai_observability_qa — 2026-10-06
**Archetype:** evergreen
**Vertical:** ai_observability_qa
**Persona:** evals_infra_eng
**Decision the reader is facing:** Whether an agent is reliable enough to ship — which number to gate the release on (a single-run pass@1 that looks green, or a repeat-trial pass^k that exposes flakiness), and what to instrument so a silently-retrying tool call is caught before release rather than after it has fabricated a "success."
**Durability:** The structural finding does not expire: a single-run score overstates reliability, and the failure modes that dominate are design and verification (not model strength), so the gate belongs on repeat-trial behaviour and the trace, not on one lucky run. Every load-bearing figure is a dated snapshot a reader can re-check — τ-bench's repeat-trial collapse is as of its 2024 paper (arXiv 2406.12045), MAST's failure taxonomy is as of arXiv 2503.13657 (2025), the production-adoption share is as of the LangChain State of AI Agents survey, and the OpenTelemetry GenAI conventions are as of the standard's 2026 documentation. The metric and instrumentation do not expire; only the specific scores drift, and each is dated.
**De-dup:** 2026-10-06_buying-ai-quality-when-the-score-belongs-to-the-judge is this vertical's nearest prior artifact (today's news run). It argues the LLM-judge's score is a property of the judge and not of the system, and it grounds that on BAER/JEV/judge-reliability papers and the Dynatrace–Arize acquisition; it shares none of this brief's sources and reaches a different beat. This brief is about release gating: measure repeat-trial pass^k instead of a single run, and instrument the per-call retry count — a durable "how do I know it's reliable enough to ship" topic, not a judge-validity argument. No evergreen brief for ai_observability_qa exists yet.
**Thesis:** Agent reliability is not a single-run score: gate the release on the repeat-trial pass^k rate and instrument the per-call retry count, because a silently-retrying tool call turns a deterministic error into a fabricated "success" — and the measured failure modes that tank repeatability are design and verification, not model capability.

**Lead:** From the vertical's own `primary_angles` ("deterministic vs probabilistic QA", "trace-level vertical flamegraphs", "redundant loop detection") and the persona's `wants` in `context/personas.json` (`evals_infra_eng`: "deterministic vs probabilistic gates, trace flamegraphs, judge calibration, schema regression tests"), reinforced by `context/growth_os/founder-voice.md` §3 (`ai_observability_qa`: "You cannot eval an LLM system with vibes or single-turn benchmarks" — bifurcate deterministic gates from probabilistic gating, and read trace flamegraphs, not token counts), and grounded in the field anecdote in `context/growth_os/customer-truth.md` (a hidden regex-validation failure on a date field that silently re-prompted the model 14 times per task, taking task latency from 42 seconds to 2.8 seconds once the schema was fixed). GSC (`scripts/gsc_analyzer.py --vertical ai_observability_qa`) is a bonus signal only on a young site and never a veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Yao et al. — "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains" (arXiv:2406.12045) | https://arxiv.org/abs/2406.12045 | 2026-10-06 | 25% pass^8 in the retail domain — even state-of-the-art function-calling agents that clear under half the tasks at pass@1 fall below 25% once you require the same result across repeated trials | measured |
| 2 | Cemri et al. — "Why Do Multi-Agent LLM Systems Fail?" (MAST), arXiv:2503.13657 | https://arxiv.org/abs/2503.13657 | 2026-10-06 | 150 traces — the MAST failure taxonomy is built from 150 analysed traces, yielding 14 unique failure modes in 3 categories (κ = 0.88), i.e. the dominant failures are system design, inter-agent misalignment and task verification, not model capability | measured |
| 3 | LangChain — "State of AI Agents" report | https://www.langchain.com/stateofaiagents | 2026-10-06 | 51% of surveyed respondents are using agents in production today, and tracing/observability tools top the list of must-have controls for reliable agents | vendor claim |
| 4 | OpenTelemetry — "Inside the LLM Call: GenAI Observability with OpenTelemetry" (GenAI semantic conventions) | https://opentelemetry.io/blog/2026/genai-observability | 2026-10-06 | 45 seconds — the standard's own framing of an unexplained slow agent ("Was it the model? A slow tool call? A retry loop?"), and the reason to record per-call `gen_ai` spans (model, `input_tokens`/`output_tokens`, tool invocations) so the retry loop is visible instead of guessed | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Gate the release on repeat-trial pass^k and instrument the per-call retry count, not a single green run | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Where to put the deterministic schema gate so a type error fails once instead of re-prompting | 9 | 9 | 6 | 9 | 8.3 | runner-up — the strongest field anchor (the 14× retry anecdote) but the public primaries for schema adherence are vendor docs without fetchable figures; folded into the winner as the field case, not carried alone |
| Re-running the eval suite: how often is often enough | 8 | 9 | 8 | 7 | 8.0 | dropped — a real durable question with a strong primary (arXiv 2609.21267, 38.5% of a full run / 1.03 pp MAE), but it is eval *cadence*, adjacent to today's published piece, and a weaker forwardable thesis than the reliability-gate collision |
| Synthetic dataset stress testing: how many adversarial cases are enough | 7 | 8 | 6 | 7 | 7.0 | dropped — no measured primary found that states a defensible case-count threshold; would have to be asserted, which the skill refuses |
| Choosing an LLM-as-a-judge backbone / calibration | 8 | 9 | 9 | 7 | 8.3 | dropped — this is today's news article (the judge-validity thesis); re-arguing it is exactly the de-dup failure the brief guards against |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:9bbf34ea67" dedup="matched a prior artifact: 2026-10-06_buying-ai-quality-when-" window_days=180 checked_at=2026-10-06T17:33:54+00:00 -->
<!-- evergreen-gate:end -->
