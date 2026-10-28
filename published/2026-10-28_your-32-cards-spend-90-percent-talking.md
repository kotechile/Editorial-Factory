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
image_path: "context/assets/illustrations/your-32-cards-spend-90-percent-talking/featured.jpg"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "Why Wide GPU Splits Stall. Isometric technical drawing of server racks with a data pathway bottleneck."
image_caption: "Why Wide GPU Splits Stall: How network latency chokes throughput past the node edge."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Split a model across 32 graphics processing units (GPUs) and the run stops being about math. Because every layer ends with the chips swapping partial results, 89.9% to 95.8% of the run time in a 2026 simulation study went to cards waiting on each other [3]. Those figures come from 768 modelled runs over four mixture-of-experts models at a fixed 32-card budget.

The study found a wide 16-way split took 3.68 to 4.35 times the average run time of a narrow split on the exact same hardware [3]. Real hardware points the same way, because on the Perlmutter cluster, the delay for a 70B model fell from one four-GPU node to two before stalling [1]. Past 16 GPUs, that delay stays flat or climbs [1].

<!-- tension -->

## The big picture:

The holdup moved off the math and onto the wire, and that wire ends at the node edge.

An H100 card carries 900 gigabytes per second (GB/s) of NVLink bandwidth, against 128 GB/s over Peripheral Component Interconnect Express (PCIe) Gen5 [4]. That PCIe route is the slower path a card takes when it leaves its local group. Cross the line and every layer pays a round trip on a network built for bulk moves rather than tight handoffs. 

A ring-style swap needs two serial stops per extra card, so the bytes each card sends barely grow while the stops keep rising. In the decode phase, the message is tiny. For a 70B model at batch eight, one swap moves about 128 kilobytes (KB) per card [1]. That creates a wait problem rather than a bandwidth problem, and it is the exact size where crossing a node hurts most.

So the buying talk has moved to rack-sized groups. An Nvidia GB200 NVL72 keeps 72 GPUs behind one switch rated at 130 terabytes per second (TB/s) [5]. My read: that rack is not a bigger server, but an answer to the same math that stalled the cluster at 16 cards.

## By the numbers

- **89.9% to 95.8% — Waiting time share:** Across the 32-card test runs, most of the run time went to cards swapping results rather than doing math [3].
- **3.68 to 4.35 times — Wide-split penalty:** A 16-way split ran that much longer than a 2-way split with 16-way expert parallelism, on the same budget [3].
- **1.86 times — Faster swap code:** A three-stage swap built on the Nvidia shared-memory library (NVSHMEM) beat the standard Nvidia Collective Communications Library (NCCL) version by 1.86 times on 32 GPUs [1].
- **20% — Single-node cost:** Even with all cards on one fast link, spreading the work costs about a fifth of the speed unless the wait gets hidden [2].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 172" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Your 32 Cards Spend 90% Talking: Why Wide Splits Stall</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">Waiting time share</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="269" height="18" rx="4" fill="#818cf8"/>
  <text x="519" y="84" fill="#f1f5f9" font-size="13" font-weight="600">89.9%</text>
  <text x="573" y="84" fill="#64748b" font-size="11">([3])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Single-node cost</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="60" height="18" rx="4" fill="#818cf8"/>
  <text x="310" y="132" fill="#f1f5f9" font-size="13" font-weight="600">20%</text>
  <text x="364" y="132" fill="#64748b" font-size="11">([2])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

- **The swap code:** For messages between 512 KB and 1 megabyte (MB), the standard version ran much slower than the Message Passing Interface (MPI) [1]. It lagged by 1.5 to 2 times across nodes on the same cluster, which means the gap belongs to the software rather than the silicon.
- **The layout ranking:** Narrow splits with wide expert splits held the low-time zone across all four models [3]. That finding holds for plain routing and direct expert swaps alike.
- **The overlap trick:** Blending the swap with the normalisation step that follows it won back most of that lost time on an eight-card system, yielding 1.19 times the speed on dense models [2]. I keep coming back to that one, because the cheap win is code that hides a wait you already pay.
- **Where your own group ends:** Per card, NVLink gives 900 GB/s against PCIe's 128 GB/s [4]. Per rack, one group gives 130 TB/s across 72 cards [5]. Those two numbers decide which split widths remain cheap on your hardware, and both are vendor claims rather than live checks.

<!-- nuanced-takeaway -->

## The catch

The wide-versus-narrow check is a model's answer rather than a stopwatch. It comes from an established test with a packet-level network model over fixed 4,096-token traces, and its authors say plainly that such times compare setups rather than predict live speed [3]. Read the ratio as a ranking on one modelled network, because the trend travels even if the exact multiple does not.

Node width is not a constant either. The Perlmutter node holds four cards and its link is not NVLink. So the edge began at eight GPUs there, while elsewhere it begins at 72 [1][5]. I could be wrong, but my read of the two results is that the firm rule remains the ratio of link speed to the message size a card must send.

The lost-time figures belong to their own test rigs too. One comes from an eight-card system running the authors' own overlap trick [2], and the swap gain was shown on 32 cards of one lab cluster [1]. Neither is a firm promise for a different network or a larger group where a single swap has more cards to line up.

Where this lands for a tech team: if the model fits inside one fast group at a split width that group supports, the next card buys speed. If it does not, the next buy is link speed or a better swap code rather than another card. The question of which phase runs where is settled in [the two-pool split](/prefill-decode-two-pool-gap/), and splitting the phases is usually the cheaper move than stretching the split past the node.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…" -> /local-ai-payback-cloud-gpu-spread/ [same site (aichieve.net); same category; topical overlap: gpus, graphics, processing, split] Link "Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…" in the section where the article touches gpus, graphics, processing. -->
<!-- internal-link hint: "Your GPU Runs Out of Cache Before It Runs Out of Math" -> /kv-cache-is-the-concurrency-ceiling/ [same site (aichieve.net); same category; topical overlap: graphics, math, model, processing] Link "Your GPU Runs Out of Cache Before It Runs Out of Math" in the section where the article touches graphics, math, model. -->
<!-- internal-link hint: "1.016M Non-GPUs: Your Chip Stopped Deciding" -> /your-chip-stopped-deciding/ [same site (aichieve.net); same category; topical overlap: gpus, graphics, processing] Link "1.016M Non-GPUs: Your Chip Stopped Deciding" in the section where the article touches gpus, graphics, processing. -->
## Related reading

- [Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…](/local-ai-payback-cloud-gpu-spread/) — more on Major Purchases & Assets
- [Your GPU Runs Out of Cache Before It Runs Out of Math](/kv-cache-is-the-concurrency-ceiling/) — more on Major Purchases & Assets
- [1.016M Non-GPUs: Your Chip Stopped Deciding](/your-chip-stopped-deciding/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** The limit on multi-card runs has moved from math to the wire. In a fixed hardware budget, a wide split spends most of its run time with cards waiting on each other rather than doing math.
- **Why It Matters:** Tech teams size clusters by counting cards, but the width a split can reach is set by how many cards share one fast link. Past that edge, the added cards mostly add network stops, and the extra spend lands on a wait.
- **What I'd Watch:** The checks that separate a layout problem from a bandwidth problem.
  - **The swap code:** The specific rule the stack runs, because a staged version beat the standard library at the exact message sizes the decode phase makes.
  - **The message size:** The batch size multiplied by the hidden dimension, which decides whether an extra card costs delay or only bytes.
  - **The domain width:** The number of cards sharing one high-speed link, because that figure sets the split width that stays cheap.
- **The Catch:** The layout ranking comes from a test on modelled traces, and the link speeds are vendor claims about one product line. The ratio that truly matters is the one a team measures on its own network and its own message sizes.

## Sources
[1] P. Singhania, S. Singh, et al. — "Understanding and Improving Communication Performance in Multi-node LLM Inference", ACM Conference on AI and Agentic Systems (CAIS '26), arXiv:2511.09557v4, 20 May 2026. https://arxiv.org/html/2511.09557v4
[2] Microsoft Research — "TokenWeave: Efficient Compute-Communication Overlap for Distributed LLM Inference", arXiv:2505.11329v5. https://arxiv.org/html/2505.11329v5
[3] Y. Liu, et al. — "Joint Effects of GPU Server Topology, Parallelism, and Congestion Control on MoE Inference" (ASTRA-sim and NS-3, 768 deterministic simulations), arXiv:2609.37828v1, 29 September 2026. https://arxiv.org/html/2609.37828v1
[4] NVIDIA — "H100 Tensor Core GPU" product specifications (interconnect row: NVLink 900GB/s, PCIe Gen5 128GB/s), retrieved 28 October 2026. https://www.nvidia.com/en-us/data-center/h100/
[5] NVIDIA — "GB200 NVL72" product page (NVLink Switch System, 130 TB/s across 72 GPUs), retrieved 28 October 2026. https://www.nvidia.com/en-us/data-center/gb200-nvl72/
