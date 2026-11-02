# Verified Brief: agentic_ai — 2026-11-02 (evergreen)

Archetype: evergreen. Source of the angle: `context/recon_proposals/2026-11-02_agentic_ai_evergreen_brief.md` (gate PASS, 10 rows, 3 hosts).
Article: `context/drafts/2026-11-02_your-192-sessions-stall-the-model-not-the-tools_final.md` — slug `your-192-sessions-stall-the-model-not-the-tools`.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Serving unit | An agent's end-to-end delay is split almost evenly between model writing and tool execution (45%-57% tools) | VERIFIED | https://arxiv.org/html/2603.18897v3 | "it accounts for 45%–57% of agent E2E latency across representative deep research, coding, and scientific tasks" |
| 2 | Load curve | Going from 1 to 192 concurrent sessions stretches model generation time more than 17x while tool time changes only modestly | VERIFIED | https://arxiv.org/html/2603.18897v3 | "when concurrency grows from one to 192 concurrent sessions, LLM generation time grows by more than 17 ×, while tool execution time changes only modestly" |
| 3 | Overlap | Running likely tool calls early cuts mean task completion time 43.5% | VERIFIED | https://arxiv.org/html/2603.18897v3 | "PASTE reduces average task completion time by 43.5% and lowers observed tool latency by 1.8 ×" |
| 4 | Overlap caveat | Doubling tool speed under load without touching the model's scheduler absorbs the gain | VERIFIED | https://arxiv.org/html/2603.18897v3 | "We confirm this effect with a controlled experiment that accelerates tool execution by 2 × while leaving the LLM-side scheduler unchanged; under high load, the extra returning workload slows LLM generation enough to absorb" |
| 5 | Prefix cache | Cached tokens are 77.7% of input tokens in a 14-day production agent trace | VERIFIED | https://arxiv.org/html/2609.33224v1 | "Input volume is approximately 192 × output volume, and cached tokens account for 77.7% of input tokens" |
| 6 | Decode share | Decode is 78.4% of measured request duration | VERIFIED | https://arxiv.org/html/2609.33224v1 | "decode accounts for 78.4% of measured LLM request duration in our production trace (Fig. 2" |
| 7 | Packing payoff | Production cluster: 34.7% fewer serving instances, 36.8% higher per-instance throughput | VERIFIED | https://arxiv.org/html/2609.33224v1 | "PackServe achieves 34.7% fewer serving instances and 36.8% higher per-instance request throughput" |
| 8 | SLO as a purchase | 13.0-16.8% fewer GPU-hours at a 30-ms TPOT target; 21.1-24.6% at 50 ms | VERIFIED | https://arxiv.org/html/2609.33224v1 | "PackServe uses 13.0–16.8% and 21.1–24.6% fewer active GPU-hours under 30-ms and 50-ms TPOT targets" |
| 9 | Program scheduling | Scheduling whole agent programs returns 4-15x program throughput at equal latency versus vLLM | VERIFIED | https://arxiv.org/html/2502.13965v1 | "Autellix improves throughput of programs by 4-15× at the same latency compared to state-of-the-art systems, such as vLLM" |
| 10 | Head-of-line | On mixed work, 5.5x over MLFQ and 4x over vLLM-opt | VERIFIED | https://arxiv.org/html/2502.13965v1 | "Autellix achieves up to 15× higher throughput than vLLM, 5.5× higher than MLFQ, and 4× higher than vLLM-opt" |
| 11 | Cache within a program | Cache-hit rate inside one agent program stays above 90% across input lengths | VERIFIED | https://arxiv.org/html/2502.13965v1 | "within a single program, cache-hit rates remain above 90% across all input lengths" |
| 12 | Quota arithmetic | A 2M input-token-per-minute limit with 80% cache hits is 10M effective tokens per minute | VERIFIED (vendor claim — provider's own worked example) | https://docs.claude.com/en/api/rate-limits | "With a 2,000,000 ITPM limit and an 80 percent cache hit rate, you could effectively process 10,000,000 total input tokens per minute" |
| 13 | Ramp rule | Above 1M input tokens per minute, grow traffic by no more than 50% every 15 minutes | VERIFIED (vendor claim — provider guidance) | https://platform.openai.com/docs/guides/rate-limits | "once your traffic reaches 1 million input tokens per minute (TPM), increase it by no more than 50% every 15 minutes" |

## Flags and limits carried into the draft

- **FLAGGED (scope):** PackServe's 77.7%, 78.4%, 34.7% and 36.8% come from one operator's 14-day trace and one production cluster (Ant Group co-authorship). The article says so in `The catch` and treats them as that fleet's behaviour, not constants.
- **FLAGGED (dependency):** Autellix's 4-15x requires program-level interception inside the serving engine; a runtime calling a hosted endpoint one request at a time cannot reproduce it. The article states this in `The catch`.
- **FLAGGED (point, not ceiling):** 192 concurrent sessions is a measurement point on a load curve, not a published limit; no cited source states sessions per GPU. The article says the number must be measured against the reader's own prefix lengths.
- **REMOVED:** none. No claim in the draft lacks a verified row above.

## Arithmetic re-derived after the rewrite

- 45%-57% (tools) and 78.4% (decode) are two different denominators — one is end-to-end task latency across three workloads, the other is request duration inside one operator's trace. The draft does not add or compare them; both stand alone.
- The 2,000,000 → 10,000,000 example is the provider's own (2M uncached + 8M cached), quoted, not computed here.
- No payback, ratio or percentage in the final was derived by this run.
