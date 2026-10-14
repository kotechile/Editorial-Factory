---
title: "Why Your Card Serves 1.6: The Two-Pool Gap"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "Prefill and decode are two different machines inside one request — one limited by math, one limited by memory speed — so splitting them into pools whose ratio matches your prompt-to-answer mix is where the next gain in served requests comes from, and the price of the split is the key-value cache the network carries between the pools."
date: 2026-10-14
slug: prefill-decode-two-pool-gap
archetype: evergreen
evergreen: true
meta_title: "Why Your Card Serves 1.6: The Two-Pool Gap"
meta_title_source: "derived_from_title"
meta_description: "One graphics processing unit (GPU) serves about 1.6 requests a second when it runs a 13-billion-parameter model by itself."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/prefill-decode-two-pool-gap/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "The Prefill Decode Split. Two distinct metallic processor modules connected by a glowing amber cable on a dark basalt surface"
image_caption: "The Prefill Decode Split: Splitting GPU tasks into two pools doubles request rates."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
One graphics processing unit (GPU) serves about 1.6 requests a second when it runs a 13-billion-parameter model by itself. Two cards on the reading step and one on the writing step served 10 requests a second between them — 3.3 for each card, or 2.1 times the rate [2]. Nobody added chips to the second setup. The cards just stopped doing two different jobs at once.

<!-- tension -->

## The big picture:

Every AI request is really two jobs that need different things.

Reading the prompt — prefill — runs in one pass and is driven by math. Writing the answer — decode — emits one token at a time and is capped by memory speed [3].

Run both on one card and they trip over each other. The researchers call it prefill-decoding interference, and it forces both phases onto one layout of the cards [2].

Across its tests, the split design served 7.4 times more requests than the setups that keep both phases on one card. It held the same latency limit for more than 90% of them [2].

The part I keep circling is that neither step is slow. They are just fast at different things. DeepSeek says its live service already splits these steps into separate pools, using a different hardware setup for each phase [1].

One number shows how far apart the two phases sit. On DeepSeek's own chips, a node read 73.7k input tokens a second while prefilling, and wrote 14.8k output tokens a second while decoding [1]. That is a five-to-one gap.

## By the numbers

- **1.6 to 3.3 requests a second — The split, per card:** One A100 card ran a 13-billion-parameter model alone and served about 1.6 requests a second at a 90% service-level objective (SLO) goal. Two cards on prefill and one on decode served 10 a second between them, or 3.3 for each card — 2.1 times the rate [2].
- **73.7k against 14.8k tokens a second — The two phases, one node:** DeepSeek's input rate for reading prompts compared to its output rate for writing answers, inside a service that already runs the pools apart [1].
- **1.13GB per 512-token request — Payload on the wire:** The size of the key-value (KV) cache for one 512-token request on a 66-billion-parameter model. At 10 requests a second the pools need about 90 gigabits per second (Gbps) of link speed before the move stops showing up in latency [2].
- **1.4× throughput at 20% lower cost — The cluster result:** Splitwise's split cluster against a standard one on the same budget, with 2.35 times the throughput as the other choice at equal cost and power [3].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that the win comes from managing traffic, not buying faster parts. Three things decide if this split works, and operators can measure all three before buying a single new card.

- **The prompt-to-answer ratio:** DeepSeek logged 608 billion input tokens against 168 billion output tokens, sizing its pools for that exact mix [1]. A chat app and a text reader need entirely different splits of the same hardware.
- **The cache hit rate:** In that same DeepSeek window, 342 billion of those input tokens — 56.3% — came from an on-disk KV cache, and the average KV length for each output token was 4,989 tokens [1]. Heavy reuse makes the reading phase cheap, which shrinks the gains from splitting the pools.
- **The wire between pools:** Moving the KV cache is the price of splitting the work. One research group hides a network switch's delay inside the reading phase and carries the cache at 0.55 to 0.78 times the cost of a 2:1 packet fabric [4]. Nvidia's own post claims its newest rack handles up to 30 times more requests [5]. I'd want per-phase numbers from a live service before I believed either claim at my own scale.

<!-- nuanced-takeaway -->

## The catch:

My read is that splitting the work moves the wait rather than removing it.

The interference this setup fixes is a shared-resource problem on the card. The transfer it creates is a speed problem on the network. On a cluster where links between nodes are thinner than the wires inside a card, moving the KV cache can cost more time than the split saved [2].

The published wins also rely on narrow tests: one lab system using A100-class parts in 2024, another in 2023, and one operator's service on custom chips. None of these promise the same results for a different model, a slower network link, or a shorter prompt.

Pool sizes must follow the traffic. A setup built for DeepSeek's mix of long prompts and short answers will not fit a coding bot that streams thousands of tokens back to the user [1].

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your GPU Runs Out of Cache Before It Runs Out of Math" -> https://giniloh.com/kv-cache-is-the-concurrency-ceiling/ [same site (giniloh.com); same category; topical overlap: graphics, model, processing, runs] Link "Your GPU Runs Out of Cache Before It Runs Out of Math" in the section where the article touches graphics, model, processing. -->
<!-- internal-link hint: "Fine-Tune or Rent: The Denominator Decides Your Break-Even" -> https://giniloh.com/fine-tune-vs-rent-by-token/ [same site (giniloh.com); same category; topical overlap: card, graphics, model] Link "Fine-Tune or Rent: The Denominator Decides Your Break-Even" in the section where the article touches card, graphics, model. -->
<!-- internal-link hint: "Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…" -> https://giniloh.com/local-ai-payback-cloud-gpu-spread/ [same site (giniloh.com); same category; topical overlap: graphics, processing, unit] Link "Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…" in the section where the article touches graphics, processing, unit. -->
## Related reading

- [Your GPU Runs Out of Cache Before It Runs Out of Math](https://giniloh.com/kv-cache-is-the-concurrency-ceiling/) — more on Major Purchases & Assets
- [Fine-Tune or Rent: The Denominator Decides Your Break-Even](https://giniloh.com/fine-tune-vs-rent-by-token/) — more on Major Purchases & Assets
- [Local AI Payback: Your Rig Just Tripled as Cloud GPUs Split…](https://giniloh.com/local-ai-payback-cloud-gpu-spread/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Serving an AI model requires two distinct jobs. Reading the prompt is limited by math, while writing the answer is limited by memory speed. Splitting these jobs onto separate pools is driving recent speed gains.
- **Why It Matters:** The bottleneck inside a request is the other phase, not the chip itself. This turns pool size, pool ratio, and the network connecting them into capacity choices that directly change hardware costs.
- **What I'd Watch:** Whether the ratio between prompt tokens and answer tokens matches the hardware pools, and whether the cache transfer stays hidden.
  - **Prompt-to-answer ratio:** The number of input tokens divided by output tokens, which tells you exactly how many cards each pool needs.
  - **Cache-hit share:** The chunk of a prompt answered from stored key-value data instead of fresh math, which lowers the value of adding extra reading power.
  - **Transfer bandwidth:** The network link speed between the pools, which must carry the key-value cache of every request without delaying the first word.
- **The Catch:** The split trades an on-card clash for a heavy network bill. A traffic mix that does not match the chosen pool design quickly loses the edge the cluster was built for.

## Sources
[1] DeepSeek, "DeepSeek-V3/R1 inference system overview" (Open Source Week day 6), production service statistics for 2025-02-27/28 — https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md
[2] Yinmin Zhong et al., "DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving" (OSDI 2024) — https://arxiv.org/html/2401.09670v3
[3] Pratyush Patel et al., "Splitwise: Efficient Generative LLM Inference Using Phase Splitting" (ISCA 2024) — https://arxiv.org/html/2311.18677v1
[4] "An optical KV cache network for disaggregated LLM serving" (arXiv, 2026-10-13) — https://arxiv.org/abs/2610.18444
[5] NVIDIA, "Introducing NVIDIA Dynamo, a low-latency distributed inference framework for scaling reasoning AI models" (2025-03-18) — https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/

## Gate report
PASS — Lead delivers the core speed stat immediately without preamble.
PASS — Tension uses highly readable, simple diction to explain the math vs. memory bottleneck and includes a first-person cue.
PASS — Tactical-insight translates technical constraints into measurable variables without issuing commands, using plain words.
PASS — Nuanced-takeaway frankly addresses the network bandwidth tradeoff and narrow testing conditions using fluent, short sentences.
PASS — TLDR strictly follows the 4-part Smart Brevity structure with indented sub-bullets for What I'd Watch.
