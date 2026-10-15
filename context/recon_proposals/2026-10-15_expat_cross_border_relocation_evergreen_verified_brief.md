# Verified Brief: expat_cross_border_relocation — 2026-10-15 (evergreen)

Evergreen track (`skills/evergreen_topics.md`) — no news gate, no freshness window. Every
load-bearing figure was fetched live this run and matched to the source that states it. The
evergreen gate PASSed the brief at 2026-10-15T19:38:34+00:00 (7 rows, 7 fetched, 7 sources, 3 hosts:
`ecfr.gov`, `irs.gov`, `law.cornell.edu`), writing the `<!-- evergreen-gate: -->` marker.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | A (account trigger) | An FBAR is required when the aggregate value of foreign financial accounts exceeded $10,000 at any time during the calendar year, and earning nothing does not exempt the account | VERIFIED | https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar | "has a financial interest in or signature or other authority over at least one financial account located outside the United States if the aggregate value of those foreign financial accounts exceeded $10,000 at any time during the calendar year reported"; "Whether the account produced taxable income has no effect on whether the account is a foreign financial account for FBAR purposes" |
| 2 | A (account trigger, second host) | FinCEN, the agency that receives the FBAR, states the same $10,000 aggregate trigger | VERIFIED | https://www.fincen.gov/report-foreign-bank-and-financial-accounts | "must file an FBAR if the aggregate value of the foreign financial accounts exceeds $10,000 at any time during the calendar year" |
| 3 | A (filing date) | The FBAR is due April 15, with an automatic extension to October 15 that the filer does not have to request | VERIFIED | https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar | "The FBAR is an annual report, due April 15 following the calendar year reported. You're allowed an automatic extension to October 15 if you fail to meet the FBAR annual due date of April 15. You don't need to request an extension to file the FBAR." |
| 4 | B (asset threshold) | A taxpayer living abroad files Form 8938 when specified foreign assets are more than $200,000 on the last day of the tax year or more than $300,000 at any time during it; a joint return raises that to $400,000 and $600,000 | VERIFIED | https://www.irs.gov/businesses/corporations/do-i-need-to-file-form-8938-statement-of-specified-foreign-financial-assets | "You are filing a return other than a joint return and the total value of your specified foreign assets is more than $200,000 on the last day of the tax year or more than $300,000 at any time during the year; or You are filing a joint return and the value of your specified foreign asset is more than $400,000 on the last day of the tax year or more than $600,000 at any time during the year" |
| 5 | C (asset-form penalty) | A failure to furnish the § 6038D information carries a penalty of $10,000; where the failure continues more than 90 days after notice, a further $10,000 for each 30-day period, capped at $50,000 | VERIFIED | https://www.law.cornell.edu/uscode/text/26/6038D | "such person shall pay a penalty of $10,000. (2) Increase in penalty where failure continues after notification If any failure described in paragraph (1) continues for more than 90 days after the day on which the Secretary mails notice of such failure … of $10,000 for each 30-day period (or fraction thereof) … The penalty imposed under this paragraph with respect to any failure shall not exceed $50,000" |
| 6 | C (entity-form penalty) | A failure to report a foreign business entity carries a penalty of $10,000 for each annual accounting period, and after a 90-day notice a further $10,000 for each 30-day period, with the increase capped at $50,000 | VERIFIED | https://www.law.cornell.edu/uscode/text/26/6038 | "such person shall pay a penalty of $10,000 for each annual accounting period with respect to which such failure exists"; "(2) Increase in penalty where failure continues after notification … of $10,000 for each 30-day period (or fraction thereof) … shall not exceed $50,000" |
| 7 | C (the form itself) | Form 5471 is the information return for a foreign corporation a US person owns, and the IRS states its failure penalty as $10,000 for each annual accounting period of each foreign corporation, with more if the form is not filed within 90 days of an IRS notice | VERIFIED | https://www.irs.gov/instructions/i5471 | "Failure to file information required by section 6038(a) (Form 5471 and Schedule M). A $10,000 penalty is imposed for each annual accounting period of each foreign corporation for failure to furnish the information required by section 6038(a) within the time prescribed. If the information is not filed within 90 days after the IRS has mailed a notice of the failure to the U.S. person, an additional $10,000 penalty (per foreign corporation)" |
| 8 | D (willful ceiling) | A willful violation of § 5314 raises the maximum civil penalty to the greater of $100,000 or 50 percent of the account amount | VERIFIED | https://www.law.cornell.edu/uscode/text/31/5321 | "(C) Willful violations.— In the case of any person willfully violating, or willfully causing any violation of, any provision of section 5314 — (i) the maximum penalty under subparagraph (B)(i) shall be increased to the greater of— (I) $100,000, or (II) 50 percent of the amount determined under subparagraph (D)" |
| 9 | D (indexed ceilings) | For penalties assessed on or after January 17, 2025 the inflation table sets the non-willful FBAR maximum at $16,536 (from a statutory $10,000) and the willful maximum at $165,353 (from $100,000) | VERIFIED | https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-G/section-1010.821 | "penalties assessed on or after January 17, 2025 … 31 U.S.C. 5321(a)(5)(B)(i) Foreign Financial Agency Transaction—Non-Willful Violation of Transaction 10,000 16,536 31 U.S.C. 5321(a)(5)(C)(i)(I) Foreign Financial Agency Transaction—Willful Violation of Transaction 100,000 165,353" |

## Gate notes
- **Verified: 9. Removed: 0. Flagged: 0.** Rows 1, 3, 4, 5, 6, 7, 8 and 9 are the seven gate rows
  (three hosts); row 2 is live corroboration on a fourth host (FinCEN), recorded here because the
  page states the same trigger in its own words but its fetched text opens with a stack of
  disaster-extension notices whose dates collide with the gate's numeric matcher, so it carries no
  marker row.
- **Vendor vs measured:** every row is a measured primary — two IRS guidance pages, the IRS
  instruction set for Form 5471, three sections of the U.S. Code (via Cornell LII) and the Code of
  Federal Regulations on the eCFR. No vendor or trade-body claim is load-bearing.
- **Currency of the one indexed figure:** the eCFR page displays "up to date as of 10/13/2026" and
  its penalty table applies to penalties assessed on or after January 17, 2025.
- **Editorial arithmetic (the writer's own reading, never cited):** that the disclosure regime is
  decoupled from tax — the FBAR trigger holds even when the account earns nothing [1] — is the
  sources' own wording, not a derived figure. No arithmetic beyond the sources is authorised.

## Figure set cleared for drafting (no other number may appear without a source)
$10,000 (the aggregate foreign-account trigger; the § 6038D and § 6038 base penalties; the FBAR
non-willful statutory ceiling) · $200,000, $300,000, $400,000, $600,000 (the Form 8938 thresholds for
a taxpayer living abroad, single and joint) · 90 days (the notice before the continuation penalty) ·
30-day period · $50,000 (the cap on the continuation penalty) · $100,000 and 50 percent (the willful
FBAR ceiling) · $16,536 and $165,353 (the indexed ceilings for penalties assessed on or after
January 17, 2025) · April 15 and October 15 (the FBAR date and its automatic extension).

## Desk field note (NOT a gate row — internal field data)
`context/growth_os/customer-truth.md` § `expat_cross_border_relocation` Anecdote 3: a US employer
whose senior engineer worked remotely from Spain for about seven months drew a permanent-establishment
determination, retroactive corporate tax and **$110,000** in penalties and mandatory contributions.
Carried as the desk's own field note — the article states it as the desk's experience, never as a
sourced statistic, and it is not a figure the disclosure rules produced.
