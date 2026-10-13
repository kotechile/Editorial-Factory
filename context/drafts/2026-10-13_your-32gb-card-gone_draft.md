---
title: Your 32GB Card, Gone: 84GB, 41% Memory Bill
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "Compute is now priced by memory content rather than compute: Nvidia is reported to be pulling its only 32 GB consumer card and reserving that die for an 84 GB professional part with no published price, while the neocloud usually cast as the cheap way to rent raised rates twice in three months with its steepest increase on memory."
date: 2026-10-13
slug: your-32gb-card-gone
synthesis: true
sources:
  - https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-halts-geforce-rtx-5090-production-in-favor-of-ai-data-center-and-professional-gpus-impending-supply-drought-expected-to-drive-up-prices-rtx-5080-24gb-rumored-as-new-gaming-flagship
  - https://www.reuters.com/technology/nebius-hikes-ai-cloud-prices-again-demand-computing-power-soars-2026-09-17
---

<!-- lead -->
The card that made local inference cheap on a desk is reported to be gone. Nvidia has stopped shipping the chip behind its 5090 — the only consumer part with 32 gigabytes (GB) of video memory — and is sending that silicon to professional boards instead [1]. Eleven days before that report, on 1 October, the cloud firm most often named as the cheap way to rent the same kind of power raised its pay-as-you-go rates for the second time in three months. Its biggest rise, about 41%, was on memory, not on compute [3].

Neither move is about speed. Both are about how much memory a chip carries, and who gets to buy it.

<!-- tension -->

## The big picture:

The build-versus-rent call in this market has always rested on two numbers: the price of a card, and the price of an hour. In the past 30 days, one input moved both.

Take the buy side first. On 10 October, Tom's Hardware reported that Nvidia has stopped selling the GB202 chip — the die under the 5090 — to makers of consumer cards. It cited a leaked notice from an unnamed factory and a second hardware leaker, who said future supply of that die is set aside for data-center and professional cards [1]. Nvidia has not confirmed this. It has given no end date, and it did not reply when the outlet asked [1].

I keep coming back to what Nvidia did list. On 14 September, product pages appeared with no fanfare for its 5500 Blackwell Workstation Edition. It has 21,760 cores — the 5090's exact count — joined to 84 GB of GDDR7 memory with error-correcting code (ECC), 1,398 GB/s of bandwidth, up to 600 watts, and a split into one 84 GB slice or two of 42 GB each [2]. No price. No ship date. No speed figures. The spec table is marked preliminary [2].

Nvidia's own pitch names a different buyer than the desk-side builder: rack-mounted gear, with graphics chips (GPUs) kept "in IT-managed racks" and shared by users [2]. That is an IT buy, not a desk buy.

The maths is plain enough. Tom's Hardware's own point: the same die on a professional or data-center board sells for "substantially more" than the consumer card did, and the full 96 GB professional part "can easily sell for $15,000" [1]. The 5090 listed at $1,999, and by mid-September third-party sellers wanted $6,500 to $9,500 [7].

## By the numbers

- **84 GB vs 32 GB — Same 21,760 cores:** the professional card Nvidia listed in September carries about 2.6 times the video memory of the consumer card it shares a core count with, and Nvidia has published no price for it [1][2].
- **41% — The memory line:** Nebius raised its rate on memory offerings from 1 October, against 17% to 21% on graphics chips and 25% on some processor-only instances. Its 96 GB workstation tier did not move at all [3][4].
- **$6,950 — The 128 GB desk box:** Nvidia's larger Spark machine now lists at that price after launching at $3,999 a year ago, while the new, half-size 64 GB model ships 23 October "starting at $4,999" [5].
- **$3.47 — The H100 hour:** the median on-demand rental across 41 providers in the week of 5 October, up 4.0% over four weeks and 16% over a year, even as the premium the big cloud firms charge narrowed to 75% [6].

<!-- tactical-insight -->

## What I'd watch:

One line in the rental data matters more to me than the price rises themselves. The gap between the discount clouds and the big three shrank to 75% because the discount side moved up [6]. The floor rose. The ceiling did not.

Three things I am watching from here.

- **Where the 84 GB part gets priced.** A card with the 5090's core count and 2.6 times its memory, priced near the old consumer number, would undercut the professional line beneath it. Priced at professional money, it says the premium is on purpose [1][2].
- **Whether the second rise holds.** Two hikes in three months test pricing power, not costs. If usage holds up after them, a memory index becomes how this industry prices everything [3][4].
- **The 32 GB resale market.** That card was already at three times its list price before the report landed. What used ones fetch in November tells you what buyers think the replacement is worth [1][7].

<!-- nuanced-takeaway -->

## The catch

My read is that this is a memory story wearing a compute story's clothes. Three caveats still apply.

First, the halt is a leak, not a statement. Nvidia has not confirmed it, has disputed it in private to at least one outlet, and cards already built can keep selling for a while [1]. The half I can stand behind is the pricing above it.

Second, renting has not closed. A one-year reservation still runs about 32% below on-demand and a three-year about 49%, and spot capacity sits near 59% of the on-demand rate [6]. A team that will tie up capital, or put up with jobs dying mid-run, can still move its number down.

Third, the rises are not universal. Of 22 rental models tracked this year, 14 went up and 8 fell, and the 96 GB workstation tier did not move at all [4][6]. What repriced is memory-heavy gear — the same thing Nvidia is re-cutting its silicon to carry more of, in a shortage its suppliers say lasts into 2028. Memory is already on course to take 68% of major cloud firms' capital spending in 2027, from 47% this year [8].

<!-- tldr -->

## At a glance

- **The Big Shift:** In the past 30 days Nvidia was reported to have stopped making its only 32 GB consumer card and to have reserved that silicon for professional boards, while quietly listing an 84 GB professional version with the same core count and no price. Separately, Nebius lifted pay-as-you-go rates for the second time in three months, hardest on memory, at about 41%.
- **Why It Matters:** Both halves of the AI compute decision — buy or rent — now move with memory content rather than with compute. A 2027 plan built on price per unit of compute, or on today's hourly rate, will come in low.
- **What I'd Watch:** three signals that will show whether memory has become this industry's price index.
  - **The 84 GB card's price:** if it lands near the old consumer number the professional line beneath it gets undercut; if it lands at professional money, the memory premium is deliberate.
  - **Whether the second rise holds:** usage after two hikes in three months is the test of pricing power.
  - **The 32 GB resale market:** a card that just stopped being restocked tells you what buyers think the replacement is worth.
- **The Catch:** the halt is an unconfirmed leak that Nvidia has disputed, and reservations and spot capacity still price well below on-demand. The rent side has not closed. It has just stopped being the cheap answer by default.

## Sources
[1] Tom's Hardware, "Nvidia reportedly halts GeForce RTX 5090 production in favor of AI data center and professional GPUs" (2026-10-10) — https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-halts-geforce-rtx-5090-production-in-favor-of-ai-data-center-and-professional-gpus-impending-supply-drought-expected-to-drive-up-prices-rtx-5080-24gb-rumored-as-new-gaming-flagship
[2] NVIDIA, 5500 Blackwell Workstation Edition product page (fetched 2026-10-13) — https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-5500/
[3] Reuters, "Nebius hikes AI cloud prices again as demand for computing power soars" (2026-09-17) — https://www.reuters.com/technology/nebius-hikes-ai-cloud-prices-again-demand-computing-power-soars-2026-09-17
[4] Nebius, AI Cloud pricing, GPU-hour rates effective 1 October 2026 (fetched 2026-10-13) — https://nebius.com/prices
[5] ServeTheHome, "NVIDIA DGX Spark 64GB Launched and Big 128GB GB10 Price Increases" (2026-10-02) — https://www.servethehome.com/nvidia-dgx-spark-64gb-launched-and-big-128gb-gb10-price-increases and the NVIDIA store listing at $6,950 — https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark
[6] getdeploying.com, GPU Price Trends, week of 2026-10-05 (fetched 2026-10-13) — https://getdeploying.com/gpu-price-trends
[7] Tom's Hardware, "Nvidia's RTX 5090 vanishes from online retail in the US" (2026-09-14) — https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu
[8] TrendForce, DRAM and NAND to account for 68% of major cloud providers' capex in 2027 (2026-08-25, dated before this window) — https://www.trendforce.com/presscenter/news/20260825-13198.html
