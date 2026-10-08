# Verified Brief: supply_chain — 2026-10-08 (evergreen)

Evergreen track (`skills/evergreen_topics.md`) — no news gate, no freshness window. Every load-bearing
figure below was fetched live this run and matched to the source that states it.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | A (measured index) | EIA publishes the weekly on-highway diesel retail price that carrier surcharges peg to; its most recent published decomposition prices diesel at $5.60/gallon (May 2026) | VERIFIED | https://www.eia.gov/petroleum/gasdiesel/ | "What we pay for in a gallon of: Regular Gasoline May 2026 Retail price: $4.48/gallon Diesel May 2026 Retail price: $5.60/gallon" |
| 2 | A (mechanism + worked example) | A per-mile fuel surcharge is (current diesel − base diesel) ÷ truck MPG; at $4.25 current, a $2.50 base and 6.5 MPG the surcharge is $0.269 per mile, or $322.80 on a 1,200-mile load | VERIFIED | https://www.dashdoc.com/en-us/blog/fuel-surcharge-trucking-complete-guide | "Formula: (Current Diesel Price - Base Diesel Price) ÷ Truck MPG = Fuel Surcharge per Mile … Current EIA diesel price: $4.25 per gallon Base fuel price (agreed upon in contract): $2.50 per gallon Truck averages: 6.5 miles per gallon Calculation: ($4.25 - $2.50) ÷ 6.5 MPG = $0.269 per mile For a 1,200-mile shipment, the fuel surcharge would be: 1,200 miles × $0.269 = $322.80" |
| 3 | A (peg/MPG slope) | The peg and the MPG assumption set the surcharge: at an index of $4.00, a peg of $1.20 and 6 MPG the surcharge is about 47 cents per mile; a lower peg raises the surcharge at every price and a lower MPG makes it more sensitive | VERIFIED | https://thefreightguru.io/fuel-surcharge-trucking-explained | "if the index is 4.00 dollars a gallon, the peg is 1.20 dollars and the schedule assumes 6 miles per gallon, the difference is 2.80 dollars, and 2.80 divided by 6 is about 47 cents per mile" / "A lower peg produces a higher surcharge at every diesel price. A lower miles-per-gallon assumption makes the surcharge more sensitive to each change in price" |
| 4 | B (banded LTL schedule) | Less-than-truckload carriers map diesel bands to a percentage of linehaul — $3.00-$3.09/gallon → 22% surcharge, $3.10-$3.19 → 23% — and the surcharge rate steps up when diesel crosses a threshold | VERIFIED | https://www.freightera.com/freight-shipping-guide/how-diesel-prices-affect-your-freight-rates | "For example: when diesel is $3.00-$3.09/gallon → 22% surcharge; when it hits $3.10-$3.19 → 23%" / "This means the surcharge rate increases when the diesel price hits certain thresholds." |
| 5 | Supporting (fuel share) | Fuel runs 20% to 30% of total operating expenses for most carriers | VERIFIED | https://www.dashdoc.com/en-us/blog/fuel-surcharge-trucking-complete-guide | "with fuel costs representing 20-30% of total operating expenses for most carriers" |
| 6 | Bridge | There is no regulated fuel-surcharge formula: each carrier sets its own baseline, MPG assumption and table, so the same diesel price yields different surcharges across carriers | VERIFIED | (rows 1–4) | Freightera: "The fuel surcharge is not regulated by government agencies; It has no universal formula; Each carrier or logistics provider sets their FSC independently"; Freight Guru: "Because every element is negotiable, two schedules can look similar and behave very differently" |

## Gate notes
- **Source floor: PASS** — 4 distinct sources on 4 distinct hosts (eia.gov, dashdoc.com, thefreightguru.io,
  freightera.com), each fetched live and shown to contain the figure cited. Recorded in the
  `<!-- evergreen-gate: -->` marker of the brief.
- **Vendor vs measured:** row 1 is the measured government index (EIA, a statistical agency). Rows 2–5 are
  industry explainers, not market data: the draft uses their *worked examples* to state the mechanism and
  labels the peg/MPG/base figures as schedule inputs a carrier picks, never as measured market values.
- **REMOVED: 0. FLAGGED: 0.**
- **Editorial arithmetic (analysis, NOT an external fact — the writer's own sum, never cited):** the
  diesel share note that a lower peg raises the surcharge "at every price" follows directly from the
  formula; the draft may present that as its own reading, not as a sourced figure.

## Figure set cleared for drafting (no other number may appear without a source)
$5.60/gallon · $4.48/gallon · $0.269 per mile · $322.80 · 1,200 miles · $4.25 · $2.50 · 6.5 MPG ·
$4.00 · $1.20 · 6 MPG · 47 cents per mile · $3.00-$3.09 → 22% · $3.10-$3.19 → 23% · 20% to 30% of
operating expenses. Editorial arithmetic permitted (label as the writer's own reading): that the peg
and the MPG assumption are the two levers that move the surcharge at a fixed diesel price.
