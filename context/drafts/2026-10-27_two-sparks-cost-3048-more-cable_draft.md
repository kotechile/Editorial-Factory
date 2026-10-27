---
title: "Two Sparks Cost $3,048 More: A 25 GB/s Cable"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "Nvidia's cheapest way into 128 gigabytes of local memory is two 64GB boxes and a cable, but the link between them runs at about 25 gigabytes a second against 273 gigabytes a second of memory inside each unit, so the pooled pair buys throughput on models that already fit one node rather than the capacity the ladder advertises."
date: 2026-10-27
slug: two-sparks-cost-3048-more-cable
synthesis: true
sources:
  - https://www.nvidia.com/en-us/products/workstations/dgx-spark/
  - https://petronellatech.com/blog/dgx-spark-64gb-specs-price-and-the-cable-to-pair-two
---

<!-- lead -->
Nvidia's new on-ramp to 128 gigabytes (GB) of local memory is two $4,999 boxes and a cable, and the cable is the part nobody priced. It carries data at 200 gigabits a second, measured at 196.08 on a two-unit test, which works out to about 25 GB a second against the 273 GB a second of memory inside each box [3]. The single 128GB machine Nvidia already sells reaches the same published ceiling of 200 billion parameters for $6,950 [2][5]. So the pair costs $3,048 more than the box it is meant to stand in for, and the part that holds the two halves together is roughly eleven times narrower than the memory it pools.

<!-- tension -->

## The big picture:

The pair exists because memory got expensive, not because the boxes got better. When Nvidia added a 64GB configuration on 23 October, the 128GB model beside it had already climbed from a $3,999 launch price to $6,950, a move the trade press put down to what a 64GB memory kit now costs [2][5]. Halving the memory gave buyers an entry price. It also left the 64GB unit rated for models up to 100 billion parameters, half the ceiling the larger box carries, with the networking left in place as the way back up [1].

I keep coming back to how the ladder is drawn. Nvidia's own page lists a 128GB pool as "up to 200B parameters" for a two-unit configuration, the identical ceiling it gives one 128GB machine, then 256GB for 400B across two larger units and 512GB for 700B across four [1]. Read as a product line, it says a second box buys back the capacity the first one lacks. Read as wiring, it says something narrower: the pool is two computers that each keep their own memory, joined by a link that has to carry whatever the two of them need to share.

Making that distinction matters more than it used to, because the pooled total in the marketing is not the speed of the link. Spheron reports the pair as delivering "546 GB/s" by doubling one unit's 273, and in the same piece concedes the gain on a real model stops short of the doubling, since traffic crossing between the units adds a hop that memory inside one box does not have [4]. Two local buses summed is a capacity figure. It is not a cable.

## By the numbers

- **$9,998 — The pair's price:** two 64GB units at $4,999 each, against $6,950 for the single 128GB unit that reaches the same "up to 200B parameters" ceiling [1][2][4].
- **196.08 Gb/s — The measured link:** a reseller's own two-unit test moved 111.86 Gb/s on one half of the port and 196.08 with both halves carrying traffic, about 25 GB a second against 273 GB a second of memory per box [3].
- **1.7x — The vendor's cluster test:** Nvidia's internal numbers use a 27-billion-parameter model, where a clustered pair reached up to 1.7x a single 128GB system as one lab reads the figures, a result that lab has not reproduced [2].
- **$3,048 — The gap:** the difference between the pair at list and the single 128GB unit it matches on capacity [4].

<!-- tactical-insight -->

## What I'd watch:

The interesting question is not whether two boxes are faster than one. It is which workloads the pair is actually faster at. My read is that the 27-billion-parameter result is the tell: a model that size sits inside one 64GB node, so the second box is doing parallel work rather than holding weights the first could not.

- **The software due at the end of October.** Nvidia's launcher for pushing one model across a single box or a pair is scheduled for month end, with the same 27-billion-parameter example. What it launches first says which shape the vendor expects buyers to run [2].
- **A published large-model number.** The claim worth waiting for is a 400-billion-parameter or larger model served across two or four units with sustained throughput attached. Nothing in the launch material goes past 27 billion [1][2].
- **Partner pricing.** The $4,999 figure is a floor set by six hardware partners rather than a single first-party price, and ServeTheHome records Nvidia describing a two-unit pool as "around $8000" [5]. If partner quotes land near that, the gap to the single box shrinks to about a thousand dollars and the arithmetic changes.
- **Where the four-unit rung gets priced.** The ladder stops at 700 billion parameters across 512GB, which is the configuration that would need the link most. Whoever publishes its cost first will say how Nvidia values the cable.

<!-- nuanced-takeaway -->

## The catch

The link is not automatically the limit. Splitting a model across two boxes can be arranged so that only small pieces of state cross the cable each step, and a lab that ran pipeline-parallel work across three hardware partners on the same 200-gigabit fabric got usable distributed inference out of it [6]. That design is what makes 1.7x possible on a model that fits one node, and it is why the pair is a fair buy for anyone whose work already fits in 64GB and who wants more of it done at once.

What the pair is not is a substitute for the larger box in the case that matters most: holding a model that does not fit on one unit. There the extra 64GB is the whole purchase, and the traffic that makes it work is the traffic on the narrow link. I have not seen that measured by anyone, and the honest reading of the evidence is that the vendor's own test avoided the case.

Two smaller caveats belong here. The 1.7x baseline is not settled across coverage, with two outlets attributing it to a single 64GB unit rather than a 128GB system, so the number is best quoted as "up to 1.7x" on that model and nothing more [2][4]. And a pair is two machines to patch, power and cool, which the $3,048 gap does not include.

<!-- tldr -->

## At a glance

- **The Big Shift:** Nvidia's 64GB desk machine arrived at $4,999 as a cheaper way into local AI, with a second unit and a cable offered as the path to 128GB. The link between two units moves data at about 25 GB a second, against 273 GB a second of memory inside each box.
- **Why It Matters:** The pair reaches the same "up to 200B parameters" ceiling as the $6,950 single 128GB unit while costing $3,048 more, so a buyer paying for capacity may be paying for a cable that decides how usable that capacity is.
- **What I'd Watch:** Whether the vendor or a lab publishes a model larger than 27 billion parameters running across a pair with throughput attached, which is the claim the launch material leaves open.
  - **Sustained cluster throughput:** speed measured over a long run on a model that does not fit one node, rather than a short test on one that does.
  - **Partner quotes:** the six partners set the $4,999 floor, so the real gap to the single box depends on what they charge.
  - **The four-unit rung:** 512GB and 700 billion parameters is where the link would carry the most, and it has no published price yet.
- **The Catch:** The pair is a fair purchase for work that already fits in 64GB, where the second box adds parallel throughput. For a model too large for one unit, the weights have to cross the link, and nobody has published that measurement.

## Sources
[1] Nvidia, DGX Spark product page (scaling ladder and networking) — https://www.nvidia.com/en-us/products/workstations/dgx-spark/
[2] StorageReview, "Nvidia DGX Spark 64GB: $4,999, October 23, Clusters to 128GB" (2026-10-23) — https://www.storagereview.com/news/nvidia-dgx-spark-64gb-october-23-4999-two-units-cluster-to-128gb
[3] Petronella Technology Group, "DGX Spark 64GB: Specs, Price, and the Cable to Pair Two" (2026-10-08) — https://petronellatech.com/blog/dgx-spark-64gb-specs-price-and-the-cable-to-pair-two
[4] Spheron, "DGX Spark 64GB Price, Specs, and Sync Clustering" (2026-10-10) — https://www.spheron.network/blog/nvidia-dgx-spark-64gb-price-specs-and-sync-clustering-2026
[5] ServeTheHome, "Nvidia DGX Spark 64GB Launched and Big 128GB GB10 Price Increases" (2026-10-21) — https://www.servethehome.com/nvidia-dgx-spark-64gb-launched-and-big-128gb-gb10-price-increases/
[6] StorageReview, "Best Desktops for Local AI 2026: Lab-Tested Rankings" (updated 2026-10-24) — https://www.storagereview.com/best/desktops-local-ai
