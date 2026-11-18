# Evergreen Brief: warehouse_automation_robotics_capex — 2026-11-18
**Archetype:** evergreen
**Vertical:** warehouse_automation_robotics_capex
**Persona:** ops_leader
**Decision the reader is facing:** How to fund the *second* purchase — whether the capital plan carries a per-machine-year renewal reserve at a replacement price, or lets the first robot cohort come back as one renewal wave the year it reaches its average replacement age. It bites in the year the first fleet ages out, when a request for the whole fleet lands in a capital budget that only ever planned the first invoice.
**Durability:** Still true in 12 months because the load-bearing material is cohort arithmetic plus a published index, not a vendor quote: the average replacement timeline is 8.3 years as of the 2026 Lift Truck Acquisition & Usage Study (117 qualified responses, fielded August 2026), the share storing replaced machines is 35% as of that same study, and the replacement price is the equipment-class producer price index as of October 2026 (383.858 on a December 1979 = 100 base). The wave arithmetic is the calendar, and the index is re-issued monthly.
**De-dup:** `2026-11-04_your-robot-budget-39-year-gap` is this vertical's nearest prior evergreen artifact — it classifies one invoice between 39-year real property and expensed interior work, i.e. *which schedule the first spend falls into*, and makes no claim about when the site spends again. Also checked and distinct: `2026-10-14_owned-shuttles-or-rented-robots` (who holds price and residual across the asset's life), `2026-11-11_your-robot-adds-a-12260-premium` (the role mix after go-live), `2026-10-28_your-charger-gap-buys-16-robots` (on-shift availability). Cross-vertical check, read and dropped as a different mechanism: `2026-10-26_your-repair-budget-buys-7-5-percent-less` prints a spending-over-price deflator for household repairs; this brief is a cohort-scheduling and funding problem with no deflator claim of its own.
**Thesis:** An automation case prices the first purchase and never the second: a fleet bought in one cohort returns as one renewal wave about eight times the annual charge, and a reserve funded at the original invoice covers only about three quarters of it, because the equipment index for this class compounds at roughly 3.5% a year while operators stretch the replacement timeline from 7.2 years in 2024 to 8.3.

**Lead:** This topic comes from the vertical's own `primary_angles` (the fleet payback / equipment-lease angle) crossed with what the persona is actually deciding — a capital plan, not a machine. The material is the mature mobile-equipment fleet already in these buildings: the 2026 Lift Truck Acquisition & Usage Study's replacement-timeline series (8.3 years, up from 7.9 and 7.2), its disposal behaviours (35% store replaced trucks, 14% cannibalise them for parts) and its spend figures, set against the Warehouse/DC Operations Survey 2026's capex-deferral signals (13% planning to add square footage, down from 33%) and the BLS producer price index for the industrial-truck and stacker machinery class.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Modern Materials Handling, 2026 Lift Truck User Survey (Bridget McCrea, August 2026; 117 qualified responses) | https://www.mmh.com/article/2026_lift_truck_user_survey_electric_use_grows_fleet_quality_matters | 2026-11-18 | 8.3 years — the average replacement timeline this year, up from 7.9 years in 2025 and 7.2 years in 2024 | measured (survey) |
| 2 | Modern Materials Handling, 2026 Lift Truck User Survey | https://www.mmh.com/article/2026_lift_truck_user_survey_electric_use_grows_fleet_quality_matters | 2026-11-18 | 35% — respondents who store replaced trucks in case they need them later, with another 14% keeping them to use for parts | measured (survey) |
| 3 | Modern Materials Handling, 2026 Lift Truck User Survey | https://www.mmh.com/article/2026_lift_truck_user_survey_electric_use_grows_fleet_quality_matters | 2026-11-18 | $182,290 — the average expected lift truck spend in 2026, down from $214,110 in 2025, while the replacement timeline stretched | measured (survey) |
| 4 | Modern Materials Handling, Warehouse/DC Operations Survey 2026 (Brian Albright, November 2, 2026) | https://www.mmh.com/article/warehouse_dc_operations_survey_2026_inventory_improvements_in_focus | 2026-11-18 | 13% — respondents planning to add overall square footage, down from 33%, so the deferral runs through the building as well as the fleet | measured (survey) |
| 5 | Federal Reserve Bank of St. Louis (FRED), PPI by Industry: Industrial Truck, Trailer, and Stacker Manufacturing, source U.S. Bureau of Labor Statistics | https://fred.stlouisfed.org/series/PCU333924333924 | 2026-11-18 | 383.858 — the October 2026 index for the equipment class (December 1979 = 100), against 379.526 in June 2026 | measured (federal index) |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The renewal wave: fund the second purchase at a replacement price, not at the invoice | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| Peak season is a renting problem, not a capex problem | 9 | 9 | 7 | 8 | 8.3 | dropped — `2026-11-11_your-robot-adds-a-12260-premium` already carries the temp-share (16.6%) and the 1.5× overtime rule; a peak piece would re-argue a seven-day-old thesis |
| The constraint moved to the dock, so the picking fleet cannot deliver its rate | 9 | 8 | 7 | 7 | 7.9 | dropped — the constraint-migration mechanism is already argued in `2026-11-05_your-port-clears-35688-boxes-dont`, and the load-bearing dock figure (31%) collides with an unrelated token on the page, so it cannot hold a clean gate row |
| The service-contract tail: what a robot costs per year after warranty | 8 | 7 | 5 | 7 | 6.9 | dropped — no fetchable primary price; every vendor service page probed is either unreachable or carries no numeric token |
| Battery replacement as a mid-life capex | 8 | 6 | 6 | 7 | 6.9 | dropped — overlaps `2026-10-28_your-charger-gap-buys-16-robots`, and the only anchors are vendor datasheets (claims, not measurements) |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=3 hosts=2 decision="sha1:3acfcaeb03" dedup="matched a prior artifact: 2026-11-04_your-robot-budget-39-ye" window_days=180 checked_at=2026-11-18T19:41:50+00:00 -->
<!-- evergreen-gate:end -->
