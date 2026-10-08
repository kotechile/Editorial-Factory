# Verified Brief: expat_cross_border_relocation — 2026-10-08 (evergreen)

Evergreen track (`skills/evergreen_topics.md`) — no news gate, no freshness window. Every
load-bearing figure below was fetched live this run and matched to the source that states it.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | A (IRS guidance) | The US Physical Presence Test needs 330 full days abroad inside a 12-consecutive-month period | VERIFIED | https://www.irs.gov/publications/p54 | "U.S. citizens and resident aliens must be physically present in a foreign country (or countries) for 330 full days during a period of 12 consecutive months." |
| 2 | A (statute) | 26 U.S.C. § 911(d)(1)(B): present in a foreign country at least 330 full days in any 12 consecutive months | VERIFIED | https://www.law.cornell.edu/uscode/text/26/911 | "during any period of 12 consecutive months, is present in a foreign country or countries during at least 330 full days in such period" |
| 3 | A (statute + IRS guidance) | The foreign housing exclusion starts from a base amount equal to 16 percent of the maximum exclusion (prorated by qualifying days) | VERIFIED | https://www.law.cornell.edu/uscode/text/26/911 and https://www.irs.gov/individuals/international-taxpayers/foreign-housing-exclusion-or-deduction | § 911: "16 percent of the amount (computed on a daily basis) in effect under subsection (b)(2)(D)"; IRS page: "The amount is 16% of the maximum exclusion amount divided by 365 (366 if a leap year), then multiplied by the number of days in your qualifying period" |
| 4 | B (host-country test) | The UK treats a person as resident under the automatic UK test after 183 or more days there in the tax year, and split-year treatment applies only in qualifying cases | VERIFIED | https://www.gov.uk/tax-foreign-income/residence | "you spent 183 or more days in the UK in the tax year"; "This is called 'split-year treatment'. You will not get split-year treatment if you live abroad for less than a full tax year before returning to the UK" |

## Gate notes
- **Source floor: PASS** — 4 rows VERIFIED on 3 distinct hosts (irs.gov, law.cornell.edu, gov.uk),
  each fetched live and shown to contain the figure it is cited for. Recorded in the
  `<!-- evergreen-gate: -->` marker of the brief.
- **Vendor vs measured:** all four rows are measured primary sources — a US statute, an IRS
  publication, an IRS help page and a UK government (HMRC/GOV.UK) residency page. No vendor claims.
- **REMOVED: 0. FLAGGED: 0.**
- **Editorial arithmetic (the writer's own reading, never cited):** that the two clocks "cannot be
  slid together" follows directly from § 911's rolling 12-month window against the UK's tax-year
  count; the article presents that as its own reading.

## Figure set cleared for drafting (no other number may appear without a source)
330 full days · 12 consecutive months · 183 days · 16% (base housing amount). If a year is named it
must be the 2025–26 tax year, not a year-specific dollar cap (the annually indexed exclusion ceiling
is deliberately NOT used — it is a news fact).

## Desk field note (NOT a gate row — internal field data)
`context/growth_os/customer-truth.md` § `expat_cross_border_relocation` Anecdote 1: a US software
executive relocated to the UK in September without synchronizing the two residency start dates and
faced an unexpected **$42,000** cash-flow deficit from timing mismatches between the IRS foreign tax
credit and HMRC self-assessment. Carried as the desk's own field note; the article states it as such
and does not present it as a sourced figure.
