# Evergreen Brief: home_equity_tco — 2026-11-23
**Archetype:** evergreen
**Vertical:** home_equity_tco
**Persona:** pro_homeowner
**Decision the reader is facing:** A contractor hands over a heat-pump quote priced to exactly the federal minimum efficiency — the reader must decide whether paying the legal floor is a real economy or the worst system he can legally buy before the $2,000 credit window closes, when the system is sized and ducts are quoted this winter.

**Durability:** The efficiency floor is statute, not a market price: 10 CFR 430.32 fixes the split-system heat-pump minimum at 14.3 SEER2 / 7.5 HSPF2 for units manufactured on or after January 1, 2023, and no rulemaking since has moved it, so the floor is stable as of the 2026 edition of the CFR. The $2,000 federal 25C credit runs by statute through products installed between January 1, 2023 and December 31, 2032 — still seven years of window as of November 2026. The electricity anchor is EIA's measured 2025 class table (17.30¢ residential, as of 2025), and the duct-leakage loss band (15–20% of space-conditioning energy) is a measured study reading carried by InterNACHI's standing inspection article, independent of season. Every load-bearing figure is a statutory constant or a dated measured value, so the arithmetic holds in 12 months.

**De-dup:** `2026-11-09_your-pmi-ends-at-78-not-todays-value` is this vertical's nearest prior evergreen artifact (also cross-checked and dropped `published/2026-11-02_your-heat-pump-cuts-everyone-13` and `published/2026-11-23_your-fuel-decided-your-winter-bill`, both other verticals — the first argues grid rate cuts shared system-wide, the second argues fuel choice setting the winter bill; neither touches the statutory minimum-efficiency floor, duct losses or the 25C credit window). This thesis prices the efficiency floor itself, which no artifact in the corpus has done.

**Thesis:** A heat-pump quote priced to exactly the federal floor (7.5 HSPF2) is the worst system you can legally buy, and the real efficiency decision is arithmetic — every step above the floor cuts heating electricity in proportion to 1/HSPF2 — while a duct run that leaks 15–20% of space-conditioning energy can eat the entire premium the quote charges for the better machine, and the $2,000 credit window (through December 31, 2032) pays down only the machine, never the ducts.

**Lead:** From the vertical's own `primary_angles` in `context/verticals.json` (angle 3, "heat pump seasonal COP curves and tariff shocks", with the COP half previously dropped by this desk on 2026-10-26 at 7.3 because no fetchable page states a temperature-specific COP — this candidate keeps the tariff/economics half and anchors on the statutory floor instead) and the persona's `wants` in `context/personas.json` (`pro_homeowner`: "TCO depreciation math … zero fluff"). The founder's standing claim in `context/growth_os/founder-voice.md` §3 that a household's real cost is the bill it keeps paying, not the price it was quoted, is exactly the floor-versus-premium question. Cross-checks: `scripts/home_lifestyle_intel_client.py --search "heat pump COP seasonal"` returned no tariff or efficiency-floor material (housing macro and design feeds only); `scripts/gsc_analyzer.py --vertical home_equity_tco` returned 0 high-potential opportunities — bonus signal only on a young site, never a veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | eCFR, 10 CFR 430.32 — Energy and conservation standards for consumer products | https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32 | 2026-11-23 | 14.3 SEER2 / 7.5 HSPF2 — the split-system heat pump floor for units manufactured on or after January 1, 2023 (13.4 SEER2 for single-package) | measured |
| 2 | ENERGY STAR — Air-Source Heat Pumps | https://www.energystar.gov/products/air_source_heat_pumps | 2026-11-23 | Up to $2,000 — federal tax credit for ENERGY STAR heat pumps, products purchased and installed between January 1, 2023 and December 31, 2032 | measured |
| 3 | EIA — Electricity prices and factors affecting prices | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | 2026-11-23 | 17.30¢ per kWh — measured 2025 residential average retail electricity price (13.41¢ commercial) | measured |
| 4 | EIA — Use of energy in homes | https://www.eia.gov/energyexplained/use-of-energy/homes.php | 2026-11-23 | 52% in 2020 — of household annual energy consumption is space heating plus water heating | measured |
| 5 | InterNACHI — HVAC inspection article | https://nachi.org/hvac.htm | 2026-11-23 | 20% on average — duct leakage increases space-conditioning energy use by 15-20%, even in new construction | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The federal floor heat pump: what a minimum-efficiency quote really costs | 9 | 9 | 9 | 8 | 8.7 | **winner** |
| Temperature-specific COP curve arbitrage for cold-climate heat pumps | 8 | 7 | 4 | 7 | 6.6 | dropped — no fetchable page states a temperature-specific COP (desk finding, 2026-10-26) |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=5 hosts=4 decision="sha1:b3a062e3ed" dedup="matched a prior artifact: 2026-11-09_your-pmi-ends-at-78-not" window_days=180 checked_at=2026-11-23T18:38:33+00:00 -->
<!-- evergreen-gate:end -->
