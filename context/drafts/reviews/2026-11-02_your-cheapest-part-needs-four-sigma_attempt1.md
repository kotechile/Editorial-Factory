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
A $200 item with a 12% margin and a 45-day lead time can defend a service level of 79.6%, which the standard normal table reads as 0.83 deviations. A blanket 98% target sits at 2.05 deviations, so that item carries about 2.5 times the buffer its own cost arithmetic justifies. A $0.60 bracket whose shortage stops a line is the opposite case: with a $30 allocated stop cost, its ratio is 99.99%, or 3.73 deviations—four sigma. A single customer target hides both ends of that spread.

<!-- tension -->

## The big picture:

Every service target is a probability, and every point of it is bought with stock. The cover cost is what holding a unit across its lead time costs: the annual carrying rate spread across the days of cover [4]. The miss cost is the margin lost on a short unit, plus whatever penalty a contract attaches to a late line [5].

Their ratio—the miss cost on top, the miss cost plus the cover cost underneath—is the target an item can defend [1][2]. At a 25% carrying rate, a $200 unit held for 45 days costs $6.16 to hold [4]. A 12% margin on that unit is $24, so the ratio is 24 divided by 30.16, or 79.6%.

The standard normal table converts that probability into a multiple of the standard deviation: 1.645 at 95%, 2.326 at 99%, and 3.090 at 99.9% [2]. The ladder is not linear: moving from 95% to 99% costs roughly 40% more safety stock than the lower rung does [3]. That is the arithmetic a blanket target spends without printing a bill.

A customer clause or retail programme can fix one order-level number, and planning systems copy that number onto every item in the catalogue. The margin-rich item and the margin-thin one then carry the same buffer, so the scorecard looks healthy while inventory money sits in the wrong rows. What I notice is how little of that displacement shows up in any weekly report.

## By the numbers

- **25% — Carrying rate:** $1,000,000 of inventory carrying $250,000 a year is a 25% rate [4]. Spread across the days of cover, it is the cover-cost leg of every ratio below.
- **0.83 — A 12% item's factor:** a $200 unit with $24 of margin and $6.16 of cover cost returns 24 ÷ 30.16 = 79.6%, which the normal table turns into 0.83 deviations [2][4].
- **2.5 — Over-funding at 98%:** the blanket target sits at 2.05 deviations, so this item carries 2.5 times the buffer its own two costs justify [2].
- **40% — The 95-to-99 step:** 2.326 against 1.645 is a bigger multiple, and the published description is roughly 40% more safety stock [2][3].

<!-- tactical-insight -->

## What I'd watch:

- **The ratio moves to the item, not the deck.** The teams getting this right run the two costs per item once a year and let the target follow the ratio. My question is whether that item-level number survives the budget review or gets averaged back into one target by the time it reaches finance.
- **The cheapest part on the line gets the highest target, not the lowest.** A $0.60 bracket whose shortage stops a line is not a margin problem: at $30 of allocated stop cost per miss, the ratio returns 99.99%, which is 3.73 deviations, or four sigma. A blanket 98% target holds 2.05 deviations, about 55% of that buffer. This is the row where a uniform number is quietly wrong in the other direction.
- **Where the miss cost comes from the contract.** A deduction on late lines belongs in the numerator [5], and its effect is uneven. A hypothetical $10 charge on a $200 unit lifts the 12% item from 79.6% to 84.7%, a move from 0.83 to 1.02 deviations. It pushes a 30% margin item from 90.7% to 91.9%.
- **The supply mode, before the stock.** Four sigma on a lumpy part is usually a signal to change how it is supplied—consignment, a line-side kanban, a second source—not to buy the buffer the formula asks for. The open question is which of those moves a team makes first.
- **The fully loaded cover cost.** The ratio is only as honest as the rate behind it; the [carrying cost rate](/inventory-carrying-cost-rate/) is where teams under-price their own buffer.

<!-- nuanced-takeaway -->

## The catch

The ratio returns a cycle service level: the chance an item is in stock at the end of its lead time. It is not the fill rate a customer scores, which lands higher on multi-unit orders, and the two should never be swapped in a review slide.

The contract floor does not bend: a clause that charges a deduction on a late line fixes the target whatever the arithmetic says, and no ratio overrides it. The honest job of the arithmetic is narrower. It shows which items the clause over-serves and which it leaves short, so the argument that reaches the customer is about the ones it leaves short.

The model also assumes demand that behaves roughly normally, which is generous with lumpy parts and long ocean lead times. My reading is that the ratio is a strong first cut and a weak final answer for the tail. There, the right move is a different supply mode rather than a better number.

<!-- tldr -->

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
