---
title: "Your 128GB Rung Eats $2,319 of Memory"
vertical: workstation_compute_economics
kind: news
persona: infra_engineer
one_big_thing: "Nvidia's laptop launch is two ladders stacked: below 48GB the chip is cut, and above it the price is a memory purchase against an index that rose 13.3% in thirty days — so the chip rung is the decision and the memory rung is a commodity you can price every morning."
date: 2026-11-03
slug: your-128gb-rung-eats-2319-of-memory
synthesis: true
sources:
  - https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs
  - https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models
  - https://ramradar.app/ram-price-index
  - https://getdeploying.com/gpu-price-trends
---

<!-- lead -->

On 31 October the median desktop DDR5 kit asked $18.12 a gigabyte, so 128GB of parts now costs $2,319 — after a year in which the memory shortage took that index up 88% [1]. The cheapest laptop Nvidia shipped on 16 October with that much unified memory costs $5,109 [2][3]. The two numbers are the same purchase read from opposite ends.

<!-- tension -->

## Two ladders, one price list

The launch looks like a memory ladder. Six makers put the same superchip into slim Windows machines — Asus, Dell, Lenovo and Microsoft among them — from a 24GB model at $2,599 to a 128GB model at $6,999.99, and the top configuration is advertised by its memory rather than its speed [2][3].

It is also a chip ladder, and that half is easy to miss. Every configuration at 24GB or 32GB carries an 18-core processor and a 5,120-core graphics processing unit (GPU). The full part — 20 cores and 6,144 cores — appears only at 48GB and above [3]. So the entry model is not a smaller version of the machine beside it. It is a different machine wearing the same name.

My read starts with the label. Nvidia's release names one local model for day one: Nemotron 3.5 Bolt 74B-A9B 24GB, a 74-billion-parameter model sized to a 24GB footprint [2]. That is exactly the capacity of the cheapest configuration, on a device where the operating system, the browser and an agent runtime also live. The label describes the model's own footprint, not the room left on the machine.

<!-- tactical-insight -->

## What the gigabyte is worth

Memory is the one line in a local box that reprices while you own it. The index behind the first number reads 211 desktop DDR5 kits daily, reports the median and the mean, and publishes the thirty-day move: 13.3% higher on 31 October than on 1 October [1]. Nine of the last eleven monthly readings were rises. The two declines, in May and June, were each followed by four straight increases [1].

That matters to a buying decision because the ladder sells two things at once. The chip rung is fixed at purchase and cannot be changed later by any firmware update or add-in card. The memory rung is a commodity with a public quote, and 64GB of it costs $1,160 as two retail kits at today's median [1]. A buyer who pays for the top step is buying the chip they needed plus memory at whatever the maker set before this month's move.

The priced alternative has its own clock. An H100 rents for a median $3.84 an hour across 39 providers, up 14% in four weeks and 29% in a year, while a three-year reservation runs about 48% below on-demand [4]. An H200, with 141GB, lists at $5.40 an hour on the dedicated clouds [4]. For a workload that peaks for a few weeks a year, the peak is the part to rent, and [the hourly price of memory is what moves that number](/gpu-hour-price-set-by-memory/).

## By the numbers

- **$2,319 — 128GB of desktop DDR5** at the 31 October median, across 211 tracked kits [1].
- **$294 — what 128GB gained in thirty days**, as the index mean moved from $17.36 to $19.66 a gigabyte [1].
- **$3,999 — the first rung that keeps the full chip**, at 48GB [3].

<!-- nuanced-takeaway -->

## The trade the ladder hides

The entry machine is a real computer and a fair price for what it holds. It is also the rung with the least headroom, because the memory it has is the memory the reference model needs before anything else runs. The step above buys 24 extra gigabytes and 1,024 extra GPU cores, and only one of those halves can be added later.

Memory can be deferred in a way silicon cannot, and not inside these machines: the rung fixes the capacity for the life of the laptop. What can be deferred is the purchase itself. A full-chip machine today, with rented hours for a peak that arrives twice a year, is a smaller commitment than the largest rung bought to cover a peak it would otherwise sit idle through.

What I keep circling is how little of the launch price the memory explains, and how much of the decision it drives. Retail parts set the floor under the top rung at less than half of what the machine sells for, and that floor moves monthly while the price on the sticker does not. A buyer comparing rungs by capacity is comparing a fixed number against a moving one.

The signal to watch is the rung, not the gigabyte. If the next launch keeps 48GB as the full-chip threshold, the threshold is the product line, and the memory on either side of it is a market price with a daily quote.

<!-- tldr -->

## At a glance

- **The shift:** Nvidia's 16 October laptop launch prices local capacity on a memory ladder, with the full chip starting at 48GB.
- **The number:** $2,319 is what 128GB of desktop DDR5 costs at the 31 October median, $294 more than a month earlier.
- **The risk:** The cheapest rung carries a cut chip, not just less memory.

## Sources
[1] RamRadar, "RAM Price Index" (data to 2026-10-31, read 2026-11-03): https://ramradar.app/ram-price-index
[2] NVIDIA Newsroom, "NVIDIA RTX Spark PCs Available Today — A New Beginning for Windows PCs" (2026-10-16): https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs
[3] Tom's Hardware, "Nvidia RTX Spark devices are now officially on sale … starting at $2,599" (2026-10-16): https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models
[4] getdeploying, "GPU Rental Price Trends (2026)" (week of 2026-10-26, read 2026-11-03): https://getdeploying.com/gpu-price-trends
