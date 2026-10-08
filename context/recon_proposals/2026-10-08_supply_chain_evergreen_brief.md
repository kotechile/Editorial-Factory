# Evergreen Brief: supply_chain — 2026-10-08
**Archetype:** evergreen
**Vertical:** supply_chain
**Persona:** ops_leader
**Decision the reader is facing:** Whether to accept the carrier's fuel-surcharge schedule as written at the next contract renewal, or renegotiate the peg, the miles-per-gallon assumption and the banding — and whether to audit the FSC line on every freight invoice against the DOE index before it is paid.
**Durability:** The mechanics do not change from year to year: a per-mile schedule is (index − peg) ÷ MPG, an LTL schedule is a diesel-banded percentage of linehaul, and the index is the same DOE/EIA weekly on-highway series — so the rule and the negotiation levers stay true for years. The one moving part is the diesel level itself, which is quoted as of EIA's weekly on-highway release (release date 6 October 2026; next release 14 October 2026) and re-published every Monday, so the article states its diesel anchor with that date rather than pretending a price is permanent.
**De-dup:** Nearest prior artifacts in the last 180 days are 2026-10-08_supply_chain_verified_brief.md (the news-track brief) and published/2026-10-08_freight-scale-bet-vs-contract-duration.md — both are about how carriers and brokers price or reprice committed capacity when the freight market will not commit; neither touches the fuel-surcharge formula, the peg/MPG negotiation, or FSC invoice audit. This topic is the durable cost-audit counterpart, not a re-argument of that news thesis.
**Thesis:** The diesel price is not your fuel-surcharge problem — the peg, the miles-per-gallon assumption and the banding are, they are set by a carrier's schedule rather than by any regulation, and they are negotiable.

**Lead:** The intel feed's own material. The 7 Oct 2026 Supply Chain Now episode *"Pressure-Test Your Shipping Decisions Before They Cost You Thousands"* (retrieved via `scripts/supply_chain_intel_client.py`) names "invoice variance / hidden surcharges" and carrier-mix/surcharge as the core cost-per-package KPIs a shipper must pressure-test, and warns that "average shipments hide losses" because the tail is where the money is. That is the same beat as the vertical's `primary_angles` ("dynamic freight routing and LTL consolidation"; "agentic exception handling and demurrage dispute pipelines") and `founder-voice.md` §3 supply_chain ("Agentic Logistics Automation … auto-disputing invalid carrier detention invoices"). The fuel surcharge is the largest variable line on a carrier invoice and, uniquely, one whose rules are fixed by a formula almost no shipper re-reads after signature.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | U.S. Energy Information Administration — Gasoline and Diesel Fuel Update | https://www.eia.gov/petroleum/gasdiesel/ | 2026-10-08 | $5.60/gallon — EIA's published on-highway diesel retail price in its most recent monthly decomposition (May 2026); the same series is re-released weekly, every Monday | measured |
| 2 | Dashdoc — What is a Fuel Surcharge in Trucking? Complete Guide | https://www.dashdoc.com/en-us/blog/fuel-surcharge-trucking-complete-guide | 2026-10-08 | $0.269 per mile — worked full-truckload example: ($4.25 current − $2.50 base) ÷ 6.5 MPG, which on a 1,200-mile load is $322.80 | measured (formula, cites EIA) |
| 3 | The Freight Guru — Fuel Surcharges in Trucking Explained | https://thefreightguru.io/fuel-surcharge-trucking-explained | 2026-10-08 | 47 cents per mile — worked example: (index $4.00 − peg $1.20) ÷ 6 MPG, showing the peg and the MPG assumption set the slope | illustrative |
| 4 | Freightera — How Diesel Prices Affect Your Freight Rates | https://www.freightera.com/freight-shipping-guide/how-diesel-prices-affect-your-freight-rates | 2026-10-08 | $3.00-$3.09 — one diesel band mapped to a 22% LTL surcharge (23% at $3.10-$3.19), showing banded schedules price the same fuel differently | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The fuel-surcharge peg/MPG/banding audit (this brief) | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Diesel-band indexation clause for LTL contracts | 8 | 8 | 7 | 8 | 7.8 | dropped — same mechanics, narrower scope; folded into the winner |
| AMR vs rigid AS/RS capex trade-off | 7 | 8 | 6 | 7 | 7.0 | dropped — re-argues `warehouse_automation_robotics_capex` published articles |
| Multi-echelon inventory (MEIO) working-capital release | 8 | 9 | 7 | 7 | 7.9 | dropped — duplicates `meio_working_capital_tco` coverage |
| 3-layer ERP/WMS/TMS decoupling stack | 9 | 9 | 5 | 6 | 7.6 | dropped — no measured primary anchor retrieves for the cost claims |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=4 decision="sha1:ea4879ebf2" dedup="matched a prior artifact: 2026-10-08_supply_chain_verified_b" window_days=180 checked_at=2026-10-08T18:38:17+00:00 -->
<!-- evergreen-gate:end -->
