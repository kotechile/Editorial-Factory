# Verified Brief: expat_cross_border_relocation — 2026-11-12 (evergreen)

Companion to `2026-11-12_expat_cross_border_relocation_evergreen_brief.md` (gate PASS, 6/6 rows verified,
3 hosts, marker `checked_at=2026-11-12T19:33:48+00:00`). Every row below was fetched today through
`citation_hub_dossier.fetch_source` — the same fetcher the gate uses — and the Verbatim cell is copied from
the returned text, not from memory.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | California resident definition | A domiciliary outside California is a resident unless the absence is for other than a temporary or transitory purpose, and a resident stays a resident while temporarily absent | VERIFIED | https://california.public.law/codes/ca_rev_and_tax_code_section_17014 | "(a) “Resident” includes: (1) Every individual who is in this state for other than a temporary or transitory purpose. (2) Every individual domiciled in this state who is outside the state for a temporary or transitory purpose." … "(c) Any individual who is a resident of this state continues to be a resident even though temporarily absent from the state." |
| 2 | California absence harbour | The only bright line in the section is a 546-consecutive-day absence under an employment-related contract | VERIFIED | https://california.public.law/codes/ca_rev_and_tax_code_section_17014 | "any individual domiciled in this state who is absent from the state for an uninterrupted period of at least 546 consecutive days under an employment-related contract shall be considered outside this state for other than a temporary or transitory purpose" |
| 3 | California visit allowance | Returns aggregating to no more than 45 days in a taxable year are disregarded | VERIFIED | https://california.public.law/codes/ca_rev_and_tax_code_section_17014 | "(1) For purposes of this subdivision, returns to this state, totaling in the aggregate not more than 45 days during a taxable year, shall be disregarded." |
| 4 | California disqualifier | The subdivision does not apply above $200,000 of intangible income in a year the contract is in effect | VERIFIED | https://california.public.law/codes/ca_rev_and_tax_code_section_17014 | "(2) This subdivision shall not apply to any individual … who has income from stocks, bonds, notes, or other intangible personal property in excess of two hundred thousand dollars ($200,000) in any taxable year in which the employment-related contract is in effect." |
| 5 | Oregon domiciliary escape | A domiciliary escapes Oregon by keeping no abode there, keeping one elsewhere, and spending not more than 30 days in the state | VERIFIED | https://oregon.public.law/statutes/ors_316.027 | "(A) An individual who is domiciled in this state unless the individual: (i) Maintains no permanent place of abode in this state; (ii) Does maintain a permanent place of abode elsewhere; and (iii) Spends in the aggregate not more than 30 days in the taxable year in this state" |
| 6 | Oregon statutory resident | A non-domiciliary with an Oregon abode and more than 200 days in the state is a resident | VERIFIED | https://oregon.public.law/statutes/ors_316.027 | "(B) An individual who is not domiciled in this state but maintains a permanent place of abode in this state and spends in the aggregate more than 200 days of the taxable year in this state unless the individual proves that the individual is in the state only for a temporary or transitory purpose." |
| 7 | Virginia resident definition | Domicile at any time in the year, or a place of abode for more than 183 days, makes a resident | VERIFIED | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-302/ | "“Resident” … includes … every person domiciled in Virginia at any time during the taxable year and every other person who, for an aggregate of more than 183 days of the taxable year, maintained his place of abode within Virginia, whether domiciled in Virginia or not." |
| 8 | Virginia domicile definition | Domicile is the place of permanent residence and the place the taxpayer intends to return to, judged on intent and conduct | VERIFIED | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-302/ | "“Domicile” means the permanent place of residence of a taxpayer and the place to which he intends to return even though he may actually reside elsewhere. In determining domicile, consideration may be given to the applicant's expressed intent, conduct, and all attendant circumstances including, but not limited to, financial independence, business pursuits, employment, income sources, residence for federal income tax purposes, marital status, residence of parents, spouse and children, if any, leasehold, sites of personal and real property owned by the applicant, motor vehicle and other personal property registration, residence for purposes of voting as proven by registration to vote, if any, and such other factors as may reasonably be deemed necessary to determine the person's domicile." |
| 9 | California anti-abuse clause | The harbour is unavailable where the principal purpose of the absence is to avoid the state's tax | VERIFIED | https://california.public.law/codes/ca_rev_and_tax_code_section_17014 | "(4) This subdivision shall not apply to any individual if the principal purpose of the individual's absence from this state is to avoid any tax imposed by this part." |

## Drafter's guardrails (from these pages, not from inference)
- § 17014(d)'s condition is literally "under an employment-related contract". A self-employed reader has no
  such contract; the article says the harbour is written for employment and therefore does not reach them.
  It does **not** assert an agency interpretation — no Franchise Tax Board page was fetchable this run.
- The 45-day allowance lives *inside* subdivision (d), so it is an allowance of the harbour, not a
  standalone safe harbour. A reader outside (d) does not get 45 days of anything.
- Oregon's 30-day limb requires all three conditions conjunctively ("unless the individual: (i) … (ii) …
  and (iii) …"), including keeping no permanent place of abode in Oregon. A retained house defeats it.
- Virginia's 183 days counts a place of abode, not domicile, and the statute says "whether domiciled in
  Virginia or not" — it is a second, independent route into residency.
- No state income-tax rate, dollar saving or computed bill appears anywhere in these three sections, so the
  article carries none. The only dollar figure in the piece is the $200,000 California disqualifier.

## Removed / not used
- A rate comparison (state top marginal rate against the host country's) — REMOVED: no fetchable primary in
  this brief states a state rate, and a rate quoted from a secondary summary is the class of figure this
  desk's gate cannot check.
- A "typical state audit cost" line — REMOVED: no primary.
