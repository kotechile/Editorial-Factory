# Evergreen Brief: supplier_risk_reshoring_decision — 2026-10-03
**Archetype:** evergreen
**Vertical:** supplier_risk_reshoring_decision
**Persona:** ops_leader
**Decision the reader is facing:** Whether to keep sourcing a product from China or shift production to Mexico/nearshore, and how to model that call honestly — on total landed cost (freight, duty, customs, inland and carrying cost), not the ex-works sticker price.
**Durability:** The load-bearing facts are structural, not news, and each carries an as-of date: China's fully-loaded manufacturing wage ($6.69/hr, NBS 2024 data) now exceeds Mexico's entry-level operator ($5.56/hr, Q1 2026 payroll), and the stacked US tariff on Chinese goods (17.5–35%, as of April 2026) versus 0% under USMCA for Mexico is a structural gap that does not expire inside 90 days. The TLC framework itself never expires; only the wage and tariff numbers are time-bound, and both are dated so a reader can re-check them in 12 months.
**De-dup:** 2026-09-26_reshoring-moved-the-tariff-upstream and 2026-10-03_tariff-split-reshoring-heavy-half (this vertical's two prior articles, both acute tariff-event news) — this is the durable total-landed-cost decision framework for the same persona, a distinct evergreen beat, and no evergreen brief exists for this vertical yet.
**Thesis:** The China-vs-Mexico sourcing call is decided by total landed cost, not ex-works price — China's cheaper sticker price evaporates once you stack its fully-loaded labor ($6.69/hr vs $5.56/hr), a 17.5–35% tariff stack, and ocean freight, leaving an illustrative product that lands ~19% cheaper from Mexico despite a higher factory price.

**Lead:** From the vertical's own `primary_angles` (angle 2: "total landed cost tlc calculator factoring tariffs customs delays currency risk quality audit travel and ocean freight volatility"), `context/growth_os/founder-voice.md` §3 ("Total Landed Cost (TLC) Transparency" — ocean freight volatility, port demurrage, quality-audit flights and customs duties add 25–40% to base costs) and `context/growth_os/customer-truth.md` Anecdote 1 (a Southeast-Asia casting quoted at $18/unit that landed at $24.80 once freight, demurrage and audit travel were counted, versus $21.50 nearshored to Monterrey with 4-day transit). GSC striking-distance is a bonus signal only (thin on a young site) and offered no meaningful query, so the topic is sourced from the vertical's durable beat, not an invented idea.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Tetakawi — "Manufacturing Wages: Mexico vs. China" (updated Sep 20, 2026; China NBS 2024 + Q1 2026 payroll) | https://tetakawi.com/blog/manufacturing-wages-mexico-vs-china | 2026-10-03 | China's average manufacturing worker costs $6.69/hr fully loaded vs Mexico's $5.56/hr entry-level operator; a 17.5–35% stacked tariff on Chinese goods vs 0% under USMCA | measured |
| 2 | American Industries Group — "Why Now Is the Time to Move Your Manufacturing from China to Mexico" (Apr 6, 2026) | https://hub.americanindustriesgroup.com/insights/time-move-manufacturing-china-mexico | 2026-10-03 | Mexico's $4.90/hr manufacturing wage undercuts China's $6.50/hr by 25%; the full tariff + logistics + labor stack yields ~36% lower unit costs in Mexico | vendor claim |
| 3 | Importivity — "Mexico vs China Manufacturing Comparison" (2026) | https://importivity.com/comparisons/mexico-vs-china | 2026-10-03 | Worked landed-cost example: China lands at $136 vs Mexico $110 (~19% lower) on an illustrative tariff-exposed unit; China's effective US tariff 29.5–33% vs Mexico 0% | vendor claim |
| 4 | Kearney 2026 Reshoring Index (PR Newswire, Apr 29, 2026) | https://www.prnewswire.com/news-releases/kearneys-2026-reshoring-index-remains-in-negative-territory-302756474.html | 2026-10-03 | Reshoring Index still negative (−115 → −91) and US manufactured-goods imports rose 4.6% — the contrarian counterweight that the sourcing call is not obvious | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Total landed cost (TLC) calculator: China vs Mexico sourcing decision | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| Dual-sourcing overhead vs risk (split POs, lost tier pricing) | 8 | 8 | 6 | 8 | 7.5 | dropped — the load-bearing discount-loss figure is the founder's own estimate (5–10%), with no fetchable measured primary |
| Disruption resilience matrix (45-day survival curve) | 8 | 8 | 5 | 7 | 7.1 | dropped — survival-curve figures are customer-truth anecdotes, not fetchable primaries |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=4 decision="sha1:5ec44b7a92" dedup="matched a prior artifact: 2026-09-26_reshoring-moved-the-tar" window_days=180 checked_at=2026-10-03T18:05:27+00:00 -->
<!-- evergreen-gate:end -->
