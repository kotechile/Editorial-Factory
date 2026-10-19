---
title: "4 Warehouses Halve Stock. Yours Won't"
vertical: meio_working_capital_tco
persona: ops_leader
one_big_thing: "The 15-30% inventory cut in a multi-echelon business case is the square-root pooling law applied to four independent, identical warehouses; your network's measured demand correlation and the 98% fill rate copied onto every internal link decide whether the real gain is half, a third or nothing."
date: 2026-10-19
slug: four-warehouses-halve-stock
archetype: evergreen
evergreen: true
---

<!-- lead -->
Four warehouses consolidated into one are supposed to halve your safety stock [3]. On a real network yours probably won't, and the gap is not a rounding error. The vendor version is softer. Multi-echelon planning usually cuts inventory 15% to 30% while holding service above 98% [4]. Both numbers rest on one piece of arithmetic, and that arithmetic needs your regional sites to rise and fall on their own.

<!-- tension -->

## The big picture:

Multi-echelon planning means planning every tier of one network at once. Plant, central warehouse, regional warehouse and store become one system instead of four [4]. The idea is sound. Buffers that each site repeats collapse into one shared buffer, and a shared buffer is smaller than the parts it replaces [3].

The saving comes from the square-root law. Fold four stocking sites into one, and total safety stock is said to drop by half [3]. The law is neat and widely quoted. It also rests on four assumptions that real networks break [3]. Demand at each site must be independent. The sites must be the same size. Demand must follow a normal curve. The central lead time must not grow when sites merge.

A peer-reviewed study ran a planning model across three network shapes. The gain moved with the shape. It beat its benchmark by 16.4% on a linear chain, 11.3% on a split network, and 6.6% on a real factory network [1].

The last case is the one I keep reading. The benchmark it beat was the company's own rule. The firm promised customers a 98% fill rate, meaning the share of order lines it could ship from stock. It then applied the same 98% to every internal link between its paper mills and its box plants [1]. The authors call that setup close to a decentralized policy [1].

What strikes me is that the 98% is not a customer promise at all. It is the customer promise copied onto internal links. That copy rebuilds the exact duplication the network was meant to remove.

Then comes the service target. A 95% fill rate needs a stock multiplier of 1.645. A 99% target needs 2.326 [2]. That is 41.4% more buffer for the last four points. The 41.4% is my arithmetic on the two table values, not a measured saving.

## By the numbers

- **50% to 0% — Correlation penalty:** Four equal sites cut safety stock 50% at zero correlation, 31% at 0.3, 16% at 0.6 and nothing at 1.0 [3]. That table is my arithmetic on the pooled-variance rule, not a source result.
- **6.6% — Real-network gain:** The planning model beat a real factory's own 98%-on-every-link rule by 6.6%. It beat a textbook chain by 16.4% [1].
- **1.645 to 2.326 — Service multiplier:** Moving a fill-rate target from 95% to 99% raises the stock multiplier by 41.4% [2].
- **15% to 30% — The quoted band:** The cut vendors and guides cite, with service held above 98% [4][5]. It is a claim, not a measurement.

<!-- tactical-insight -->

## What I'd watch:

The people closest to this decision are not arguing about the band. They are arguing about which number goes into the model.

- **The shared spread, not the site count:** For N equal sites with pairwise correlation rho, pooled spread is the single-site spread times the square root of N times one plus (N minus one) times rho. At four sites, a correlation of 0.3 turns a 50% cut into 31%. A correlation of 0.6 turns it into 16%. Measuring rho on two years of real shipments is the step that decides the business case.
- **Where the 98% is written:** A fill rate promised to the customer belongs at the customer-facing node. Once it is copied onto every mill-to-plant link, each internal handoff carries its own buffer [1]. I would want to read the policy before the savings estimate.
- **The lead-time leg:** Pooling moves stock further from the buyer. If the central-to-region lane adds transit days, the shared buffer has to cover that gap [3]. The lane time belongs in the model beside the demand spread.
- **The price of the last four points:** A 99% target at every node costs 41.4% more stock than 95% [2]. On a network where pooling returned 16%, that one setting can erase the gain. I would want both numbers on the same page.

<!-- nuanced-takeaway -->

## The catch

My read on the 6.6% is that it is not a measurement of the pooling law. It is one planning model against three benchmarks on three networks of different size and shape [1]. Treat it as evidence that the gain thins as a network gets real, not as the saving your network will book.

The source for the law's four assumptions is undated commentary from a warehouse consultancy, not a study [3]. The assumptions are standard textbook material. The arithmetic checks out. Nobody measured how often real networks break them.

Correlation is also hard to estimate with care. Two years of shipment data may miss the shared promotion or the single national customer that makes four regions move together. A low measured rho can be an artefact of the sample. The saving it promises is the first thing a finance reviewer will question.

Pooling also moves risk rather than removing it. One buffer in one building is cheaper to hold. It is also a single point of failure that every region now depends on. The vendor pages say little about that trade [4][5].

Our own field note points the same way, and it is one case rather than evidence. A medical device distributor pooled six regional buffers into one central buffer. It released $14.2M and held 99.4% service. That is one company's result, not a benchmark.

<!-- tldr -->

## At a glance

- **The Big Shift:** Multi-echelon planning promises 15% to 30% less inventory. The math behind that promise halves safety stock when four equal, independent warehouses become one [3][4]. Real networks rarely meet those terms.
- **Why It Matters:** The saving is the working capital an operations leader is asked to release. A peer-reviewed run on a real factory network beat its own 98%-on-every-link rule by 6.6%, not 30% [1].
- **What I'd watch:** I am watching which number goes into the model before the target is signed.
  - **Shared spread:** The spread of combined demand, which depends on how closely the sites move together, not on how many sites there are [3].
  - **Fill-rate rule:** Where the 98% promise is written, because copying it onto internal links rebuilds the repeat buffers [1].
  - **Service multiplier:** The factor a target applies to the buffer, 1.645 at 95% and 2.326 at 99% [2].
- **The Catch:** The 6.6% comes from one study across three network shapes, and the correlation estimate is easy to get wrong [1][3]. Pooling also leaves one building holding the risk for every region.

## Sources

[1] Geevers, van Hezewijk and Mes, "Multi-echelon inventory optimization using deep reinforcement learning", Central European Journal of Operations Research 32:653-683, published 19 July 2023 — 16.4% / 11.3% / 6.6% improvement by network shape, and the CardBoard Company benchmark that enforced a 98% fill rate on every internal connection. https://link.springer.com/article/10.1007/s10100-023-00872-2
[2] NIST/SEMATECH e-Handbook of Statistical Methods, "Cumulative Distribution Function of the Standard Normal Distribution" — critical values 1.645 at p=0.950 and 2.326 at p=0.990. https://www.itl.nist.gov/div898/handbook/eda/section3/eda3671.htm
[3] Inventory Path, "The Square-Root Law of Inventory Pooling Is Often Wrong" — the four-warehouse halving, its four assumptions, and the note that correlation, unequal sites and longer central lead times erode the benefit. https://www.inventorypath.com/the-square-root-law-of-inventory-pooling-is-wrong-more-often-than-its-right
[4] ToolsGroup, "Multi-Echelon Inventory Optimization: Benefits & Best Practices" — the 15% to 30% typical reduction and service targets above 98%. https://www.toolsgroup.com/blog/multi-echelon-inventory-optimization-toolsgroup-guide
[5] Re:innovation, "Multi-Echelon Inventory Optimization: The Complete Guide to Multi-Tier Networks, Safety Stock & Service Level Targets" — the 15-30% range as reported by multiple industry sources, and the z-score curve behind near-perfect targets. https://www.reinnovation.eu/post/multi-echelon-inventory-optimization-the-complete-guide-to-multi-tier-networks-safety-stock-serv

## Gate report
Draft stage — section gates run at Loop 3.
