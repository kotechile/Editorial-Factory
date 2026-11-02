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
The claim travels well: double your orders, the slide says, and safety stock falls 30%. The math is right, because the page that prints it also prints the step doing the work — doubling the frequency halves the lead time [1]. A purchase order does not shorten a factory's queue. Leave the supplier's clock where it is, and the same doubling returns 13.4% on a one-week replenishment, 4.3% on a 35-day one and 2.0% on a 90-day import. The buffer shrinks only with the square root of the window it covers [2][3]. The inventory cut that scales with the order calendar is a different line on the same sheet: the cycle stock bought in each order, which halves when the order quantity halves.

<!-- tension -->

## The big picture:

A safety buffer is sized to cover an exposure window: the days between reviews plus the supplier's own lead time. Both terms sit inside one square root, so the buffer grows with the square root of their sum rather than with either term alone [2]. Doubling the order frequency halves the first term and leaves the second untouched. How much of the clock the order interval was therefore decides the whole result.

The headline cut is the case where the interval was all of it. In the model that produces it, doubling the frequency is treated as halving the lead time, and the same page's shelf example says why: "the maximum delay time between replenishments is 1 day; hence, the lead time is also 1 day" [1]. That is a fair description of a shop floor, or of a same-day delivery from your own depot. On an item crossing an ocean, the gap between two orders is a rounding error on a nine-week clock.

My read is that the figure survives the trip to a finance review because nobody re-runs it against their own lead time. Halve a weekly review to three and a half days and the cut is already single digits once the supplier needs a month [2][3]. Set the same change against a 90-day import and it is worth a fraction of one point of stock.

The second line on the sheet moves the other way. Average cycle stock is about half the order quantity, so halving the quantity halves it whatever the lead time does [2]. On a fast mover that stock is the larger of the two balances, which is why the order calendar still matters. It matters through quantity, not through the buffer.

## By the numbers

- **29.3% — The ceiling:** halving a weekly review to three and a half days cuts the buffer 29.3% only when the supplier's own lead time is zero, which is the shelf case the model was written on [1][2].
- **13.4% — One week of replenishment:** give the supplier a seven-day lead and the same doubling returns 13.4%; at 35 days it is 4.3%, and on a 90-day import, 2.0% [2][3].
- **$722 — Cycle stock:** a part moving 12,000 units a year at $50, held at a 25% carrying rate, sits on $5,775 of average cycle stock with weekly orders; twice-weekly halves that and cuts the carrying bill by $722 a year [2].
- **$13.87 — Break-even per extra order:** $722 spread over 52 extra purchase orders, the most one more order can cost before the cadence change loses money [5].

<!-- tactical-insight -->

## What I'd watch:

I watch the supplier's clock first, because it decides whether the order calendar is a lever or a rounding error. Where the whole lead time is under about ten days, the interval is a large share of what the buffer covers, and halving it moves real money. On a four-week replenishment the same change is small, and on an import it is close to nothing [2][3].

What a receipt costs is the other half of the decision. At the 2025 median of $21.76 an hour for shipping, receiving and inventory clerks, fifteen minutes on the dock is $5.44 a line [5]. Freight minimums, invoice handling and the dock's fixed shifts land on top, which is why the break-even above is worth running before a second weekly run is approved.

The saving itself sits in the order quantity. Average cycle stock is half the order, so the quantity that matters is the one on the purchase order, not the number of them [2]. A price break sitting at the weekly quantity is the trap in the other direction: order half as much twice as often, and the unit cost can rise by more than the carrying bill falls.

One level down the building, the same trade is already visible: [a shelf holding a week of stock costs ten miles of walking](/your-golden-zone-costs-10-miles/), while a face refilled every hour swamps the crew doing the refilling.

<!-- nuanced-takeaway -->

## The catch

Every anchor here except the wage is a software vendor's explainer, and the headline cut is a model, not a measurement. The page that prints it is dated 2 February 2023 and signed by the planning vendor's own chief operating officer, which makes it careful math rather than a field result [1]. Nothing in the fetched text was tested on a real network.

Lead-time variance also swamps the calendar. Take a part with a ten-day lead time: at a fixed lead it needs 104 units of buffer, and at a three-day standard deviation on that lead it needs 506, a 4.9× swing the order interval cannot touch [4]. If the goal is a smaller buffer, the supplier's reliability is the bigger lever, and no planning calendar can pull it.

There is a unit trap inside the math. The review-period page labels its spread as weekly demand and then puts a day-denominated window under the root, which overstates a buffer by about √7 [2]. A planner copying the shape of that example onto their own numbers should convert the spread first, and the second explainer says so in one line: "always use the same time unit for lead time and demand" [3].

I keep circling the evidence, because a model that is right about its own assumption is still easy to quote as a promise. The honest position is narrower. Ordering more often is a cadence call, and its size depends on the clock the part is actually on.

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
