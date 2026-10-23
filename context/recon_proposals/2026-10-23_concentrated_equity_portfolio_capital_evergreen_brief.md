# Evergreen Brief: concentrated_equity_portfolio_capital — 2026-10-23
**Archetype:** evergreen
**Vertical:** concentrated_equity_portfolio_capital
**Persona:** financial_architect
**Decision the reader is facing:** Whether to harvest the paper loss on employer shares after a down-vest or hold through the drawdown — because the deduction reaches salary income at only $3,000 a year, while keeping it means not holding the same stock for a 61-day band that starts 30 days before the sale.
**Durability:** The 61-day band and the $3,000 / $1,500 ceiling are statutory (26 U.S.C. § 1091; § 1211(b)) and are not re-indexed annually, so the mechanic holds for every tax year until Congress amends the code; the regulation is current as of the eCFR edition dated 21 October 2026, and the dollar figures are as of the 2026 tax year.
**De-dup:** `2026-10-23_why-your-swap-died-at-25` is this vertical's only prior artifact (same day) and it argues the § 351 / § 721 wrapper question — a contribution of appreciated shares to a pooled vehicle and the 25% single-issuer test that decides who qualified. This brief is a different statute and a different decision: § 1091 disallows a loss inside a 61-day band and § 1211(b) caps what that loss can offset, which is the arithmetic of harvesting a loss on a position the reader already holds. Cross-vertical check: `grep -ril "wash sale\|wash-sale\|1091" published/ context/recon_proposals/ context/drafts/` returned nothing, so no artifact in the corpus has touched either statute.
**Thesis:** Harvesting a loss on employer stock is not a tax optimisation that keeps your exposure — the 61-day band forbids holding the same stock across it, and the ceiling against salary is $3,000 a year, so a six-figure loss is a two-decade deduction paid for with a real exit from the position.

**Lead:** The vertical's own `primary_angles` row 4 — "Exchange funds vs. systematic tax-loss harvesting for $500k+ single-stock tech positions" — read for its harvesting leg only (the exchange-fund leg belongs to today's news artifact and is dropped here), combined with the `financial_architect` persona's stated wants (RSU vest-vs-hold math, asset location). The specific material is the three statutory sentences that decide it: the band runs from 30 days before the sale to 30 days after it, the loss is disallowed rather than lost (it rides into the basis of the replacement shares), and the claim against non-capital income is the lesser of $3,000 ($1,500 married filing separately) or the net loss. GSC returned 0 striking-distance queries for this vertical (`2026-10-23_gsc_concentrated_equity_portfolio_capital_opportunities.md`) — thin impressions on a young site, a bonus signal only and never a veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | eCFR, 26 CFR § 1.1091-1 (Losses from wash sales of stock or securities), edition current as of 2026-10-21 | https://www.ecfr.gov/current/title-26/section-1.1091-1 | 2026-10-23 | 61-day period — the band runs from 30 days before the sale to 30 days after it, and a loss is disallowed if within it the taxpayer acquired, or entered a contract or option to acquire, substantially identical stock or securities | primary rule text (regulation) |
| 2 | IRS, Topic no. 409 Capital gains and losses | https://www.irs.gov/taxtopics/tc409 | 2026-10-23 | $3,000 — the excess capital loss claimable against other income is the lesser of $3,000 ($1,500 if married filing separately) or the total net loss shown on Schedule D | primary rule text (agency guidance) |
| 3 | Cornell LII, 26 U.S.C. § 1211 — Limitation on capital losses | https://www.law.cornell.edu/uscode/text/26/1211 | 2026-10-23 | $3,000 — for a taxpayer other than a corporation, losses are allowed only to the extent of gains, plus the lower of $3,000 ($1,500 if married filing separately) or the excess of losses over gains | primary rule text (statute) |
| 4 | Investor.gov (SEC), glossary: Wash Sales | https://www.investor.gov/introduction-investing/investing-basics/glossary/wash-sales | 2026-10-23 | 30 days before or after the sale — a wash sale occurs when you sell or trade securities at a loss and, within 30 days before or after the sale, you buy substantially identical securities | primary rule text (regulator explainer) |

Supporting citations held in prose and in `## Sources` rather than as gate rows, because their paragraphs carry no figure a matcher can lead on: IRS Publication 550's "Substantially identical" paragraph ("Ordinarily, stocks or securities of one corporation are not considered substantially identical to stocks or securities of another corporation", https://www.irs.gov/publications/p550), and 26 U.S.C. § 1091(d) on the unadjusted basis of the replacement shares (https://www.law.cornell.edu/uscode/text/26/1091).

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The 61-day band and the $3,000 ceiling: what harvesting a loss on employer stock actually pays | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| 2026 § 415(c) $72,000 mega-backdoor room: what the plan document must permit before the ceiling is reachable | 8 | 6 | 9 | 9 | 7.9 | dropped — the load-bearing figure ($72,000 for 2026) is replaced when the 2027 limits take effect on 1 January 2027, so its value expires inside the 90-day line and it belongs to the news track |
| 10b5-1 cooling-off clock (90 days, capped at 120, 30 days for non-insiders) | 9 | 9 | 4 | 8 | 7.6 | dropped — `ecfr.gov` 17 CFR § 240.10b5-1 fetches, but `sec.gov` answers HTTP 403 to the verifier and Investor.gov's 10b5-1 glossary page (2,447 chars) carries no figures, so the topic cannot reach the two-host floor |
| RSU vest fallacy: holding post-vest shares is buying company stock on margin | 9 | 9 | 5 | 6 | 7.5 | dropped — no primary source prices the margin the analogy invokes (broker margin-rate pages are client-rendered or blocked), so the thesis would rest on an unsourced interest rate |
| Exchange funds vs. systematic tax-loss harvesting for $500k+ single-stock positions | 8 | 8 | 8 | 8 | 8.0 | refused outright under the de-dup rule, not on score — the exchange-fund leg is the argument of `2026-10-23_why-your-swap-died-at-25`, published today; this run keeps only the harvesting leg, which that piece does not touch |

## Gate result

<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=4 decision="sha1:182efc1978" dedup="matched a prior artifact: 2026-10-23_why-your-swap-died-at-2" window_days=180 checked_at=2026-10-23T17:03:44+00:00 -->
<!-- evergreen-gate:end -->
