---
title: "Your 98% Fill Rate: 18% Don't Ship"
vertical: sales_order_service_level_otif
persona: ops_leader
archetype: evergreen
evergreen: true
one_big_thing: "Order fill is not a blurrier copy of line fill — it is roughly line fill raised to the power of the lines on the order, so a 98% line fill is an 81.7% complete-order rate on a ten-line basket, and the cheapest points to buy back sit in the few SKUs that appear on the most orders rather than in more stock spread evenly."
date: 2026-10-26
slug: your-98-fill-rate-18-dont-ship
---

<!-- lead -->
Your order desk reports a 98% fill rate. Your ten-line orders still arrive short.

Both figures are honest, because they count different things. Line fill counts the lines that shipped. Order fill counts only the orders that shipped complete, so one missing stock-keeping unit (SKU) fails the whole basket [1].

At 98% per-line stock, a ten-line order ships complete 81.7% of the time, which means 18.3% of them go out short. A twenty-line order manages 66.8% [1]. No push at the packing line closes that gap. The basket does it.

<!-- tension -->

## The big picture:

An order ships complete only if every line on it is in stock. So the order-level score is the line-level score raised to the power of the lines per order, and that power grows with every item the customer adds [1].

A five-line order with one shortage still scores 80% on lines. As baskets grow, the two numbers drift apart [1]. One firm put it best: customers do not feel a 94% line fill, they feel a box missing the one item they waited for.

My read is that this is the most under-reported number on the order desk. The firm that sells an "initial order fill rate" report calls it the best service metric there is, then notes it is rarely used, because many teams file it as a stock measure [2]. Those same teams report the line metric every morning.

Its client records show how wide the gap runs. A $30 million food business averaged 2.25 lines per order, and it called its backorder rate low. Then it logged an 88.5% complete-order rate in week one, with 11.5% of customers not shipped when they ordered [2].

A $25 million apparel company read a 10% backorder rate as 90% service. Its first season of order-level counting came in at 76.5% [2].

At 2.25 lines, the math alone predicts 78.9% from a 90% line fill, an 11-point drop [1][2]. What the firm measures is worse: complete orders run 10-15 points below the line rate [2]. That extra distance is where the money sits.

## By the numbers

- **88.5% — Order fill at a 2.25-line basket:** the first week of order-level counting at a $30 million food business whose backorder rate looked low [2].
- **76.5% — Order fill against a 90% assumption:** one apparel company's first season, after reading a 10% backorder rate as service [2].
- **96% — Line fill hiding an 82% order fill:** one industrial distributor, where three or four slow-moving items sat on a huge share of orders [3].
- **92-98% — Quoted healthy band:** the range one logistics provider gives for fill rate, which is an order-level number in its own definition [4].

<!-- tactical-insight -->

## What I'd watch:

The distributor case is the one to copy. Line fill was 96%. Order fill sat near 82%, and management was in a panic [3].

The cause was not broad stock trouble. Three or four slow-moving items showed up on a huge share of orders, and fixing those few lines moved the order number sharply [3].

That calls for a ranking most planning tools will not give you: SKUs sorted by how many orders they sit on, not by how badly they fill. A short line that appears on one order in fifty barely dents the score. The same short line on one order in three can hold it down by itself.

- **Score the order, not the line:** mark each order as a hit or a miss, the way the practitioner case does, instead of averaging lines and calling it service [3].
- **Split the basket sizes:** a ten-line order and a two-line order do not belong in one figure, because the power is not the same [1].
- **Run the inverse before you promise:** a 95% complete-order target needs 99.5% per-line stock at ten lines, and 99.7% at twenty [1].
- **Check the tail by reach:** the SKUs that recur across big baskets decide the score, and they are seldom the worst fillers [3].

What I would watch next is whether the order-level number survives a meeting with finance. It is easy to pull from order history and hard to argue with once the biggest customers appear in it. The same failure, priced per repair, is the other half of this: [Your $30 Exception Bill Is Wrong](/your-30-exception-bill-is-wrong/) puts a wage on each broken order rather than on the missing line.

<!-- nuanced-takeaway -->

## The catch

My read is that the math is a model, not a measurement. It assumes every line is in stock on its own, and real shortages cluster on the same items in the same weeks. That is why the measured gap of 10-15 points runs wider than the model at small baskets [2]. Read 81.7% as a floor, never as a forecast for a named customer.

The client figures come from one firm's unnamed jobs, not a survey, so they prove the gap is real without sizing it for your business [2]. The distributor case ran in March 2018, which makes it a lasting picture of the mechanic and not a current benchmark [3]. The 92-98% band is one provider's rule of thumb for a healthy fill rate, not a census [4].

Then there is cost, which this math does not settle. Buying 99.5% per-line stock to reach a 95% complete-order target is a big inventory decision, and the power tells you what it takes, not whether the customer is worth it.

What it does settle is where to look first: the few lines that appear on most orders, before anyone talks about adding stock across the catalogue.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Order fill counts only the orders that shipped complete, so it falls as line fill raised to the power of the lines per order. A 98% line fill is an 81.7% order fill on a ten-line basket [1].
- **Why It Matters:** The line metric is the one most order desks report, while complete orders run 10-15 points lower in one firm's records [2]. The service a customer feels can be far worse than the morning report says.
- **What I'd Watch:** How the number is built, and which SKUs carry it.
  - **Order-level scoring:** each order counted as a hit or a miss, not as an average of its lines [3].
  - **Basket split:** the biggest orders scored apart, because the power punishes them hardest [1].
  - **Reach ranking:** SKUs sorted by how many orders they sit on, which is where the cheap points are [3].
- **The Catch:** The math assumes lines are in stock on their own and real shortages cluster, so it sets a floor, not a forecast; the client evidence is one firm's unnamed jobs, and the cost of buying the last points is not settled here.

## Sources

[1] Inventoros — "Order Fill Rate: Definition, Formula, and How to Calculate It" (19 June 2026) — https://inventoros.com/blog/order-fill-rate
[2] F. Curtis Barry & Co. — "Use Initial Order Fill Rate to Measure Your Customer Service" (undated, retrieved 26 October 2026) — https://www.fcbco.com/blog/use-initial-order-fill-rate-to-measure-customer-service
[3] Benchmarking Success (Rob O'Byrne) — "Understanding Fill Rate KPIs: Line Fill Rate" (March 2018) — https://www.benchmarkingsuccess.com/understanding-fill-rate-kpis-line-fill-rate
[4] DCL Logistics — "Fill Rate: Definition, Formula, and How to Calculate It" (7 July 2026) — https://dclcorp.com/blog/fulfillment/fill-rate
