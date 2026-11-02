---
title: "Your 98% Target Hides Four Sigma"
vertical: sales_order_service_level_otif
kind: evergreen
archetype: evergreen
evergreen: true
persona: ops_leader
one_big_thing: "A fill target is a ratio — miss cost divided by miss cost plus cover cost — so a blanket 98% keeps about 2.5 times the buffer a 12%-margin item can pay for while holding barely half the buffer a cheap part that stops a line justifies."
date: 2026-11-02
slug: your-cheapest-part-needs-four-sigma
---

<!-- lead -->
A $200 bracket with a 12% margin and a 45-day lead time gets pushed toward a 98% fill target, though its own cost ratio asks for only 0.83 deviations of safety stock. That gap is about 2.5 times the buffer the item can pay for. At the other end of the same target sits a $0.60 bracket that can stop a line, and its $30 miss cost demands roughly four sigma. One retail number hides this entire spread because one programme sets it once and every planning system copies it outward.

## The big picture:

Every fill target is a probability, and every point of it is bought with stock. Two costs set the price. The cost of cover is what you pay to hold a unit across its lead time — the annual carrying rate prorated to the days of cover [4]. The cost of a miss is the margin lost on the short unit plus whatever penalty a contract attaches to a late line [5].

Their ratio is the target an item can defend: miss cost divided by miss cost plus cover cost [1][2]. At a 25% carrying rate, a $200 unit held for 45 days costs $6.16 to carry [4]. A 12% margin on that unit is $24, so the ratio is 24 divided by 30.16, or 79.6%.

The standard normal table turns that probability into a multiple of the standard deviation: 1.645 at 95%, 2.326 at 99%, and 3.090 at 99.9% [2]. The table is not linear, which is why moving from 95% to 99% costs roughly 40% more safety stock than the lower rung does [3]. That is the arithmetic a blanket target spends without ever printing the bill.

Retail programmes grade at order level and fix a single number, and planning systems copy that number onto every item in the catalogue. The margin-rich item and the margin-thin one then carry the same buffer. The scorecard looks healthy while inventory money sits in the wrong rows. I keep coming back to how little of that displacement shows up in any weekly report.

## By the numbers

- **25% — Carrying rate:** $1,000,000 of inventory carrying $250,000 a year is a 25% rate [4], and prorated across the days of cover it is the overage leg of every ratio below.
- **0.83 — A 12% item's factor:** a $200 unit with $24 of margin and $6.16 of cover cost returns 24 ÷ 30.16 = 79.6%, which the normal table turns into 0.83 deviations [2][4].
- **2.5 — Over-funding at 98%:** the blanket target sits at 2.05 deviations, so this item carries 2.5 times the buffer its own two costs justify [2].
- **40% — The 95-to-99 step:** 2.326 against 1.645 is the same ladder rung two publishers describe, one as a ratio and one as roughly 40% more stock [2][3].
- **98.5% — Vendor model:** Lokad's own milk-pack example, with stock-out cost at three times gross margin, returns about 98.5% as its optimized result, not the simple ratio [5].

## What I'd watch:

- **The ratio moves to the item, not the deck.** Teams getting this right run the two costs per item once a year and let the target follow the ratio. What I'd watch is whether the number is defended item by item in the budget review or averaged back into one target by the time it reaches finance.
- **The cheapest part on the line gets the highest target, not the lowest.** A $0.60 bracket whose shortage stops a line is not a margin problem at all: at $30 of allocated stop cost per miss, the ratio returns 99.99%, which is 3.73 deviations, or four sigma. The blanket target holds barely half that buffer, so this is the row where a uniform number is quietly wrong in the other direction.
- **Where the miss cost comes from the contract.** A deduction on late lines belongs in the numerator, and its effect is uneven. A $10 charge on a $200 unit lifts the 12% item from 79.6% to 84.7%, or 1.02 deviations, and leaves a 30% item almost where it was [5].
- **The supply mode, before the stock.** Four sigma on a lumpy part is usually a signal to change how it is supplied — consignment, a line-side kanban, a second source — not to buy the buffer the formula asks for.
- **The fully loaded cover cost.** The ratio is only as honest as the rate behind it; the [carrying cost rate](/inventory-carrying-cost-rate/) is where teams under-price their own buffer by a factor of three.

## The catch

The ratio returns a cycle service level, the chance an item is in stock at the end of its lead time. It is not the fill rate your customer scores, which lands higher on multi-unit orders, and the two should never be swapped in a review slide [2].

What I find hard to square is the contract floor. A clause that charges a deduction on a late line fixes the target whatever the arithmetic says, and no ratio overrides it. The honest job of the arithmetic there is narrower than it sounds: it shows which items the clause over-serves and which it leaves short, so the argument to take to the customer is about the ones it leaves short.

The model also assumes demand that behaves roughly normally, which is generous with lumpy parts and long ocean lead times. The ratio is a strong first cut and a weak final answer for the tail, where the right move is a different supply mode rather than a better number.

## At a glance

**The shift:** Service targets are being derived per item from the two error costs instead of copied from one customer clause.
**The number:** 2.5 times the buffer a 12%-margin item can pay for.
**The risk:** A contract floor still binds, and the cheap part that stops a line needs a supply-mode change, not more stock.

## Sources
[1] Wikipedia — "Newsvendor model", critical fractile and worked example: https://en.wikipedia.org/wiki/Newsvendor_model
[2] NIST/SEMATECH e-Handbook of Statistical Methods, § 1.3.6.7.1, Cumulative Distribution Function of the Standard Normal Distribution: https://itl.nist.gov/div898/handbook/eda/section3/eda3671.htm
[3] MetricGate — "Safety Stock – Newsvendor Service Level" (calculator documentation, page dated May 05, 2026): https://metricgate.com/docs/safety-stock-newsvendor
[4] SourceDay — "Inventory Holding Costs: Formula, Examples, and How to Reduce": https://sourceday.com/blog/inventory-holding-costs
[5] Lokad — "Optimal Service Level Formula (Supply Chain)", last revised January 2012: https://www.lokad.com/service-level-definition-and-formula
