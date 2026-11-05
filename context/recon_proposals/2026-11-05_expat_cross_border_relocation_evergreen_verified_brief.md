# Verified Brief: expat_cross_border_relocation — 2026-11-05 (evergreen)

**Angle type:** evergreen (Loop 1E). No news gate, no virality score — the floor was
`scripts/evergreen_gate.py` (PASS, 6 rows, 3 hosts: govinfo.gov, irs.gov, greenbacktaxservices.com).

**Topic.** The fund wrapper a cross-border reader purchases in their host country is a passive foreign
investment company (PFIC) to the United States, and the default rule taxes the holding at ordinary
rates with an interest charge rather than at capital-gain rates.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| C1 | Definition | A foreign corporation is a PFIC if 75 percent or more of its gross income is passive income, or at least 50 percent of its assets produce passive income. | VERIFIED | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partVI-subpartD-sec1297.htm | "the term "passive foreign investment company" means any foreign corporation if— (1) 75 percent or more of the gross income of such corporation for the taxable year is passive income, or (2) the average percentage of assets … is at least 50 percent." — 26 U.S.C. § 1297(a) |
| C2 | Distributions | An excess distribution is the amount received in the year above 125 percent of the average received in the three preceding years. | VERIFIED | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partVI-subpartA-sec1291.htm | "The term "total excess distribution" means the excess (if any) of— (i) the amount of the distributions in respect of the stock received by the taxpayer during the taxable year, over (ii) 125 percent of the average amount received in respect of such stock by the taxpayer during the 3 preceding taxable years" — 26 U.S.C. § 1291(b)(2)(A) |
| C3 | Mechanics | The excess distribution is spread ratably across every day of the holding period, and only the current-year slice is ordinary income now. | VERIFIED | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partVI-subpartA-sec1291.htm | "the amount of the excess distribution shall be allocated ratably to each day in the taxpayer's holding period for the stock" — 26 U.S.C. § 1291(a)(1)(A) |
| C4 | Rate | Each earlier-year slice is taxed at the highest rate of tax in effect for that year under section 1 or 11. | VERIFIED | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partVI-subpartA-sec1291.htm | "by the highest rate of tax in effect for such taxable year under section 1 or 11, whichever applies" — 26 U.S.C. § 1291(c)(2) |
| C5 | Interest | An interest charge is added, computed with the rates and method for underpayments under section 6621. | VERIFIED | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partVI-subpartA-sec1291.htm | "shall be determined … by using the rates and method applicable under section 6621 for underpayments of tax for such period" — 26 U.S.C. § 1291(c)(3)(A) |
| C6 | Sale | The entire gain on a sale of the fund is treated as an excess distribution. | VERIFIED | https://www.irs.gov/instructions/i8621 | "The entire amount of gain from the disposition of a section 1291 fund is treated as an excess distribution." — Instructions for Form 8621 (12/2025) |
| C7 | Filing | A separate Form 8621 must be filed for each PFIC held, directly or indirectly. | VERIFIED | https://www.irs.gov/instructions/i8621 | "A separate Form 8621 must be filed for each PFIC in which stock is held directly or indirectly." — Instructions for Form 8621 (12/2025) |
| C8 | Filing exception | No Part I reporting if all PFIC stock totals $25,000 or less at year end ($50,000 joint) **and** no excess distribution is received and no gain is recognised — so the exemption ends in the year of the sale. | VERIFIED | https://www.irs.gov/instructions/i8621 | "A shareholder is not required to complete Part I with respect to a specific section 1291 fund if the shareholder meets the $25,000 exception on the last day of the shareholder's tax year and the shareholder does not receive an excess distribution from, or recognize gain on the sale or disposition of the stock of, the section 1291 fund." / "Shareholders filing a joint return have a combined threshold of $50,000 instead of $25,000" |
| C9 | Top rate | The highest rate of tax under section 1 was 37% for tax years 2018 through 2025. | VERIFIED | https://www.irs.gov/instructions/i8621 | table: "2018–2025 37%" — Instructions for Form 8621 (12/2025), rate table for line 16d |
| C10 | Comparison rate | A 20% capital-gains rate applies above the thresholds set for the 15% capital-gain rate. | VERIFIED | https://www.irs.gov/taxtopics/tc409 | "a capital gains rate of 20% applies to the extent that your taxable income exceeds the thresholds set for the 15% capital gain rate" — IRS Topic no. 409 |
| C11 | Elections (secondary) | A mark-to-market election taxes ordinary income with no interest charge, but the fund must trade on a qualified exchange; a QEF election needs the fund's own annual information. | VERIFIED (as cited — practitioner page, secondary) | https://www.greenbacktaxservices.com/knowledge-center/pfic/ | "Tax Rate: Ordinary income rates (up to 37%), but no interest charges Requirements: PFIC must be traded on a qualified exchange Election made on Form 8621 with your tax return Can be made in any year you own th…" |

**Rulings for the drafter.**
1. **Do not compute a saving.** 37% and 20% are two rates on two different bases; the interest charge sits
   on top of the 37% slice. The article may say the slice is taxed at the top ordinary rate instead of the
   20% capital-gain rate, and must not present the 17-point difference as the total cost of the wrapper.
2. **The $25,000 line is a reporting exemption, not a tax exemption** (C8). The year the reader sells is
   the year the exemption stops applying — that is the article's gotcha.
3. **The 125 percent test governs distributions; a sale is entirely an excess distribution** (C6).
4. **The rate is the top rate for the year each slice is allocated to**, not the top rate at sale (C4).
5. **No claim that a local fund "is" a PFIC as a matter of law for every reader.** The tests are C1; a fund
   that fails both tests is not one. Write "meets the tests" / "is a PFIC to the US", and note that most
   foreign index and mutual funds are held to meet them because they hold securities and earn dividends.
6. **Elections are prose under a verified row**, and C11 is a practitioner page: attribute it ("practitioner
   guides put it …") rather than stating the requirement as statute.
7. Nothing in the corpus (any vertical) previously argues this regime — grep for `PFIC|passive foreign`
   across `published/` and `context/recon_proposals/` returned no artifact.
