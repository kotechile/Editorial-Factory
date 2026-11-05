# Signals: home_ops_execution — 2026-11-05
**Window:** 2026-10-06 → 2026-11-05
**Queries run:** 23 — one `home_lifestyle_intel` MCP pull (`--recent 30 --vertical home_ops_execution --format signals`: 10 items, Canary Media grid/VPP, Ars Technica hardware, Remodelista interiors, Home Assistant release — **zero** on the permitting, contractor-contract, lien or payment beats, the same empty result as every prior run of this vertical), 13 web fan-outs across the vertical's configured beats (contractor licensing statutes, municipal permit reform, ASHRAE residential ventilation, the 2027 IECC cycle, CSLB enforcement, state AG contractor-fraud actions, lien/retainage statutes, maintenance-contract pricing, insurance and bond requirements), and 9 page fetches plus 2 PDF probes (Census C30 release PDF read with `pdftotext`).

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Census: September 2026 construction spending | https://www.census.gov/construction/c30/pdf/release.pdf | 2026-11-02 | Residential construction $848.8B SAAR, 5.5% below the revised August estimate of $898.0B; total construction $2,186.1B, 1.9% below August and 2.7% below September 2025 (release CB26-176) | Demand collapse | 92 |
| 2 | NAHB reads the same release's improvement line | https://eyeonhousing.org/2026/11/private-residential-construction-slips-as-remodeling-weakens | 2026-11-02 | Improvement (remodeling) spending fell 13.0% in September and 18.0% over the year; private residential 8.9% below a year ago; data center construction 90.3% above a year ago | Demand collapse | 90 |
| 3 | JCHS Leading Indicator of Remodeling Activity, Q3 2026 | https://www.jchs.harvard.edu/blog/remodeling-spending-continues-stagnate | 2026-10-22 | Year-over-year growth in renovation and repair spending projected to reach just 1.5% by 2027-Q3; annual spending hovers near $525B; retail building-product spending flat to negative and remodeling permits stagnant | Horizon | 88 |
| 4 | NCS Credit Lien Index, Q3 2026 | https://www.ncscredit.com/education-center/blog/lien-index-q3-2026 | 2026-10-09 | Index fell to 47, matching the Q3 2022 low, 10% below Q2's revised 52 and 16% below Q3 2025's 56; West 38, Northeast 42 (29% year-over-year decline, lowest in data back to 2018), Midwest 32, South 60 | Payment stress | 91 |
| 5 | Epiq AACER small-business reorganizations | https://www.epiqglobal.com/en-us/resource-center/news/small-business-subchapter-v-elections-increase-46-compared-to-last-year | 2026-10-08 | 2,442 Subchapter V elections in the first nine months of 2026, up 46% from 1,672; September alone 276, up 38%; commercial Chapter 11 filings 6,560, up 11% | Solvency | 84 |
| 6 | CSLB multi-state sting and sweep | https://www.cslb.ca.gov/Resources/PressReleases/2026/NR%20CSLB%20NASCLA%20FINAL.pdf | 2026-11-02 | 39 separate stings and sweeps produced 73 enforcement actions, part of a NASCLA-coordinated multi-state initiative (CSLB #26-03) | Enforcement | 68 |

**Dating note.** Every row is event-dated inside the window. Row 1 is the Census release dated 2026-11-02 (CB26-176); row 2 is NAHB's same-day reading of the Census improvement line, which the release PDF carries only as a footnote ("Includes private residential improvements") — the improvement figure is therefore attributed to NAHB's analysis, not to the Census release itself. Row 6 is a PDF press release dated 2026-11-02.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=0 heuristic=- window=2026-10-06..2026-11-05 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Dated background

- JCHS LIRA, prior edition — "Remodeling Spending Poised for Further Slowdown", 2026-07-23 (https://www.jchs.harvard.edu/press-releases/remodeling-spending-poised-further-slowdown). Out of window; the Q3 release above supersedes it.
- JCHS LIRA, Q1 edition — "Remodeling Growth to Slow Sharply in Early 2027", 2026-05-05 (https://www.jchs.harvard.edu/press-releases/remodeling-growth-slow-sharply-early-2027). Out of window; quoted only if a longer arc is needed.
- California SB 342 (Umberg), Chapter 967, Statutes of 2026 — approved and chaptered 2026-09-30, effective 2027-01-01 (https://www.billtrack50.com/billdetail/1830924). Six days outside the window, so it is **not** an anchor; it is recorded here only because a later run may want the licensing-lapse remedy.
- Pennsylvania Office of Attorney General, home improvement contractor charged with taking more than $80,000 in deposits from four Erie County homeowners — undated on the page and therefore not admissible as an in-window event; the URL is kept for a future enforcement piece (https://www.attorneygeneral.gov/taking-action/charges-home-improvement-contractor-used-erie-county-homeowners-deposits-for-jewelry-legal-fees-for-divorce-attorney).
- International Code Council, 2027 I-Codes cycle closed in late August 2026 with no appeals filed against the 2027 IECC, publication targeted 2026-12-01 — out of window (https://www.energyefficientcodes.org/news-articles/2027-iecc-final).
- City of Pittsburgh permitting reform, Executive Summary dated 2026-09-23 — out of window, and municipal process rather than a contract signal (https://content.govdelivery.com/attachments/PAPITT/2026/09/23/file_attachments/3790900/Permitting%20Reform%20Executive%20Summary%209.23.26%20final.pdf).
