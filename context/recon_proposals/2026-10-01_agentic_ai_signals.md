# Signals: agentic_ai — 2026-10-01

**Window:** 2026-09-01 → 2026-10-01
**Queries run:** 14

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Planner-as-Router (PaR): joint plan-time model routing for cost-efficient multi-agent workflows | https://arxiv.org/abs/2609.32917 | 2026-09-26 | A frontier model "can cost 25 times what a small model costs per token"; PaR folds model-tier selection into planning (small/mid/frontier per subtask) with dependencies visible before any specialist runs; no separate router model or training data; "cuts cost 44% against all-frontier routing while giving up 2.9 points of accuracy"; 1,157 evaluations across 8 routers × 3 seeds; EntBench = 54 enterprise agentic tasks / 7 classes graded by executing SQL + MongoDB against live databases; preliminary (not validated) hypothesis that "cheap routing may carry a hidden compounding penalty on compositional workflows" | subagent cost optimization + multi-agent coordination modes | 82 |
| 2 | OpenAI Agents API gains computer use: agents drive an OpenAI-hosted browser | https://developers.openai.com/api/docs/guides/agents-api/tools/computer-use | 2026-09-29 | "Added computer use to the Agents API. Agents can complete tasks in an OpenAI-hosted browser, with website access approvals and sign-in handled by your application." (changelog, Sep 29); each browser step sends a fresh screenshot back to the model, inflating per-step token volume | tool use + deterministic RPC boundaries | 70 |
| 3 | OpenAI DevDay "Dots": always-on agents with their own cloud computer + browser | https://openai.com/index/openai-devday | 2026-09-29 | Always-on agents inside ChatGPT, each with its own cloud computer and browser, connecting to 4,000+ apps via the plugin ecosystem, running on GPT-6 Astra; keeps working between conversations | agent runtime / distributed architecture | 66 |
| 4 | "Be Careful Who You Trust": coordination dynamics under corrupted communication in LLM multi-agent games | https://arxiv.org/abs/2609.31704 | 2026-09-29 | Measures how LLM multi-agent coordination degrades when inter-agent communication is corrupted; trust/coordination fragility as a load-bearing failure mode in agent swarms | multi-agent coordination modes | 62 |
| 5 | GLIDE: generalized layer-wise intrinsic distributional evaluation for heterogeneous LLM agents | https://arxiv.org/abs/2609.32295 | 2026-09-26 | Layer-wise intrinsic distributional evaluation for heterogeneous LLM agent ensembles; accepted EMNLP 2026 Findings | eval / observability (adjacent) | 60 |

**Notes:**
- Signal #1 is the strongest in-window primary: on-vertical (subagent cost optimization + multi-agent coordination), primary arXiv source, concrete figures, and a contrarian "hidden compounding penalty" hypothesis that is precisely the kind of tension the vertical's founder-voice rewards.
- Signal #2 is a fresh primary (OpenAI docs + Sep 29 changelog) but is an incremental extension of the Agents API whose runtime loop was already won by the 09-14 run (`openai-agents-api-managed-runtime`); the *new* load-bearing fact is the computer-use tool primitive and its per-step screenshot token cost.
- Signal #3 (Dots) is same-day, same-vendor as #2 and shares its always-on-agent-runtime framing — listed for de-dup transparency; not an independent leg.
- Signals #4–#5 are fresh arXiv primaries but lower-intensity (game-theory / eval-adjacent), kept for the pairing scan only.
- Prior-cycle de-dup (§3.5): OWASP excessive agency (09-03), Anthropic multi-agent turf war (09-07), Google 4 patterns (09-10), OpenAI Agents API runtime (09-14), Salesforce harness > model (09-17), MCP Skills transport (09-21), MASkills skills-as-learning (09-24), GPT-6 prompt caching (09-28). PaR's thesis (plan-time model-tier routing + error-compounding penalty) is distinct from prompt-caching (cache-stability → interface rule) and from harness-evolution (training); it is a fresh angle on the subagent-cost axis.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=5 candidates=0 heuristic=- window=2026-09-01..2026-10-01 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
