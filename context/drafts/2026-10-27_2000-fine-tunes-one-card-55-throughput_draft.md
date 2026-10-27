---
title: "2,000 Fine-Tunes Cost You 5.5% Throughput"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "A shelf of task-specific fine-tunes is not a shelf of models: an adapter is a thousandth of its base model's bytes, so one 80GB card carried 2,000 of them at 7.61 requests a second against 8.05 with five, which makes host memory and a packing serving stack the next purchase for a multi-model local deployment rather than another graphics card."
date: 2026-10-27
slug: 2000-fine-tunes-one-card-55-throughput
archetype: evergreen
evergreen: true
---

<!-- lead -->
Going from five task-specific models to 2,000 on one 80-gigabyte (GB) A100 card moved throughput from 8.05 to 7.61 requests a second, a loss of 5.5% [1]. That is the whole measured cost of a four-hundredfold jump in the number of models served. It is also the number that decides whether a team buys a second graphics processing unit (GPU) or a stick of memory. The habit it breaks is the costly one: one fine-tune, one card, priced model by model as the fleet grows.

<!-- tension -->

## The big picture:

My read starts with the label. A fine-tuned model gets described as a model, and that label quietly sets the hardware budget. A low-rank adaptation (LoRA) adapter is not a model. It is a pair of small matrices bolted onto chosen weight matrices inside the base model, so its size tracks rank and layer width, not the base's parameter count [6]. The effect is that the base weights load once and every task shares them, which turns a fleet of models into one model plus a catalog.

The sums behind that are plain, and they explain the benchmark. A rank-16 adapter over a 4096-wide matrix in a 7-billion-parameter model trains under 1% of the original parameter count [6]. Measured on published files, one adapter is 13.6 megabytes (MB) against a 14.48 GB base, under a thousandth of its size, and thirty of them add about 3% to the memory the base already holds [3][4]. On an 80 GB card [5], a thousandth per task is not a rounding problem. It is a different purchasing category.

What fails first is the serving path, and the study measured that too. Its baseline, a system that copied adapters per batch, held 2.04 requests a second with five adapters and ran out of memory at 100 [2]. That is what naive adapter support looked like in 2023. The card was not full. The packing was. Once adapters are scheduled per request instead of rebuilt per batch, the limit moves to system memory (RAM), and the authors say so plainly: adapter count scales with the host's main memory [1].

That inversion belongs in a purchase order. The 80 GB of video memory (VRAM) holds the base model, the key-value cache for live requests and a small set of resident adapters. The catalog sits in RAM. A team that has trained twenty task models and is quoting a twenty-first card is pricing the wrong part by an order of magnitude. The bill it should be reading is a memory and disk bill.

## By the numbers

- **7.61 requests a second — throughput at 2,000 adapters:** One A100 80GB card served 2,000 adapters at 7.61 requests a second against 8.05 with five, so the four-hundredfold model count cost 5.5% of served rate [1].
- **2.04 requests a second — the naive baseline:** Copying adapters per batch managed 2.04 requests a second with five adapters and ran out of memory at 100, on hardware that was nowhere near full [2].
- **13.6 MB — one adapter's size:** A published adapter is 13.6 MB against a 14.48 GB base model, under a thousandth of its size, and thirty of them add roughly 3% to what the base already holds [3][4].
- **27.2 GB — the catalog's real home:** At 13.6 MB each, 2,000 adapters are 27.2 GB of host memory, where 2,000 copies of the 14.48 GB base would be 28.96 terabytes [3]. That gap is the whole argument.

<!-- tactical-insight -->

## What I'd watch:

The payback math that settled whether to tune a model at all is [priced in an earlier piece on this desk](/fine-tune-vs-rent-by-token/), and it treats a single model as the unit of comparison. Everything above changes that unit. What I keep coming back to is that the second through twentieth models are a memory and scheduler problem. The signals are visible before a purchase order goes out.

- **The live set against the catalog:** The card holds a working set of adapters while the fleet waits in RAM [1]. At 13.6 MB an adapter, a hundred task models come to 1.36 GB, about 1.7% of an 80 GB card [3][5], so the pressure lands on server memory and on how fast adapters page in.
- **The packing setting:** A serving path that rebuilds adapters per batch is where the 100-adapter failure came from, and its trace is throughput sinking as the catalog grows rather than as the card fills [2]. The modern form of that choice is a server flag: current stacks take a maximum adapter count and a maximum rank as arguments, and the default is not a promise.
- **The rank bill:** The rank you set is memory reserved for every slot, so a stack set for rank 128 pays for 128 even when each adapter is rank 16 [1][6]. The study's rank-16 example is where the under-1% figure holds, and raising rank moves both memory and quality.
- **The quality ledger:** Low-rank adapters did worse than full fine-tuning on code and math in the same study, came out level on a general instruction mix, and forgot less of the source domain [6]. Serving twenty models on one card is cheaper only if each of the twenty clears the bar its own task needs.

<!-- nuanced-takeaway -->

## The catch

My read is that the 2,000-adapter headline is a benchmark of a serving design, not a promise for your traffic. The authors ran 7-billion and 13-billion-parameter models on A100 cards of 40 GB and 80 GB, against synthetic request traces whose adapter popularity follows a power law [1][2]. Real traffic spread evenly across a catalog keeps more adapters live at once, and that changes how much paging the box does.

The failure mode has moved since the study. The out-of-memory result belongs to a baseline with naive adapter support in 2023 [2], and current stacks batch mixed adapters natively. A modern setup is more likely to lose throughput to a bad adapter limit or rank than to die at a hundred models. That is a settings defect, and from the outside it looks exactly like a capacity problem.

The size figures carry their own warnings. The 13.6 MB number is one published adapter, not a constant: rank, which modules were adapted and the saved weight format all move it. The 3% line is the hosting platform's own worked example, not a separate measurement [3][4]. What survives all of it is the ratio, and a ratio near a thousandth is what makes a fleet cheap to hold and hard to reason about.

<!-- tldr -->

## At a glance

- **The Big Shift:** A task-specific fine-tune is a small adapter bolted onto a shared base model, not a second model. One 80 GB card carried 2,000 of them at 7.61 requests a second against 8.05 with five, a 5.5% cost for a four-hundredfold rise in model count.
- **Why It Matters:** A team that has trained twenty task models and is pricing a twenty-first GPU is buying the wrong part. The catalog lives in host memory, at 27.2 GB for 2,000 adapters against 28.96 terabytes for 2,000 base models, so the next purchase is RAM and disk.
- **What I'd Watch:**
  - **The live set:** The card holds a working set of adapters while the catalog waits in RAM, so paging and host memory decide how a larger catalog feels.
  - **The packing setting:** The measured 100-adapter failure came from copying adapters per batch, and its modern form is a maximum-adapter argument left at a default.
  - **The rank bill:** Configured rank reserves memory per slot, so a stack set for a high rank pays for it on every adapter whether or not it needs it.
- **The Catch:** The benchmark used 7B and 13B models on A100 cards with synthetic power-law traffic, the out-of-memory result is dated to a 2023 baseline, and low-rank adapters measured weaker than full fine-tuning on code and math, so a twenty-model fleet needs a quality test per task.

<!-- internal-links -->

## Sources

[1] Sheng et al., "S-LoRA: Serving Thousands of Concurrent LoRA Adapters" (arXiv 2311.03285v1), Table 3 and §1 — https://arxiv.org/html/2311.03285v1
[2] Same paper, Table 3 baseline columns and §1 (naive LoRA support in the comparison serving system) — https://arxiv.org/html/2311.03285v1
[3] Hugging Face, "TGI Multi-LoRA: Deploy Once, Serve 30 Models", 18 July 2024 (adapter size against base size) — https://huggingface.co/blog/multi-lora-serving
[4] Same post, adapter memory overhead as a share of the base model — https://huggingface.co/blog/multi-lora-serving
[5] NVIDIA, A100 Tensor Core GPU product page (80 GB capacity, memory bandwidth) — https://www.nvidia.com/en-us/data-center/a100/
[6] Biderman et al., "LoRA Learns Less and Forgets Less" (arXiv 2405.09673v2), §2 and §4.1–§4.4 — https://arxiv.org/html/2405.09673v2
