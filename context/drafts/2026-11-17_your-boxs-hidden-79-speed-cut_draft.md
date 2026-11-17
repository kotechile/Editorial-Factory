---
title: "Your Box's Hidden 79% Speed Cut: Rent Is the Audit"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "In November 2026 the two numbers a local AI purchase rests on — usable memory and sustained tokens a second — are set by the maker's firmware and the operating system rather than by the chip, so two hands-on Linux runs on the same platform landed 2.22x apart while the rental alternative became a published, re-runnable price table; the box is now the un-auditable side of build versus rent."
date: 2026-11-17
slug: your-boxs-hidden-79-speed-cut
kind: news
synthesis: true
sources:
  - https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop
  - https://github.com/datareceipts/data-receipts/tree/main/109-gpu-pricing
---

<!-- lead -->
A laptop with 128 GB (gigabytes) of memory was bought to end a bill for rented cloud cards. Its models ran at 13.9 tokens a second on native Linux and 65.4 on the Windows it shipped with. That is a 79% cut in speed, and it is hidden: the box's spec sheet never mentions it. Every purchase like this rests on two numbers, and only one of them is printed. The other half of the same decision now arrives as a table anyone can rerun, because an H100 card's hourly price is published across four providers with the script beside it — an audit of the rent side that costs one command. Owning has become the opaque half of this choice.

<!-- tldr -->
## At a glance
- **The shift:** A local AI box's speed is set by firmware, not by its chip.
- **The number:** 116 GiB visible on one laptop of this type, 28 GiB on another.
- **The risk:** A payback model built on a spec sheet can be wrong fourfold.

<!-- tension -->
## The clock is a firmware decision

The Spark platform reached buyers before anyone measured it on Linux. The laptops from MSI (a laptop maker), Asus and Dell ship with Windows on Arm, and only Nvidia's own desktop box leaves the factory on Nvidia's build of Linux. On 21 October a developer writing an inference engine reported a wall on Nvidia's forum [3]. With about 96 GiB set aside for the graphics chip, his machine still showed 30.49 GiB of processor-visible memory and a 60.25 GiB commit limit, the ceiling on memory a program may claim. His model needed roughly 70 GiB of weights, and so it would not fit. The figure on the product page and the figure the software can reach are decided in different places.

The published Linux test followed on 4 November, and its cause is not a driver bug [1]. Nvidia's platform controller hands the processor and the graphics chip a shared power budget, and the table of settings it applies arrives encrypted, with the key held on the Windows side [1]. The tester proved the link by switching that controller off inside Windows: the chip fell to 786 MHz, the same clock Linux was stuck at, and speed dropped from about 83 tokens a second to 31 [1]. Switching it back restored full speed. The setting lives in firmware, so an operating-system patch cannot close it.

Memory follows the same pattern. Windows splits the pool into a graphics region, a shared region and a processor-only region, and a slider in Nvidia's Windows app moves the line between them [2]. On the MSI unit, Linux reported 28 GiB of the 128 until the tester dropped the Windows-side figure to 4 GiB and rebooted, which exposed 120 GiB [1]. A box sold as one size is really three, and the number a buyer reads is only one of them. The knife that carves it belongs to the maker.

A second install reached the opposite end. Josephine Pfeiffer, an Arch Linux package maintainer, put Arch on an Asus ProArt P16 and got 116 GiB reported to both the operating system and to CUDA (Nvidia's parallel-computing platform) [2]. Her run on vLLM (an inference server for large models) measured 30.9 tokens a second beside published Windows figures of 29.4 and 31.4 [2]. She adds that the quants and runtimes differ and that the comparison does not isolate the operating system; processor work came out level to slightly ahead. Both readings can be true of one platform, and that is the awkward part.

I have read both reports twice, and the variable between them is not Linux at all. It is the firmware and the memory split each maker ships, and neither shows up anywhere a buyer can read before paying.

## By the numbers
- **13.9 tokens a second:** What native Linux managed on the tested laptop [1].
- **4.57 times:** The gap between the cheapest and dearest H100 hour in one November dataset [4].
- **$3.08 an hour:** The H100 index on 16 November, up 8.8% in twenty-nine days [5].

<!-- tactical-insight -->
## Where this bites

I have spent the week on the price side of this, and it is the mirror image of the speed side. The same H100 hour costs $2.69 through one provider and $12.29 through another [4]. The dataset states its own limits: list prices only, one region each, spot and reserved deals left out [4]. The index has climbed for four weeks, and the newer chips moved hardest in the last seven days, with the B200 reading up 10.9% [5]. Where the work runs is a separate question from what it costs. A rate quoted daily is a rate a payback model can be checked against, which the buy side cannot offer.

The speed side has no equivalent. The reviewers fell back on WSL (Windows Subsystem for Linux), which inherits the Windows clock behaviour and needs its memory set-aside raised from a 14 GiB default before a large model will load [1]. That answers a test, not the question of what the hardware does on the machine a team deploys on. The hardware is the same in both cases; the permission is not. Nothing in a receipt records a clock that was never allowed to rise. Power limits are the lever this firmware moves out of reach, and the desk's earlier piece on [where a card's power limit sits](/cap-your-card-at-80/) shows how far speed follows the clock.

What I am watching is whether any maker publishes a measured figure for its own laptop on Linux, in writing, before the next launch. One that will not is selling a demo as a spec.

<!-- nuanced-takeaway -->
## The catch

I can defend the capacity half of this more easily than any general rule about Linux, because the evidence runs both ways. One unit lost most of its speed and showed a quarter of its memory; another on the same platform held parity on processor work and reported 116 GiB to the operating system and to CUDA [2]. Two reviewers, one chip family, and opposite results on the same task. The mechanism is identified and reproducible inside Windows, but no lab has repeated the Linux test on the same hardware, and the two Asus machines were not a controlled comparison [2].

None of that makes a rented hour a substitute for an owned box. A unified pool of this size runs models that do not fit on a rented card, and the rented card brings far more memory bandwidth [4]. My read, held loosely, is narrower than it sounds: the number a buyer needs is now available on one side of the decision and missing on the other, and that gap is what a budget should carry a line for.

## Sources
- [1] MindStudio, "Linux on the Nvidia RTX Spark Laptop: What Actually Works", 2026-11-04 — https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop
- [2] Josephine Pfeiffer, "putting linux on my rtx spark laptop because i don't have a microsoft account", 2026-10-19 — https://josie.lol/blog/linux-rtx-spark
- [3] NVIDIA Developer Forums, "RTX Spark on Windows: CUDA allocations consume system commit even with 96 GiB dedicated GPU memory", 2026-10-21 — https://forums.developer.nvidia.com/t/rtx-spark-on-windows-cuda-allocations-consume-system-commit-even-with-96-gib-dedicated-gpu-memory/386453
- [4] data-receipts, "109: What an H100 actually costs per hour", 2026-11-09 — https://github.com/datareceipts/data-receipts/tree/main/109-gpu-pricing
- [5] Silicon Data, "H100 Rental Price Index (SDH100RT)", updated 2026-11-16 — https://www.silicondata.com/products/silicon-index/h100
