# Signals: demand_sensing_advanced_sop — 2026-10-01

**Window:** 2026-09-01 → 2026-10-01 (30 calendar days)
**Queries run:** 14 (web: demand sensing / forecast accuracy / S&OP-IBP / Gartner supply chain planning + supply_chain_intel MCP `--recent 30` + `--search "demand sensing forecast S&OP planning"`)
**Sources swept:** supply_chain_intel (healthy), gartner_supply_chain, supply_chain_brain, supply_chain_dive, harvard_business_review, journal_of_business_forecasting, x_ai (+ web fallback: SCMR, ToolsGroup, Arkieva, e2open, o9, RELEX, GAINS, Board, Demand-Planning.com, UT GSCI)

## Raw candidate table

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Gartner: Only 5% of orgs will make ≥10% of planning decisions autonomously by 2030 | https://www.gartner.com/en/newsroom/press-releases/2026-09-24-gartner-predicts-only-5-percent-of-organizations-will-make-at-least-10-percent-of-supply-chain-planning-decisions-autonomously-by-2030 | 2026-09-24 | By 2030 only **5%** of orgs running planning automation will make **≥10%** of planning decisions autonomously; **83%** spent ≥$3M on planning automation (51% $3–10M); survey of **243 senior leaders** (Nov 11–Dec 18, 2025, revenue ≥$500M) | autonomous planning vs human oversight / ERP-native vs specialized S&OP | 92 |
| 2 | Supply Chain Dive: 6 food manufacturers (Barclays) — General Mills AI demand forecasting, Nestlé SKU cuts | https://www.supplychaindive.com/news/6-food-manufacturers-talk-supply-chain-tactics/831214/ | 2026-09-25 | General Mills uses AI for demand forecasting/logistics/manufacturing + $1B savings by 2030 target; Nestlé cutting underperforming SKUs in China; Constellation $200M savings by FY2028 | demand forecasting in practice / S&OP cost discipline | 72 |
| 3 | Supply Chain Dive: Amazon announces 2 AI supply chain agents (inbound planning + aged inventory) | https://www.supplychaindive.com/news/amazon-ai-supply-chain-agents-among-seller-upgrades/831164/ | 2026-09-24 | 2 AI agents (inbound planning, aged inventory) for sellers; no performance benchmarks disclosed | autonomous planning / agentic S&OP | 62 |
| 4 | Supply Chain Dive: TJX CEO — distribution model will help weather El Niño | https://www.supplychaindive.com/news/tjx-ceo-distribution-model-will-help-weather-el-nino/830665/ | 2026-09-18 | TJX holding capability aligns inbound seasonal merchandise with weather-driven customer demand (El Niño) | promo & seasonality shock / weather-driven demand sensing | 60 |
| 5 | Supply Chain Dive: HPE combats memory constraints with supplier help + better forecasting | https://www.supplychaindive.com/news/hpe-combats-memory-constraints-with-supplier-help-better-forecasting/830199/ | 2026-09-15 | HPE leans on better forecasting to combat memory-supply constraints | forecast accuracy under supply constraint | 60 |
| 6 | SupplyChainBrain (4flow): Evermark's Kinaxis transformation journey | https://www.supplychainbrain.com/articles/from-rapid-mobilization-to-measurable-value-evermarks-kinaxis-transformation-journey-with-4flow | 2026-09-17 | Vendor case study: S&OP transformation from rapid mobilization to measurable value (self-reported) | ERP-native vs specialized S&OP point solutions | 60 |

## Sweep verdict

- **Fresh primary landed in-window (first for this anchor-driven vertical).** Gartner's Sep 24 press release is a genuine primary analyst forecast squarely on the vertical's "autonomous planning / ERP-native vs specialized S&OP" axis, with hard figures (5% / 10% / 83% / $3M / 51% / 243 leaders) and a named analyst (Buse Aras). Prior-cycle sweep (2026-09-24) had flagged "Gartner Critical Capabilities (H2 2026)" as a watch-item — this is a *different, fresher* Gartner artifact (a forecast press release, not the MQ/Critical Capabilities companion).
- **Corroborating in-window field evidence** (#2–#5) shows the thesis playing out in real earnings calls: heavy AI/planning spend alongside human-led SKU/cost decisions.
- **No valid synthesis pair expected** at the token layer: the Gartner signal carries the "automation" token but no working-capital/safety-stock leg; the food-manufacturers row carries cost/SKU tokens, not the axis-a working-capital set. The Judge owns whether a cross-topic fusion clears the ≥8 gate.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=0 heuristic=- window=2026-09-01..2026-10-01 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
