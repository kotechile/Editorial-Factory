# Evergreen Brief: control_tower_exception_orchestration — 2026-10-27
**Archetype:** evergreen
**Vertical:** control_tower_exception_orchestration
**Persona:** supply_chain_architect
**Decision the reader is facing:** How to set the arrival-exception thresholds in a control tower — one fixed hour buffer per lane, or a window sized as a share of the remaining transit time — the decision bites at design time when the alert rules are configured, and again every time planners start silencing a lane whose alerts are either noise or late.
**Durability:** The relationship the article turns on is structural, not seasonal: arrival-prediction error grows with the length of the voyage leg, so a threshold expressed in fixed hours is necessarily slack on short legs and tight on long ones. The measured bands are as of the studies' own 2021 AIS record sets (published 2026 and 2022 respectively); the wage anchor is the 2025 O'NET vintage (median wages (2025)); the feed-latency figures are a vendor claim as of the 2026-10-27 retrieval and are labelled as such. None of these is a monthly statistic, and the design rule does not change when the numbers are re-published.
**De-dup:** `2026-10-13_shippers-stuck-in-the-gap` is this vertical's nearest prior artifact — it measures carrier punctuality (a 49.9% global vessel on-time rate and a 12-month high in rail dwell), i.e. how often the ship and the train are late. This brief is about the estimator, not the carrier: how wrong any arrival-time estimate is at a given voyage length, and what threshold that error can support. The event-standard neighbour `2026-10-20_your-3-0-0-feed-stuck-until-2027` argues whose timestamp counts in a DCSA 3.0.0 event; the retention piece `2026-10-20_your-exception-log-owes-5-years` argues how long the joined record must survive; `2026-10-13_hour-14-recovery-wall` prices the crew clock after a miss. None of them cites an arrival-prediction error metric, and no published artifact in the corpus contains the string "ETA" or "mean absolute error" (checked across published/, all verticals). Cross-vertical, the build-vs-buy candidate was refused by hand for this vertical in `2026-10-20_control_tower_exception_orchestration_evergreen_brief.md` because `2026-10-14_your-cluster-hidden-clock` already argues that a managed layer sells the upgrade calendar; that ground is not re-argued here.
**Thesis:** An arrival prediction is a percentage, not a stopwatch: measured AIS-based studies put average absolute error at 2.21 hours on voyage legs under a day, 6.89 hours on 1–3 day legs, 11.97 hours on 3–7 day legs and 26.92 hours beyond a week, and the best published graph model lands within 20% of the actual arrival time on only 69.1% of trajectories — so a threshold written in fixed hours is too slack to catch a miss on a short lane and too tight to survive a long one, and the exception window belongs as a share of the remaining transit.

**Lead:** The vertical's own first beat, `primary_angles` #1 — "assessing software and operational investment from reactive tracking to predictive ai exception management" — plus the persona's `wants` ("RTTV telematics pipelines"). The material: two independent AIS-based arrival-time studies (a multi-task transformer forecasting voyage-segment durations, and a global historical knowledge graph for maritime ETA) give per-duration-band absolute errors, and the vendor page of an AIS feed supplier gives the pipe's own freshness (13,000+ receivers, ~25-second average message frequency, ~5-second average data latency). The gap between a five-second pipe and a 27-hour estimate on a week-long leg is the article.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | arXiv — "Beyond the Next Port: A Multi-Task Transformer for Forecasting Future Voyage Segment Durations" (2601.08013v2) | https://arxiv.org/html/2601.08013v2 | 2026-10-27 | 2.21 h — mean absolute error on voyage legs under 24 hours; the same table gives 6.89 h on 24–72 h legs, 11.97 h on 72–168 h legs and 26.92 h on 168–504 h legs (MAPE 22.51% to 10.94%) | measured (preprint, 2021 AIS records) |
| 2 | arXiv — "Historical Knowledge Graphs for Global Maritime Estimated Time of Arrival" (2605.18408v1) | https://arxiv.org/html/2605.18408v1 | 2026-10-27 | 62.1% — on a second held-out test set only 62.1% of trajectories fell within 20% of the actual arrival time (69.1% on the first set); the graph holds 5,433 nodes and 12,334 edges | measured (preprint) |
| 3 | Kpler AIS (served at spire.com/maritime) | https://spire.com/maritime/ | 2026-10-27 | 13,000+ AIS receivers — vendor reports 300,000+ vessels tracked daily, average message frequency 25 seconds and average data latency 5 seconds | vendor claim |
| 4 | O*NET OnLine — 13-1081.00 Logisticians | https://www.onetonline.org/link/summary/13-1081.00 | 2026-10-27 | $39.58 — median hourly wage for logisticians (2025), $82,320 annual | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Arrival-prediction error by voyage length, and the threshold it can support | 9 | 9 | 9 | 9 | 9.0 | **winner** — two independent measured studies give per-band absolute error, a vendor page gives the feed's freshness, and a wage anchor prices the manual re-check |
| Control-tower build vs. buy: maintenance headcount against a per-shipment tracking fee | 8 | 8 | 7 | 8 | 7.8 | dropped — the mechanism (a bought layer sells the version/support calendar you would otherwise staff) is already argued cross-vertical in `2026-10-14_your-cluster-hidden-clock`, and this vertical's own 2026-10-20 brief refused it by hand for exactly that reason |
| Cold-chain sensor interval: what a reefer temperature record must prove | 8 | 9 | 6 | 7 | 7.5 | dropped — the statutory anchors fetch (21 CFR 1.908/1.912) but they are the same retention clauses `2026-10-20_your-exception-log-owes-5-years` already builds on, and no measured in-transit spoilage rate was retrievable: the IATA and thesis figures live in PDFs the verifier returns `unsupported` |
| Autonomous exception resolution tiers priced by loss severity | 7 | 7 | 6 | 6 | 6.5 | dropped — already published for this vertical as `2026-10-06_control-tower-silent-exception` (cargo-theft identity fraud, autonomy tiered by loss severity) |

## Notes for the drafting stage
- The four band figures are one study's own table and must be attributed to it, not generalised to "all control towers"; the study's data is 2021 AIS records, and its model is a research model, so the honest reading is that these are a *floor* under a commercial product's error, not a competitor's benchmark.
- `20%` is the tolerance the second study measures against, not a recommendation the paper makes. The article's rule is the author's derivation and must be written as one.
- The vendor row labels the feed as fast *on its own terms*; do not restate the 5-second latency as an end-to-end ETA freshness.
- The wage row prices a manual re-check only. A 15-minute check at $39.58/hour is $9.90 — show the two inputs, do not state a per-alert cost without its basis.
- Any headline figure must exist in the body's own numbers section; the ladder is the safest anchor.

## Gate result

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:4fcdd41b0c" dedup="matched a prior artifact: 2026-10-13_shippers-stuck-in-the-g" window_days=180 checked_at=2026-10-27T20:04:59+00:00 -->
<!-- evergreen-gate:end -->
