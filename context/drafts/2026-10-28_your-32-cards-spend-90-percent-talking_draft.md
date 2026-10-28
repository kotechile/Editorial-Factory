---
title: "Your 32 Cards Spend 90% Talking: Why Wide Splits Stall"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "Past the node boundary tensor parallelism stops turning cards into throughput, because every layer ends in a swap whose decode-phase message is only about 128 kilobytes — so in a fixed 32-card budget the wide-split layout took 3.68 to 4.35 times the run time of a narrow one, and the lever that recovers it is the swap routine, not another card."
date: 2026-10-28
slug: your-32-cards-spend-90-percent-talking
archetype: evergreen
evergreen: true
meta_title: "Your 32 Cards Spend 90% Talking: Why Wide Splits Stall"
meta_description: "In a 32-card budget, the wide tensor-parallel layout took 3.68 to 4.35 times the run time of a layout that kept the split narrow."
---

<!-- lead -->
Split a model across 32 graphics processing units (GPUs) and the run stops being arithmetic. Because every layer ends with the cards swapping partial results, 89.9% to 95.8% of the run time in a 2026 simulation study went to cards waiting on each other [3].

Those figures come from 768 simulated runs over four mixture-of-experts models at a fixed 32-card budget. The study also found that the layout beats the card count. A wide 16-way split took 3.68 to 4.35 times the average run time of a narrow one, on the same hardware [3].

Real hardware points the same way. On Perlmutter, tensor-parallel latency for a 70B model fell from one four-GPU node to two, then stalled. Past 16 GPUs it stays flat or climbs [1].

<!-- tension -->

## The big picture:

The bottleneck moved off the multiply and onto the wire, and the wire ends at the node edge.

An H100 card carries 900GB/s of NVLink bandwidth, against 128GB/s over PCIe Gen5, the slower path a card takes when it leaves that group [4]. Cross the line and every layer pays a round trip on a network built for bulk moves, not for tight handoffs. A ring-style all-reduce needs two serial stops per extra card, so the bytes each card sends barely grow while the number of stops keeps rising.

In decode the message is small. For a 70B model at batch 8, one swap moves about 128KB per card. That is a delay problem, not a bandwidth problem, and it is the size where crossing a node hurts most [1].

So the buying conversation has moved to rack-sized domains. A GB200 NVL72 keeps 72 GPUs behind one switch rated at 130 terabytes per second (TB/s), which is a vendor selling node width as a product [5]. My read: that rack is not a bigger server. It is an answer to the same arithmetic that stalled the cluster at 16 cards.

<!-- tactical-insight -->

## By the numbers

- **89.9% to 95.8% — Waiting share:** Across the 32-card mixtures runs, most of the average run time went to cards swapping results rather than doing math [3].
- **3.68 to 4.35 times — Wide-split penalty:** A 16-way split ran that much longer than a 2-way split with 16-way expert parallelism, on the same budget [3].
- **1.86 times — Faster swap:** A three-stage all-reduce built on NVSHMEM (NVIDIA's shared-memory library) beat the standard NCCL (NVIDIA Collective Communications Library) version by 1.86 times on 32 GPUs [1].
- **20% — Overhead inside one node:** Even with all cards on one fast link, spreading the work costs about a fifth of the throughput unless the wait gets hidden [2].

## What I'd watch:

- **The swap routine.** For 512KB to 1MB messages, the standard version ran 1.5 to 2 times slower than MPI (the Message Passing Interface) across nodes on the same cluster [1]. That gap belongs to the algorithm and its launch path, not to the silicon.
- **The layout ranking.** Narrow tensor splits with wide expert parallelism held the low-time region across all four models [3]. That holds for uniform routing and direct expert exchange.
- **The overlap trick.** Fusing the swap with the normalisation step that follows it recovered most of that overhead on an eight-card system, for 1.19 times throughput on dense models [2]. I keep coming back to that one. The cheap win is a kernel that hides a wait you already pay.
- **Where your own domain ends.** Per card, NVLink gives 900GB/s against PCIe's 128GB/s [4]. Per rack, one domain gives 130 TB/s across 72 cards [5]. Those two numbers decide which split widths are cheap on your hardware, and both are vendor figures rather than measurements.

<!-- nuanced-takeaway -->

## The catch

The wide-versus-narrow comparison is a simulator's answer, not a stopwatch. It comes from an established simulator with a packet-level network model, over fixed 4,096-token traces, and its authors say plainly that such times compare setups rather than predict live latency [3]. Read the ratio as a ranking on one modelled fabric. The direction travels; the exact multiple does not.

Node width is not a constant either. Perlmutter's node holds four cards and its fabric is not NVLink, so the edge began at eight there, and elsewhere it begins at 72 [1][5]. I could be wrong, but my read of the two results together is that the durable constant is the ratio of link speed to the size of the message a card must send, and that ratio is yours to compute.

The overhead figures belong to their own test rigs too. One comes from an eight-card system running the authors' own overlap strategy [2], and the swap gain was shown on 32 cards of one national-lab cluster [1]. Neither is a promise for a different fabric or a larger domain, where a single swap has more cards to line up.

Where this lands for a team choosing what to buy: if the model fits inside one fast domain at a split width that domain supports, the next card buys throughput. If it does not, the next purchase is link speed or a better swap routine, not another card. The question of which phase runs where is settled in [the two-pool split](/prefill-decode-two-pool-gap/), and separating the phases is usually the cheaper move than widening the split past the node.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** The limit on multi-card inference has moved from arithmetic to the wire. In a fixed hardware budget, a wide tensor split spends most of its run time with cards waiting on each other rather than multiplying matrices.
- **Why It Matters:** Teams size clusters by counting cards, but the width a tensor split can reach is set by how many cards share one fast link. Past that edge the added cards mostly add stops, and the spend lands on a wait.
- **What I'd Watch:** The measurements that separate a layout problem from a bandwidth problem.
  - **The swap routine:** Which all-reduce the stack actually runs, since a staged one beat the standard library by a wide margin at exactly the message sizes decode produces.
  - **The message size:** Batch size times hidden dimension, which decides whether an extra card costs delay or only bytes.
  - **The domain width:** How many cards share one high-speed fabric, because that number, not the cluster size, sets the split width that stays cheap.
- **The Catch:** The layout ranking comes from a simulator on modelled traces, and the link speeds are vendor claims about one product family. The ratio that matters is the one a team measures on its own fabric and its own message sizes.

## Sources
[1] P. Singhania, S. Singh, et al. — "Understanding and Improving Communication Performance in Multi-node LLM Inference", ACM Conference on AI and Agentic Systems (CAIS '26), arXiv:2511.09557v4, 20 May 2026. https://arxiv.org/html/2511.09557v4
[2] Microsoft Research — "TokenWeave: Efficient Compute-Communication Overlap for Distributed LLM Inference", arXiv:2505.11329v5. https://arxiv.org/html/2505.11329v5
[3] Y. Liu, et al. — "Joint Effects of GPU Server Topology, Parallelism, and Congestion Control on MoE Inference" (ASTRA-sim and NS-3, 768 deterministic simulations), arXiv:2609.37828v1, 29 September 2026. https://arxiv.org/html/2609.37828v1
[4] NVIDIA — "H100 Tensor Core GPU" product specifications (interconnect row: NVLink 900GB/s, PCIe Gen5 128GB/s), retrieved 28 October 2026. https://www.nvidia.com/en-us/data-center/h100/
[5] NVIDIA — "GB200 NVL72" product page (NVLink Switch System, 130 TB/s across 72 GPUs), retrieved 28 October 2026. https://www.nvidia.com/en-us/data-center/gb200-nvl72/
