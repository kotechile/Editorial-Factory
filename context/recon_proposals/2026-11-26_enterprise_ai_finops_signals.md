# Signals: enterprise_ai_finops — 2026-11-26
**Window:** 2026-10-27 → 2026-11-26
**Queries run:** 11 (web_search ×6, web_extract ×5, HN Algolia date checks ×3, WP-REST date probes ×2)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Gemini 4 Carbon and Argon introductory rates expire Dec 1 | https://ai.google.dev/gemini-api/docs/pricing | 2026-11-26 (observation) | Google's own rate card: Carbon and Argon paid tier $2.00 input / $10.00 output per 1M tokens "through November 30, 2026. $4.00 starting December 1, 2026"; context caching $0.10 → $0.20 on the same date; both models unavailable on the Free tier; thinking tokens billed as output. Price doubles on input, output AND cache in one calendar event. | cost per resolved work-unit; token cost attribution | 92 |
| 2 | FinOps working group: direct model APIs are the unmanageable channel | https://www.finops.org/wg/token-economics-saas | 2026-10-28 (page footer "Last updated: October 28, 2026") | Paper "Managing AI Token Costs from Direct Model Provider APIs": a model provider invoice breaks down at most by API key/project/workspace, "with no concept of business unit, cost center, or application"; developers buy with personal cards before Procurement knows; Sept 2026 State of Tokenomics survey: proving value/ROI the most-named challenge (43%), 86% evaluating/using model routers, and when buyers were asked what they want from providers, 23% asked for transparency and only 4% for lower prices. FOCUS v1.5 brings AI token data into the spec. The paper's six buying channels run from direct provider APIs to self-hosted open-weight models (no per-token charge; cost is GPU hours plus the platform team to run it) — the one channel with no teaser prices and no rate card to expire. | token cost attribution by business unit; HITL/value | 86 |
| 3 | Kion: forecast AI token spend — rates must be re-validated whenever pricing changes | https://kion.io/blog/how-to-forecast-ai-token-spend | 2026-11-06 (publisher's related-resources listing on kion.io/hidden-token-costs-ai-finops) | 6-step forecast: price uncached input, output, cache-read and cache-write separately; "Validate rates when building the forecast and whenever pricing, contracts, or model selection changes"; compare forecast vs actuals at least monthly. No step names a calendar checkpoint for a scheduled rate change — the control is reactive. | cost per work-unit; forecasting | 74 |
| 4 | Gemini 4 Carbon GA'd to all paid developers Nov 10 with a visible expiry date | https://neomanex.com/news/gemini-4-carbon-ga-paid-api-2-10-until-nov-30-then-4-20 | 2026-11-10 (event date stated in slug and body) | Google opened the paid API to every paying developer on 10 November with the intro price ending 30 November; sibling Gemini 4 Hydrogen shipped 12 November at $1.50/$7.50 with a free tier and no intro period — Carbon at December rates is ~2.7× Hydrogen. Advises budgeting any production use at the $4/$20 December rate. | pilot-to-production | 70 |
| 5 | Three Gemini 4 models in 30 days, one carrying an expiry-dated price | https://shattered.io/gemini-4-carbon-price-doubles-4-input-nov-30-argon-hydrogen | 2026-11-16 (dated in-text: "Today is November 16, 2026") | Carbon's intro rate leaves 14 days; a router can split easy requests to Hydrogen ($1.50/$7.50) and escalate to Carbon, and the routing gap widens Dec 1. The ramp pattern (ship three rungs, expire one's price) is new vendor behavior. | high-throughput deterministic routing ROI | 66 |
| 6 | Rate card ≠ bill: cost per accepted task is the only number that survives a price cut | https://sesamedisk.com/llm-token-pricing-inference-cost | 2026-11-17 (price table "as of November 17, 2026") | Ten-step agent re-reading 30K input tokens/step bills 300K input tokens — 10× a one-shot call with zero price change; at 90% cache hit the same loop costs ~$0.17 vs $1.20, but cache writes at $5/M can never earn back a prefix that changes every turn. Lists "Promotional expirations: Gemini 4 Carbon moves from $2/$10 to $4/$20 on December 1" as a watch item. | CRW economics; caching | 75 |
| 7 | AI chargeback model guidance lands the same month a rate doubles | https://kion.io/how-to-build-ai-chargeback-model/ | 2026-10-30 (publisher's related-resources listing) | Chargeback build guide published inside the window while Google's teaser window is live: chargeback requires allocation at business-unit grain — exactly the data the FinOps WG paper says model-provider invoices do not carry. | token cost attribution; chargeback | 62 |

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=4 heuristic=0.77-0.82 window=2026-10-27..2026-11-26 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #1 ⨂ #2 | economics_x_architecture | A: cost per resolved work-unit; token cost attribution | B: token cost attribution by business unit; HITL/value | https://ai.google.dev/gemini-api/docs/pricing https://www.finops.org/wg/token-economics-saas | 0.82 | legB:url_already_cited |
| 2 | #2 ⨂ #6 | economics_x_architecture | A: token cost attribution by business unit; HITL/value | B: CRW economics; caching | https://www.finops.org/wg/token-economics-saas https://sesamedisk.com/llm-token-pricing-inference-cost | 0.78 | legA:url_already_cited |
| 3 | #2 ⨂ #3 | economics_x_architecture | A: token cost attribution by business unit; HITL/value | B: cost per work-unit; forecasting | https://www.finops.org/wg/token-economics-saas https://kion.io/blog/how-to-forecast-ai-token-spend | 0.77 | legA:url_already_cited |
| 4 | #2 ⨂ #7 | economics_x_architecture | A: token cost attribution by business unit; HITL/value | B: token cost attribution; chargeback | https://www.finops.org/wg/token-economics-saas https://kion.io/how-to-build-ai-chargeback-model/ | 0.77 | legA:url_already_cited; prior_cycle_token_overlap:model |

**Heuristic terms (advisory):**
- #1: token_coverage=0.75 intensity=0.89 angle_fit=1.0 contrast=0.67 → 0.82 (economics_x_architecture)
- #2: token_coverage=0.5 intensity=0.81 angle_fit=1.0 contrast=1.0 → 0.78 (economics_x_architecture)
- #3: token_coverage=0.5 intensity=0.8 angle_fit=1.0 contrast=1.0 → 0.77 (economics_x_architecture)
- #4: token_coverage=0.75 intensity=0.74 angle_fit=1.0 contrast=0.6 → 0.77 (economics_x_architecture)
<!-- synthesis-seed:end -->

## Dated background
- State of FinOps 2026 (Feb 19, 2026): 98% manage AI spend, up from 31% in 2024 — https://www.prnewswire.com/news-releases/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-302691410.html
- Tokenomics Foundation launched Aug 4, 2026 (intent announced Jun 3, 2026) — https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management
- CIO Dive on the FinOps X launch (June 12, 2026) — https://www.ciodive.com/news/foundation-tackle-ai-token-cost-management/822839
- Kion's AI-FinOps framing column (Forbes Tech Council, Sep 17, 2026; out of window) — https://kion.io/hidden-token-costs-ai-finops
- Gemini 4 Carbon pricing walkthrough with a worked budget-vs-actual example ($131 → $262 on identical usage from Dec 1) — https://www.activepieces.com/blog/gemini-4-carbon-pricing-costs-and-limits-in-2026
- LLM API pricing comparison, November 2026 edition (rate-card landscape; Oct 7 Haiku 5.5 cuts are out of window) — https://getnadir.com/blog/llm-api-pricing-june-2026-complete-comparison
- HN discussion "Price per 1M tokens is meaningless" (Jul 6, 2026) — https://news.ycombinator.com/item?id=48809542
- Provider pricing pages read 2026-11-16 for the rate landscape — https://straitly.ai/llm-inference-cost-statistics
