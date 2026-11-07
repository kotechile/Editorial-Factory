# Verified Brief: personal_microeconomics_tinkering_tax — 2026-11-07 (evergreen)

**Companion to:** `context/recon_proposals/2026-11-07_personal_microeconomics_tinkering_tax_evergreen_brief.md`
**Topic:** the prepay ladder — the break-even month, the audit that cannot see an annual charge, and the notice that is the only exit.
**Method:** every claim below was fetched live through `citation_hub_dossier.fetch_source` on 2026-11-07 and the verbatim cell is copied from the fetched body, not from memory or from a secondary writeup.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | C+R Research survey | Consumers estimated $86 a month on subscriptions and itemized $219 — 2.5 times the estimate, $133 higher | VERIFIED | https://www.crresearch.com/blog/subscription-service-statistics | "the average monthly spend for consumers was more than 2.5 times the amount they thought at $219 – a whopping $133 higher than their original estimate" |
| 2 | C+R Research survey | 42% had stopped using a subscription service and kept paying for it | VERIFIED | https://www.crresearch.com/blog/subscription-service-statistics | "a significant minority (42%) admit that they’ve stopped using a subscription service(s) but forgot they were still paying for the service" |
| 3 | Fastmail pricing | The same mailbox is priced on four terms: $6 monthly, $5/mo yearly ($60 for 12 months), $4.75/mo over 24 months ($114), $4.67/mo over 36 months ($168) | VERIFIED | https://www.fastmail.com/pricing/ | "$6 per month Pay yearly and save $12 $5 per month $60 for 12 months $4.75 per month $114 for 24 months $4.67 per month $168 for 36 months" |
| 4 | Backblaze Computer Backup pricing | $9 monthly, $8.25/mo paid annually, $7.88/mo on a two-year term; the two-year plan is $189 and saves $27; the annual licence saves $9 | VERIFIED | https://www.backblaze.com/cloud-backup.html | "Monthly $9/mo BEST VALUE 2 YEARS $7.88/mo paid bi-annually Save 8% Yearly $8.25/mo paid annually" … "you can save $ 9 annually by signing up for an annual license, or save $ 27 when you sign up for a two year license" |
| 5 | Backblaze Computer Backup pricing | A two-year licence costs $189 | VERIFIED | https://www.backblaze.com/cloud-backup.html | "For the best value, choose a two-year backup plan for $189." |
| 6 | Google One plans | Annual billing saves "up to 16%" | VERIFIED | https://one.google.com/about/plans | "Monthly Annual Save up to 16%" |
| 7 | Cal. Bus. & Prof. Code § 17602(b)(2) | Where the initial term is one year or longer, renewal notice must be given at least 15 days and not more than 45 days before the renewal charges | VERIFIED | https://california.public.law/codes/ca_bus_and_prof_code_section_17602 | "the notice shall be provided at least 15 days and not more than 45 days before the automatic renewal offer or continuous service offer renews" |
| 8 | Cal. Bus. & Prof. Code § 17602(a) | The section binds a business making an automatic renewal offer "to a consumer in this state" — the article must not say it applies nationally | VERIFIED | https://california.public.law/codes/ca_bus_and_prof_code_section_17602 | "It is unlawful for any business that makes an automatic renewal offer or continuous service offer to a consumer in this state to do any of the following" |
| 9 | Cal. Bus. & Prof. Code § 17602(c)(1) | The statute requires a cancellation mechanism that is "cost-effective, timely, and easy-to-use"; it requires notice and cancellation, not a refund of a prepaid term | FLAGGED (negative claim, established by reading the whole section) | https://california.public.law/codes/ca_bus_and_prof_code_section_17602 | "it shall provide another cost-effective, timely, and easy-to-use mechanism for cancellation that shall be described in the acknowledgment" — no refund clause appears anywhere in § 17602, so the article may say the notice is a calendar prompt, never a safety net |
| 10 | C+R Research survey | The survey's figures are 2022 fieldwork, page last updated 2024-07-26 — every use must be dated | VERIFIED | https://www.crresearch.com/blog/subscription-service-statistics | "Last Updated: July 26, 2024 … Subscription Service Statistics and Costs 2022" |

**Claims REMOVED:** none. **Claims FLAGGED at claim level:** 1 (row 9, a negative claim established by reading the section, not a number).

## Authorised desk arithmetic (inputs printed; language must say "desk arithmetic")

- Break-even month = annual price ÷ monthly price. Fastmail: 60 ÷ 6 = **10 of 12**; 114 ÷ 6 = **19 of 24**; 168 ÷ 6 = **28 of 36**. Backblaze: 8.25 × 12 = 99, 99 ÷ 9 = **11 of 12**; 189 ÷ 9 = **21 of 24**.
- Discounts against the monthly rate: Fastmail 12 months 12 ÷ 72 = **16.7%**; 24 months 30 ÷ 144 = **20.8%**; 36 months 48 ÷ 216 = **22.2%**. Backblaze 12 months 9 ÷ 108 = **8.3%** (one month, not two); 24 months 27 ÷ 216 = **12.5%**.
- Forfeit if abandoned at month 12: Fastmail 24-month rung 114 − 72 = **$42**; 36-month rung 168 − 72 = **$96**; 12-month rung at month 6, 60 − 36 = **$24**.
- Monthly cost of the ladder's 12-month rung, Backblaze: 108 − 9 = **$99** (the page prints $8.25/mo and a $9 annual saving, not the $99 total).

## Drafter rulings

1. **The ladder is a price page, not a measurement.** Rows 3–6 are vendor claims about their own prices; the article must attribute them to the page and must not present a vendor's discount as a market average.
2. **The survey is dated and self-reported.** Every use of $86 / $219 / 42% carries the 2022 vintage and the word "survey"; the numbers describe respondents, not readers.
3. **The statute is California's and covers consumers there.** Never generalise it to "the law requires" or to any other jurisdiction; row 8 is the string that constrains the sentence.
4. **No refund claim.** § 17602 requires notice and a cancellation path; it does not require a refund. The catch may say the notice is "a calendar prompt and not a safety net" and nothing stronger.
5. **"Two months free" is a shape, not a universal.** It is exactly true of Fastmail's 12-month rung (16.7%) and Google One's 16% ceiling; Backblaze's 8.3% is closer to one month, and the article says so.
6. **The break-even is the article's own division.** It is arithmetic the reader can re-run; label it as such where it appears and never present it as a figure the vendor published.
