# Verified Brief: home_equity_tco — 2026-11-02 (evergreen)

Companion to `context/recon_proposals/2026-11-02_home_equity_tco_evergreen_brief.md` (gate PASS,
5 rows fetched, 2 hosts, marker 2026-11-02T18:35:58+00:00). Every row below was read out of the
fetched page text in this run, not from a summary.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Depreciation clock | Residential rental property is written off over 27.5 years under the general depreciation system | VERIFIED | https://www.irs.gov/publications/p527 | "Under GDS, the addition is depreciated as residential rental property over 27.5 years" |
| 2 | Depreciation clock (statute) | The statute's own table fixes the recovery period at 27.5 years | VERIFIED | https://www.law.cornell.edu/uscode/text/26/168 | "Residential rental property 27.5 years" (beside "Nonresidential real property 39 years") |
| 3 | Parts inside the building | Appliances and carpet in a rental run on 5-year GDS schedules, not the 27.5-year building clock | VERIFIED | https://www.irs.gov/publications/p527 (Table 2-1) | "Appliances, such as: Stoves Refrigerators 5 years 9 years Carpets 5 years 9 years" |
| 4 | Basis at conversion | The depreciable basis at conversion is the lesser of fair market value or adjusted basis on the conversion date | VERIFIED | https://www.irs.gov/publications/p527 | "When you change property you held for personal use to rental use (for example, you rent your former home), the basis for depreciation will be the lesser of the FMV or adjusted basis on the date of conversion" |
| 5 | When the clock starts | Depreciation starts at the change of use, not at the date the work was finished | VERIFIED | https://www.irs.gov/publications/p527 | "If you place property in service in a personal activity, you can't claim depreciation. However, if you change the property's use to business or the production of income, you can begin to depreciate it at the time of the change" |
| 6 | Passive limit | The special allowance is $25,000, falls by 50 percent of modified adjusted gross income above $100,000, and is unavailable at $150,000 or more | VERIFIED | https://www.irs.gov/publications/p925 | "is reduced by 50% of the amount of your modified adjusted gross income that is more than $100,000 ($50,000 if you're married filing separately). If your modified adjusted gross income is $150,000 or more … you generally can't use the special allowance" |
| 7 | Recapture rate | Unrecaptured section 1250 gain is taxed at 25 percent | VERIFIED | https://www.law.cornell.edu/uscode/text/26/1 | "(E) 25 percent of the excess (if any) of— (i) the unrecaptured section 1250 gain (or, if less, the net capital gain …)" |
| 8 | Sale exclusion | The Section 121 exclusion is $250,000, or $500,000 on a joint return | VERIFIED | https://www.irs.gov/publications/p523 | "you may exclude the first $250,000 of gain from the sale of your home … The exclusion is increased to $500,000 for a married couple filing jointly" |
| 9 | Exclusion vs depreciation | The exclusion is reduced to the extent of the depreciation taken on the rented portion | VERIFIED | https://www.irs.gov/publications/p523 | "The Section 121 exclusion is reduced to the extent of any depreciation adjustments in connection with the rental or business use of your residence" |
| 10 | Residence test | The exclusion requires ownership and use as a main home for 2 of the last 5 years | VERIFIED | https://www.irs.gov/publications/p523 | "You owned the home for at least 2 of the last 5 years and lived in the home for at least 2 (1 if you become disabled) of the last 5 years leading up to the date of the sale" |
| 11 | The three-year window | A tenancy that runs past roughly three years ends the residence test, because the last five years then hold fewer than two years of residence | VERIFIED as arithmetic on row 10; FLAGGED as a simplification | https://www.irs.gov/publications/p523 | Row 10's sentence is the rule; the "three years" is 5 minus 2. It assumes the owner moves out on the first day of the tenancy and claims no exception. Pub 523's "Eligibility Step 5" carries partial-exclusion exceptions (change of employment, health, unforeseen circumstances) that can rescue a longer absence — the article never says the exclusion is lost automatically |
| 12 | Nonqualified use | The exclusion is prorated for periods after 2008 when the property was not a principal residence | FLAGGED (section verified, mechanism not quoted) | https://www.irs.gov/publications/p523 | Pub 523 carries a section headed "Nonqualified use of entire property after 2008" and a proration worksheet; this run did not extract the formula, so the drafter must state the direction only ("the rented years cut the exclusion") and must not print a percentage |
| 13 | Annual slice | 1 ÷ 27.5 = 3.64 percent a year; $60,000 × 3.64% = $2,182; $30,000 × 3.64% = $1,091 | DERIVED (desk arithmetic, inputs printed) | rows 1 and 2 | No source states 3.64 percent; it is 100 ÷ 27.5. The drafter may print it only as arithmetic ("one divided by 27.5") |
| 14 | Cycle arithmetic in The catch | 24% × $60,000 = $14,400 saved; 25% × $60,000 = $15,000 recaptured; 35% × $60,000 − 25% × $60,000 = $6,000, about $218 a year over 27.5 years | DERIVED (desk arithmetic) + FLAGGED | rows 7, 13 | The 25 percent in row 7 is a **maximum**, so a filer below that rate pays their own rate back and the cycle is a wash rather than a loss; the drafter must keep the conditional phrasing ("at a 24 percent marginal rate … at 35 percent …") and must not present either as every filer's outcome. It also assumes the deduction is usable against rent collected (row 6) |

**Drafter rulings (carry these, they are load-bearing):**
- The 27.5-year clock is the *building*; appliances and carpet are separate 5-year assets. Never present a
  conversion as one asset.
- The basis is the **lesser** of fair market value or adjusted basis — never "what you paid".
- The deduction is only worth what it shelters. For a household above $150,000 of modified adjusted gross
  income it is a suspended loss, so it works against rent and never against salary.
- The exclusion is reduced by the depreciation taken **and** cut by the rented years. Two separate reductions;
  never describe them as one.
- No tax advice: the article is a reading of published rules and says so. No "you should rent" or "don't rent".
- Do not name a bracket table or a 2026 rate schedule — the piece never needs one.
