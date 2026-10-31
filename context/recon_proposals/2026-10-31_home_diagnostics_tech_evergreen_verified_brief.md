# Verified Brief: home_diagnostics_tech — 2026-10-31 (evergreen)

Gate: `python3 scripts/evergreen_gate.py --brief context/recon_proposals/2026-10-31_home_diagnostics_tech_evergreen_brief.md` → **PASS** (rows=10, fetched=10, sources=7 distinct URLs, hosts=4, checker run 2026-10-31T19:34:11Z).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | radon risk | About 21,000 radon lung-cancer deaths a year in the U.S., about 2,900 among people who never smoked | VERIFIED | https://www.epa.gov/radon/health-risk-radon | "Radon is responsible for about 21,000 lung cancer deaths every year. About 2,900 of these deaths occur among people who have never smoked." (same page gives the uncertainty range "8,000 to 45,000") |
| 2 | risk below the action line | A never-smoker exposed to 1.3 pCi/L carries a 2 in 1,000 lifetime lung-cancer risk; a smoker at the same level, 20 in 1,000 | VERIFIED | https://www.epa.gov/radon/health-risk-radon | "a person who never smoked (never smoker) who is exposed to 1.3 pCi/L (50 Bq/m 3 )has a 2 in 1,000 chance of lung cancer; while a smoker has a 20 in 1,000 chance of dying from lung cancer" |
| 3 | action line + "consider fixing" band | Fix at 4 pCi/L or more; consider fixing between 2 and 4 pCi/L | VERIFIED | https://www.epa.gov/radon/radon-publications | "EPA strongly recommends that you fix your home if your test shows 4 picocuries per litre (pCi/L) (150 becquerels per meter cubed (Bq/m 3 )) or more. If your test shows between 2 and 4 pCi/L (75 - 150 Bq/m 3 ), consider fixing." |
| 4 | state kit price | $12.25 from the New York State Department of Health, including kit, lab analysis and return postage | VERIFIED | https://www.health.ny.gov/environmental/radon/ | "Homeowners in New York State can order a radon test from the State Department of Health for $12.25 by completing this order form . Price includes test kit, analysis and postage to send the test kit to the laboratory." |
| 5 | closed-house precondition (strict version) | Doors and windows closed 24 hours before and during the test | VERIFIED | https://www.health.ny.gov/environmental/radon/ | "It very is important that the home is sealed up and all doors or windows to the outside are closed 24 hours before and during the entire testing period to ensure an accurate test." |
| 6 | testing interval | Every five years, or every two years with a mitigation system | VERIFIED | https://www.health.ny.gov/environmental/radon/ | "When to Test Every five years, or every two years if you have a radon mitigation system to make sure it's working properly." |
| 7 | ventilation decay (the mechanism) | A ventilation shortcut depresses the reading, and the concentration returns to its prior value within about 12 hours of closing up | VERIFIED | https://www.health.ny.gov/environmental/radon/mitigation.htm | "once windows, doors and vents are closed, radon concentrations most often return to previous values within about 12 hours" |
| 8 | post-install test protocol | Two- to seven-day measurement after install; doors/windows closed 12 hours before and during; post-mitigation test within 30 days, no sooner than 24 hours of the fan running | VERIFIED | https://www.health.ny.gov/environmental/radon/mitigation.htm | "To test the system's effectiveness, a two- to seven-day measurement is recommended. Test conditions: windows and doors must be closed 12 hours before and during the test, except for normal entry and exit." / "A post-mitigation radon test should be done within 30 days of system installation, but no sooner than 24 hours after your system is in operation with the fan on" |
| 9 | suspect-quote floor | Avoid inexpensive mitigation rates; quotes under $1,000 are often too good to be true | VERIFIED | https://www.health.state.mn.us/communities/environment/air/radon/mitigation.html | "Avoid unlicensed installers and inexpensive mitigation rates (less than $1,000). Price quotes promising really low installation rates are often too good to be true and leave the consumer with sub-standard workmanship and materials" |
| 10 | action level restated by a state | EPA action level 4 pCi/L, mitigation recommended at or above it; consider between 2 and 4 | VERIFIED | https://www.health.state.mn.us/communities/environment/air/radon/index.html | "The Environmental Protection Agency (EPA) has set the action level at 4 pCi/L (picocuries of radon per liter of air). MDH recommends installing a radon mitigation system when the radon level is at 4 pCi/L or higher. Between 2 and 4 pCi/L, a radon mitigation system can be considered" |
| 11 | short-term window + placement | Short-term tests take two to seven days; the kit goes in the lowest level regularly used | VERIFIED | https://www.lung.org/clean-air/indoor-air/indoor-air-pollutants/radon | "Short-term tests usually take two to seven days. To use a short-term radon test, place the kit in the lowest level regularly used in your home and where it will not be disturbed." |
| 12 | long-term alternative + retest clock | Long-term tests take at least three months; retest within 24 hours–30 days after install and every 2 years after | VERIFIED | https://www.lung.org/clean-air/indoor-air/indoor-air-pollutants/radon | "Long-term radon tests take at least three months and measure long-term averages." / "re-test your home within 24 hours – 30 days after a mitigation system is installed and every 2 years after that" |

## FLAGGED / do-not-use

- **No install price is citable.** The American Lung Association page prints its cost band as "The cost can range from $1,00 - $2,500 or more" — a typographical range that cannot be restated as $1,000–$2,500 without publishing a figure the page does not print. The article carries the state health department's *quote floor* (row 9) and sends the reader for three bids; it prints no dollar range for mitigation.
- **The closed-house clock is not one number.** New York's consumer page says 24 hours before and during (row 5); New York's own mitigation page and the Lung Association's kit guidance use 12 hours before (rows 7–8, and ALA's "Begin closed-house conditions at least 12 hours prior to the start of the testing period"). The article must say the laboratory's instruction sets the clock, and that 24 hours satisfies every version. Never average the two, never print 12 hours as "the rule".
- **21,000 is an estimate with a published range** ("8,000 to 45,000") on the same page; 2,900 is the never-smoker share of that estimate, not a measured annual count.
- **1.3 pCi/L risk is a lifetime estimate for a never-smoker**, not an annual rate and not a threshold below which nothing happens. Do not convert it into a "safe level".

## Figures the draft must carry, and the sections allowed to hold each (article_shape: max two body sections per figure)

| Figure | Sections |
|---|---|
| 3.9 pCi/L (illustrative reading; not a sourced figure) | lead only |
| 4 pCi/L (action line) | lead, at-a-glance |
| $12.25 | lead, tactical |
| 12 hours (decay) | tension |
| 24 hours (seal / post-install wait) | tactical |
| 2,900 / 21,000 | numbers |
| 1.3 pCi/L and 2 in 1,000 | numbers |
| two to seven days | numbers, tactical |
| less than $1,000 | numbers, catch |
| five years / two years, 30 days | tactical |
