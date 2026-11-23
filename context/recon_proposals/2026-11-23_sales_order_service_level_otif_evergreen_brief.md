# Evergreen Brief: sales_order_service_level_otif — 2026-11-23
**Archetype:** evergreen
**Vertical:** sales_order_service_level_otif
**Persona:** ops_leader
**Decision the reader is facing:** Where the next margin-defence dollar goes against Walmart's OTIF and SQEP fine schedule — whether to fund the ASN/master-data and label fixes that kill the per-defect fees, fund the fill-rate and on-time work that moves the 3% COGS penalty, or absorb the fines and treat them as a cost of doing Walmart volume — the call that bites when the first quarterly SQEP deduction lands and the ops leader has to say which spend prevents it.
**Durability:** The Walmart fine schedule is a published policy structure, not a market price: the 3% COGS OTIF chargeback has held since the 2017 launch, the SQEP $200-plus-per-unit defect fees have held since the 2021 launch, and the three component thresholds (90% on-time prepaid, 98% collect-ready, 95% in-full) were last moved in 2018 when the overall OTIF bar rose 85% to 87%. Figures are as of 2026-11-23: the 3% rate and 98% threshold as Walmart's current published program terms, the SQEP fee schedule as of its Phase 1–3 rollout (2021–2024), and the quarterly OTIF billing cadence as of February 2024. A 12-month horizon only changes the numbers if Walmart publishes a new phase or threshold, which would be an announced policy event, not drift.
**De-dup:** `2026-11-02_your-cheapest-part-needs-four-sigma` is this vertical's nearest prior evergreen artifact (per-SKU newsvendor service targets from the two error costs, published 2026-11-02) — it derives an internal stock target and never prices a retailer's fine schedule. Also checked and distinguished: `2026-10-27_your-miss-costs-9x-the-chargeback` (cross-vertical, control tower) already cites Walmart's 3% COGS fine and 98% mark as one input inside a $100B total-miss-cost argument, but never opens the per-defect SQEP arithmetic ($200 + $1/case, $25 ASN, $4/pallet, $20/load) or asks which fixes pay against which fee class — that schedule-versus-fix arithmetic is the whole of this piece. Cross-vertical grep over `published/` and `context/recon_proposals/` for `SQEP`, `$4 per pallet` and `$20 per load` returns zero artifacts that argue the fee schedule.
**Thesis:** Walmart's fine schedule is a three-class cost curve, not one 3% scare number — the per-defect SQEP fees ($200 plus per-case, per-pallet, per-load charges) punish data and packaging work you control in-house at near-zero cost, while the 3% COGS OTIF penalty punishes fill-rate and on-time performance that costs real inventory money — so the fine arithmetic itself tells you which fixes to fund first, and most suppliers fund the expensive class while the cheap class keeps billing.

**Lead:** The vertical's own `primary_angles` — "retailer chargeback exposure (Walmart OTIF and SQEP, Target, Kroger) and the fill-rate threshold that triggers it" — this is the only primary angle untouched by the vertical's prior evergreen runs (per-touch cost 2026-10-19, order-vs-line fill exponent 2026-10-26, per-SKU newsvendor target 2026-11-02); the persona (ops_leader) wants concrete numbers and a decision framework, and the founder's standing position (agentic automation on bounded transactional workflows) lands on auto-disputing and preventing retailer deductions.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Vendormint — Walmart Supplier Quality Excellence Program (SQEP) Explained | https://vendormint.com/blog/walmart-supplier-quality-excellence-program-sqep | 2026-11-23 | $25 flat fee per defective PO for ASN not downloaded (DSDC and Pharmacy); $200 per defect plus $1 per case for all other document-accuracy defects | vendor claim (Walmart's published SQEP fee schedule, as reported) |
| 2 | Harvest Group — How to Prevent Common SQEP and OTIF Fines at Walmart | https://harvestgroup.com/prevent-common-sqep-and-otif-fines-walmart | 2026-11-23 | $4 per pallet pallet-compliance fee and $20 per load load-compliance fee, each on top of a $200 administrative fee per PO | vendor claim (Walmart's published SQEP fee schedule, as reported) |
| 3 | Coldstream Logistics — Walmart SQEP Explained: Phases, Defects, and Chargebacks | https://www.coldstreamlogistics.com/blog/walmart-sqep-explained | 2026-11-23 | 3% of the cost of goods OTIF fine on every case that misses, applied when the supplier's score falls below target | vendor claim (Walmart's published OTIF policy terms, as reported) |
| 4 | Inymbus — Walmart OTIF Performance Metrics Explained | https://blog.inymbus.com/walmart-otif-performance-metrics | 2026-11-23 | 3 percent of the cost of goods penalty on non-compliant cases only, against thresholds of 90% On-Time Prepaid, 98% Collect Ready and 95% In-Full; billing cadence moved to quarterly in February 2024 | vendor claim (Walmart's published program terms, as reported) |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Walmart OTIF/SQEP fine-schedule arithmetic: which fee class each fix pays against | 9 | 9 | 8 | 9 | 8.9 | **winner** |
| Target and Kroger chargeback programmes compared with Walmart's | 8 | 6 | 4 | 6 | 6.3 | dropped — Kroger/Target programme pages not verified fetchable; schedule would rest on one host |
| OTIF root-cause decomposition shares (stockout vs master data vs carrier) | 8 | 7 | 5 | 7 | 6.9 | dropped — no primary source publishes category shares; distribution unverifiable |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=4 decision="sha1:6359045526" dedup="matched a prior artifact: 2026-11-02_your-cheapest-part-need" window_days=180 checked_at=2026-11-23T20:03:07+00:00 -->
<!-- evergreen-gate:end -->
