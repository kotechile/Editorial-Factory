---
title: "Two Sparks Cost $3,048 More: The 25 GB/s Cable"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "Nvidia's cheapest way into 128 gigabytes of local memory is two 64GB boxes and a cable, but the link between them runs at about 25 gigabytes a second against 273 gigabytes a second of memory inside each unit, so the pooled pair buys throughput on models that already fit one node rather than the capacity the ladder advertises, and it costs $3,048 more than the single box that reaches the same ceiling."
date: 2026-10-27
slug: two-sparks-cost-3048-more-cable
synthesis: true
sources:
  - https://www.nvidia.com/en-us/products/workstations/dgx-spark/
  - https://petronellatech.com/blog/dgx-spark-64gb-specs-price-and-the-cable-to-pair-two
meta_title: "Two Sparks Cost $3,048 More: The 25 GB/s Cable"
meta_title_source: "derived_from_title"
meta_description: "Two small Sparks and one cable now hold the 128 gigabytes (GB) of memory Nvidia's $6,950 desk machine holds, for $9,998, and the cable is the part nobody…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/two-sparks-cost-3048-more-cable/featured.jpg"
image_style: "editorial_macro"
image_model: "flux"
image_alt: "The $3,048 Bottleneck. A thick data cable plugged into a metal server port under low lighting."
image_caption: "The $3,048 Bottleneck: Why linking two 64GB Nvidia Sparks costs more for less."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Two small Sparks and one cable now hold the 128 gigabytes (GB) of memory Nvidia's $6,950 desk machine holds, for $9,998, and the cable is the part nobody prices [2][4]. It runs at 200 gigabits a second, measured at 196.08, which is about 25 GB/s against the 273 GB/s of memory inside each box [3]. So the pair costs $3,048 more and joins its two halves through a link roughly eleven times narrower than the memory it pools, while both setups stop at the same published ceiling of 200 billion parameters [1][2][4]. That gap, not the gigabytes, is what decides whether two Sparks are one bigger computer or two computers.

<!-- tension -->

## The big picture:

The pair exists because memory got expensive, not because the boxes got better. Nvidia added a 64GB unit on 23 October, and by then the 128GB model beside it had climbed from a $3,999 launch price to $6,950, a move the trade press puts down to what a 64GB memory kit now costs [2][5]. Halving the memory bought the line an entry price at $4,999. It also halved what one unit can hold, to models rated up to 100 billion parameters, and left the networking in place as the way back up [1][2].

I keep coming back to how the ladder is drawn. Nvidia lists the pair at the same rung as the single large box:

| Setup | Local memory | Model ceiling | Hardware cost |
| :--- | :--- | :--- | :--- |
| One 64GB unit | 64GB | 100 billion parameters | $4,999 |
| One 128GB unit | 128GB | 200 billion parameters | $6,950 |
| Two 64GB units, cabled | 128GB pooled | 200 billion parameters | $9,998 |
| Four units | 512GB | 700 billion parameters | Not published |

Read as a product line, that says a second box buys back the capacity the first one lacks. Read as wiring, it says something narrower. A pool is two computers that each keep their own memory, joined by a link that carries whatever the two of them need to share, and the pooled total in the marketing is not the speed of that link. Spheron reports the pair at 546 GB/s by doubling one unit's 273 [4].

The same piece concedes the gain on a real model stops short of a doubling. Traffic crossing between the units adds a hop that memory inside one box does not have. Two local buses summed is a capacity figure. It is not a cable.

## By the numbers

- **$9,998 — The pair:** two 64GB units at $4,999 each, against $6,950 for the single 128GB unit that reaches the same 200-billion-parameter ceiling [1][2][4].
- **196.08 Gb/s — The measured link:** a reseller's two-unit test moved 111.86 Gb/s (gigabits a second) on one half of the port and 196.08 with both halves carrying traffic, about 25 GB/s against 273 GB/s of memory per box [3].
- **1.7x — The vendor's cluster test:** Nvidia's internal numbers use a 27-billion-parameter model, where a cabled pair reached up to 1.7x a single 128GB system as one lab reads the figures [2]. That lab has not repeated the result.
- **$3,048 — The gap:** the pair at list against the single 128GB unit it matches on capacity, before two machines' worth of power, cooling and patching [4].

<!-- tactical-insight -->

## What I'd watch:

The interesting question is not whether two boxes are faster than one. It is which work the pair is actually faster at, and my read is that the 27-billion-parameter test is the tell. A model that size sits inside one 64GB node, so the second box is doing parallel work rather than holding weights the first one could not fit.

- **The launcher due at the end of October.** Nvidia's software for pushing one model across a single box or a pair is scheduled for month end, with the same 27-billion-parameter example. What it launches first says which shape the vendor expects buyers to run [2].
- **A number above 27 billion.** The claim worth waiting for is a 400-billion-parameter or larger model served across two or four units, with a long-run speed figure attached. Nothing in the launch material goes past the small test [1][2].
- **Partner pricing.** The $4,999 figure is a floor set by six hardware partners rather than a single first-party price, and ServeTheHome records Nvidia describing a two-unit pool as "around $8000" [5]. If partner quotes land near that, the gap to the single box falls to about a thousand dollars and the arithmetic changes.
- **The four-unit rung.** The ladder stops at 512GB and 700 billion parameters, which is the configuration that would lean hardest on the link. Whoever publishes its price first will say how Nvidia values the cable.

<!-- nuanced-takeaway -->

## The catch

My read is that the link is not automatically the limit. Splitting a model across two boxes can be arranged so that only small pieces of state cross the cable at each step [6]. A lab that ran that style of work across three hardware partners on the same 200-gigabit fabric got usable split inference out of it. That design is what makes 1.7x possible on a model that fits one node, and it is why the pair is a fair buy for anyone whose work already fits in 64GB and who wants more of it done at once.

What the pair is not is a stand-in for the larger box in the case that matters most: holding a model that does not fit on one unit. There the extra 64GB is the whole purchase, and the traffic that makes it work is the traffic on the narrow link. I have not seen that measured by anyone, and the honest reading of the evidence is that the vendor's own test avoided the case.

Two smaller caveats belong here. The 1.7x baseline is not settled across coverage, with two outlets tying it to a single 64GB unit rather than a 128GB system, so the figure is best quoted as "up to 1.7x" on that model and nothing more [2][4]. And a pair is two machines to patch, power and cool, which the price gap does not include. The shape of the finding is familiar from the cache ceiling that decides how many requests one card can serve at once: [the limit a buyer meets is rarely the one the spec sheet prints](/kv-cache-is-the-concurrency-ceiling/).

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your 32GB Card, Gone" -> /your-32gb-card-gone/ [same site (aichieve.net); same category; topical overlap: gigabytes, memory] Link "Your 32GB Card, Gone" in the section where the article touches gigabytes, memory. -->
<!-- internal-link hint: "Your GPU Runs Out of Cache Before It Runs Out of Math" -> /kv-cache-is-the-concurrency-ceiling/ [same site (aichieve.net); same category; topical overlap: holds, memory] Link "Your GPU Runs Out of Cache Before It Runs Out of Math" in the section where the article touches holds, memory. -->
<!-- internal-link hint: "Self-Hosted AI: When to Buy vs Rent GPUs" -> /self-hosted-ai-when-to-buy-vs-rent-gpus/ [same site (aichieve.net); same category; topical overlap: cost] Link "Self-Hosted AI: When to Buy vs Rent GPUs" in the section where the article touches cost. -->
## Related reading

- [Your 32GB Card, Gone](/your-32gb-card-gone/) — more on Major Purchases & Assets
- [Your GPU Runs Out of Cache Before It Runs Out of Math](/kv-cache-is-the-concurrency-ceiling/) — more on Major Purchases & Assets
- [Self-Hosted AI: When to Buy vs Rent GPUs](/self-hosted-ai-when-to-buy-vs-rent-gpus/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Nvidia's 64GB desk machine arrived at $4,999 as a cheaper way into local AI, with a second unit and a cable offered as the path to 128GB. The link between two units moves data at about 25 GB/s, against 273 GB/s of memory inside each box.
- **Why It Matters:** The pair reaches the same 200-billion-parameter ceiling as the $6,950 single 128GB unit while costing $3,048 more, so a buyer paying for capacity is also paying for a cable that decides how usable that capacity is.
- **What I'd Watch:** Whether the vendor or a lab publishes a model larger than 27 billion parameters running across a pair with sustained speed attached, which is the claim the launch material leaves open.
  - **Sustained cluster speed:** speed held over a long run on a model that does not fit one node, rather than a short test on one that does.
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

## Gate report
lead: PASS — Opens on the two price figures and the narrow link in the first two sentences, no preamble, and the name of the product is in the body.
tension: PASS — Names what shifted (memory cost), shows the ladder as a table, and separates a summed capacity figure from a cable speed.
tactical-insight: PASS — Reports which evidence is missing rather than advising the reader, with a first-person cue and four concrete signals to watch.
nuanced-takeaway: PASS — Concedes the pipeline-parallel case, flags the unsettled 1.7x baseline and the unmeasured large-model case, and carries a first-person cue.
tldr: PASS — Four-part card naming the shift, the stakes, the signals being watched and the trade-off, with plain-English sub-bullets.
