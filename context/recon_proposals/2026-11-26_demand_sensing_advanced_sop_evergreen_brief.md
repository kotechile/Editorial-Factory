# Evergreen Brief: demand_sensing_advanced_sop — 2026-11-26
**Archetype:** evergreen
**Vertical:** demand_sensing_advanced_sop
**Persona:** ops_leader
**Decision the reader is facing:** Whether the promised MAPE improvement of a demand-sensing upgrade (or any forecast-accuracy project) is worth its price — settled by pricing the accuracy point against their own inventory carrying-cost rate and replenishment physics, before signing the renewal or the new tool budget.
**Durability:** The links between forecast error, safety stock and cash are formula-level facts that do not expire: carrying-cost rules of thumb (15%–25% per the ASCM-chapter page), the error-variance basis of safety stock, and the M5-competition simulation findings (80% of accuracy improvements had no decision impact) are all structural. The figures are as of 2026: the EJOR M5 analysis is vol. 322 (2025), the M5-value simulation is the demand-planning.com study published August 2024, the arXiv newsvendor study is 2603.16815 (March 2026), and the carrying-cost rules of thumb are the ASCM partner page as of 2026.
**De-dup:** `2026-10-15_forecast-value-added-lose-to-last-period` is this vertical's nearest prior evergreen artifact: it scored planning layers (baseline, overrides, consensus) against a naive benchmark at the freeze lag. This brief differs: it does not score layers — it prices a point of accuracy itself, with the empirical conversion rates (only 12.6% of accuracy gains produced superior economic performance in the M5-value simulation; 80% changed nothing) and the carrying-cost math that converts a safety-stock delta into cash. Cross-vertical check: `grep -ril "carrying cost" published/` named `2026-10-05_inventory-carrying-cost-rate` (vertical: meio_working_capital_tco) — that article prices the holding cost rate itself (20–30%, models loading only the borrowing rate); this article spends a carrying-cost rate the reader already has to value an accuracy improvement, so its mechanism is the conversion, not the rate. Checked and dropped as a duplicate: nothing.
**Thesis:** A point of MAPE is not a dollar until it changes a replenishment decision: the M5 evidence shows most accuracy improvements change nothing, so the reader should price the accuracy point against their own carrying-cost rate, their own safety-stock formula and their own order quantum — and demand a measured decision-impact estimate, not an accuracy delta, before funding a sensing upgrade.

**Lead:** The vertical's own beat, the persona's wants, and real field friction. `context/verticals.json` `primary_angles` #2 ("forecast accuracy amortization reducing MAPE percentage driving millions in excess safety stock reduction") is the exact decision; `context/personas.json` `ops_leader` wants working-capital math; `context/growth_os/founder-voice.md` §3 states the 1–2-MAPE-point claim; `context/growth_os/customer-truth.md` supplies the tether case (Anecdote 1: a 24%→21% MAPE cut let a CPG brand trim $8.5M of finished-goods inventory) and its fragility (Anecdote 2: a viral 400% spike no accuracy gain would have predicted). Negative findings recorded: the GSC export and the supply-chain intel client were not re-run this pass; the 2026-10-15 brief's recorded negative findings (0 GSC candidates; intel feed returned only newsroom/podcast items, no vendor_evaluations) are carried forward. The 2026-10-15 FVA brief covered layer scoring, so its evidence set was not reused; hosts below were probed fresh except demand-planning.com and arxiv.org, which are proven fetchable on this beat (casebook, 2026-10-22 and 2026-11-12 probes).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Demand-Planning.net (Johann Robette), "Forecasting Fallacy Exposed: The Economics Behind Accuracy", 19 Aug 2024 | https://demand-planning.com/2024/08/19/forecasting-fallacy-exposed-the-economics-behind-accuracy | 2026-11-26 | 80% — in 80% of the 9.4 million simulated cases, improving the forecast had no impact on the replenishment decision and thus on economic performance | measured |
| 2 | Demand-Planning.net, same study | https://demand-planning.com/2024/08/19/forecasting-fallacy-exposed-the-economics-behind-accuracy | 2026-11-26 | 12.6% — improving the forecast produced superior economic performance in 12.6% of cases (about 1 in 8), and gains were cut roughly 28% by underperformance cases | measured |
| 3 | arXiv:2603.16815, "Beyond Accuracy: Evaluating Forecasting Models by Multi-Echelon Inventory Cost", Marik/Saha/Chatterjee, submitted 17 Mar 2026 | https://arxiv.org/abs/2603.16815 | 2026-11-26 | seven — the study evaluates seven forecasting approaches through single- and two-echelon newsvendor simulators on the M5 Walmart dataset and prices them by inventory cost and fill rate, not accuracy | measured |
| 4 | APICS Princeton-Ocean chapter (ASCM partner), "Cost of Carrying Inventory" | https://apicsprsjorg.starchapter.com/blog/id/6 | 2026-11-26 | 15% — the standard rule of thumb for inventory carrying cost is 15% to 25% of inventory value on hand, with component ranges (cost of money 6%–12%, obsolescence 6%–12%) summing to 25%–55% | vendor claim |
| 5 | Horizon Solutions, "Forecast Accuracy: MAPE, WMAPE, MAD and RMSE Explained", 10 Nov 2026 | https://www.horizonsolutions.ai/supply-chain-planning/forecast-accuracy | 2026-11-26 | 8-15% — a 5 percentage-point improvement in SKU-weekly MAPE typically reduces safety stock by 8-15% for mid-volume items, because safety-stock formulas are built on forecast-error variance | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Pricing a MAPE point: does the promised accuracy gain of a sensing upgrade convert to cash? | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| ERP-native planning vs specialized S&OP point solutions (integration tax) | 8 | 8 | 5 | 7 | 7.2 | dropped — primary integration-tax figures are vendor marketing; the 2026-11-12 batch-window article already argued adjacent ground |
| Promo-shock sandbox simulation before campaign launch | 8 | 6 | 4 | 7 | 6.3 | dropped — the 2026-10-29 promo-spike article covers the mechanism; fresh anchors are vendor-only |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=4 hosts=4 decision="sha1:0b938b5bce" dedup="matched a prior artifact: 2026-10-15_forecast-value-added-lo" window_days=180 checked_at=2026-11-26T20:04:46+00:00 -->
<!-- evergreen-gate:end -->
