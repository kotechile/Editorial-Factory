# Verified Brief: meio_working_capital_tco — 2026-11-02

Companion to `2026-11-02_meio_working_capital_tco_evergreen_brief.md` (evergreen track — no 30-day window,
no virality Judge). Every row below was fetched on 2026-11-02 through the same fetcher the evergreen gate
uses (`citation_hub_dossier.fetch_source`, `Mozilla/5.0 (compatible; EditorialFactorySourceVerifier/1.0)`),
and each figure was checked against the retrieved text, not against a search snippet. The gate PASSed on
the first run: rows=5, fetched=5, sources=5, hosts=5, dedup=`2026-10-26_your-15-air-rule-195-break-even`.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | The claim under audit | Doubling replenishment frequency is said to cut safety stock 30%, by multiplying the old buffer by 1/√2 = 0.707 | VERIFIED | https://blog.arkieva.com/replenishment-frequency | "New SS = (1/√2) * Original SS = 0.707 * Original SS. So, if the replenishment frequency is doubled, one would need 30% less inventory as safety stock assuming the desired service level does not change. By similar math, one can also see that if the replenishment frequency is halved, one would need 41% more inventory as safety stock." |
| 2 | The assumption doing the work | The same page states the step explicitly: doubling frequency halves the lead time | VERIFIED | https://blog.arkieva.com/replenishment-frequency | "Thus, if the lead time is halved (which is what happens when replenishment frequency is doubled), then the new SS = Z-score* σ D *√(L/2)" |
| 3 | The page's own model | Its shelf example defines the lead time AS the interval between replenishments — the world the 30% is true in | VERIFIED | https://blog.arkieva.com/replenishment-frequency | "In this model, the maximum delay time between replenishments is 1 day; hence, the lead time is also 1 day." |
| 4 | Review-period model | Safety stock is computed over the review interval plus the lead time, both inside one square root | VERIFIED | https://www.netstock.com/blog/safety-stock-meaning-formula-how-to-calculate | "Desired service level: 95% (Z = 1.65) Standard deviation of weekly demand: 25 units Supplier lead time: 14 days Safety Stock = 1.65 × 25 × √(7 + 14) ≈ 165 units For businesses with weekly ordering cycles, this formula accounts for the additional variability during both the review period and lead time." |
| 5 | Review period listed as lead-time | A second explainer lists the order interval first among the factors that make lead time uncertain | VERIFIED | https://abcsupplychain.com/safety-stock-formula-calculation | "There are also supply hazards: specifically, lead time uncertainty. Indeed, there are many factors impacting the total lead time : Review period: how often you order … Transportation time / transit time … Customs" |
| 6 | A real lead-time case | A worked case runs a 35-day average lead time against a 40-day maximum, ten deliveries a year, and lands a 427-piece buffer and a 1,578-unit reorder point | VERIFIED | https://abcsupplychain.com/safety-stock-formula-calculation | "The average lead time was 35 days , and the maximum lead time was 40 days . Applying the formula, we have a Safety Stock of 427 pieces … Here we have a Reorder point of 1578 units." |
| 7 | The unit rule | The same page warns that lead time and demand must share a time unit | VERIFIED | https://abcsupplychain.com/safety-stock-formula-calculation | "Make sure to always use the same time unit for lead time and demand." |
| 8 | What dwarfs the cadence | Lead-time variance, not the order interval, dominates the buffer: 104 units with a fixed 10-day lead, 506 with a 3-day standard deviation on it | VERIFIED | https://usersolutions.com/blog/safety-stock-calculation | "Safety Stock = 1.65 x sqrt(4,000 + 90,000) Safety Stock = 1.65 x sqrt(94,000) Safety Stock = 1.65 x 306.6 = 506 units. Notice the dramatic difference: 506 units vs. 104 units. The lead time variability (sigma_L = 3 days) dominates the calculation." |
| 9 | Labour anchor for a receipt | Shipping, receiving and inventory clerks: median $21.76 an hour, $45,260 a year (2025 wage table) | VERIFIED | https://onetonline.org/link/summary/43-5071.00 | "Median wages (2025) $21.76 hourly, $45,260 annual" |
| 10 | Buffer cut by supplier lead time (desk arithmetic) | Halving the review interval from 7 days to 3.5 cuts the buffer 29.3% at a zero supplier lead time, 13.4% at 7 days, 4.3% at 35 days and 2.0% on a 90-day clock | DERIVED | rows 4, 5, 6 | 1 − √((T/2 + L)/(T + L)) with T = 7. L=0: 1 − √0.5 = 0.29289. L=7: 1 − √(10.5/14) = 0.13397. L=35: 1 − √(38.5/42) = 0.04257. L=83: 1 − √(86.5/90) = 0.01956. The 29.3% end agrees with row 1's 1/√2 to the decimal, which is the audit: the published 30% is this formula at L = 0. |
| 11 | Cycle-stock saving (desk arithmetic) | 12,000 units a year at $50 with a 25% carrying rate holds $5,775 of average cycle stock on weekly orders; twice-weekly halves it and cuts the carrying bill $722 a year | DERIVED | rows 4, plus the vertical's own established 25% carrying rate (`2026-10-05_inventory-cost-rate` is the published treatment; the 20–30% band is not re-rowed here) | Weekly order 12,000 ÷ 52 = 230.8 units; average cycle stock 115.4 units × $50 = $5,769.23; carrying at 25% = $1,442.31. Half the quantity gives $2,884.62 and $721.15. Difference $721.15. Average cycle stock is half the order quantity — the identity Netstock states in words ("cycle stock is your regular inventory that you consume between replenishments") and the article performs visibly. |
| 12 | Break-even per extra order (desk arithmetic) | $721.15 ÷ 52 extra orders = $13.87 — the most one more purchase order can cost before the cadence change loses money | DERIVED | rows 5, 9, 11 | 721.15 ÷ 52 = 13.868. 15 minutes of a receiving clerk at $21.76 an hour is $5.44, so the labour alone is under the line and freight minimums, dock time and invoice handling sit on top of it. |
| 13 | Provenance of the 30% | The 30% is a model result on a planning-software vendor's page dated 2 February 2023, not a measurement, and its author is the company's own COO | FLAGGED | https://blog.arkieva.com/replenishment-frequency | Byline and dateline read out of the fetched page ("By Sujit Singh February 2nd, 2023"; "About the Author: Sujit Singh As COO of Arkieva"). The article may not write "companies that doubled frequency cut 30%" or attribute the figure to a study. It may write that the arithmetic is right and the assumption is narrow. |
| 14 | Evidence quality | Four of the five anchors are software-vendor or consultancy explainers; only the wage is a measured government series | FLAGGED | rows 1, 4, 5, 8, 9 | Label the 30%, the 165 units, the 427 pieces and the 506 units as the pages' own illustrations. The load-bearing claim is the identity in row 10, computed from the cited model, not any vendor's outcome. |
| 15 | Unit-mixing trap on the cited page | Row 4's page labels its spread as *weekly* demand and then puts a day-denominated (7 + 14) under the root — copying that shape overstates a buffer by √7 | FLAGGED | rows 4, 6, 7 | √7 = 2.646. Carry as a warning with the AbcSupplyChain sentence (row 7) as the rule, and never print 165 units as a measured quantity. |
| 16 | Field anecdote | $85M of stock across four hubs, 26% holding-cost cut, 99.4% service kept | UNVERIFIED (desk field note — illustration only) | `context/growth_os/customer-truth.md` §meio_working_capital_tco Anecdote 1 | Optional at most; if used, attribute as the desk's own field note and attach no arithmetic to it. |

## Drafter's constraints

- **The title carries 30% and 13.4%, so both must appear in the lead paragraph** — and 13.4% must be written
  with its one-week precondition in the same sentence, never as a general result.
- **Do not write that the vendor is wrong.** Its arithmetic is correct and its own shelf example is honest
  about the model (row 3). The article's claim is narrower and stronger: the 30% holds where the order
  interval *is* the clock, so quoting it for a supplier with a four-week transit imports an assumption.
- **Every derived figure shows its two inputs in the sentence that uses it** (rows 10–12). No bare "you'll
  save 30%" and no bare "13.4%".
- **The ladder is 29.3 / 13.4 / 4.3 / 2.0 at 0 / 7 / 35 / 83 supplier days.** If a rung is dropped the
  argument goes with it; the 35-day rung is the one the cited case supports (row 6).
- **Money budget:** $5,775, $722 and $13.87 live in `By the numbers`; $5.44 may appear once in the tactical
  section. Do not restate $722 or $13.87 in the catch or in `At a glance`.
- **One inline internal link, already probed 200 on 2026-11-02:**
  `[a shelf holding a week of stock costs ten miles of walking](/your-golden-zone-costs-10-miles/)` — same
  vertical, same front, and the destination's own subject is days of cover at the pick face.
- **No hands-on claim.** This desk has no warehouse; write "planners I have watched" only for what the
  cited pages describe, never for a test the desk ran.
- **At a glance stays figure-free** so the shape gate sees each number in at most two sections.
