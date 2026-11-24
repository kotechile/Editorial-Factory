# Signals: ai_observability_qa — 2026-11-24
**Window:** 2026-10-25 → 2026-11-24
**Queries run:** 8 (web_search ×6, HN Algolia ×1, arXiv API ×2)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | TradeoffBench: LLM judges silently complete their own trade-off premise | https://arxiv.org/abs/2611.28940v1 | 2026-11-21 | Six open-weight non-reasoning judges pass all dominance/equality controls yet pick unsupported winners on 9%–81% of 1,345 criterion conflicts; all 577 order-stable choices follow an explicitly banned majority rule; GPT-6.1-sol omits its completion premise in 29.8% of 400 verified conflicts on raw text; four reasoning judges still issue strict verdicts on up to 35/46 valid presentations | LLM-as-a-judge calibration — a judge that "passes" can still assert values no rubric ever specified | 88 |
| 2 | LangSmith BYOC moves the eval data plane into the customer's cloud | https://www.langchain.com/blog/langsmith-byoc-aws-gc-azure | 2026-11-03 | GA on AWS, Beta on Azure and Google Cloud; LangChain runs the control plane (auth, workspace config, billing metadata); the customer's data plane holds traces, evals, datasets, prompts and agent deployments; data planes created on or after 2026-10-21 run SmithDB only, ClickHouse deprecated, support ends in v0.19 | Deterministic vs probabilistic QA — judge/eval infrastructure is becoming embedded per-tenant production plumbing | 72 |
| 3 | Snowflake Observe ships online LLM-as-judge against production traces | https://www.snowflake.com/en/blog/ai-agent-observability-monitor-debug-optimize-llm-applications | 2026-11-13 | Agent Observability in private preview as of 2026-11-13; Observe supports online LLM-as-judge evaluations against production traces "turning results into metrics teams can monitor over time," each result linked to the underlying interaction; Snowflake explicitly frames model choice trade-offs by failed-evaluation rate, not token price | Trace-level observability — judge scores become a standing production metric, sampled and alerted on | 70 |

## Dated background (out of window, do not pair)
- Dynatrace completed its $915M acquisition of Arize on 2026-10-01 (dynatrace.com press release) — outside window; context only.
- LongJudgeBench (EMNLP 2026, Budapest, conference 2026-10-24/29) reports "a substantial reliability gap" across LLM judges — 1 day outside window start; corroborating context for signal #1, not a row.
- Launch HN: Laminar (RL-trained model that finds errors in agent traces) 2026-10-19 — outside window.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=3 candidates=0 heuristic=- window=2026-10-25..2026-11-24 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
