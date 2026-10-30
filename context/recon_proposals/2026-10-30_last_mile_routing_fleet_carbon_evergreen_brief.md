# Evergreen Brief: last_mile_routing_fleet_carbon — 2026-10-30
**Archetype:** evergreen
**Vertical:** last_mile_routing_fleet_carbon
**Persona:** supply_chain_architect
**Decision the reader is facing:** What a route change is actually worth — whether to buy, renew or re-configure a routing optimizer, and which currency to measure it in: the miles a vendor quotes saved, or the stops and driver-minutes the P&L actually pays for. The decision bites at the annual license renewal, when a vendor pitches a miles-saved return, and whenever a route plan trades distance against time.
**Durability:** The mechanism is standing: a mile is diesel and an hour is wages, so a route's value is two published constants multiplied out. As of the 2024 edition of FHWA Highway Statistics (Table VM-1), a delivery truck averages 7.1928 miles per gasoline gallon equivalent against 18.5 for a light truck/van; as of the 2025 O*NET wage vintage, a light truck driver's median is $21.57 an hour. Only one input moves week to week — the diesel print, as of the week of 10/26/2026 at $6.352 a gallon on the EIA series — and the article states that print with its date and re-runs the exchange rate at the year-ago print ($2.634) so the reader can see the rule hold at both ends rather than bank a snapshot.
**De-dup:** `2026-10-23_your-routes-5x-stop-gap` is this vertical's nearest prior evergreen artifact, and it argues that the stop *set* (50 to 250 stops a route, a 35.8% driver-knowledge effect) is the lever an optimizer cannot reach. This piece takes the router's own inputs as given and prices them: what a mile of diesel costs at the federal vocational mpg, what a driver-minute costs at the O*NET wage, and the exchange rate between the two. Also checked by hand across the corpus and kept distinct: `2026-10-16_your-fleets-charger-gap` (amps and tariff class at the depot wall), `2026-10-09_last-mile-carbon-number-is-a-rate-table` (grams, not dollars — emission factors and boundaries), and the cross-vertical `2026-10-08_fuel-surcharge-peg-mpg-audit` (supply_chain), which prices a *carrier's* surcharge formula and never states what a fleet's own mile costs.
**Thesis:** A last-mile truck mile costs about 79 cents of diesel at the 10/26/2026 print — 2.6 times a light van's mile — which is the same money as 2.2 minutes of a driver's wage, so a route change that adds more than 2.2 minutes to save a mile loses, and an optimizer's return lives in stops per paid hour rather than in the miles a vendor quotes.

**Lead:** The vertical's own second `primary_angles` beat ("dynamic routing software ROI mileage reduction fuel burn drops and stop-density improvements vs saas license fees"), read against `founder-voice.md` §3 pillar 1 ("pays for itself not through hypothetical miles saved, but through measurable stops-per-driver increases and fuel burn reductions"), and grounded on three measured primaries the vertical has never cited: the FHWA vocational fuel-economy table (via AFDC's chart), the EIA weekly on-highway diesel print, and the O*NET light-truck-driver wage. The franchise specific material: the FHWA table prices a *delivery truck* at 7.1928 miles per gasoline gallon equivalent while a *light truck/van* in the same table is 18.5 — a 2.6x spread that no vendor deck uses when it quotes miles saved.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | U.S. Department of Energy, Alternative Fuels Data Center — "Average Fuel Economy by Major Vehicle Category" (source: FHWA, Highway Statistics 2024, Table VM-1) | https://afdc.energy.gov/data/10310 | 2026-10-30 | 7.1928 miles per gasoline gallon equivalent — the delivery truck category's average fuel economy in the federal table | measured |
| 2 | Same source — the light truck/van category in the same table | https://afdc.energy.gov/data/10310 | 2026-10-30 | 18.5 miles per gasoline gallon equivalent — the light truck/van figure a fleet inherits when it budgets fuel from its vans | measured |
| 3 | U.S. Department of Energy, Alternative Fuels Data Center — "Fuel Properties Comparison" | https://afdc.energy.gov/fuels/properties | 2026-10-30 | 1.12 — one gallon of low sulfur diesel equals 1.12 gasoline gallon equivalents, the factor that turns the table's GGE figure into 8.06 miles per diesel gallon | measured |
| 4 | U.S. Energy Information Administration — "Gasoline and Diesel Fuel Update" (diesel release date October 27, 2026) | https://www.eia.gov/petroleum/gasdiesel/ | 2026-10-30 | 6.352 — U.S. on-highway diesel, dollars per gallon, week of 10/26/2026; the same row carries 2.634 a year ago | measured |
| 5 | O*NET OnLine, U.S. Department of Labor — 53-3033.00 Light Truck Drivers | https://onetonline.org/link/summary/53-3033.00 | 2026-10-30 | 21.57 — median hourly wage for light truck drivers, 2025 vintage ($44,860 annual) | measured |
| 6 | U.S. Department of Energy and Environmental Protection Agency — FuelEconomy.gov, "Where the Energy Goes: Gasoline Vehicles" | https://www.fueleconomy.gov/feg/atv.shtml | 2026-10-30 | 12% to 30% — the share of the fuel's energy that reaches the road in a conventional vehicle, with the page's own diagram estimated for stop-and-go city driving under the EPA FTP-75 procedure | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| What a route mile costs and what a driver-minute costs — the exchange rate that decides whether a routing change pays | 9 | 8 | 9 | 9 | 8.4 | **winner** |
| The depot's monthly demand charge (peak kilowatts) beside the energy charge | 9 | 8 | 6 | 8 | 7.7 | dropped — re-argues `2026-10-16_your-fleets-charger-gap`, which already prices the depot wall; refused as a retread of a published article, not for its evidence |
| Dynamic routing's measured operating-cost gain on an unchanged fleet | 8 | 8 | 4 | 8 | 7.0 | dropped — the only source found for the 24.3% / 68.1% → 92.8% figures is a vendor summary page (netzeroinsights.com) whose cited paper could not be located on nature.com, so the load-bearing row is a restatement, not a primary |
| Ton-mile versus per-parcel as the carbon denominator for last-mile | 8 | 9 | 5 | 6 | 7.2 | dropped — no fetchable primary states a per-parcel factor that would not re-argue the 2026-10-09 rate-table piece |
| Electric van payload penalty against a diesel step van | 8 | 8 | 3 | 7 | 6.8 | dropped — manufacturer payload pages did not retrieve; the angle would rest on numbers this desk could not fetch |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=5 hosts=4 decision="sha1:d769dfee29" dedup="matched a prior artifact: 2026-10-23_your-routes-5x-stop-gap" window_days=180 checked_at=2026-10-30T19:05:03+00:00 -->
<!-- evergreen-gate:end -->
