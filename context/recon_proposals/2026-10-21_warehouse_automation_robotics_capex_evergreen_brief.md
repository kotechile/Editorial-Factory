# Evergreen Brief: warehouse_automation_robotics_capex — 2026-10-21
**Archetype:** evergreen
**Vertical:** warehouse_automation_robotics_capex
**Persona:** ops_leader
**Decision the reader is facing:** How many robots to commit to per pick station before signing the capex — and how to tell, from two stopwatch numbers, when the next robot stops earning its amortization.
**Durability:** No price, rate or vendor quote is load-bearing here: the argument is queueing arithmetic plus station service time, and the cited figures are dated (peer-reviewed studies published 2018 and 2024; a 2024 deployment announcement and a 2026 survey). As of October 2026 the mechanism is unchanged — robots feed stations, and stations bind — so the rule stays true while prices, vendors and robot models change under it.
**De-dup:** `2026-10-07_automation-payback-splits-by-sku-geometry` is this vertical's nearest prior artifact on throughput economics — it segmented capex by SKU class (which goods to automate), not how many machines to buy. Also checked and distinct: `2026-10-21_your-seller-wont-stay` (price deflation and vendor consolidation), `2026-10-14_wage-floor-sets-robot-payback` (the wage input to payback), `2026-10-14_owned-shuttles-or-rented-robots` (own versus rent) and `2026-10-07_warehouse-pick-error-tax-payback` (mispick cost). None of them sizes a fleet. A cross-vertical grep for "pick station" / "fleet siz" / "robots per station" over `published/` found no other piece arguing saturation.
**Thesis:** A robot fleet has a computable saturation point set by the pick station's handling time and the robot's round trip, so the vendor's robots-per-station ratio over-buys small catalogues and under-buys large ones — and every robot past saturation is capex that can never be amortized by throughput.

**Lead:** The vertical's own `primary_angles` #1 and #2 ("financial modeling for fulfillment centers manual picking workflows vs amr and asrs capital deployment"; "amr fleet payback period calculator equipment lease maintenance facility modifications") combined with the founder pillar "The Operational Reality Angle (Physical Meets Digital)" in `context/growth_os/founder-voice.md` §2.6, and the field friction in `customer-truth.md` Anecdote 1 (32 AMRs, UPH 65 → 195). GSC showed zero striking-distance queries for this vertical (thin impressions, bonus signal only). The specific material: two peer-reviewed queueing studies of robotic mobile fulfilment systems that report the station-throughput ceiling and the diminishing-return point of additional robots, plus two published deployment ratios (a 24-station/4,500-lines-per-hour design target and a 4-robots-per-associate product claim) that the arithmetic does not support as a general rule.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Merschformann, Lamballais, de Koster & Suhl — "Decision Rules for Robotic Mobile Fulfillment Systems" (arXiv:1801.06703v1, 2018) | https://arxiv.org/html/1801.06703v1 | 2026-10-21 | 91% — with 1,000 SKUs and small orders, four robots per pick station reach 91% of the picking-station throughput ceiling, and a fifth adds six points | measured (peer-reviewed discrete-event simulation, Table 10) |
| 2 | Merschformann et al. (same paper) | https://arxiv.org/html/1801.06703v1 | 2026-10-21 | 20.29% — replenishment operations consume 20.29% of the overall time consumed by the robots across the phase-2 runs | measured (simulation) |
| 3 | Xie & Otten — "Introducing Combi-Stations in Robotic Mobile Fulfilment Systems" (arXiv:2403.12798v1, 2024) | https://arxiv.org/html/2403.12798v1 | 2026-10-21 | 17 robots — the minimum number of robots for a two-picking-station, two-replenishment-station system to be stable, against 16 with two combi-stations | measured (queueing analysis) |
| 4 | Xie & Otten (same paper) | https://arxiv.org/html/2403.12798v1 | 2026-10-21 | 40 robots — with more than 40 robots, it is not possible to significantly increase the arrival rate with additional robots | measured (queueing analysis) |
| 5 | Modern Materials Handling — "S&S Activewear partners with Körber Supply Chain Software and Geekplus on robotics deployment" (2024-05-29) | https://www.mmh.com/article/ss_activewear_partners_with_koerber_supply_chain_software_and_geekplus_on_robotics_deployment | 2026-10-21 | 4,500 lines per hour through 24 picking stations — the PopPick system is designed to support more than 4,500 lines per hour through 24 picking stations | vendor claim (announced design target) |
| 6 | Locus Robotics — "How P2G Creates Unlimited Warehouse Throughput with Fast Pick" | https://locusrobotics.com/blog/p2g-unlimited-warehouse-throughput-fast-pick | 2026-10-21 | 300-400 units per hour — one associate working alongside four Locus robots enables 300-400 units per hour from bulk locations | vendor claim |
| 7 | Modern Materials Handling — "2026 Automation Study: Warehouse automation ticks upward" (January 2026) | https://www.mmh.com/article/2026_automation_study_warehouse_automation_ticks_upward | 2026-10-21 | 48% — goods-to-person picking solutions are used by 48% of companies now, and 51% are preparing updates or new deployments | measured survey (Peerless Research Group, 120+ buyers) |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Fleet sizing: the station sets the saturation point, the vendor ratio does not | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| Building readiness: sprinkler clearance, charger circuits and floor work as hidden capex | 8 | 9 | 5 | 7 | 7.4 | dropped — only general-industry code fetches; no measured source about robots on those constraints |
| Battery and charging as the second capex line (asset life shorter than the amortization schedule) | 8 | 7 | 5 | 7 | 6.9 | dropped — no fetchable measured cycle-life figure tied to warehouse robots; would have rested on vendor claims |
| VDA 5050 interoperability as a procurement clause (multi-vendor fleets) | 7 | 7 | 6 | 7 | 6.8 | dropped — adjacent to the 2026-10-21 published piece on seller consolidation (lock-in), and its fact base is a standards version that moves |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=5 hosts=3 decision="sha1:5dd06d9f38" dedup="matched a prior artifact: 2026-10-07_automation-payback-spli" window_days=180 checked_at=2026-10-21T19:35:11+00:00 -->
<!-- evergreen-gate:end -->
