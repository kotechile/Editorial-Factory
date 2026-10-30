# Evergreen Brief: career_velocity_equity_engineering — 2026-10-30

**Archetype:** evergreen
**Vertical:** career_velocity_equity_engineering
**Persona:** equity_career_strategist
**Decision the reader is facing:** Whether to buy restricted stock or exercise options now and file a section 83(b) election inside 30 days so the qualified-small-business-stock clock starts at the grant — or to wait for a liquidity event and pay full long-term rates on the whole gain; the choice bites twice, once at grant and again at the first round that pushes the company's gross assets past $75 million, after which shares issued later can never qualify.
**Durability:** Every load-bearing figure is a statute, a regulation or a published rate, not a price. The 3/4/5-year exclusion ladder and the $15,000,000 per-issuer cap are 26 U.S.C. § 1202(a)(5) and (b)(4) as of the current United States Code text reflecting Pub. L. 119-21, enacted July 4, 2025; the $75,000,000 gross-assets ceiling is § 1202(d)(1) as of the same text; the 30-day filing window is 26 CFR § 1.83-2(b) as of the eCFR edition read on 2026-10-30; the 20% capital-gains rate and the 3.8% net investment income tax are the Internal Revenue Service's own pages as of 2026-10-30. Both dollar thresholds are indexed for inflation in $10,000 steps for tax years beginning after 2026, which is precisely why the piece dates them and states the indexing rule rather than treating them as constants.
**De-dup:** `2026-10-09_post-termination-option-clock-tax` is this vertical's nearest prior artifact on the same mechanic — it prices the window in which you may still exercise after leaving and the ordinary-income bill an exercise without an election creates; this piece starts at the opposite end, the 30 days after a grant, and its load-bearing figures (the 50/75/100 percent ladder, the $15,000,000 cap, the $75,000,000 gross-assets test) appear nowhere in it. Also distinct from `2026-10-23_your-26-week-cliff-kills-4-years` (what unvested equity is worth when you leave), `2026-10-16_your-ipo-payday-tax-bill` (RSU settlement withholding), `2026-10-09_staggered-lockup-six-selling-decisions` (post-IPO lockup windows), `2026-10-30_why-one-share-outvotes-5300-staff` (voting rights against economics) and `2026-09-25_carta-unexercised-options-401k`. Cross-vertical check per the skill's 2026-10-19 rule: `grep -ril "83(b)\|qualified small business\|QSBS" published/` returns no article, so no other vertical owns this thesis. This is also the candidate the 2026-10-23 evergreen run parked for cadence at 8.8; it re-enters with the 2025 statutory ladder that draft did not carry.
**Thesis:** The gain you keep from private-company stock is set by a rung you can choose — 50 percent excluded at three years, 75 percent at four, 100 percent at five, for shares issued after July 4, 2025 — but the rung is reachable only if the company's gross assets were under $75 million when your shares were issued, and only a 30-day election puts your whole grant on one clock instead of one clock per vest tranche.

**Lead:** The vertical's own beat — `primary_angles` #2 in `context/verticals.json` ("equity growth and scenario matrix startup strike prices vs enterprise comp"), reinforced by the `equity_career_strategist` persona's declared wants in `context/personas.json` ("ISO/NSO strike modeling, secondary liquidity math") and by founder-voice §3 `career_velocity_equity_engineering` ("stress-test ... strike exercise windows, 409A valuations against illiquid exit scenarios"). The material is the statute itself, which the desk has not read for this beat before: Pub. L. 119-21 rewrote § 1202 in July 2025, replacing the single five-year/100-percent rule with a three-rung table and lifting the gross-assets ceiling from $50 million to $75 million, and the 2026-10-23 run parked the 83(b)/§1202 candidate before that ladder existed in the brief. Field colour only, never a gate row: customer-truth §2's $190,000-base / 0.75-percent-equity director whose common stock washed out at $0.00 in a down-round acquisition — the reason a rung you can reach in three years is worth more than a rung that requires the company to survive five.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | 26 U.S.C. § 1202 — per-issuer limitation on eligible gain (Cornell Legal Information Institute) | https://www.law.cornell.edu/uscode/text/26/1202 | 2026-10-30 | $15,000,000 — for qualified small business stock acquired after the applicable date the per-issuer exclusion cap is $15,000,000, reduced by excluded gain taken into account in prior taxable years | measured (the statute itself) |
| 2 | 26 U.S.C. § 1202 — per-issuer limitation on eligible gain (Cornell Legal Information Institute) | https://www.law.cornell.edu/uscode/text/26/1202 | 2026-10-30 | 10 times — the cap is the greater of the applicable dollar limit or 10 times the aggregate adjusted bases of the qualified small business stock disposed of during the year | measured (the statute itself) |
| 3 | 26 CFR § 1.83-2 — time for making the section 83(b) election (eCFR) | https://www.ecfr.gov/current/title-26/section-1.83-2 | 2026-10-30 | 30 days — the election shall be filed not later than 30 days after the date the property was transferred | measured (Treasury regulation) |
| 4 | Internal Revenue Service — Topic no. 409, capital gains and losses | https://www.irs.gov/taxtopics/tc409 | 2026-10-30 | 20% — a capital gains rate of 20% applies to the extent taxable income exceeds the thresholds set for the 15% rate | measured (the agency's own published rate) |
| 5 | Internal Revenue Service — Net Investment Income Tax | https://www.irs.gov/individuals/net-investment-income-tax | 2026-10-30 | 3.8 percent — taxpayers are liable for a 3.8 percent Net Investment Income Tax on the lesser of net investment income or the excess of modified adjusted gross income over the statutory threshold | measured (the agency's own published rate) |
| 6 | Internal Revenue Service — Topic no. 409, capital gains and losses (the section 1202 sentence) | https://www.irs.gov/taxtopics/tc409 | 2026-10-30 | 28% — the taxable part of a gain from selling section 1202 qualified small business stock is taxed at a maximum 28% rate | measured (the agency's own published rate) |

## Figures that ride in prose under these citations (read by eye, not given a row)

- **$75,000,000 — the gross-assets ceiling.** § 1202(d)(1): a qualified small business is a domestic C corporation whose "aggregate gross assets ... at all times on or after the date of the enactment of the Revenue Reconciliation Act of 1993 and before the issuance did not exceed $75,000,000", and whose assets "immediately after the issuance ... do not exceed $75,000,000". Its own evidence window lands on the phrase "75 percent" in § 1202(a)(3) (the tokenizer splits the comma group), so it must not carry a row; quote the sentence in the verified brief and cite § 1202 in Sources.
- **The ladder — "3 years 50% / 4 years 75% / 5 years or more 100%".** § 1202(a)(5)'s table reads, verbatim: "Years stock held: Applicable percentage: 3 years 50% 4 years 75% 5 years or more 100%". Its evidence window lands on § 1202(a)(1)(A) — the *pre*-enactment 50-percent rule — so it rides in prose too. The article must state that the table applies to stock "acquired after the applicable date" and that pre-enactment stock still needs five years for 100 percent under § 1202(a)(4).
- **The applicable date is July 4, 2025.** Not stated in the section text, only in the amendment note on the same page: "Pub. L. 119–21, title VII, §§ 70302(b)(11), 70431(a)(1)–(3), (4)(B), (5), (b)(1)–(3), (c)(1), (2), July 4, 2025, 139 Stat. 192, 240–242." Cite the page; do not assert a date the section itself does not print.
- **The holding period follows the election.** 26 CFR § 1.83-4(a), same eCFR title and part as row 3: "if the person who has performed the services ... has made an election under section 83(b), the holding period of such property shall begin just after the date such property is transferred", against "the holding period ... shall begin just after such property is substantially vested" without one.
- **Qualification is at original issue.** § 1202(c)(1)(B): stock must be "acquired by the taxpayer at its original issue (directly or through an underwriter)—(i) in exchange for money or other property (not including stock), or (ii) as compensation for services". This is what makes exercise of a company-granted option a qualifying acquisition and a purchase of shares from another employee in a tender or secondary sale a non-qualifying one.
- **The exclusion the reader does not expect: engineering services.** § 1202(e)(3)(A) excludes "any trade or business involving the performance of services in the fields of health, law, engineering, architecture, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage services, or any trade or business where the principal asset of such trade or business is the reputation or skill of 1 or more of its employees." A reader at an engineering-services firm may be holding stock that was never qualified small business stock at all.
- **The per-issuer cap has a second shape.** § 1202(b)(1)(B): the 10-times-basis alternative, computed "without regard to any addition to basis after the date on which such stock was originally issued".

## Arithmetic the draft must carry (every input above, no invented rate)

| Quantity | Formula | Result |
|---|---|---|
| Taxable portion of the gain at each rung | 50% / 25% / 0% | three-year / four-year / five-year rung |
| Federal rate on that taxable portion | 28% maximum (§ 1202 gain) + 3.8% NIIT | 31.8% |
| Effective tax on the whole gain | 31.8% × 50% / × 25% / × 0% | 15.9% / 7.95% / 0% |
| The same three rungs on a $1,000,000 gain | $1,000,000 × 15.9% / 7.95% / 0% | $159,000 / $79,500 / $0 |
| The same gain with no exclusion at all | $1,000,000 × 23.8% | $238,000 |
| What the two extra years buy (year 3 to year 5) | 15.9 − 0 | 15.9 points, $159,000 per $1,000,000 of gain |
| After-tax share kept by selling at year 3 | 1 − 0.159 | 84.1% — holding to year 5 wins only if the position keeps more than that |
| Where 10 times basis overtakes the dollar cap | $15,000,000 ÷ 10 | $1,500,000 of adjusted basis |
| Last tranche's five-year mark, four-year monthly vest, election filed | 0 + 60 months | 60 months after grant |
| Same grant without an election | 48 + 60 months | 108 months after grant — the last shares wait four more years |

Worked example the article may run as arithmetic (hypothetical, and it must say so): 100,000 shares bought at $1.00 with a $1.30 fair market value at grant costs $100,000 and creates $30,000 of ordinary income under an election; with the election the whole block's holding period starts at the grant, and a sale at $12.00 produces $1,100,000 of gain — $550,000 taxable at the three-year rung ($174,900 at 31.8%), $275,000 taxable at four ($87,450), none taxable at five, against a 10-times-basis cap of $1,000,000 that the $15,000,000 dollar limit still beats.

## Candidate topics considered

| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The 2025 section 1202 ladder plus the 30-day election: which rung you can reach, and whose stock was ever qualified | 9 | 9 | 9 | 9 | 9.0 | **winner** |
| Cliff-forfeiture valuation: price the unvested equity you leave behind and negotiate it into the offer | 9 | 8 | 5 | 8 | 7.6 | dropped — unchanged from three earlier runs: the only figures available live in the desk's own field anecdote, and no fetchable primary prices a forfeiture |
| Equity scenario matrix: startup paper against enterprise liquid comp, and the preference stack that washes out common | 9 | 8 | 6 | 7 | 7.7 | dropped — 409A valuations and preference waterfalls remain paywalled or client-rendered to the gate's fetch path; the S-1 route was used for today's news piece and does not generalise to a matrix |
| Restricted stock against RSU against option: a tax-timing table | 8 | 9 | 7 | 7 | 7.9 | dropped — overlaps the 2026-10-09 exercise-window and 2026-10-16 RSU-withholding pieces without adding a load-bearing figure this run can fetch |
| The post-termination exercise window and its ten-year extension | 8 | 8 | 5 | 8 | 7.3 | dropped — `2026-10-09_post-termination-option-clock-tax` owns this mechanic and no primary source states a comparative cost |

Composite = round(0.35·U + 0.25·D + 0.25·E + 0.15·A, 1).

## Notes for the drafter and verifier

- **The ladder is the thesis, and it is a table, not a sentence.** Write all three rungs and say which shares each rung applies to: post-enactment shares get 50/75/100 at three/four/five years; pre-enactment shares still need five years and still get 100 percent under § 1202(a)(4). Do not collapse the two regimes into "the exclusion is 100 percent".
- **"Applicable date" is a defined term.** If the article needs the date, it is July 4, 2025 from the amendment note, not from the section text; attribute it that way.
- **The two years from year 3 to year 5 are worth 15.9 points of gain, not 50, and not 11.9.** The taxable half at the three-year rung is taxed at a maximum 28 percent (row 6), not the 20 percent ordinary long-term rate, so the effective burden on the whole gain is 15.9 percent with the surtax, not 11.9. Recompute the 84.1 percent after any rewrite: it is 1 − 0.159, and a rewrite that turns it into "you keep half" or "you pay a fifth" is the derived-percentage class the desk has been burned by twice.
- **The 28 percent rate is the finding the article exists for.** Most readers assume the taxable part of a qualified-small-business gain rides at the ordinary long-term rate; the Internal Revenue Service's own sentence says the taxable part is taxed at a maximum 28 percent. State it as the agency states it, say it is capped rather than fixed, and never present 31.8 percent as a statutory rate — it is 28 plus a separate 3.8 percent surtax that applies only when the reader's income clears the threshold.
- **A dollar ceiling indexed after 2026 is a dated figure.** State both thresholds as of 2026, name the indexing rule and the $10,000 rounding, and never write "$75 million" as if it were permanent.
- **No vendor claims and no survey.** Every figure in this piece is statute, regulation or an agency-published rate; if a sentence needs a market number (how many startups are near $75 million of gross assets, what a 409A says), cut the sentence rather than sourcing it to a survey.
- **The engineering-services exclusion is the honest caveat, not a scare.** § 1202(e)(3)(A) names engineering and consulting among the excluded service businesses; say the reader has to check what the corporation actually did, not what the reader's job title was, and that the company's own C-corporation status is a separate requirement under § 1202(c)(2)(A).
- **Do not claim anything about how restricted stock units are taxed.** This brief has no verified source for the RSU holding-period start; if the drafter needs the contrast, it may only say an unvested option is not stock until it is exercised, which row 3 and § 1202(c)(1)(B) both support.
- **Field colour, labelled.** The customer-truth washed-out common story is an anecdote; it may open a section and must not be presented as a measured outcome. No invented probability of a down round.
- **No chart.** Three rates and two thresholds are a table, not a series; the accessibility floor prefers a short table to a derived plot.
- **Accessibility.** Expand C corporation, QSBS, ISO and NSO at first use; the acronym gate hard-fails ALL-CAPS tokens. Keep Flesch at or above 50 (target 60).
- **Headline shape that clears the owner's four rules:** a figure from the piece plus a verb of consequence, six words or fewer in the core — e.g. "Your 3-Year Rung Pays Half the Gain" or "File in 30 Days, Keep 100 Percent". Score it against the final body, never standalone, and confirm the lead carries the title's own words.

## Gate result

<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=4 hosts=3 decision="sha1:a460a8578c" dedup="matched a prior artifact: 2026-10-09_post-termination-option" window_days=180 checked_at=2026-10-30T18:35:06+00:00 -->
<!-- evergreen-gate:end -->
