---
title: "Double Orders, Cut 13.4%: Not 30%"
vertical: meio_working_capital_tco
kind: evergreen
archetype: evergreen
evergreen: true
persona: ops_leader
one_big_thing: "Doubling replenishment frequency halves the order interval, not the supplier's lead time, so the safety-stock cut runs 29.3% at zero lead time, 13.4% on a one-week replenishment, 4.3% on 35 days and 2.0% on a 90-day import — and the saving that does scale is cycle stock, which halves with the order quantity and pays only when one more purchase order costs less than the saving it buys."
date: 2026-11-02
slug: your-30-inventory-cut-is-13-4
---

<!-- lead -->
The slide says doubling your order frequency cuts safety stock 30%. The math is sound only because the source page says the step out loud: doubling the frequency halves the lead time [1]. A purchase order does not shorten a supplier's queue, so leaving the supplier's clock alone turns the same doubling into 13.4% on a one-week replenishment, 5.1% on four weeks, 4.3% on 35 days, and 2.0% on a 90-day import [2][3]. The buffer shrinks with the square root of the window it covers, and the inventory line that moves with the calendar is cycle stock, which halves when the order quantity halves [2].

<!-- tension -->

## The big picture:

A safety buffer covers an exposure window: the days between reviews plus the days the supplier takes to deliver. Both terms sit under one square root, so the buffer grows with the square root of the total, not with either term by itself [2]. Doubling order frequency halves the first term and leaves the second alone. The result depends on how much of the window was the review interval in the first place.

The 30% headline comes from the shelf case, where the 0.707 multiplier, the 30% cut, and the 41% result all come from the same halved-lead-time model [1]. In the page's own example, "the maximum delay time between replenishments is 1 day; hence, the lead time is also 1 day" [1]. That describes a shop floor or same-day depot, not a part crossing an ocean, where the gap between orders is a rounding error against a 90-day clock.

I ran the same halving against a four-week supplier and the cut came out near 5.1%, not 30%—my guess is the slide survives because nobody does that [2]. Once the supplier needs a month or more, the order calendar is already a small share of the exposure window, and on an import it is close to nothing.

The second inventory line moves the other way: average cycle stock is about half the order quantity [2]. Halve the quantity and that balance halves, whatever the lead time does. On a fast mover, cycle stock is often the larger balance, so the calendar still matters—through quantity, not through the buffer.

## By the numbers

- **29.3% — The ceiling:** halving a weekly review to three and a half days trims the buffer 29.3% only when the supplier's lead time is zero, which is the shelf case the model was written on [1][2].
- **13.4% — One week of replenishment:** give the supplier a seven-day lead and the same doubling returns 13.4%; at 35 days it returns 4.3%, and on a 90-day import, 2.0% [2][3].
- **$722 — Cycle stock:** a part moving 12,000 units a year at $50, with a 25% carrying rate, holds $5,775 of average cycle stock on weekly orders; twice-weekly halves that and cuts the carrying bill by $722 a year [2].
- **$13.87 — Break-even per extra order:** $722 spread over 52 extra purchase orders is the most one more order can cost before the cadence change loses money [5].

<!-- tactical-insight -->

## What I'd watch:

I am watching the teams closest to this decision weigh the supplier's clock first, because it decides whether the order calendar is a lever or a rounding error. Where the whole lead time is under about ten days, the review interval is a large share of the exposure window, and halving it moves real money. On a four-week replenishment the same change is close to 5.1%, and on an import it is close to nothing [2][3].

The open question is what a receipt costs at the 2025 median of $21.76 an hour for shipping, receiving, and inventory clerks: fifteen minutes on the dock is $5.44 a line [5]. Freight minimums, invoice processing, and fixed dock shifts land on top, so the people closest to the decision are rerunning the $13.87 break-even before they approve a second weekly run.

The next answer sits in the order quantity, not the order count: average cycle stock is half the order [2]. A price break at the old weekly quantity is the trap in the other direction: order half as much twice as often, and the unit cost can rise by more than the carrying bill falls.

<!-- nuanced-takeaway -->

## The catch

Every anchor here except the wage is a software vendor's explainer, and the headline cut is a model, not a measurement. The page producing it is dated 2 February 2023 and signed by the planning vendor's chief operating officer; its 30% and 41% results are careful arithmetic, not field results [1]. Nothing in the fetched text was tested on a real network.

Lead-time variance swamps the calendar: a part with a ten-day lead time needs 104 units of buffer at a fixed lead. Add a three-day standard deviation to that lead and the same part needs 506, a 4.9× swing the order interval cannot touch [4]. If the goal is a smaller buffer, the supplier's reliability is the bigger lever.

There is also a unit trap inside the math, and it matters for planners copying the example. One review-period example labels its spread as weekly demand and then places a day-denominated window under the root, which overstates the buffer by about √7 [2]. A planner copying that shape should convert the spread first; the other explainer puts the rule in one line: "always use the same time unit for lead time and demand" [3].

I used to think the arithmetic was the hard part; the harder part is quoting a model without carrying its assumptions into the room. Ordering more often is a cadence call, and its size depends on the clock the part is on; that is a smaller claim, and a defensible one.

<!-- tldr -->

## At a glance

**The shift:** Ordering more often shortens the order interval, not the supplier's clock.
**The number:** The buffer saving is a square-root effect, so it shrinks as the lead time grows.
**The risk:** Cycle stock is the saving that scales, and one more order can spend it.

## Sources

[1] Arkieva, Sujit Singh (chief operating officer), "Effect of Change in Replenishment Frequency", 2 February 2023 — the 0.707 multiplier, the 30% and 41% results, the sentence that doubling frequency halves the lead time, and the shelf model in which the delay between replenishments is the lead time. https://blog.arkieva.com/replenishment-frequency
[2] Netstock, "How to Calculate Safety Stock Using 3 Methods" — the review-period formula that puts the order interval and the lead time under one square root, the 1.65 × 25 × √(7 + 14) worked example, and the definition of cycle stock as the stock consumed between replenishments. https://www.netstock.com/blog/safety-stock-meaning-formula-how-to-calculate
[3] AbcSupplyChain, "6 Best Safety Stock Formulas" — the review period listed first among the factors that make lead time uncertain, the 35-day average against a 40-day maximum with ten deliveries a year, the 427-piece buffer and 1,578-unit reorder point, and the one-line rule that lead time and demand share a time unit. https://abcsupplychain.com/safety-stock-formula-calculation
[4] User Solutions, "Safety Stock Calculation for Manufacturing" — the 104-unit fixed-lead result against the 506-unit result once a three-day standard deviation enters a ten-day lead time. https://usersolutions.com/blog/safety-stock-calculation
[5] O*NET OnLine, 43-5071.00 Shipping, Receiving, and Inventory Clerks — median wages of $21.76 an hour and $45,260 a year in the 2025 wage table. https://onetonline.org/link/summary/43-5071.00
