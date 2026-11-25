# Evergreen Brief: warehouse_automation_robotics_capex — 2026-11-25
**Archetype:** evergreen
**Vertical:** warehouse_automation_robotics_capex
**Persona:** ops_leader
**Decision the reader is facing:** Whether the next automation dollar should fund a robot fleet or a retention program — i.e., which lever actually moves the loaded labor rate the payback math divides by, when roughly two-fifths of the floor turns over every year and a new hire works at a fraction of standard for a month or more.
**Durability:** This is true for months, not weeks: the separation rate is an annual government series (roughly 40% a year for transportation and warehousing as of the BLS JOLTS 2026 annual estimate), the Gallup replacement rule (40% of annual salary, about $21,800 at warehousing's April 2026 average hourly earnings of $26.76) is a standing methodology, and the O*NET median wage is pinned to the 2025 vintage ("as of" 2025). None of these figures expires with a news cycle; only the JOLTS vintage moves, annually.
**De-dup:** `2026-10-14_wage-floor-sets-robot-payback` is this vertical's nearest prior labor piece, and it prices the wage level the robot replaces (federal median by occupation, state floors) — it names turnover only as a survey figure inside its inputs. `2026-10-28_100000-totes-skip-the-cost` lists "attendance and turnover" as one of four inputs a vendor sells back to the buyer, but never prices the replacement stream itself. No published artifact in this vertical (or anywhere in `published/`, grepped) argues that the loaded labor rate should be built from replacement cost, or that retention spend competes line-for-line with robot capex. The mispick error tax was separately ruled out as a re-argue of `2026-10-07_warehouse-pick-error-tax-payback`.
**Thesis:** The labor line an automation case replaces is not a wage — it is a replacement stream: at roughly 40% annual separations a warehouse re-staffs two-fifths of its floor every year, each exit costs about 40% of that worker's annual salary, and a new hire runs at 60–70% of standard for weeks, so the loaded labor rate in a robot payback should be priced from replacement cost — and a $2,000–5,000-per-associate retention program competes directly with robot capex for the same dollars, per dollar of labor line it moves.

**Lead:** The vertical's own primary_angles entry "labor volatility risk index — rising wages and warehouse labor shortages altering the automation ROI curve" (context/verticals.json), combined with the ops_leader persona's standing want for working-capital math on the labor line. Evidence gathered from Fountain's warehouse-turnover analysis (Gallup replacement rule, BLS April 2026 warehousing earnings), CognitOps's turnover-cost breakdown (JOLTS separation rate, replacement cost bands, ramp-up productivity), and the O*NET 2025 wage table for the picker occupation.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Fountain — Warehouse turnover rate: how to calculate and reduce it (citing Gallup and BLS) | https://www.fountain.com/posts/warehouse-turnover-rate | 2026-11-25 | 40% of salary is the cost of replacing a frontline employee — roughly $21,800 in warehousing, where BLS reported average hourly earnings of $26.76 in April 2026 (about $54,500 annualized) | measured (survey rule applied to official wage series) |
| 2 | Fountain — same analysis (Fountain frontline retention research) | https://www.fountain.com/posts/warehouse-turnover-rate | 2026-11-25 | 43% of workers are gone within 90 days — most warehouse leavers exit before reaching full picking speed | measured |
| 3 | CognitOps — The Real Cost of Warehouse Employee Turnover (citing BLS JOLTS and Center for American Progress) | https://cognitops.com/warehouse-employee-turnover-costs | 2026-11-25 | 40% a year is the separation rate for transportation and warehousing workers (BLS JOLTS, 2026); replacing a worker earning under $50,000 costs about 20% of annual pay | measured (official series, restated) |
| 4 | CognitOps — same analysis | https://cognitops.com/warehouse-employee-turnover-costs | 2026-11-25 | 50–150% of annual salary is the typical replacement cost of a warehouse associate; a mid-size DC running 40% turnover on a 200-person workforce absorbs $1.5 million or more a year in replacement costs | measured (cost model) |
| 5 | CognitOps — same analysis | https://cognitops.com/warehouse-employee-turnover-costs | 2026-11-25 | 60–70% of standard productivity is what new associates average in their first month, with recruiting and screening alone at $800 to $1,500 per hire | measured (cost model) |
| 6 | O*NET OnLine — Summary report 53-7062.00, Laborers and Freight, Stock, and Material Movers, Hand | https://www.onetonline.org/link/summary/53-7062.00 | 2026-11-25 | Median wages (2025) $19.35 hourly, $40,240 annual for the hand-mover occupation the picking floor is staffed from | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The replacement stream: price the loaded labor rate from turnover cost, and make retention spend compete with robot capex | 9 | 8 | 8 | 9 | 8.5 | **winner** |
| The pick-and-pack error tax: what one mispick costs and when validation pays | 9 | 9 | 9 | 9 | 9.0 | dropped — re-argues `2026-10-07_warehouse-pick-error-tax-payback`, which owns the error-rate-as-capital-budget thesis |
| Peak-season temp surge as the automation trigger | 8 | 8 | 7 | 8 | 7.8 | dropped — `2026-11-11_your-robot-adds-a-12260-premium` already carries the temp share and the 1.5× overtime rule |
| Facility readiness (floor flatness, sprinkler clearance, charger circuits) before the fleet order | 7 | 9 | 6 | 8 | 7.4 | dropped — casebook 2026-10-21: only statute rows fetch on this beat; the requirement numbers sit in unreachable PDFs |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=3 hosts=3 decision="sha1:c9456d0a77" dedup="matched a prior artifact: 2026-10-14_wage-floor-sets-robot-p" window_days=180 checked_at=2026-11-25T19:35:37+00:00 -->
<!-- evergreen-gate:end -->
