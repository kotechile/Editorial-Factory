# Signals: home_infrastructure_lifecycle_tco — 2026-11-23
**Window:** 2026-10-24 → 2026-11-23
**Queries run:** 9 (3 vertical angles × fan-out + Home Lifestyle Intel MCP sweep, 10 candidates, 4 in-window kept)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | HVACR manufacturers announce a new November 2026 price-increase round, 3%–15% where disclosed | https://www.achrnews.com/articles/166947-hvac-price-increase-list-november-2026 | 2026-11-07 | Duro Dyne 4–15% (Nov 1); Aire Technologies 8%; Southwark 8%; MMF 8% metal/8.5% aluminum; IBC Tankless Heaters 5%; Gastite 6% (Nov 23) — replacement-path components repricing inside one month | Smart home and HVAC transition TCO break-even timelines | 88 |
| 2 | Federal producer-price data: HVAC equipment up ~60% since 2019 vs +31% CPI (+22% real); August 2026 is the highest reading in the series back to 2019; 25C credit expired for anything placed in service after 2025-12-31 | https://thehvacbrief.com/hvac-prices-2026 | 2026-11-01 | +60% nominal / +22% real equipment cost vs 2019; prices rose in 21 of 31 month-over-month comparisons since Jan 2024; losing 25C adds up to $2,000 out-of-pocket on a qualifying heat pump installed from Jan 1, 2026 | Smart home and HVAC transition TCO break-even timelines | 92 |
| 3 | NAHB/Wells Fargo Housing Market Index falls to 25, down 4 points, lowest since April 2012 | https://www.mortgagenewsdaily.com/news/11202026-builder-confidence-nahb-hmi | 2026-11-20 | HMI 25: affordability pressure at a 14-year low in builder confidence | The 10-year home capex roadmap | 76 |
| 4 | Pending home sales hit a second consecutive record low, −4.7% MoM | https://www.mortgagenewsdaily.com/news/11202026-pending-home-sales | 2026-11-20 | October Pending Home Sales Index −4.7% MoM, second consecutive record low — the "move up or out" exit is closing, so owners stay and live with their assets longer | The 10-year home capex roadmap | 80 |
| 5 | Modelled 24/7 clean power for data centers via industrial heat batteries at $120/MWh | https://www.canarymedia.com/articles/batteries/24-7-clean-power-giant-heat-batteries | 2026-11-23 | $120/MWh hybrid thermal power cost including dedicated solar/wind — thermal-battery economics reach the grid edge, the same physics homeowners buy as heat-pump-plus-thermal-storage | Solar and backup battery payback models | 68 |
| 6 | New winter electric rates for Massachusetts heat-pump owners saved $37M across 140,000+ households | https://www.canarymedia.com/articles/heat-pumps/winter-rates-massachusetts-heat-pump-owners | 2026-03-31 (published spring 2026; OUT OF WINDOW — background only) | $37M seasonal savings, >$250 average per household, Nov 1–Mar 31 rate window | Solar and backup battery payback models | 55 |
| 7 | NEADA's November 2026 Winter Heating Forecast (released 2026-11-10) prices the season by fuel: oil households $2,977 (+70.2% from $1,749), electric $1,215 (+6.0%), propane $1,350 (+5.0%), natural gas flat at $686 (0.0%) | https://neada.org/neada-projects-home-heating-costs-will-rise-7-1-this-winter-with-heating-oil-costs-up-70 | 2026-11-10 | All-fuels average $1,002 (+7.1%, +$66); Northeast +$221/+16.9% to $1,532; EIA week ending 2026-11-02 residential heating oil $6.14/gal, −1.5% w/w but ~69% above a year earlier; since winter 2021–22 oil +110.1% and electricity +32.1%; 1 in 6 households behind on utility payments, $23bn arrears | Solar and backup battery payback models | 92 |

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=2 heuristic=0.77-0.80 window=2026-10-24..2026-11-23 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #2 ⨂ #7 | electrification_subsidies_x_utility_rates | A: Smart home and HVAC transition TCO break-even timelines | B: Solar and backup battery payback models | https://thehvacbrief.com/hvac-prices-2026 https://neada.org/neada-projects-home-heating-costs-will-rise-7-1-this-winter-with-heating-oil-costs-up-70 | 0.8 | - |
| 2 | #2 ⨂ #5 | electrification_subsidies_x_utility_rates | A: Smart home and HVAC transition TCO break-even timelines | B: Solar and backup battery payback models | https://thehvacbrief.com/hvac-prices-2026 https://www.canarymedia.com/articles/batteries/24-7-clean-power-giant-heat-batteries | 0.77 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=0.5 intensity=0.92 angle_fit=1.0 contrast=1.0 → 0.8 (electrification_subsidies_x_utility_rates)
- #2: token_coverage=0.5 intensity=0.8 angle_fit=1.0 contrast=1.0 → 0.77 (electrification_subsidies_x_utility_rates)
<!-- synthesis-seed:end -->

## Dated background
- ACHR News price-increase list is a trade-press roundup of manufacturer bulletins; the fact_check gate must confirm per-manufacturer figures on the same page before any headline cites a percentage.
- The 25C expiry and the EPA removal of the R-410A installation deadline are statutory/regulatory facts dated 2025-12-31 and 2025; they are load-bearing context, not 30-day signals, and belong in the brief's background block.
- Tariff relief on residential HVAC (25% → 15%, June 8, 2026, expires Dec 31, 2027) predates the window; background only.
