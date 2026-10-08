---
title: Your Safety Stock Is Sized Off the Wrong Number
vertical: demand_sensing_advanced_sop
persona: ops_leader
one_big_thing: "Safety stock should be sized off the forecast's own error, not the spread of demand, and the two common short-cuts fail in opposite directions: sizing off demand volatility over-buffers (26 units of error where the forecast error is 10), while swapping in a raw error metric with the textbook service factor under-sizes it (a planned 95% service level arrives at 92.7%)."
date: 2026-10-08
slug: safety-stock-forecast-error-not-demand-noise
archetype: evergreen
evergreen: true
---

<!-- lead -->
Feed a safety-stock formula the standard deviation of demand and it builds a bigger buffer than the forecast needs. In one worked five-month example that spread implies 26 units of error, where the forecast's own error is 10 [2]. That single swap is where a lot of idle stock comes from. It is also the number an operations leader is asked to trust when a planning tool quotes a better forecast.

<!-- tension -->

## The big picture:

Safety stock exists because forecasts are wrong, not because demand moves. Those are two different spreads. The buffer should track the first one.

The standard build multiplies three things: the service factor, the spread of the forecast error, and the square root of the exposure period over the forecast period [3][4]. The service factor is the z-value for the target service level. It is 1.28 for 90%, 1.65 for 95% and 2.33 for 99% [3]. The middle term is the one teams get wrong.

What strikes me here is that the two common short-cuts fail in opposite directions. Size the buffer off the spread of demand, as many spreadsheets and old planning modules still do, and it overstates the error — 26 units where the forecast error is 10 [2]. Now swap in a real error metric, such as the root mean squared error (RMSE, the typical size of a miss). Keep the textbook service factor unchanged and the buffer comes out too small. A plan that aims for a 95% service level reaches only 92.7% [1].

Both errors are small in the formula and large on the balance sheet. A consumer-goods brand in our own field notes cut its demand error by three points and freed $8.5 million of finished goods. If an operator cannot name the spread that feeds the buffer, they cannot tell whether that money is free or already spent.

The forecast is only as live as the system behind it. Our field notes carry a manufacturer whose planning module synced with its core records once a night. Planners there committed stock against numbers a day old.

## By the numbers

- **26 units — Demand spread, overstated:** A worked five-month case sizes the buffer off the spread of demand. That implies 26 units of error, where the forecast's own error is 10 [2].
- **92.7% — Service level missed:** Swap in a forecast-error metric but keep the textbook service factor, and the buffer comes out too small. A planned 95% service level arrives at 92.7% [1].
- **41, 52, 74 units — The service ladder:** For one stock-keeping unit (SKU) at 50 units a day, a demand spread of 12 and a seven-day lead time, safety stock is 41 units at 90%, 52 at 95% and 74 at 99% [3].
- **61 units — A second SKU:** An independent example at a 90% service level, with a demand spread of 15 and a ten-day lead time, lands at 61 units of safety stock [4].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are arguing about which number goes into the middle of the formula. Here is what I am watching next.

- **The error term in the plan:** I am watching whether teams point the buffer at the forecast's own error, measured as plan minus actual, rather than at demand spread [2]. That is the one change that moves the number most.
- **The service factor:** A team that swaps in a forecast-error metric but keeps the old service factor will quietly miss its target, as the 92.7% case shows [1]. I want to see the factor and the error metric chosen together.
- **The cost of each rung:** Moving a target from 90% to 99% on one SKU takes the buffer from 41 units to 74 [3]. I am curious whether the service level is set once for everything, or priced per SKU.
- **Where the error comes from:** A forecast refreshed once a night carries a stale error term. I am watching how often the refresh rate, not the algorithm, is what caps the accuracy a team can bank.

<!-- nuanced-takeaway -->

## The catch

My read is that this prices only the error a better forecast can remove. It says nothing about a demand shock no forecast saw coming.

The figures here are examples, not a real SKU. Change the demand rate, the spread or the lead time and every number moves [3][4]. What travels is the method. Forecast error, not demand spread, drives the buffer.

There is also a floor on how small the buffer can safely get. A team can size its buffer perfectly and still run short. That happens when the lead time is unstable, or the forecast is biased rather than just noisy [1]. Accuracy gains buy room only against the error the model can learn.

Where I can see the least is the hand-off. If the planning system syncs on a slow batch, the buffer is sized off one number and refilled off another. Our own field notes show a three-point error cut turning into $8.5 million of freed stock — but only once the live error, not a stale one, fed the plan.

<!-- tldr -->

## At a glance

- **The Big Shift:** Safety stock is meant to cover how wrong the forecast is, not how much demand moves. Size the buffer off the spread of demand and the error is overstated — 26 units where the forecast error is 10 [2]. Swap in a real error metric with the old service factor and the buffer comes out too small, so a planned 95% service level lands at 92.7% [1].
- **Why It Matters:** The buffer is a working-capital line, and the wrong spread inflates it. Each rung of the service ladder has a price: 41 units at 90%, 52 at 95% and 74 at 99% for the same SKU [3]. A tighter forecast turns into cash only if the buffer is pointed at the forecast's own error.
- **What I'd Watch:**
  - **The error term:** Whether teams measure plan minus actual rather than demand spread, since that one choice moves the buffer most [2].
  - **The service factor:** Whether the factor and the error metric are picked together, because pairing a new metric with an old factor misses the target [1].
  - **The refresh rate:** How often a nightly batch, not the model, is what caps usable accuracy.
- **The Catch:** This prices only the reducible forecast error. It does not cover a demand shock, the example inputs are examples rather than a real SKU, and a biased or unstable lead time puts a floor under how small the buffer can safely get [1][3].

## Sources
[1] Databricks, "How a Fresh Approach to Safety Stock Analysis Can Optimize Inventory." https://www.databricks.com/blog/2020/04/22/how-a-fresh-approach-to-safety-stock-analysis-can-optimize-inventory.html
[2] Demand Planning LLC, "Error Measure for Safety Stocks: MAPE vs RMSE." https://demandplanning.net/error-measure-to-be-used-in-safety-stock
[3] SPS Commerce, "How to Calculate Safety Stock: Formulas and Methods That Fit Your Data." https://www.spscommerce.com/community/articles/how-to-calculate-safety-stock-formulas-and-methods-that-fit-your-data
[4] Netstock, "How to Calculate Safety Stock Using 3 Methods." https://www.netstock.com/blog/safety-stock-meaning-formula-how-to-calculate
