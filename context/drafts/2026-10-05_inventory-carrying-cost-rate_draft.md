---
title: "Your Inventory Carrying Cost Is 20–30% a Year, Not Your 7% Borrowing Rate"
vertical: meio_working_capital_tco
persona: ops_leader
one_big_thing: "The all-in cost of holding inventory is 20–30% a year, but most planning models load only the borrowing rate (bank prime is 7.00%), so they under-cost a buffer by roughly 3× and over-hold stock."
date: 2026-10-05
slug: inventory-carrying-cost-rate
archetype: evergreen
evergreen: true
---

<!-- lead -->
Bank prime sits at 7.00% [3]. The all-in cost of holding a dollar of inventory runs 20% to 30% a year [1][2]. Feed the first number into a planning model and it will tell you to hold roughly three times more stock than the second number can justify.

<!-- tension -->

## The big picture:

Holding inventory is not one cost. It is four stacked on top of each other: the capital tied up in the goods, the warehouse space and labor, the service costs like insurance and taxes, and the risk of shrinkage and obsolescence [1].

Most teams only price the first one. They take their cost of capital, call it the "cost of holding," and load it into the safety-stock formula. That is the number that decides how deep a regional buffer gets, how much of the long tail survives a SKU review, and whether an expedited shipment looks wasteful or rational.

What strikes me here is how the arithmetic flips once the other three costs enter the model. Financing is the smallest share of the total at today's rates, so a model fed only the borrowing rate is not slightly off. It is off by a factor that would change the answer.

## By the numbers

- **20% to 30% — Annual carrying cost:** What a dollar of inventory costs to hold for a year once capital, storage, service and risk are all counted [1][2]. A mid-range 25% means a $1M buffer burns roughly $250,000 a year just to sit there.
- **7.00% — Bank prime loan rate:** The financing leg alone, and the rate most companies actually borrow at [3]. It is roughly a quarter to a third of the true cost of holding.
- **1.30 — US inventories/sales ratio:** The July 2026 reading for total US business inventories, which stood at $2,764.7 billion on the books [4]. That is the pile the wrong rate gets applied to.
- **3.12 per kilogram — Global air cargo spot rate:** July 2026 pricing, up 28% from a year earlier [5]. Taiwan–US lanes ran as high as $7.02 per kilogram in May [6].

<!-- tactical-insight -->

## What I'd watch:

The operators closest to this are re-running one input, not rebuilding the model. My read: the rate is the lever nobody audits.

- **What the rate does to buffer depth:** Every extra week of safety stock costs about a half to two-thirds of a percent of its value. At a 25% rate, a month of buffer on a $1M item family runs roughly $21,000 — and the model should only keep it if it prevents more than that in stockouts.
- **Where expedited freight starts to beat the buffer:** Air cargo spot rates around $3.12 a kilogram [5] are the counter-price. A distributor holding $2.5M of regional spare parts faced roughly $575,000 a year in carrying cost against about $85,000 a year absorbing chartered air freight — the buffer was the expensive option, not the shipment.
- **How the long tail reads differently:** Slow SKUs that look margin-positive on a gross-margin report turn negative once storage, handling and markdown are loaded at a real rate. I'd want to see which items flip when the rate moves from 7% to 25%.
- **What I'm watching next:** The Federal Reserve's H.15 release updates the financing leg every business day [3], and the air-cargo indexes publish monthly [5][6]. Both ends of the break-even move; the gap between them is what I'd track.

<!-- nuanced-takeaway -->

## The catch

I could be wrong to treat 20% to 30% as a fixed law. It is a convention drawn from industry references [1][2], not a measured constant, and it moves by business.

Wholesale and fast-turning operations run lower — the same sources cite ranges near 8% to 15% — while seasonal or specialty goods run higher. A single number applied across every category is its own kind of error.

The rate also does not answer how much stock to hold. For a critical part that stops a line, a stockout can cost far more than the carrying cost of the buffer, no matter how high the rate climbs. The rate sets the price of the bet; it does not decide the bet on its own.

<!-- tldr -->

## At a glance

- **The Big Shift:** The cost of holding inventory is far higher than the rate most teams put in their models. The fully loaded figure runs 20% to 30% a year [1][2], while the financing leg — bank prime — sits at 7.00% [3].
- **Why It Matters:** A model fed only the borrowing rate under-costs a buffer by roughly three times, so it recommends more safety stock and keeps more slow-moving stock than the real economics support. That ties up cash and warehouse space that a higher rate would release.
- **What I'd Watch:** Whether teams move the rate they load into safety-stock, MEIO and SKU reviews from the cost of capital to the full carrying cost.
  - **MEIO:** Multi-Echelon Inventory Optimization — placing stock across a central warehouse and regional hubs so the whole system holds less while still filling orders.
  - **The break-even:** The point where paying for expedited freight on rare stockouts costs less than carrying a permanent buffer, set by the air-cargo spot rate [5][6].
  - **The long tail:** Low-turnover items whose true cost only shows up once storage, handling and markdown are priced at a real rate.
- **The Catch:** The 20% to 30% band is a working convention, not a fixed law; fast-turning wholesalers run lower, seasonal goods run higher, and a critical part can still justify a buffer even at a high rate.

## Sources
[1] Clear Spider, "Inventory Carrying Cost: How to Calculate, Reduce & Optimize" — https://clearspider.net/blog/inventory-carrying-cost
[2] SourceDay, "Inventory Holding Costs: Formula, Examples, and How to Reduce" — https://sourceday.com/blog/inventory-holding-costs
[3] Federal Reserve Board, "H.15 Selected Interest Rates (Daily)" — https://www.federalreserve.gov/releases/h15
[4] U.S. Census Bureau, "Manufacturing and Trade Inventories and Sales, July 2026" — https://www.census.gov/mtis/current/index.html
[5] Cargo Solutions Network, "Air Cargo Spot Rates July 2026: Slowing Growth, No Peak Season" — https://cargosolutionsnetwork.com/insights/air-cargo-spot-rates-july-2026-slowing-growth-no-peak-season
[6] Xeneta, "What the Air Freight Market Looks Like Right Now — and Where It's Heading" — https://www.xeneta.com/blog/what-the-air-freight-market-looks-like-right-now-and-where-its-heading

<!-- linkedin -->
I keep coming back to one number in inventory planning: the rate you load for holding stock.

Bank prime is 7.00% today. The all-in cost of carrying inventory — capital, storage, service, and the risk of shrink and obsolescence — runs 20% to 30% a year. Most models use the first number and call it the cost of holding.

My read: that single input is doing more work than any forecast. Load 7% and the model keeps deep buffers and long-tail SKUs that the real economics would prune; load 25% and a $1M buffer suddenly costs $250,000 a year to sit there.

It also moves the expedited-freight question. Air cargo spot rates were around $3.12/kg in July, and one distributor I've seen held $2.5M of regional spares at roughly $575k a year in carrying cost against ~$85k a year of chartered air freight. The buffer was the expensive choice.

Where I've landed: the rate is the lever nobody audits. I'm curious how other ops teams set theirs — cost of capital, or fully loaded?

#inventory #workingcapital #supplychain #MEIO #operations
