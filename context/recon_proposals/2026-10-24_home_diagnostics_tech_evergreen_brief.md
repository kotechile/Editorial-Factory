# Evergreen Brief: home_diagnostics_tech — 2026-10-24
**Archetype:** evergreen
**Vertical:** home_diagnostics_tech
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether to spend $250–$500 on a smartphone thermal imager to audit his own envelope this winter, or pay a professional for a blower-door test — and specifically whether a camera image can settle "does my house leak" at all.
**Durability:** The load-bearing claims are physics and federal guidance, not market news: the minimum indoor–outdoor temperature difference an IR scan needs (15°–20°F), the 15-minute settle time after the HVAC is switched off, the CFM50 bands that separate a sealed house from a leaky one (under 1,500 vs above 4,000), and EPA's modeled air-sealing savings ladder are all standing rules. Figures as of: PNNL Building America guide last updated 2025-08-05; ENERGY STAR sealing page and its savings methodology as of 2026; EIA electricity price as of the 2025 annual average and household consumption as of 2022; InterNACHI's inspection guidance is undated practitioner practice that has not changed with any product cycle. Instrument prices are the only soft figure and are stated as the PNNL page's own "$250 to $500" band as of 2025, not as a today's-street-price claim.
**De-dup:** `2026-10-19_20-percent-of-your-ac-never-arrives` (home_infrastructure_lifecycle_tco) is the nearest adjacent artifact in the corpus: it argues that a replacement HVAC unit's factory rating is destroyed by the ducts, and its remedy is scope (load calc, airflow, leakage test). This brief is a different object — the *instrument's operating envelope* (temperature difference, settle time, depressurization) plus the one number a camera cannot produce (CFM50) — and it prescribes no HVAC purchase. This vertical has no prior brief or published article of its own; a corpus-wide grep for `thermal imag`, `infrared cam`, `blower door` and `moisture meter` across `published/` and `context/recon_proposals/` returned no article arguing this mechanism (the only hits were a 2026-09-03 supply-chain tariff table and the duct piece above).
**Thesis:** A thermal imager is a condition-dependent pointing device, not a leak detector — it only yields a defensible image when the indoor–outdoor difference is 15°–20°F with the HVAC off for 15 minutes, it cannot tell air leakage from missing insulation without a depressurization test, and the number that actually settles whether the envelope leaks is CFM50, which is why $250–$500 buys localization and a blower-door test buys the verdict.

**Lead:** `primary_angles` #1 of the vertical ("a sub-$300 thermal imager as a DIY energy audit: the delta-T tell for missing insulation in 20 minutes"), sharpened by the persona's `wants` — payback math, gotchas, code/incentive reality — and by the field reality that PNNL's own DIY guide tells a homeowner to depressurize the house with exhaust fans, which is the step that decides whether the streaks in the image mean air or just a cold stud bay.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | InterNACHI, "IR Cameras: Inspecting for Air Leaks" (Gromicko) | https://www.nachi.org/ir-cameras-inspection.htm | 2026-10-24 | 15° to 20°F — "Achieving a 15° to 20º difference in temperature is ideal. The heat or air conditioning should then be turned off, and the inspector should wait at least 15 minutes before commencing with the IR inspection" | measured (association practice standard) |
| 2 | PNNL Building America Solution Center, "Look for Missing Insulation Using Thermal Imaging" | https://basc.pnnl.gov/diy-guides/look-missing-insulation-using-thermal-imaging | 2026-10-24 | $250 to $500 — "Thermal imaging devices that attach to a smartphone are now available to purchase for as low as $250 to $500" | measured (DOE-funded lab guidance; page last updated 2025-08-05) |
| 3 | InterNACHI, "Blower Door Testing" | https://www.nachi.org/blower-door-test.htm | 2026-10-24 | 1,500 CFM at 50 pascals — "Air flow in a well-sealed building will generally be less than 1,500 CFM at 50 pascals. Air flow above 4,000 CFM would be considered leaky" | measured (association practice standard) |
| 4 | ENERGY STAR, "Seal and Insulate with ENERGY STAR" | https://www.energystar.gov/saveathome/seal_insulate | 2026-10-24 | 10% — sealing air leaks "and adding insulation can help your home be more comfortable and energy efficient and provide up to a 10% savings on your annual energy bills" | measured (program claim, modeled) |
| 5 | ENERGY STAR, "Methodology for Estimated Energy Savings" | https://www.energystar.gov/saveathome/seal_insulate/methodology | 2026-10-24 | 11% average — "EPA estimates that homeowners can save an average of 15% on heating and cooling costs (or an average of 11% on total energy costs) by air sealing their homes and adding insulation"; Table 1 runs 16%/18% in CZ 8 down to 5%/7% in CZ 1 | measured (DOE-2 energy model, Beacon Residential) |
| 6 | U.S. EIA, "Use of energy in homes" | https://www.eia.gov/energyexplained/use-of-energy/homes.php | 2026-10-24 | 52% — "more than half—52% in 2020—of a household's annual energy consumption is for just two energy end uses: space heating and air conditioning" | measured |
| 7 | U.S. EIA, "How much electricity does an American home use?" | https://www.eia.gov/tools/faqs/faq.php?id=97&t=3 | 2026-10-24 | 10,791 kilowatthours — "In 2022, the average annual amount of electricity sold to (purchased by) a U.S. residential electric-utility customer was 10,791 kilowatthours" | measured |
| 8 | U.S. EIA, "Prices and factors affecting prices" | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | 2026-10-24 | 17.30¢ per kWh — "The annual average retail electricity prices by major types of utility customers in 2025 were: residential 17.30¢ per kWh" | measured |

## Notes on the rows

- Row 1's cell carries two rules in one sentence (the 15°–20°F band and the 15-minute settle time); the matcher's first token `15` lands inside that sentence, which is why the band and the wait are written together rather than split into two rows that would both evidence on the same clause.
- Rows 4 and 5 are the same program disagreeing with itself: the consumer page says "up to a 10% savings on your annual energy bills" while the methodology behind it models an 11% average on total energy costs and 15% on heating and cooling. The article may not quote both as if they were one number; the modeled 11%/15% ladder is the defensible one and the 10% is the conservative headline. Recompute any dollar figure from the ladder, never from the headline.
- Row 7 + row 8 are the payback denominator and are *electricity only*: 10,791 kWh × $0.1730 = $1,866.84 a year, and 11% of that is ~$205. The 11% is of **total** household energy cost, which includes gas, so the $205 is a floor for an all-electric-adjacent reading, not a full-bill saving — the article must say so in the same sentence or drop the dollar figure.
- Row 2's price is a 2025-dated band from a government guide, not a live retail price; it is the only price anchor that fetches (FLIR, HIKMICRO and Seek Thermal product pages either 404 to the verifier or render nav only).

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The imager's operating envelope (15°–20°F, 15-minute settle) vs the CFM50 number a camera cannot produce | 9 | 9 | 9 | 9 | 9.0 | **winner** |
| Pin vs pinless moisture meters: the dry-to-the-touch lie on drywall, subfloor and framing | 9 | 9 | 6 | 8 | 8.0 | dropped — only one fetchable primary (InterNACHI) carries the 20% threshold; the second host for a pinless-vs-pin accuracy figure (manufacturer or extension page) did not retrieve, so it cannot clear MIN_HOSTS honestly |
| The $80 articulating borescope against a $450 drywall repair | 8 | 8 | 5 | 8 | 7.1 | dropped — no fetchable measured source for either the repair cost or the scope's resolution limit; every price page was a client-rendered listing |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=8 fetched=8 sources=8 hosts=4 decision="sha1:78033fe7df" dedup="matched a prior artifact: 2026-10-19_20-percent-of-your-ac-n" window_days=180 checked_at=2026-10-24T19:32:56+00:00 -->
<!-- evergreen-gate:end -->
