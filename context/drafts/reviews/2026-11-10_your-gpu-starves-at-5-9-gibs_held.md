---
title: "Your GPU Starves: The 5.9 GiB/s Gap"
vertical: workstation_compute_economics
kind: evergreen
archetype: evergreen
evergreen: true
persona: infra_engineer
one_big_thing: "A training box is fed by bytes per sample times samples a second: at the benchmark's own pressure one accelerator wants about 5.9 GiB/s of steady read, roughly one fast consumer drive each, and because the measured stall survives a dataset that fits entirely in memory the next purchase is processor cores, not a faster drive."
date: 2026-11-10
slug: your-gpu-starves-at-5-9-gibs
meta_title: "Your GPU Starves at 5.9 GiB/s"
meta_description: "One accelerator wants about 5.9 GiB/s of steady read at benchmark pressure, yet the measured stall survives even a fully cached dataset. Size the feed, not the drive."
---

<!-- lead -->

Keeping one accelerator busy is a feed problem. MLCommons' storage benchmark puts the demand at about 5.9 GiB/s of steady read for one simulated accelerator on its hungriest training workload [1]. A top consumer drive moves 14,500 megabytes a second over a PCIe 5.0 link [6]. Read plainly, those two numbers suggest two cards per drive. The catch is that the stall does not lift once the whole dataset is already in memory [4].

<!-- tldr -->

## At a glance

- **The shift:** Storage is sized per card, not per box [3].
- **The number:** 5.9 GiB/s per simulated card at full busy time [1].
- **The risk:** A faster drive cannot fix a stall that survives a cached dataset [4].

<!-- tension -->

## The feed is a rate

The benchmark reads large scan files of about 140 MiB, one training sample per file, in batches of seven, with four reader threads per card [2]. That turns storage into a metered input rather than a shelf. A storage result only counts while the cards stay busy 90% of the time on one workload and 85% on the other [3]. So a storage figure and a compute figure are the same number seen from two sides.

The build rule follows from a small piece of arithmetic. Take the bytes one sample carries and multiply by the samples a second the card can use. What comes out is the read rate the drive has to hold, every second, for the length of the run. At the benchmark's pressure that product is 5.9 GiB/s per card [1].

Two fast drives cover two cards. A four-card box is therefore a storage build as much as a graphics build, and the drive count is set before the second card ships. I keep circling how few of these boxes are planned that way: the cards get ordered first and the feed is patched afterwards.

Cloud nodes make the same point from the other end. A general-purpose cloud volume is listed at 125 MiB/s of baseline throughput, included in the price, with more sold separately [7]. That is about one forty-seventh of what one card wants at benchmark pressure. The volume a cloud machine boots from is not the volume it trains from, which is why cloud training jobs stage their data on local disks or a parallel file system.

<!-- By the numbers -->

## By the numbers

- **5.9 GiB/s per accelerator:** the steady read that holds one simulated card at full busy time [1].
- **65% of epoch time:** what the measured study lost to input prep, even with the dataset cached [4].
- **125 MiB/s baseline:** the included throughput on a general-purpose cloud volume [7].

<!-- tactical-insight -->

## Cores before drives

The people who instrumented the stalls count cores before they count drives. The same study found that its models needed anywhere between 3 and 24 central processing unit (CPU) cores per accelerator for input prep [5]. That puts the host processor on the critical path beside the feed. Their own fix for the stall was a decoded cache and a coordinated prefetch, because the work being repeated every epoch is decoding the same bytes again [4].

What I'd watch on a new box is busy time, not a drive's benchmark line. If the cards hold 90% across an epoch [3], the feed is doing its job and the next dollar belongs somewhere else. If they sag while the drive sits half idle, the bottleneck is upstream, in the decode path or in a dataset that gets re-read because it never fit in memory. Capacity and feed are two different purchases, and the other half of this ledger is what fits inside the card: [one card served 2,000 fine-tunes because the adapters were tiny](/2000-fine-tunes-one-card-55-throughput/), and this is the stream that has to run past it while those adapters are served. That stream is the one nobody budgets for.

<!-- nuanced-takeaway -->

## Where the number stops

My reading, held loosely: the 5.9 GiB/s figure is a ceiling, not a budget. It comes from the hungriest workload in the suite, reading 140 MiB image files fast enough to hold a simulated card at full busy time [2]. A text fine-tune reading small token shards at a few thousand samples a second needs a fraction of that. A reader who buys two drives for a single-card text pipeline has bought capacity that will sit unused.

The honest use of the number is as the top of a range you compute yourself. Bytes per sample times samples a second gives the floor. The surprise comes from the measured stall. The study's nine models lost 10 to 70% of epoch time to blocking reads, even with part of the dataset cached [4]. Drives and cores are separate line items. The drive is usually the cheaper of the two, and it is rarely the one that fixes the wait.

## Sources
- [1] MLCommons, "Benchmark MLPerf Storage v3.0 Results" — training workload description (read 2026-11-10): https://mlcommons.org/benchmarks/storage/
- [2] MLCommons, "Benchmark MLPerf Storage v3.0 Results" — Unet3D input pattern (read 2026-11-10): https://mlcommons.org/benchmarks/storage/
- [3] MLCommons, "Benchmark MLPerf Storage v3.0 Results" — accelerator-utilization validity rule (read 2026-11-10): https://mlcommons.org/benchmarks/storage/
- [4] Mohan, Phanishayee, Raniwala and Chidambaram, "Analyzing and Mitigating Data Stalls in DNN Training", VLDB 2021, arXiv:2007.06775v3: https://arxiv.org/html/2007.06775v3
- [5] Same paper, §5.1 sizing finding: https://arxiv.org/html/2007.06775v3
- [6] Tom's Hardware, "Best SSDs 2026" (read 2026-11-10): https://www.tomshardware.com/reviews/best-ssds,3891.html
- [7] Amazon Web Services, "Amazon EBS General Purpose SSD (gp3) volumes" (read 2026-11-10): https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html
