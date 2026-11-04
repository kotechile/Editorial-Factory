---
title: "18x LPDDR Isn't 18 TB/s"
vertical: gpu_hardware
kind: news
persona: infra_engineer
one_big_thing: "Microsoft's Maia 300 and Qualcomm's high bandwidth compute answer the same memory-bound inference problem in opposite directions, and the two headline numbers measure different things against different bases — 18.0 terabytes a second of HBM4 on one card versus 18x the bandwidth of low-power memory — so the one unit that would settle a purchase, tokens per watt on your own traffic, is exactly the one neither vendor publishes on a comparable basis."
date: 2026-11-04
slug: 18x-lpddr-isnt-18tbs
synthesis: true
sources:
  - https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments
  - https://www.qualcomm.com/news/onq/2026/11/qualcomm-hbc-validated-silicon-ai-inference
---

<!-- lead -->
On 2 November Qualcomm said its first high bandwidth compute chip had run a full memory read and write path in the lab. The design moves data 18 times faster than the low-power memory (LPDDR) it stacks under the compute die [1]. Three weeks earlier Microsoft put a number on the other approach: its Maia 300 card moves 18.0 terabytes a second (TB/s) from eight stacks of fourth generation high bandwidth memory (HBM4) [2]. 18x LPDDR isn't 18 TB/s, because one is a ratio against a base the other machine does not use [3].

<!-- tension -->

## Two answers to one bottleneck

Both firms start from the same premise. Inference is limited by how fast model weights reach the arithmetic, not by how much arithmetic the chip can do, and Microsoft says as much when it calls data movement the bottleneck rather than raw compute [2]. From that shared view the two build opposite machines, since each has a different cost to attack.

Microsoft keeps the stacked memory and widens it. It spends 950 watts per card and a multi-chiplet package to reach 18.0 TB/s [2]. Qualcomm removes the stacked memory: it bonds a stack of low-power memory on top of the compute die, so data moves micrometres instead of millimetres [1][3]. One buys speed with power and packaging, the other with distance.

Then the units break. Microsoft's figure is a rate on one defined machine. Qualcomm's is a multiple against low-power memory, a base Microsoft's part does not use. The part I keep circling is the missing common measure: Microsoft forecasts 40% more tokens per megawatt than "leading GPU-based systems" it never names, and Qualcomm gives no tokens-per-megawatt figure at all [2][3].

## What each side can sell

The ownership split matters as much as the silicon. Microsoft calls Maia 300 the main inference system for its own products and services, scaling to multi-gigawatt sites from 2027, and the post carries no price and no part number [2]. That is not a fault in the chip. It is what a first-party part is for. It does mean the 40% figure is a case for Microsoft's own fleet before it is a buying fact for anyone else.

Qualcomm's answer is a merchant chip, and it is a year out. The lab work covered a full read and write path and near-memory compute at production sizes. One data center product has taped out, and the Dragonfly AI250 that carries the design should sample in the first half of 2027 [1]. The lab result is the ticket into design reviews, which is why a firm that ships huge volumes of phone chips wrote a blog post about a chip bring-up.

Nvidia took a third route, and it sharpens the point. Its custom memory design moves the memory controller off the graphics chip and into the base die of the stack. The trade press reports that this is not an industry standard, and Nvidia says it adds up to 30% more bandwidth and frees 25% of compute-die area against standard HBM4E [4]. Three vendors, three memory designs, three bases for the number on the box.

## By the numbers

- **27.6 terabytes — memory per rack:** a full Maia 300 rack holds 96 cards, 27.6 terabytes of stacked memory and 1.7 petabytes a second of total bandwidth inside a 167-kilowatt envelope [2].
- **40% — Microsoft's tokens-per-megawatt claim:** the base is "leading GPU-based systems" with no model, vendor or test named, so the reader supplies it [2].
- **5x — Qualcomm's efficiency estimate:** the firm puts high bandwidth compute at five times the terabit-per-second-per-watt of HBM4, on lab silicon and normalised to target conditions [3][1].

<!-- tactical-insight -->

## Where the buyers are stuck

The people closest to this are not reading spec sheets. They are building the test that will outlive both vendors' marketing. Firms with their own silicon can design against their own traffic, which is what Microsoft says it did when it fed Maia 200 production data into the Maia 300 design [2]. Merchant vendors have to prove the tech in a lab first, because their customer is a design review rather than a fleet.

That leaves the ordinary buyer, a team renting capacity or refreshing a cluster in 2027, reading numbers that were never built to be compared. What I'm watching next is whether either side publishes an outside tokens-per-watt result on a named workload. That one number would fold three designs into a single column. Until then the honest test is the one a team runs on its own prompt mix, which is also the only one that prices the memory bill.

The shift is already visible in rental pricing, where [the cost of a rented graphics card hour tracks memory](/gpu-hour-price-set-by-memory/) rather than compute.

<!-- nuanced-takeaway -->

## The catch

The tidy story is that these numbers are marketing and the buyer should ignore them. I could be wrong, because a ratio is not automatically a weaker claim than a rate. If low-power memory is truly what Qualcomm's machine draws from, then 18x is the right multiple for its own design. Five times the terabit-per-second-per-watt of HBM4 is also a like-for-like claim on energy. The defect is not the arithmetic. It is that the comparison exists only inside Qualcomm's own footnote, which calls the figures estimates normalised to target conditions that may vary by workload and setup [1].

The same caveat runs the other way. Microsoft's 40% is a forecast for a part that ships in 2027, against a base it declines to name, and no outside test of either machine is public [2]. Two vendors can both tell the truth and still leave a buyer with nothing to put in a spreadsheet. That is the real state of the inference memory market this quarter.

<!-- tldr -->

## At a glance

**The shift:** The two escapes from the memory wall landed three weeks apart, and one is a speed while the other is a multiple against a memory the first does not use.
**The number:** 18.0 TB/s of HBM4 on Maia 300 against 18x LPDDR on Qualcomm's lab silicon — two different quantities, not a ranking.
**The risk:** No outside tokens-per-watt result exists for either part, so the only usable test in 2027 is your own workload.

## Sources

[1] Qualcomm, "Qualcomm HBC demonstrates AI inference leadership with validated silicon", 2026-11-02 — https://www.qualcomm.com/news/onq/2026/11/qualcomm-hbc-validated-silicon-ai-inference
[2] Microsoft, "Microsoft to expand Azure Maia system to multi-gigawatt deployments", 2026-10-12 — https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments
[3] The Next Platform, "Qualcomm Has Eyes On The AI Inference Datacenter With HBC And AI250", 2026-11-02 — https://www.nextplatform.com/ai/2026/11/02/qualcomm-has-eyes-on-the-ai-inference-datacenter-with-hbc-and-ai250/5306954
[4] The Register, "Nvidia sidesteps JEDEC HBM standard", 2026-10-26 — https://www.theregister.com/ai-ml/2026/10/26/nvidia-sidesteps-jedec-hbm-standard/5305323
