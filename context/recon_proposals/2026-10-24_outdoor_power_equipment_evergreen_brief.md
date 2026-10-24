# Evergreen Brief: outdoor_power_equipment — 2026-10-24
**Archetype:** evergreen
**Vertical:** outdoor_power_equipment
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether to buy a heated mat, a cordless shovel or a battery two-stage blower for this winter's driveway and walk — and how many square feet of melting the property can actually justify — a decision made before the first storm, because the capital cost and the electrical circuit are both fixed at the point of purchase.
**Durability:** The physics and the device ratings do not drift — 35 watts per square foot of HeatTrak mat (5.8 amps at 120 volts over 20 square feet), a stated melt ceiling of up to 2 inches per hour, 13 amps per GFCI power unit, 0.84 kWh in a pair of 7.5 Ah 56 V packs, and 50 W/sq ft as the embedded-system design density — all as of October 2026 and true for the life of the hardware. The durable article carries two clocks: list prices as of 2026-10-24 (HeatTrak walkway mat $229.99, driveway mat $1,075) and the electricity rate as of EIA's 2025 annual average (17.30¢ per kWh residential), so a reader in 2027 can re-price the same arithmetic instead of trusting a stale total.
**De-dup:** `2026-10-24_your-1-acre-mowers-04-acre-trap` is the nearest prior artifact in the desk corpus — yesterday's yard_robotics evergreen, which made the rated-number-versus-usable-number argument about a machine's headline spec. This piece is a different subject and a different mechanism: it prices snow removal per square foot and per inch against electrical load and capital cost, and it does not argue about acreage, robots or mowing capacity. This vertical has no prior brief and no published article of any kind in the 180-day window, and a corpus grep for "snow blower", "heated driveway", "snow mat" and "power shovel" over `published/` returns nothing.
**Thesis:** Melting snow is 35 to 50 watts per square foot of continuous load while moving it is one 14.5-cent battery charge, so a heated mat is only defensible where bare pavement over a small area is the actual requirement — the electricity is never the deciding number; the dollars per square foot and the circuit are.

**Lead:** The vertical's own beats in `context/verticals.json` `primary_angles` #1 ("two-stage battery snow blower versus power shovel versus heated driveway mat: cost per inch cleared") read against #6 (cold-weather failure modes) and the persona's `wants` in `context/personas.json` — "payback math, gotchas, code/incentive reality". The specific material is the load arithmetic the vendors publish but do not put side by side: EGO's per-charge capacity claim, HeatTrak's nameplate amps and melt rate, and WarmlyYours' watts-per-square-foot design density, priced against the EIA's 2025 residential rate. The intel feed carried nothing on this beat (`home_lifestyle_intel_client.search_local` returns home-decor and grid-battery noise for snow queries) and `gsc_analyzer.py --vertical outdoor_power_equipment` returned 0 opportunities, so neither is the lead — bonus signal only, as the SOP requires.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | EGO POWER+ 24 in. Self-Propelled 2-Stage Snow Blower SNT2400 product page | https://www.egopowerplus.com/two-stage-snow-blower-snt2400 | 2026-10-24 | 8 inches — Clears up to an 18-car driveway with 8 inches of snow on a single charge when used with the two recommended 7.5Ah ARC Lithium batteries | vendor claim |
| 2 | EGO POWER+ SNT2400 product page (platform and throw) | https://www.egopowerplus.com/two-stage-snow-blower-snt2400 | 2026-10-24 | 56-Volt — this cordless electric snow blower combines the power of any two EGO 56V ARC Lithium batteries and throws snow up to 50 feet | vendor claim |
| 3 | HeatTrak Heated Snow & Ice Melting Driveway Mat product page | https://www.heattrak.com/products/heated-snow-ice-melting-driveway-mat | 2026-10-24 | 5.8-amps — 24 x 10 ft 120V driveway mats are 5.8 amps each | vendor claim |
| 4 | HeatTrak Heated Snow & Ice Melting Driveway Mat product page (larger size) | https://www.heattrak.com/products/heated-snow-ice-melting-driveway-mat | 2026-10-24 | 11.7-amps — 24 x 20 ft 120V driveway mats are 11.7 amps each | vendor claim |
| 5 | HeatTrak home page (list prices) | https://www.heattrak.com/ | 2026-10-24 | $ 229.99 USD — Heated Snow Melting Walkway Mat 20x60 sale price | vendor claim |
| 6 | HeatTrak FAQs (cost to run) | https://www.heattrak.com/pages/faqs | 2026-10-24 | $0.18 per hour — The average cost to operate a HeatTrak system is only about $0.18 per hour | vendor claim |
| 7 | HeatTrak FAQs (melt rate) | https://www.heattrak.com/pages/faqs | 2026-10-24 | 2 inches per hour — melts existing snow and ice and helps prevent new accumulation at a rate of up to 2 inches per hour | vendor claim |
| 8 | HeatTrak FAQs (circuit cap) | https://www.heattrak.com/pages/faqs | 2026-10-24 | 13 amps — no more than 13 amps should be on a single plug, and one GFCI power unit connects up to 13 amps | vendor claim |
| 9 | HeatTrak FAQs (service life) | https://www.heattrak.com/pages/faqs | 2026-10-24 | 5-6 years — On average, HeatTrak mats have a lifespan of 5-6 years | vendor claim |
| 10 | WarmlyYours snow melting systems guide (design density) | https://www.warmlyyours.com/en-US/snow-melting | 2026-10-24 | 1.00 per energized hour — at 50 W/sq ft, every 100 sq ft draws 5 kW, or $1.00 per energized hour at an illustrative $0.20/kWh | vendor claim |
| 11 | WarmlyYours snow melting systems guide (400 sq ft worked example) | https://www.warmlyyours.com/en-US/snow-melting | 2026-10-24 | 24.00 for six energized hours — a 400 sq ft full-coverage driveway draws 20 kW, $4.00 per energized hour | vendor claim |
| 12 | WarmlyYours snow melting systems guide (driveway sizing) | https://www.warmlyyours.com/en-US/snow-melting | 2026-10-24 | 400-800 sq ft — Typical driveways | vendor claim |
| 13 | U.S. Energy Information Administration, Electricity explained: prices and factors affecting prices | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | 2026-10-24 | 17.30 cents — the annual average retail price of electricity for residential customers in 2025 was 17.30¢ per kWh | measured |
| 14 | Snow Joe electric snow shovel listing (11-inch, 10 amp, price) | https://snowjoe.com/collections/snow-blowers | 2026-10-24 | 11-Inch — Snow Joe Electric Snow Shovel, 11-Inch, 10 Amp Motor, Headlights | vendor claim |
| 15 | Snow Joe electric snow shovel listing (price) | https://snowjoe.com/collections/snow-blowers | 2026-10-24 | 124.99 — Snow Joe Electric Snow Shovel regular price $124.99 | vendor claim |

## Derived arithmetic (computed here, stated in the article as derived)

| Figure | Basis | Value |
|---|---|---|
| Energy in one blower charge | 2 × 56 V × 7.5 Ah (rows 1–2) | 840 Wh = 0.84 kWh |
| Cost of one blower charge | 0.84 kWh × 17.30¢ (rows 1, 13) | 14.5¢ |
| HeatTrak mat power density | 5.8 A × 120 V ÷ 20 sq ft (row 3) | 696 W ≈ 34.8 W/sq ft |
| HeatTrak 24×20 mat density (cross-check) | 11.7 A × 120 V ÷ 40 sq ft (row 4) | 1,404 W ≈ 35.1 W/sq ft |
| Driveway mat capital per square foot | $1,075 ÷ 20 sq ft (row 3 + page price) | $53.75/sq ft |
| Walkway mat capital per square foot | $229.99 ÷ 8.33 sq ft (row 5) | $27.60/sq ft |
| 400 sq ft of portable mat | 400 ÷ 20 = 20 mats × $1,075 | $21,500 |
| Melt energy per sq ft per inch | 34.8 W × 0.5 h (row 7 melt ceiling) | 17.4 Wh/sq ft-in ≈ $0.0030 at 17.30¢ |
| One blower charge as melt | 840 Wh ÷ 17.4 Wh/sq ft-in | ≈ 48 sq ft of 1-inch snow (≈ 6 sq ft at 8 inches) |
| Mat square feet per 120 V plug | 13 A × 120 V ÷ 34.8 W/sq ft (row 8) | 1,560 W ≈ 45 sq ft |
| 200 sq ft of mat, six energized hours | 200 × 34.8 W × 6 h × 17.30¢ | 41.8 kWh ≈ $7.23 |
| Mat storm cost vs blower charge | $7.23 ÷ 14.5¢ | ≈ 50× |
| Embedded 400 sq ft system draw | 400 × 50 W (rows 10–11) | 20 kW ≈ 83 A at 240 V |
| HeatTrak's "$0.18/hour" implied area | 0.18 ÷ 0.1730 = 1.04 kW ÷ 34.8 W/sq ft | ≈ 30 sq ft — a walkway set, not a driveway |

## Notes / hand-checked claims that cannot carry a gate row

- **Driveway mat list price, $1,075 for 20 sq ft** (https://www.heattrak.com/products/heated-snow-ice-melting-driveway-mat, read 2026-10-24): the page prints "Heated Snow & Ice Melting Driveway Mat Sale price $ 1,075.00 USD". Every phrasing of that cell that leads on the price matches the phone number in the page header first, so the row would record coincidental evidence; the price is carried in prose under rows 3–4, whose URL is the same page and is in `## Sources`.
- **Embedded install cost, "$10 and $25 per square foot, including materials and labor"** (https://www.warmlyyours.com/en-US/snow-melting, read 2026-10-24): present on the page and carried in prose under rows 10–12, but a cell leading on `$10` or `$25` matches the page's navigation ("10+ bars", "25 people found this helpful"), so it is not a gate row.
- **HeatTrak positions the driveway mat as a tire track, not full coverage** — its FAQ says the mats "lay as a track for one tire". The $21,500 figure is therefore arithmetic on the portable-mat list price, labelled as such, never as HeatTrak's recommendation for a 400 sq ft pour.
- WarmlyYours' "$0.20/kWh" is an illustrative rate on the vendor's own page; every dollar figure in the article is recomputed at the EIA 2025 average (17.30¢) and the vendor's illustrative rate is quoted only where the vendor's own worked example is being reproduced.

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Heated mat vs battery two-stage blower vs cordless shovel: dollars per square foot, watts per square foot, and the inch-cleared cost of each | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| The battery platform trap: true five-tool cost across EGO, Greenworks, DeWalt FlexVolt and Ryobi | 9 | 7 | 5 | 8 | 7.4 | dropped — the four platforms' battery and bare-tool prices are the whole thesis and no fetchable primary page carries them (EGO's own configuration table reads "Coming Soon" with no prices) |
| What actually stops a battery blower at -10C: pack temperature limits, voltage sag and charge lockouts | 8 | 9 | 6 | 7 | 7.6 | dropped — no measured low-temperature discharge curve on a host the verifier can fetch; every number would have had to come from a vendor FAQ |
| Buy-window timing: end-of-season markdown versus paying peak for the storm you are not ready for | 8 | 4 | 7 | 8 | 6.8 | dropped — a price-calendar piece expires inside 90 days, which routes it to the news track by the SOP's own rule |
| Electric zero-turn acre-per-charge and the pack replacement cliff | 8 | 7 | 5 | 7 | 6.9 | dropped — the acreage figures verify, the replacement-pack prices do not exist on any fetchable page |
| Pressure washers where PSI sells and GPM cleans | 7 | 9 | 6 | 7 | 7.3 | dropped — a cleaning-performance piece with no invoice in it; the persona's decision is a purchase, and the numbers that decide a purchase (GPM, nozzle orifice, pump life) are not published as text |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=15 fetched=15 sources=7 hosts=5 decision="sha1:a6834639e6" dedup="matched a prior artifact: 2026-10-24_your-1-acre-mowers-04-a" window_days=180 checked_at=2026-10-24T19:05:05+00:00 -->
<!-- evergreen-gate:end -->
