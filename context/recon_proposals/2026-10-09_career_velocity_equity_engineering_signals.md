# Signals: career_velocity_equity_engineering — 2026-10-09

**Window:** 2026-09-09 → 2026-10-09
**Vertical:** career_velocity_equity_engineering (Career Velocity, Equity Liquidity & Offer Engineering)
**Persona:** equity_career_strategist
**Queries run:** 31 (six source fan-outs across the vertical's sources — levels_fyi, carta_equity_reports, sec_edgar_filings, blind_tech_threads, hacker_news, comp_gauge — plus date-agnostic fallback phrasing and primary-page fetches; every hit timestamp-checked against the window)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | SpaceX staged lockup clears the next tranches | https://www.fool.com/investing/2026/09/29/elon-musk-cant-sell-spacex-shares-until-2027-heres | 2026-09-29 | 15 primary lockup dates, five already reached; another 328.4M shares clear on both Oct 9 and Oct 24; a ~1.3B-share release follows Q3 earnings; ~797.6M more on Dec 8; >7B across H1 2027; Musk's ~6.42B shares (48.4% of the company) locked until June 12, 2027 | equity liquidity now arrives in tranches, not one cliff | 88 |
| 2 | SpaceX COO sells into the unlock | https://www.fool.com/investing/2026/09/29/elon-musk-cant-sell-spacex-shares-until-2027-heres | 2026-09-29 | President/COO Gwynne Shotwell filed Sept 23 to sell 342,170 shares (~$50M); SPCX fell into the Sept 24 unlock | insiders time sales to the unlock calendar | 80 |
| 3 | SpaceX staged-release mechanics + the tax clock | https://bfawealth.com/deals/spacex-lockup | 2026-10-05 | Time-based releases at days 70/90/105/120/135 after pricing = Aug 20, Sep 9, Sep 24, Oct 9, Oct 24, 7% each; the 30%-over-$135 price trigger was missed (top close $125.33); 28% after Q3; remainder Dec 8; RSU withholding at 22% supplemental (37% above $1M); NSO spread = ordinary income, ISO = AMT risk; 10b5-1 cooling-off 30 days for staff, 90–120 for officers | the calendar, not the headline, is the decision surface | 90 |
| 4 | SpaceX S-1 staged-release terms | https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm | 2026-06-12 | Eligible holders sell up to 20% of locked shares from the second full trading day after Q2 earnings, +10% if the stock trades 30% above $135 for 5 of 10 days; 7% at each of days 70/90/105/120/135; +28% after Q3; remainder at day 180 | primary filing of record | 85 |
| 5 | SpaceX's float more than doubles on the first unlock | https://www.reuters.com/business/spacex-shares-slip-lockup-expiry-adds-post-ipo-woes-2026-08-06 | 2026-08-06 | First release on Aug 6 freed 911.5M shares (adding to ~639M sold in the IPO); restrictions lifting through Dec 8 lift the tradeable float to ~40% of the company; the remaining 60% (including Musk's stake) stays locked until mid-2027 | supply overhang meets employee cash-out | 80 |
| 6 | SpaceX priced the IPO at $135; SPCX listed June 12, 2026 | https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/ | 2026-06-12 | IPO prospectus (Form 424B4) filed with the SEC; $135 a share; the largest U.S. listing by proceeds; fewer than 5% of shares floated at the debut | the anchor event | 84 |
| 7 | "Six selling decisions, not one" | https://savantwealth.com/savant-views-news/article/spacexs-staggered-lockup-means-six-selling-decisions-not-one-how-employees-should-think-about-each-window | 2026-07 | A staggered lockup turns one sell-or-hold call into a sequence of six (seven with the Q2 price-based release); "decide once, execute six times"; the day-180 window ending Dec 9, 2026 is a deliberate bridge into the 2027 tax year | planning framework | 72 |
| 8 | The market price of a software engineer is $196K; the top is $1M | https://www.levels.fyi/t/software-engineer | 2026-10-04 | Median U.S. software-engineer total comp $196,000 (25th $139K, 75th $282K, 90th $390K) across 51,030 submissions; top-paying companies Cursor $1,000,000, Anthropic $882,500, OpenAI $760,000 — most of the top figure is stock | equity is now most of tech pay | 65 |
| 9 | Reuters lockup-schedule table | https://www.reuters.com/legal/government/lockup-expiry-will-offer-next-test-investor-appetite-spacex-shares-2026-08-05 | 2026-08-05 | Timed releases: Sept 9, 2026 — 319M shares; Sept 10 — 59M (a separate Rule 144 affiliate tranche) | schedule detail | 78 |

**Primary-source notes.** The load-bearing anchor for rows 1–3 and 5–9 is the SpaceX IPO prospectus filed with the SEC on June 12, 2026 — Form 424B4 at https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/ and the earlier Form S-1 at https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm — which sets the staged-release schedule the secondary coverage renders. Row 8 is a rolling compensation aggregate (Levels.fyi), carried as the pay-context signal only, never as the article's anchor.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=9 candidates=0 heuristic=- window=2026-09-09..2026-10-09 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

