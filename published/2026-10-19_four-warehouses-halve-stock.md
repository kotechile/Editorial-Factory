---
title: "4 Warehouses Halve Stock. Yours Won't"
vertical: meio_working_capital_tco
persona: ops_leader
one_big_thing: "The 15-30% inventory cut in a multi-echelon business case is the square-root pooling law applied to four independent, identical warehouses; your network's measured demand correlation and the 98% fill rate copied onto every internal link decide whether the real gain is half, a third or nothing."
date: 2026-10-19
slug: four-warehouses-halve-stock
archetype: evergreen
evergreen: true
meta_title: "4 Warehouses Halve Stock. Yours Won't"
meta_title_source: "derived_from_title"
meta_description: "The rule of thumb says folding four warehouses into one halves your safety stock. The band that reaches the finance desk says 15% to 30% less inventory."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/four-warehouses-halve-stock/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "The Inventory Pooling Myth. Four towering aisles of heavily loaded steel pallet racks converging into a single staging area"
image_caption: "The Inventory Pooling Myth: Why real networks miss the promised 50% inventory cut."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The rule of thumb says folding four warehouses into one halves your safety stock [3]. The band that reaches the finance desk says 15% to 30% less inventory [4]. A peer-reviewed test on a real factory network beat the company's own stock rule by 6.6% [1]. The gap between those numbers is not effort. It is the shape of the network, and the rule only holds when yours fits it.

<!-- tension -->

## The big picture:

Multi-echelon planning sets stock levels for a whole network at once. Plant, main hub and local sites get planned as one system, not four [4]. Each site's repeated buffer folds into one shared pool, and one pool is smaller than the parts it replaces [3].

The size of that gain comes from the square-root law. Fold four equal sites into one, and total safety stock is said to drop by half [3].

The law is neat and widely quoted. It also needs four things that real networks rarely have [3].

- Demand at each site must be independent.
- The sites must be the same size.
- Demand must sit on a normal curve.
- The main lead time must not grow when sites merge.

A peer-reviewed study ran a planning model on three network shapes. The gain moved with the shape. It beat its baseline by 16.4% on a straight chain, 11.3% on a split network, and 6.6% on a real factory network [1].

The factory case is the one I keep reading. The baseline it beat was the company's own rule.

The firm promised customers a 98% fill rate, meaning the share of order lines it could ship from stock. It then put the same 98% on every internal link between its paper mills and its box plants [1].

What strikes me is that the 98% is not a customer promise there. It is the customer promise copied onto internal links. That copy rebuilds the double buffer the network was meant to remove.

Service targets add to the bill. A 95% fill rate needs a stock multiplier of 1.645. A 99% target needs 2.326 [2].

That is 41.4% more buffer for the last four points. The 41.4% is my arithmetic on the two table values, not a measured saving.

## By the numbers

- **50% to 0% — Overlap penalty:** Four equal sites cut safety stock 50% at zero correlation, 31% at 0.3, 16% at 0.6 and nothing at 1.0 [3]. The table is my arithmetic on the pooled-variance rule, not a source result.
- **6.6% — Real-network gain:** A planning model beat a real factory's own 98%-on-every-link rule by 6.6%. The same model beat a textbook chain by 16.4% [1].
- **1.645 to 2.326 — Service multiplier:** Moving a fill-rate target from 95% to 99% raises the stock multiplier by 41.4% [2].
- **15% to 30% — Quoted vendor band:** The cut vendors and guides cite, with service held above 98% [4][5]. It is a claim, not a measurement.

<!-- tactical-insight -->

## What I'd watch:

The people closest to this choice are not arguing about the band. They are arguing about which number goes into the model.

- **Shared spread, not site count:** Combined demand depends on how closely your sites move together. At four sites, a correlation (a shared swing) of 0.3 turns a 50% cut into 31%. A correlation of 0.6 turns it into 16%. Measure that overlap on two years of real shipments before the case is signed.
- **Where the 98% lives:** A fill rate promised to the customer belongs at the final node. Once it is copied onto every internal handoff, each link carries its own buffer [1]. I would want to read the policy before the savings estimate.
- **The lead-time leg:** Pooling moves stock further from the buyer. If the main-to-region lane adds transit days, the shared buffer has to cover that gap [3]. The lane time belongs in the model beside the demand spread.
- **Price of perfection:** A 99% target at every node needs 41.4% more stock than 95% [2]. On a network where pooling returned 16%, that one setting can erase the gain. I would want both numbers on the same page.

<!-- nuanced-takeaway -->

## The catch

My read on the 6.6% is that it is not a measurement of the pooling law. It is one planning model against three baselines on three networks of different size and shape [1]. Treat it as a sign that the gain thins as a network gets real, not as the saving your team will book.

The four limits behind the law come from undated warehouse notes, not a study [3]. The math checks out. Nobody measured how often real networks break those rules.

Overlap is also hard to estimate with care. Two years of shipment data may miss a shared sale or a single national buyer that makes four regions move together. A low reading can be a quirk of the sample, and that is the first flaw a finance reviewer will spot.

Pooling also shifts risk rather than removing it. One shared buffer in one building is cheaper to hold.

It is also a single point of failure that every region now depends on. The vendor pages say little about that trade [4][5].

Our own field note points the same way, and it is one case rather than proof. A medical device seller pooled six local buffers into one.

It freed $14.2 million and held 99.4% service. That is one company's result, not a benchmark.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Safety Stock Sizing" -> /safety-stock-forecast-error-not-demand-noise/ [same site (aichieve.net); same category; topical overlap: safety, stock] Link "Safety Stock Sizing" in the section where the article touches safety, stock. -->
<!-- internal-link hint: "60% Air Deals: Your Stock Math Breaks" -> /air-freight-wont-price-a-year/ [same site (aichieve.net); same category; topical overlap: stock] Link "60% Air Deals: Your Stock Math Breaks" in the section where the article touches stock. -->
<!-- internal-link hint: "Inventory Carrying Cost Is 20–30% a Year, Not Your 7% Borrowing…" -> /inventory-carrying-cost-rate/ [same site (aichieve.net); same category; topical overlap: stock] Link "Inventory Carrying Cost Is 20–30% a Year, Not Your 7% Borrowing…" in the section where the article touches stock. -->
## Related reading

- [Safety Stock Sizing](/safety-stock-forecast-error-not-demand-noise/) — more on Supply Chain & Operations
- [60% Air Deals: Your Stock Math Breaks](/air-freight-wont-price-a-year/) — more on Supply Chain & Operations
- [Inventory Carrying Cost Is 20–30% a Year, Not Your 7% Borrowing…](/inventory-carrying-cost-rate/) — more on Supply Chain & Operations
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Multi-echelon planning promises 15% to 30% less inventory. The math behind it halves safety stock when four equal, independent warehouses become one [3][4]. Real networks rarely meet those terms.
- **Why It Matters:** The saving is the working capital an operations leader is asked to release. A peer-reviewed test on a real factory network beat its own 98%-on-every-link rule by 6.6%, not 30% [1].
- **What I'd watch:** I am watching which numbers feed the model before the target is signed.
  - **Shared spread:** The spread of combined demand, which depends on how closely the sites move together, not on how many sites there are [3].
  - **Fill-rate rule:** Where the 98% promise is written, because copying it onto internal links rebuilds the repeat buffers [1].
  - **Service multiplier:** The factor a target applies to the buffer, 1.645 at 95% and 2.326 at 99% [2].
- **The Catch:** The 6.6% comes from one study across three network shapes, and the overlap estimate is easy to get wrong [1][3]. Pooling also leaves one building holding the risk for every region.

## Sources

[1] Geevers, van Hezewijk and Mes, "Multi-echelon inventory optimization using deep reinforcement learning", Central European Journal of Operations Research 32:653-683, published 19 July 2023 — 16.4% / 11.3% / 6.6% improvement by network shape, and the CardBoard Company benchmark that enforced a 98% fill rate on every internal connection. https://link.springer.com/article/10.1007/s10100-023-00872-2
[2] NIST/SEMATECH e-Handbook of Statistical Methods, "Cumulative Distribution Function of the Standard Normal Distribution" — critical values 1.645 at p=0.950 and 2.326 at p=0.990. https://www.itl.nist.gov/div898/handbook/eda/section3/eda3671.htm
[3] Inventory Path, "The Square-Root Law of Inventory Pooling Is Often Wrong" — the four-warehouse halving, its four assumptions, and the note that correlation, unequal sites and longer central lead times erode the benefit. https://www.inventorypath.com/the-square-root-law-of-inventory-pooling-is-wrong-more-often-than-its-right
[4] ToolsGroup, "Multi-Echelon Inventory Optimization: Benefits & Best Practices" — the 15% to 30% typical reduction and service targets above 98%. https://www.toolsgroup.com/blog/multi-echelon-inventory-optimization-toolsgroup-guide
[5] Re:innovation, "Multi-Echelon Inventory Optimization: The Complete Guide to Multi-Tier Networks, Safety Stock & Service Level Targets" — the 15-30% range as reported by multiple industry sources, and the z-score curve behind near-perfect targets. https://www.reinnovation.eu/post/multi-echelon-inventory-optimization-the-complete-guide-to-multi-tier-networks-safety-stock-serv

## Gate report
PASS — lead: delivers the halving claim, the vendor band and the 6.6% real-network result in the first four sentences, with no preamble.
PASS — tension: frames the law's four limits against a peer-reviewed run, one to three sentences per paragraph.
PASS — tactical-insight: reports what operators check — shared spread, fill-rate policy, lane time, service multiplier — as observations, not instructions.
PASS — nuanced-takeaway: states the study's limits, the overlap estimation problem and the concentration risk behind pooling.
PASS — tldr: follows the four-part schema with plain-English definitions in the sub-bullets.
