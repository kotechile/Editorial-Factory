# Evergreen Brief: career_velocity_equity_engineering — 2026-10-09
**Archetype:** evergreen
**Vertical:** career_velocity_equity_engineering
**Persona:** equity_career_strategist
**Decision the reader is facing:** Whether to exercise vested stock options — and when: inside the roughly 90-day post-termination window while they still qualify as incentive stock options, later once they have converted to nonstatutory options, or never — given the alternative minimum tax the ISO spread triggers at exercise and the two-year holding test that decides whether the gain is capital or ordinary income.
**Durability:** The load-bearing rules do not expire: the three-month post-termination cutoff that costs an option its ISO status (26 U.S.C. §422(a)(2)), the two-year/one-year holding test, and the $100,000 annual ISO grant cap are statutory. Only the alternative minimum tax figures move — they are the IRS's tax-year-2025 numbers (26% of the first $239,100 of taxable excess; Instructions for Form 6251), re-indexed each year, so the article cites them *as of* tax year 2025 and the method outlives the number.
**De-dup:** Nearest prior artifact for this vertical: published/2026-09-25_carta-unexercised-options-401k ("Why 70% of Startup Options Go Unexercised") — that piece is about exercise *rates* (behaviour: how few people exercise) and the 401(k) as the substitute; this one is the *mechanics and cost* of the exercise decision itself (the §422 three-month clock, the AMT bill, the holding test). Also distinct from published/2026-10-09_staggered-lockup-six-selling-decisions (SpaceX staged-lockup tranches, a selling-schedule thesis).
**Thesis:** The real price of exercising a vested option is not the strike price you pay — it is the tax bill the exercise creates: leave the company and §422 silently turns your ISOs into nonstatutory options after three months, and the ISO spread you exercise into triggers alternative minimum tax at 26% of the first $239,100 (tax year 2025), a liability the option itself does not pay.

**Lead:** The vertical's own beat — `primary_angles` #2 in `context/verticals.json` ("equity growth and scenario matrix startup strike prices vs enterprise comp", which names the strike exercise windows, 90-day vs. 10-year PTEP, and ISO/NSO strike modeling) — reinforced by the `equity_career_strategist` persona's stated wants in `context/personas.json` ("ISO/NSO strike modeling, secondary liquidity math") and by founder-voice §3 `career_velocity_equity_engineering` ("Equity Growth Matrix (Startup Paper vs. Enterprise Liquid Comp)": stretch-test the strike exercise windows and 409A valuations). The measurable anchors are the tax statute, the IRS publication and form instructions, and Carta's own equity data. Field colour only (never a gate row): customer-truth §1 Anecdote 2, the $500k startup paper-wealth wipeout where four years of illiquid equity ended at $0.00.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Internal Revenue Service, Instructions for Form 6251 (2025) — Alternative Minimum Tax | https://www.irs.gov/instructions/i6251 | 2026-10-09 | 26% — the AMT rate on the first $239,100 of taxable excess for noncorporate taxpayers in tax year 2025 (28% above it, minus $4,782), the rate that applies to the ISO spread on exercise | measured |
| 2 | Internal Revenue Service, Publication 525 — Taxable and Nontaxable Income (Statutory Stock Options) | https://www.irs.gov/publications/p525 | 2026-10-09 | 2 years — ISO shares must be held at least 2 years from the grant date (and 1 year from exercise); a sale before then is a disqualifying disposition that makes the spread ordinary wages, not capital gain | measured |
| 3 | Cornell Law School, Legal Information Institute — 26 U.S.C. § 422 (Incentive stock options) | https://www.law.cornell.edu/uscode/text/26/422 | 2026-10-09 | 3 months — an option exercised more than 3 months after the holder stops being an employee loses ISO status, and §422(d) caps ISO grants at $100,000 of stock value per year | measured |
| 4 | Carta, "Trends in 409A valuations" (Data Desk report) | https://carta.com/data/trends-409a-valuations-2023 | 2026-10-09 | 90 days — the window an employee typically has after leaving the company to decide whether to exercise, and more employees now let the option expire rather than pay the exercise cost | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The exercise clock: what the ~90-day post-termination window costs (ISO→NSO conversion + the AMT bill on the spread) | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Cliff forfeiture valuation: price the unvested equity you leave behind and negotiate it into the offer | 9 | 8 | 6 | 8 | 8.0 | dropped — the forfeiture figures live in the desk's own customer-truth anecdote ($78k case), not a primary source the gate can fetch; keep as the reserve for a future run with a measured vesting dataset |
| Equity scenario matrix: startup paper vs. enterprise liquid comp, and the preference stack that washes out common | 9 | 9 | 6 | 7 | 8.1 | dropped — the liquidation-preference and 409A outcome figures are paywalled/aggregate Carta tables that do not retrieve a distinctive number under the gate's fixed user-agent |
| Upskilling ROI: the payback window on a certification (tuition + exam + study hours ÷ salary bump) | 8 | 8 | 5 | 9 | 7.5 | dropped — the salary-premium anchors are vendor/aggregator claims, not measured primary sources |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:d77ab155fc" dedup="matched a prior artifact: 2026-09-25_carta-unexercised-optio" window_days=180 checked_at=2026-10-09T18:32:18+00:00 -->
<!-- evergreen-gate:end -->
