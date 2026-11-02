# Signals: home_infrastructure_lifecycle_tco — 2026-11-02
**Window:** 2026-10-03 → 2026-11-02
**Queries run:** 17 discovery pulls (1 Home & Lifestyle Intel MCP `--recent 30 --vertical home_infrastructure_lifecycle_tco --format signals` returning 10 items, 8 off-axis; 16 date-agnostic web fan-outs across the vertical's four primary angles) + 7 primary-source reads, with a publication-date check on every hit before it entered this table.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | RMI — The Opportunity for Heat Pumps to Put Downward Pressure on Electricity Rates | https://rmi.org/resources/the-opportunity-for-heat-pumps-to-put-downward-pressure-on-electricity-rates | 2026-10-15 | Roughly 109 million US homes (three in four) could heat and cool with heat pumps inside today's winter grid headroom — 86 million more than the 23 million now; an all-electric-only strategy would cut residential rates by 6% on average in summer-peaking states ($6.7 billion a year, $86 per customer), while an all-electric-plus-hybrid mix would cut them 13% ($15.6 billion, $200 per customer) because hybrids lift deployment potential about 65% (Illinois 30% → 100% of homes, on 8.9 GW of winter headroom, split 21% all-electric / 79% hybrid) | Heat-pump rate and sizing economics (directional model, not a forecast) | 92 |
| 2 | J.D. Power — Quarterly Share of Wallet Tracker: U.S. Utilities, October 2026 | https://www.jdpower.com/business/news/quarterly-share-of-wallet-tracker-u-s-utilities-october-2026 | 2026-11-02 | Average monthly residential electric bill $188 in Q3 2026, up 5.6% from $178 a year earlier; gas $119 (up 5.3% from $113), water $102 (down 4.7% from $107); the three utilities total $409 a month, up 2.8% year over year and equal to 5.6% of a median household income of $87,460; 23% of electric customers, 22% of gas and 21% of water customers still owed the utility a balance, against 22%/19%/19% a year earlier | Household utility bill burden and arrears | 86 |
| 3 | AE2S — 2026 Utility Rate Survey Results | https://ae2snexus.com/2026-utility-rate-survey-results | 2026-11-02 | Average 2026 rate increases for water, wastewater and stormwater systems serving 5,000 people or more were 6.8%, 7.1% and 8.3% (2025: 7.5%, 6.6%, 11.7%); 75% of non-metro large systems raised water rates; the average monthly water-plus-wastewater bill at 6,000 gallons rose 10.5% from 2025 and the median rose 9.3% | Water and sewer rate trend (published late October 2026) | 82 |
| 4 | Food & Water Watch — Surging Water Costs amid the US Affordability Crisis | https://www.foodandwaterwatch.org/research/2026/10/06/surging-water-costs-amid-the-us-affordability-crisis | 2026-10-06 | Across the 500 largest community water systems (155 million people, 45% of the US), the average household drinking-water bill was $531 in 2025 for 60,000 gallons, up 62% from 2015 — 1.6 times the inflation rate and more than twice the grocery rate; the cheapest system charged $133 and the dearest $1,416; bills were unaffordable for low-income households in 93% of systems; for-profit systems averaged $823 against $494 for public ones | Water bill compounding and affordability | 78 |
| 5 | ACHR News — HVAC Price Increase List: October 2026 | https://www.achrnews.com/articles/166764-hvac-price-increase-list-october-2026 | 2026-10-07 | Manufacturer price increases effective 2026-10-01: Heat Controller water-source heat pumps and residential geothermal products up to 5%, Regal Rexnord select motors and parts 2.5%, Western Enterprises 3%, with several lines carrying item-by-item increases | Equipment price drift during the refrigerant transition | 62 |

**Dating note:** rows 2 and 3 carry the observation date (2026-11-02) because both are live pages whose underlying releases are datable only by month: J.D. Power's tracker is the Q3 2026 wave published in October 2026, and the AE2S survey results page was published in late October 2026 (search index dates it six days before this sweep). Their claim cells state the release period, not an event date. Rows 1, 4 and 5 are event-dated by their publishers.

**Off-axis dropped (not carried):** the Home & Lifestyle Intel pull returned ten items, of which eight were interior-design posts, subscription offers and mortgage-rate notes the `home_equity_tco` run already carries; the two on-axis items (Boise's geothermal network for 300 affordable homes, 2026-11-02; Meta's low-carbon cement purchase, 2026-10-30) are municipal and industrial stories with no household allocation decision in them, and the geothermal item was already scored 6.9 by today's `home_equity_tco` brief.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=5 candidates=0 heuristic=- window=2026-10-03..2026-11-02 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Dated background

- EIA, 2026–27 Winter Fuels Outlook press release, 2026-10-06 — https://www.eia.gov/pressroom/releases/press593.php — heating oil $2,115 for the season (+21%), natural gas −9%, propane −3%, electricity +4% to $1,196; 3,150 heating degree days, 3% below the 10-year average. **Already Anchor A of the 2026-10-12 `home_equity_tco` winner `cheapest-fuel-priciest-pipe`; corroboration only, never an anchor here.**
- EIA, Winter Fuels Outlook page (same release) — https://www.eia.gov/outlooks/steo/report/winterfuels.php
- JCHS, Remodeling Spending Continues to Stagnate (LIRA), 2026-10-22 — https://www.jchs.harvard.edu/blog/remodeling-spending-continues-stagnate — already the Anchor A of this vertical's 2026-10-26 winner.
- EPA, Frequent Questions on the Phasedown of Hydrofluorocarbons — https://www.epa.gov/hfcs/frequent-questions-phasedown-hydrofluorocarbons — servicing of existing R-410A systems continues; from 2026 a whole new system must use a lower-GWP refrigerant; reclaimed HFC sold from 2026 may contain no more than 15% virgin HFC by weight.
- EPA final rule allowing installation of pre-2025 R-410A equipment until supplies deplete (NAHB summary, May 2026) — https://www.nahb.org/blog/2026/05/epa-hvac-refrigerants-r-410a-final-rule
