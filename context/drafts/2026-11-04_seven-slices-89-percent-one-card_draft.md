---
title: "Seven Slices, 89% of One Card"
vertical: gpu_hardware
kind: evergreen
archetype: evergreen
evergreen: true
persona: infra_engineer
one_big_thing: "A Multi-Instance GPU profile is metered by the memory fraction, not the compute fraction — a 1g slice measured about 13% of a 96 gigabyte card's memory bandwidth against a seventh of its cores — so seven tenants book roughly 89% of one card's bandwidth and 85% of its cores, never seven cards, and the profile has to be sized from the resource a workload saturates."
date: 2026-11-04
slug: seven-slices-89-percent-one-card
---

<!-- lead -->
Seven slices of one 96 gigabyte card do not buy seven cards. Cut a Hopper card into the smallest Multi-Instance GPU (MIG) profile, and each tenant gets 16 cores and 406 gigabytes a second (GB/s) of memory speed, against 3,175 GB/s for the whole card [1][4]. A tenant therefore sees about 13% of the pipe, not the seventh its core count suggests, because the card divides its memory in eighths and its compute in sevenths. Add the seven tenants up and the split books 112 of 132 cores and about 89% of the memory rate [1].

<!-- tension -->
## A slice is not a seventh

The vendor's own wording carries that split. A memory slice is "roughly one eighth" of the card's memory, "including both capacity and bandwidth", and each slice also takes a share of the engines that move data in and out, while a compute slice is "roughly one seventh" of the cores [4]. Memory, memory speed and copy engines fall in eighths; compute falls in sevenths. I keep coming back to that gap, because most sizing advice counts only cores.

The numbers agree. Two 24 gigabyte profiles, one with 26 cores and one with 32, both run at 812 GB/s. The two 48 gigabyte profiles run at 1,611 and 1,635 GB/s, four cores apart [1]. Core count moves around, while the memory slice sets the rate.

A seven-way split then costs more than the table suggests. Seven smallest profiles book 112 of 132 cores, so 15% of the card stays unusable, and they book 77 of its 96 gigabytes as usable memory [1]. Four larger profiles book 104 cores, 92 gigabytes and 3,248 GB/s in total [1]. Fewer tenants, more of the card. Memory turns out to be the scarce half.

The shape is not a Hopper artefact. On a GB200 the card offers seven 23 gigabyte, four 46 gigabyte or two 93 gigabyte instances, sold on dedicated memory, cache and speed per tenant [3]. Every generation meters the tenant in eighths.

## By the numbers

- **39.6 GB/s — copy-path ceiling:** copies from host memory through the copy engine on a 1g slice ran at 39.6 GB/s, against 276.3 GB/s with no split, and larger profiles ran at the same rate [1].
- **17.5 gibibytes — memory left unbooked:** seven smallest instances leave 17.5 gibibytes unused, because each books 11 usable rather than the 12 printed in its name [1].
- **30% — what isolation is worth:** the sharing study gives MPS (multi-process service) up to 30% in good conditions, and takes about 30% away under memory contention, which MIG's hardware split removes [2].

<!-- tactical-insight -->
## What operators probe instead

Teams close to this stop reading the profile table and change one axis at a time. Grow the profile that carries cores, and a core-bound job speeds up. Grow the memory slice, and a memory-bound job speeds up. The paper's own reward model lands where that test points: for 8-bit Llama3 serving and vector search, the setup built on the smallest profile won when waste dominated, and the full card won when per-request speed dominated [1].

Separation is the other half of the choice. Sharing one memory space pays while jobs do not collide, and costs when they do. Splitting the hardware removes that clash, then charges for it in fixed sizes, because a job whose needs fall between two profiles wastes the gap [2]. What I'm watching next is the copy anomaly: the paper calls its flat copy rate "likely a bug", so a driver release could retire that row [1].

<!-- nuanced-takeaway -->
## The catch

I could be wrong to lead with memory speed, and the same paper says why. Its language model case scaled almost perfectly with core count, so that test is core-bound, and short prompts on an 8-bit model will see the seventh rather than the eighth [1]. The rule binds on long-context decoding, where each token reads a cache the slice can barely feed — the same ceiling one layer up, where [a card runs out of cache before it runs out of math](/kv-cache-is-the-concurrency-ceiling/), the running state a model keeps for each open chat (its KV cache).

Two limits matter too. The numbers come from one card in one machine: an HBM3 Hopper part inside a Grace Hopper system, so the copy figures describe that machine's chip-to-chip link at 450 GB/s per direction, not a PCIe host [1]. And the vendor's "roughly one seventh" is a rounding, because the measured count is 16 cores of 132 [1][4].

None of this makes the split useless. It makes the count on the box the wrong unit, which is why the floor a memory-bound tenant should expect is 13%. The test for going bigger is which profile change moves tokens a second.

<!-- tldr -->
## At a glance

**The shift:** One card now splits into seven tenants metered in eighths of memory and bandwidth, but sevenths of compute.
**The number:** 13% of the card's bandwidth per smallest slice.
**The risk:** Compute-bound serving scales with cores, so the bandwidth rule binds only long-context decode.

## Sources
[1] G. Schieffer, R. Shi, J. Ren and I. Peng, "Taming GPU Underutilization via Static Partitioning and Fine-grained CPU Offloading", arXiv:2604.08451v1, 9 April 2026 — https://arxiv.org/html/2604.08451v1
[2] J. Villarrubia, L. Costero, F. D. Igual and K. Olcoz, "A comprehensive evaluation of spatial co-execution on GPUs using MPS and MIG technologies", arXiv:2604.22430v2, 29 April 2026 — https://arxiv.org/html/2604.22430v2
[3] NVIDIA, "Multi-Instance GPU" technology page (GB200 partition shapes) — https://www.nvidia.com/en-us/technologies/multi-instance-gpu
[4] NVIDIA, "Multi-Instance GPU User Guide — Concepts" (memory slice and SM slice definitions) — https://docs.nvidia.com/datacenter/tesla/mig-user-guide/concepts.html
