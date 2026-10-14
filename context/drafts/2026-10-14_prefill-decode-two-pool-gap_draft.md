---
title: "Why Your Card Serves 1.6: The Two-Pool Gap"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "Prefill and decode are two different machines inside one request — one limited by math, one limited by memory speed — so splitting them into pools whose ratio matches your prompt-to-answer mix is where the next gain in served requests comes from, and the price of the split is the key-value cache the network carries between the pools."
date: 2026-10-14
slug: prefill-decode-two-pool-gap
archetype: evergreen
evergreen: true
---

<!-- lead -->
One graphics processing unit (GPU) ran a 13-billion-parameter model and answered about 1.6 requests per second. The same model, split so that two cards read the prompt and one card wrote the answer, served 10 requests a second — 3.3 per card, a little over twice the rate [2]. Nobody added silicon. The cards were doing different jobs.

<!-- tension -->

## The big picture:

Every request is two jobs with opposite appetites. Prefill reads the prompt in one pass, and math sets its speed. Decode writes the answer one token at a time, and memory speed sets its speed [3]. Run both on one card and each waits on the other. The team that measured the 1.6 figure calls it prefill-decoding interference, and it also forces both phases onto one layout of the cards [2].

The part I keep circling is that neither phase is slow. They are fast at different things. DeepSeek reports its production service already runs prefill and decode as separate pools, with a different layout for each phase [1].

One number shows how far apart they are. On DeepSeek's own hardware, a node moved about 73.7k tokens a second of input while prefilling, against about 14.8k tokens a second of output while decoding. That is roughly five to one [1].

## By the numbers

- **1.6 to 3.3 requests a second — the split, per card:** One A100 card ran a 13B model on its own at a 90% service-level objective (SLO) goal and served about 1.6 requests a second. Two cards on prefill and one on decode served 3.3 each, which the authors call 2.1× [2].
- **73.7k against 14.8k tokens a second — the two phases, one node:** DeepSeek's per-node input rate while prefilling against its output rate while decoding, in a service that already runs the two pools separately [1].
- **1.13GB per 512-token request — the payload on the wire:** The size of the key-value (KV) cache for one 512-token request on a 66-billion-parameter model. At 10 requests a second the pools need about 90Gbps between them before the transfer stops showing up in latency [2].
- **1.4× throughput at 20% lower cost — the cluster result:** Splitwise's phase-split cluster against a conventional one on the same budgets, with 2.35× the throughput as the other choice at equal cost and power [3].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that the payoff comes from the traffic, not from the parts. Three things carry it, and all three are measurable before anyone buys a card.

- **The ratio between prompt and answer.** DeepSeek's own window logged 608B input tokens against 168B output tokens, and its pools were sized for that mix rather than for a round number [1]. A chat app and a summariser want different splits of the same hardware.
- **Whether the cache already does the work.** In that same day, 342B of the 608B input tokens — 56.3% — came from an on-disk KV cache, and the average KV length for each output token was 4,989 tokens [1]. Heavy reuse makes prefill cheap, which shrinks the gain left to collect.
- **The wire between the pools.** The transfer is the price of the split. One research group hides a switch's delay inside prefill and carries the cache at 0.55 to 0.78 times the cost of a 2:1 packet fabric [4]. Nvidia's own post claims up to 30× more requests served on its newest rack [5]. I'd want per-phase numbers from an operator before I believed either at my own scale.

<!-- nuanced-takeaway -->

## The catch:

My read is that the split moves the queue rather than removing it. The interference it fixes is a shared-resource problem. The transfer it creates is a bandwidth problem, and on a cluster whose cross-node links are thinner than its cards, the second can cost more than the first saved [2].

The published gains also come from narrow setups: one research system on A100-class parts in 2024, another in 2023, and one operator's service on its own silicon. None of them is a promise about a different model, a different link, or a shorter prompt.

And the sizes follow the traffic. A pool plan built for DeepSeek's mix of long prompts and short answers will not fit a code assistant that streams thousands of tokens out [1].

<!-- tldr -->

## At a glance

- **The Big Shift:** Serving a language model is really two jobs. Reading the prompt is limited by math, and writing the answer is limited by memory speed. Splitting those jobs onto separate pools, instead of running both on every card, is where the recent gains in served requests come from.
- **Why It Matters:** The bottleneck inside a request is the other phase, not the chip. That turns pool size, pool ratio and the network between the pools into capacity decisions with real money attached, and it changes what a throughput number on a spec sheet is worth.
- **What I'd Watch:** Whether the ratio between prompt tokens and answer tokens matches the pools, and whether the cache transfer stays invisible.
  - **Prompt-to-answer ratio:** The number of input tokens divided by output tokens, which sets how many cards each pool needs.
  - **Cache-hit share:** How much of the prompt is answered from stored key-value data instead of being computed again, which lowers the value of extra prefill capacity.
  - **Transfer bandwidth:** The link speed between the pools, which has to carry the key-value cache of every request without showing up in the time to the first token.
- **The Catch:** The split trades interference for a network bill, and the measured gains come from specific hardware and specific traffic. A mix that does not match the pool plan loses the advantage it was built for.

## Sources
[1] DeepSeek, "DeepSeek-V3/R1 inference system overview" (Open Source Week day 6), production service statistics for 2025-02-27/28 — https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md
[2] Yinmin Zhong et al., "DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving" (OSDI 2024) — https://arxiv.org/html/2401.09670v3
[3] Pratyush Patel et al., "Splitwise: Efficient Generative LLM Inference Using Phase Splitting" (ISCA 2024) — https://arxiv.org/html/2311.18677v1
[4] "An optical KV cache network for disaggregated LLM serving" (arXiv, 2026-10-13) — https://arxiv.org/abs/2610.18444
[5] NVIDIA, "Introducing NVIDIA Dynamo, a low-latency distributed inference framework for scaling reasoning AI models" (2025-03-18) — https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/
