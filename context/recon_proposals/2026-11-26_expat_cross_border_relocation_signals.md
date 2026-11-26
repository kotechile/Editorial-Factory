# Signals: expat_cross_border_relocation — 2026-11-26
**Window:** 2026-10-27 → 2026-11-26
**Queries run:** 9

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Türkiye opens a residence-by-investment permit with no property purchase | https://www.imidaily.com/turkey-investor-residence-permit | 2026-11-18 | Presidential Decision No. 11994, signed 2026-11-17, published in Official Gazette No. 33434 2026-11-18, in force same day. US$150,000 in qualifying Turkish financial assets → 3-year residence permit (18-month minimum hold); US$200,000 → 5 years (30-month hold) | residency gating | 85 |
| 2 | The Türkiye permit's four financial instruments — and its two exclusions | https://atexpress.net/turkiye-investor-residence-permit-150000 | 2026-11-19 | Article 2: bank deposits (BDDK), government debt (Treasury), REIF/VCIF units (SPK), private pension (SEDDK). No real estate in the list. Article 4: permit is NOT assessed under Citizenship Law Art. 12 — no citizenship step. No work rights; family scope limited to spouse + dependent children. Ministry of Interior procedures still unpublished | residency gating | 82 |
| 3 | The 183-day rule is not a universal safe harbor | https://flamingo.tax/blog/183-day-rule-for-tax-residency-367 | 2026-11-05 | US: 183 *weighted* days across 3 years plus ≥31 current-year days; UK: 183 conclusive only in the SRT's first automatic test — below 183, other automatic tests + sufficient-ties decide; Ireland: 183/tax-year or 280 across two tax years (a year with ≤30 days ignored). "182 days is not a globally recognised 'safe' number" | dual-jurisdiction compliance | 70 |
| 4 | The Dutch expat ruling steps down 30% → 27% from 2027 | https://getwherenext.com/changes | 2026-11-08 | The 30% ruling holds through 2026 and becomes 27% on 1 January 2027 (Upcoming · 2027-01-01); partial non-resident status ends then except the documented pre-2024 grandfathered cohort. A five-year projection for a newer arrival must model the step-down | cross-border net cash flow | 68 |
| 5 | Pillar Two Side-by-Side lands in national law in a 3-day November burst | https://oecdpillars.com/pillar-two-developments-tracker-2026 | 2026-11-04 | Slovenia FURS published a substance-based tax incentive explanation 3 Nov + updated its general/procedural explanation 5 Nov 2026; UK Finance Bill 173 published 4 Nov 2026, Clause 35 + Schedule 7 ¶9–11 carry the OECD-list default for Side-by-Side recognition; Greece AADE decisions A.1236/A.1237 (dated 30 Oct, published 2 Nov) prescribe domestic top-up and IIR/UTPR self-assessment returns; Isle of Man 5 Nov | remote work tax nexus | 75 |
| 6 | PwC's Pillar Two country tracker updated with the Side-by-Side wave | https://www.pwc.com/gx/en/services/tax/pillar-two-readiness/country-tracker.html | 2026-11-03 | "What's new: 3 November 2026." Finland enacted Law No. 187/2026 incorporating the OECD Side-by-Side Package (Simplified ETR Safe Harbour still expected later in 2026); follows the 11 Sep 2026 IF package (revised GIR + full legislative review framework) | remote work tax nexus | 72 |
| 7 | US international tax developments roundup mid-November | https://taxnews.ey.com/news/2026-2451-report-on-recent-us-international-tax-developments-13-november-2026 | 2026-11-13 | IRS official calls upcoming CAMT reproposal changes "cleanup issues and smoothing things out"; transition rules expected in reproposed rules. Senior Treasury official: US favors additional Pillar Two safe harbors "based on current taxpayer data or proxy models" to cut compliance burdens | remote work tax nexus | 72 |
| 8 | Numbeo current cost-of-living index (observation-dated) | https://www.numbeo.com/cost-of-living/rankings_current.jsp | 2026-11-26 | Live, continuously updated index as observed 2026-11-26; historical snapshots are published periodically (2026 mid-year: Bermuda 135.8, Cayman 119.9, Switzerland 109.8 at country level). No discrete November release event | cost of living trade-offs | 62 |

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=8 candidates=9 heuristic=0.45-0.75 window=2026-10-27..2026-11-26 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #4 ⨂ #6 | tax_enforcement_x_cross_border_mobility | A: cross-border net cash flow | B: remote work tax nexus | https://getwherenext.com/changes https://www.pwc.com/gx/en/services/tax/pillar-two-readiness/country-tracker.html | 0.75 | - |
| 2 | #4 ⨂ #7 | tax_enforcement_x_cross_border_mobility | A: cross-border net cash flow | B: remote work tax nexus | https://getwherenext.com/changes https://taxnews.ey.com/news/2026-2451-report-on-recent-us-international-tax-developments-13-november-2026 | 0.75 | - |
| 3 | #1 ⨂ #6 | tax_enforcement_x_cross_border_mobility | A: residency gating | B: remote work tax nexus | https://www.imidaily.com/turkey-investor-residence-permit https://www.pwc.com/gx/en/services/tax/pillar-two-readiness/country-tracker.html | 0.67 | legA:url_already_cited |
| 4 | #1 ⨂ #7 | tax_enforcement_x_cross_border_mobility | A: residency gating | B: remote work tax nexus | https://www.imidaily.com/turkey-investor-residence-permit https://taxnews.ey.com/news/2026-2451-report-on-recent-us-international-tax-developments-13-november-2026 | 0.67 | legA:url_already_cited |
| 5 | #2 ⨂ #6 | tax_enforcement_x_cross_border_mobility | A: residency gating | B: remote work tax nexus | https://atexpress.net/turkiye-investor-residence-permit-150000 https://www.pwc.com/gx/en/services/tax/pillar-two-readiness/country-tracker.html | 0.67 | legA:url_already_cited |
| 6 | #2 ⨂ #7 | tax_enforcement_x_cross_border_mobility | A: residency gating | B: remote work tax nexus | https://atexpress.net/turkiye-investor-residence-permit-150000 https://taxnews.ey.com/news/2026-2451-report-on-recent-us-international-tax-developments-13-november-2026 | 0.67 | legA:url_already_cited |
| 7 | #5 ⨂ #6 | tax_enforcement_x_cross_border_mobility | A: remote work tax nexus | B: remote work tax nexus | https://oecdpillars.com/pillar-two-developments-tracker-2026 https://www.pwc.com/gx/en/services/tax/pillar-two-readiness/country-tracker.html | 0.46 | prior_cycle_token_overlap:pillar|side-by-side |
| 8 | #5 ⨂ #7 | tax_enforcement_x_cross_border_mobility | A: remote work tax nexus | B: remote work tax nexus | https://oecdpillars.com/pillar-two-developments-tracker-2026 https://taxnews.ey.com/news/2026-2451-report-on-recent-us-international-tax-developments-13-november-2026 | 0.46 | - |
| 9 | #6 ⨂ #7 | tax_enforcement_x_cross_border_mobility | A: remote work tax nexus | B: remote work tax nexus | https://www.pwc.com/gx/en/services/tax/pillar-two-readiness/country-tracker.html https://taxnews.ey.com/news/2026-2451-report-on-recent-us-international-tax-developments-13-november-2026 | 0.45 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=0.5 intensity=0.7 angle_fit=1.0 contrast=1.0 → 0.75 (tax_enforcement_x_cross_border_mobility)
- #2: token_coverage=0.5 intensity=0.7 angle_fit=1.0 contrast=1.0 → 0.75 (tax_enforcement_x_cross_border_mobility)
- #3: token_coverage=0.5 intensity=0.79 angle_fit=0.5 contrast=1.0 → 0.67 (tax_enforcement_x_cross_border_mobility)
- #4: token_coverage=0.5 intensity=0.79 angle_fit=0.5 contrast=1.0 → 0.67 (tax_enforcement_x_cross_border_mobility)
- #5: token_coverage=0.5 intensity=0.77 angle_fit=0.5 contrast=1.0 → 0.67 (tax_enforcement_x_cross_border_mobility)
- #6: token_coverage=0.5 intensity=0.77 angle_fit=0.5 contrast=1.0 → 0.67 (tax_enforcement_x_cross_border_mobility)
- #7: token_coverage=0.5 intensity=0.73 angle_fit=0.5 contrast=0.0 → 0.46 (tax_enforcement_x_cross_border_mobility)
- #8: token_coverage=0.5 intensity=0.73 angle_fit=0.5 contrast=0.0 → 0.46 (tax_enforcement_x_cross_border_mobility)
- #9: token_coverage=0.5 intensity=0.72 angle_fit=0.5 contrast=0.0 → 0.45 (tax_enforcement_x_cross_border_mobility)
<!-- synthesis-seed:end -->

## Dated background
- PwC's $2.2bn sale of its Global Mobility Tax & Immigration Services business to CD&R is a 2021 transaction (FIDI Focus datelined 20 Oct 2021; CD&R announcement itself undated but contemporaneous) — NOT an in-window signal: https://www.fidifocus.org/news/pwc-sells-off-mobility-services-arm · https://www.cdr.com/news/cdr-reaches-agreement-to-acquire-pwcs-global-mobility-tax-and-immigration-services-business
- InterNations Expat Insider 2026 coverage is August 2026 (BBC 2026-08-14) — outside window: https://www.bbc.com/travel/article/20260814-the-worlds-best-countries-for-expats-in-2026 · https://qz.com/best-countries-expats-2026
- Spain's Digital Nomad Visa SMI/200%-SMI mechanics come from Real Decreto 126/2026, BOE 19 Feb 2026 — outside window, background for any DNV comparison: https://relotus-relocation.com/en/journal/digital-nomad-visa-income-threshold-2026
- FEIE 2026 figure ($132,900; housing limitation $39,870) was set by the IRS announcement of 9 Oct 2025 (Rev. Proc. 2025-32) — outside window, background only: https://www.irs.gov/individuals/international-taxpayers/figuring-the-foreign-earned-income-exclusion
- The IRS substantial presence test page — the primary record behind the 183-day leg's US clause (cited in the article's Sources as [4]) — is a standing .gov page with no publication event: https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test
- Türkiye's citizenship-by-investment threshold ($400k real estate, 3-year hold) is unaffected by Decision 11994 and predates it: https://www.globalcitizensolutions.com/turkey-new-investor-resident-permit
- EY Global Immigration Index (remote work / digital nomads), last updated Jan–Feb 2026 — outside window: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/insights/workforce/documents/ey-gl-global-immigration-index-remote-work-and-digital-nomads-03-2026.pdf
