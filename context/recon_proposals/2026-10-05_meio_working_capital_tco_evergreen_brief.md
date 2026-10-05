# Evergreen Brief: meio_working_capital_tco — 2026-10-05
**Archetype:** evergreen
**Vertical:** meio_working_capital_tco
**Persona:** ops_leader
**Decision the reader is facing:** What fully-loaded inventory carrying-cost rate to load into this planning cycle's safety-stock, MEIO and SKU-rationalization models — the ~7% bank-prime rate the company actually borrows at, or the 20–30% all-in cost of holding a dollar of inventory for a year — because that one input decides how much regional buffer gets deployed and which long-tail SKUs survive the prune.
**Durability:** The load-bearing claim is structural, not a print: financing is only the *minority* share of what it costs to hold inventory, so a model fed the borrowing rate under-costs a buffer. The 20–30% band is a standing industry convention (as of the current 2025–26 reference literature); every time-sensitive figure in the brief is dated and re-checkable — the 7.00% bank-prime financing leg is as of the Federal Reserve H.15 release (October 2026), the 1.30 US inventories/sales ratio and $2.76 trillion stock are as of the Census MTIS July 2026 release, and the $3.12/kg global air-cargo spot rate is as of July 2026. The rate legs drift quarter to quarter; the rule (load the fully loaded rate, not the WACC) does not expire, and none of the figures here expire inside 90 days.
**De-dup:** 2026-10-05_fed-rate-hike-inverts-working-capital-trap is this vertical's nearest prior artifact — a *news* synthesis arguing a rate hike landed on an already-lean inventory system, anchored to a two-week collision of fresh releases and carrying September-snapshot numbers. This brief makes a different, durable argument: the fully-loaded carrying-cost *rate itself* (20–30%) is the model input that decides buffer depth and SKU pruning, and it is dated rather than expiring. The same-week briefs 2026-10-05_meio_working_capital_tco_signals and 2026-10-05_meio_working_capital_tco_angle_brief are that news run, not an evergreen argument; no `meio_working_capital_tco` evergreen brief exists yet.
**Thesis:** Inventory is a loan that never shows up on the credit line — a dollar of stock costs 20–30% a year all-in to hold, yet the financing leg is only about 7 points of that (bank prime), so any safety-stock, MEIO or SKU-rationalization model fed the borrowing rate alone under-costs a buffer by roughly 3×; loading the fully-loaded rate is what makes expedited air freight (~$3.12/kg spot) beat a bloated regional buffer and what makes the long tail read as the liability it is.

**Lead:** From the vertical's own `primary_angles` in `context/verticals.json` — "the working capital trap carrying cost of stagnant inventory against volatile supplier lead times" and "expedited freight vs safety stock calculator — air freight surcharges vs excess regional buffer stock" — and the persona's `wants` (`context/personas.json`, `ops_leader`: "working capital / MEIO math"). Reinforced by `context/growth_os/founder-voice.md` §3 (`meio_working_capital_tco`: "The Working Capital Trap … a 20–30% annual holding cost"; "Expedited Freight vs. Buffer Stock Arbitrage") and the founder's field notes in `context/growth_os/customer-truth.md` (Anecdote 1: the $14M safety-stock trap at 45 days of forward buffer per node; Anecdote 2: $575k/yr carrying cost on $2.5M of regional spares vs $85k/yr of chartered air freight — 6.7× more capital-efficient). The founder's "20–30%" claim had no fetchable primary in the corpus, so it was grounded against live industry references and the Federal Reserve's own rate release rather than asserted. GSC is a bonus signal only on a young site and no exported opportunities file exists for this vertical, so it neither seeded nor vetoed the topic.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Clear Spider — "Inventory Carrying Cost: How to Calculate, Reduce & Optimize" | https://clearspider.net/blog/inventory-carrying-cost | 2026-10-05 | 20% to 30% of inventory value annually — the fully-loaded carrying-cost band (capital + storage + service + risk) | vendor/industry reference |
| 2 | SourceDay — "Inventory Holding Costs: Formula, Examples, and How to Reduce" | https://sourceday.com/blog/inventory-holding-costs | 2026-10-05 | 20% to 30% of total inventory value annually, with a worked example landing at 25% | vendor/industry reference |
| 3 | Federal Reserve Board — H.15 Selected Interest Rates (Daily) | https://www.federalreserve.gov/releases/h15 | 2026-10-05 | 7.00% — bank prime loan rate, the financing leg of carrying cost (only ~1/4 of the all-in rate) | measured |
| 4 | U.S. Census Bureau — Manufacturing and Trade Inventories and Sales, July 2026 | https://www.census.gov/mtis/current/index.html | 2026-10-05 | 1.30 — total US business inventories/sales ratio (July 2026); $2,764.7 billion of business inventories on the books | measured |
| 5 | Cargo Solutions Network — "Air Cargo Spot Rates July 2026: Slowing Growth, No Peak Season" | https://cargosolutionsnetwork.com/insights/air-cargo-spot-rates-july-2026-slowing-growth-no-peak-season | 2026-10-05 | 3.12 per kg — global air-cargo spot rate, July 2026 (up 28% year-on-year); China–W. Europe 4.15/kg | vendor/market |
| 6 | Xeneta — "What the Air Freight Market Looks Like Right Now — and Where It's Heading" | https://www.xeneta.com/blog/what-the-air-freight-market-looks-like-right-now-and-where-its-heading | 2026-10-05 | 3.40 per kg — global air-cargo spot rate May 2026 (+41% year-on-year); Taiwan–US 7.02/kg | vendor/market |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The fully-loaded carrying-cost rate as the model input: 20–30% all-in vs the 7% you borrow at, and the expedited-freight break-even it sets | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| MEIO echelon pooling: how much buffer belongs at the central DC vs each regional node (risk-pooling math) | 8 | 9 | 5 | 8 | 7.5 | dropped — the pooling factor is a textbook formula, not a fetchable primary figure; the only worked example in the corpus is our own field note |
| SKU rationalization: the long tail's true net margin after holding, handling and markdown | 8 | 8 | 5 | 8 | 7.2 | dropped — the −18% net-margin figure and the 2,400-SKU cut exist only in our own field note; no fetchable primary states them |
| Expedited air freight vs regional buffer stock: the plain $/kg break-even | 8 | 7 | 7 | 9 | 7.7 | dropped — a subset of the winner, and the global air-rate figure is a monthly snapshot whose value drifts faster than a year; it belongs as the winner's actionability leg, not the thesis |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=6 hosts=6 decision="sha1:a8cc3ad127" dedup="matched a prior artifact: 2026-10-05_fed-rate-hike-inverts-w" window_days=180 checked_at=2026-10-05T19:33:37+00:00 -->
<!-- evergreen-gate:end -->
