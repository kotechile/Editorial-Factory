# Signals: enterprise_ai_finops — 2026-10-08

**Window:** 2026-09-08 → 2026-10-08
**Vertical:** enterprise_ai_finops (AI FinOps & Value Realization)
**Queries run:** 12 web_search fan-outs (AI FinOps unit economics, FinOps Foundation / State of Tokenomics, LLM token pricing Sept–Oct 2026, AI budget overruns, GPU utilization, pilot-to-production failure, HITL overhead, prompt caching economics, token attribution) + 7 primary-source fetches (silicondata.com index, help.openai.com Pro tiers, futurumgroup.com overrun survey, cloudzero.com Sept pulse, kpmg.com Q3 pulse, cnbc.com token index, openai.com pricing post).
**Prior-cycle de-dup target:** 2026-09-24 `enterprise_ai_finops` winner `ai-spend-27t-cost-visibility-mandate` (Gartner Sept 16 $2.7T → cost visibility as a buying requirement) and 2026-10-01 `enterprise_ai_finops` winner `token-prices-halved-cfo-cant-read-bill` (Sept 22 OpenAI/Anthropic price cuts ⨂ State of Tokenomics Sept 23 → the unit of account moves to CRW). Any candidate that re-argues "spend scale → visibility/attribution as the buying requirement" is a retread; so is a candidate whose only new leg is the *same* Sept 16 Gartner release or the *same* Sept 23 Tokenomics survey.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Silicon Data LLM Token Expenditure Index hits an all-time low | https://www.silicondata.com/products/silicon-index/llm-token-expenditure-index | 2026-10-04 | Broad-market ticker SDLLMTK printed $0.96 per million tokens as of Oct 4, 2026 (−4.9% over 7 days) — the first time below $1; CNBC logged the $0.97 crossing on Sep 1 as "the index's lowest reading since its creation late last year," down "more than half from the high recorded earlier this summer" | prompt prefix caching economics / CRW economics | 88 |
| 2 | OpenAI repriced up the stack at DevDay: $500 ChatGPT Pro 500, and the $200 tier's allowance halved | https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers | 2026-09-29 | New tier table Pro 100 $100 / Pro 200 $200 / Pro 500 $500 per month; "Ultrafast" is exclusive to Pro 500; Pro 200 weekly GPT‑6 Pro messages fall 200 → 100 and its Work/Codex allowance drops from 20× to 10× the Plus allowance at the same $200 price (announced at DevDay, Sep 29) | high-throughput deterministic automation ROI / pricing structure | 82 |
| 3 | Futurum 2H 2026 CIO survey: AI spend is over budget and the overrun gets funded | https://futurumgroup.com/insights/enterprise-ai-overruns-hit-46-9-is-the-reckoning-in-fy2027 | 2026-09-14 | "46.9% of enterprises reported running over budget on AI, while only 5.6% said spending came in below plan"; 10% have no formal AI budget; among the 767 over-budget orgs, 47.6% sought supplemental funding and 43.3% rolled the overrun into the next cycle vs about one-sixth that cut or paused scope | cost per resolved work-unit CRW economics / unit economics | 90 |
| 4 | CloudZero AI Economics Pulse: AI share of the cloud bill crossed a tenth for the top quartile | https://www.cloudzero.com/blog/ai-economics-pulse-september-2026 | 2026-09-08 | Across a same-store panel of 430 orgs, median AI spend reached 2.66% of the cloud bill in August (13th straight monthly rise); the 75th percentile jumped 9.63% → 11.12% in one month; the share of orgs at ≥10% AI rose to 28.2% from 23.9%; two-thirds now spend ≥ $1,000/month on AI | token cost attribution by business unit | 84 |
| 5 | KPMG Q3 2026 AI Pulse: leadership now reports measurable AI value | https://kpmg.com/us/en/media/news/q3-ai-pulse-2026.html | 2026-09-24 | "Nearly 6 in 10 leaders report measurable business value from their AI initiatives": productivity 55%, faster decision-making 49%, better customer/employee experiences 38%, stronger financial performance 37%; cost management and governance move to the forefront | pilot-to-production graveyard / value realization | 86 |

**Primary-source upgrade notes (used during fact-check):**
- #1 primary = Silicon Data index page (silicondata.com, reading dated "As of Oct 4, 2026", $0.96 USD/M tokens, −4.9% 7D). CNBC (https://www.cnbc.com/2026/09/01/ai-token-prices-lows.html, Sep 1, 2026) is corroboration for the record-low trajectory and the "more than half from the summer high" framing; it is *outside* the 30-day window and is used as dated background, never as the freshness anchor — the anchor is the current (Oct 4) index reading.
- #2 primary = OpenAI Help Center "About ChatGPT Pro tiers" (help.openai.com): plan table Pro 100 / Pro 200 / Pro 500 and "Ultrafast … Included" only on Pro 500, plus the allowance/grandfathering change. The Sep 29, 2026 DevDay announcement date and the Pro 200 allowance-halving are corroborated by Business Insider and Engadget.
- #3 primary = Futurum Research insight (futurumgroup.com), Publication Date September 14, 2026, Document # AINMA202609, "2H 2026 CIO & Technology Buyers Decision Maker Survey."
- #4 primary = CloudZero "Your AI Economics Pulse for September 2026" (cloudzero.com, September 08, 2026), CloudZero's own anonymized customer panel (430 organizations), usage month August 2026.
- #5 primary = KPMG US news release, September 24, 2026, "KPMG Q3 2026 AI Quarterly Pulse Survey."

## Dropped (out of window — anchor-driven / stale / retread)
- **Gartner "Worldwide AI Spending to Grow 49.5% in 2026" (Sept 16, 2026, $2.7T).** In window on the calendar, but it was the *load-bearing primary of the 2026-09-24 cycle* (`ai-spend-27t-cost-visibility-mandate`) — re-using it as a freshness anchor is a retread. Background context only.
- **Tokenomics Foundation "State of Tokenomics, September 2026" (Sept 23).** Load-bearing primary of the 2026-10-01 cycle. Retread; background only.
- Harness "State of AI in FinOps 2026" (Jul 29) and S&P Global "42% abandoned most AI initiatives" (2025 vintage): out of window.
- Mavvrik/Benchmarkit "State of AI Cost Governance 2026" (Jul 29; n=396, fielded Apr–May 2026) and Flexera 2026 State of ITAM / AI Pulse (blog Jul 20): out of window; background context only.
- Gartner "AI Inference Costs Per Agentic Workflow +5× Through 2028" (Aug 17): out of window.
- Cast AI "2026 State of Kubernetes Optimization Report" (5% GPU utilization; Apr 2026) and VentureBeat's "$401B / 5% utilization" piece (Apr 2026): out of window.
- CloudZero/Mostly Metrics $61,656 invoice teardown (Sep 1): out of window (one day before the window opens).

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=5 candidates=0 heuristic=- window=2026-09-08..2026-10-08 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

