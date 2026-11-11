---
title: "Batch 32 Kills Your 4-Bit Win"
vertical: gpu_hardware
kind: evergreen
archetype: evergreen
evergreen: true
persona: infra_engineer
one_big_thing: "A quantization recipe's speedup is the share of your step time that is memory-bound, so 4-bit weights are 1.95x faster than 16-bit at batch 1 and 1.16x at batch 32, where eight-bit arithmetic overtakes them; past that point four bits buys capacity and a small accuracy bill, never throughput."
date: 2026-11-11
slug: batch-32-kills-your-4-bit-win
meta_title: "Batch 32 Kills Your 4-Bit Win"
meta_description: "Four-bit weights beat BF16 by 1.95x at batch 1 and 1.16x at batch 32, where FP8 overtakes them. Size the recipe from your batch, not the model card."
image_path: "context/assets/illustrations/batch-32-kills-your-4-bit-win/featured.jpg"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "Split-screen cutaway of two accelerator boards: one amber weight block on the left, a fan of blue cables into stacked memory on the right"
image_caption: "Batch 32 Kills Your 4-BIT Win: Size the recipe from your batch, not the model card."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A 4-bit checkpoint looks like free throughput, and at batch 1 it very nearly is. On one H100 serving an 8-billion-parameter open model, the 4-bit build decodes 255 tokens a second where the 16-bit build manages 131 [5]. Batch 32 kills that win: the same build reaches 3,241 tokens a second, the eight-bit recipe reaches 3,586, and the four-bit choice is now the slower of the two [5]. Your batch decides which of those you get, because the saving was never in arithmetic: it was in bytes moved.

<!-- tldr -->

## At a glance

- **The shift:** four-bit weights save bandwidth, so they pay at batch 1 and fade as batches grow.
- **The number:** 1.02x is all that is left at batch 256.
- **The risk:** four bits buys capacity there, plus a small accuracy bill.

<!-- tension -->

## Where the speedup actually comes from

Decode at batch 1 reads every weight for every token it emits. The step is limited by bytes moved, and 4-bit weights move a quarter of the bytes that 16-bit weights do [1]. The measured gain lands between 1.35x and 2.12x rather than at 4x. Unpacking the weights, the attention work and the stored per-token cache a decode step re-reads do not shrink with them [1]. A weight-only recipe shrinks the book you re-read on every step, not the arithmetic that reads it.

Raise the batch and one read of the weights serves many sequences at once. The matrix multiplies become compute-bound, and 4-bit weights still multiply in 16 bits, so the saving disappears: Gemma 3 12B gains just 1.02x at batch 256 [1]. A long prompt reaches the same wall from the other side, and the A100 gain on Qwen2.5-14B falls from 2.12x at a one-token input to 1.64x at a 30,720-token input [2]. Capacity and speed come apart at different batch sizes, and a team can buy one while believing it bought the other.

Eight-bit recipes change the arithmetic, not only the storage. FP8 runs the multiply in eight bits. Hopper's FP8 tensor cores are rated at 3,958 teraFLOPS, against 1,979 for BF16 [7]. That is why an eight-bit build overtakes the four-bit one as the work turns compute-bound: on an H20 at a 30,720-token prompt, FP8 is 1.68x faster than 16-bit and an activation-aware weight quantization (AWQ) build is 1.42x [2].

| Recipe | Batch 1 | Batch 32 | Batch 32, four-way split | What it changes |
|---|---|---|---|---|
| 16-bit compiled baseline | 131 tokens/s | 2,799 | 5,575 | nothing, it is the yardstick |
| 4-bit weight-only | 255 | 3,241 | 6,334 | bytes moved per token |
| Float8 dynamic | 166 | 3,586 | 6,159 | precision of the multiply |

I read this table twice before I believed it: the recipe that wins is the one whose saving survives the batch you actually run. The table is one model on one card, and it is the cleanest measurement in the record.

Telling which regime you are in takes one measurement and no theory. Run the same prompt at batch 1 and at the batch your scheduler reaches, and record tokens a second for the 4-bit build and the 16-bit build. If the ratio holds near its batch-1 value, the step is waiting on bytes and the recipe is doing its job. If it falls toward parity, the multiply is the limit, and capacity is all you are buying. A memory-bound step also leaves the compute units idle, so an engine metric that reports queue depth will say which side of the roof you landed on.

## By the numbers

The three figures that matter are the ceiling, the footprint and the quality bill.

- **1.02x:** what Gemma 3 12B's 4-bit build still returns at batch 256 in vLLM, 13.81 s against 14.07 s [1].
- **9.94 gigabytes:** the Qwen2.5-14B footprint in 4-bit, against 28.08 gigabytes for 16-bit [2].
- **69.48 points:** the shipped Gemma 3 12B 4-bit checkpoint on MMLU (a general knowledge test), against 71.51 for the model it was built from [6].

<!-- tactical-insight -->

## What I'd watch in the scheduler

My suspicion is that batch size is rarely yours to pick. Interactive traffic holds batch 1, because a queue of one request is what a user experiences, so the 4-bit recipe keeps most of its advantage there [5]. A throughput tier that packs 32 requests into a step gives most of it back, and teams running both tiers end up serving two checkpoints of one model [5]. That is a second copy of weights in memory, which is the cost the 4-bit build was bought to avoid. None of it is a hardware defect; it is the arithmetic of a batch.

The signal I would watch next is an eight-bit timing at high batch on hardware you own. The record tests FP8 at batch 1 and with long prompts, and grades its large-batch claim low because no in-band source measured it above batch 1 [1]. Until that number exists for your card, treat the crossover as a direction rather than a position, and measure your own engine at your own batch — the same lesson [the prefill and decode split](/prefill-decode-two-pool-gap/) taught about moving work between pools.

<!-- nuanced-takeaway -->

## The catch

Most published accuracy deltas cannot settle the choice, because the benchmark is the weaker instrument here. A reader who wants one decisive number will not get it from this record. A recipe that looks costly on one test can look free on another, and the size of the model moves the answer again. HumanEval holds 164 questions, so one run carries a standard error near 3.9 points. That is wider than the −3.05 to +6.10 spread of every delta in the record [3]. No recipe's code score survives that yardstick, so a code benchmark tells you little about which build to ship [3].

The losses that do survive sit on GSM8K (a grade-school maths word-problem set). The activation-aware weight quantization (AWQ) recipe gives up 4.17 points on Qwen3-14B, and generalized post-training quantization (GPTQ) gives up 4.02 on Mistral NeMo, both beyond three standard errors [4]. Meanwhile every eight-bit delta on MMLU stays inside 0.77 points, and 4-bit costs 0.43 to 1.43 [4].

The shipped Gemma 3 12B card is the useful counterweight: its own 4-bit checkpoint reads 2.03 points below its 16-bit parent on the full MMLU set, above the compiled range, and training that simulates the rounding recovers part of that gap [6]. None of the timings in that record came from a current engine release, and the other accelerator vendors publish no timing in this band at all [1]. The direction is what I trust; the constants are what I would re-measure.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "2,000 Fine-Tunes Cost You 5.5% Throughput" -> /2000-fine-tunes-one-card-55-throughput/ [same site (aichieve.net); same category; topical overlap: throughput] Link "2,000 Fine-Tunes Cost You 5.5% Throughput" in the section where the article touches throughput. -->
<!-- internal-link hint: "1.016M Non-GPUs: Your Chip Stopped Deciding" -> /your-chip-stopped-deciding/ [same site (aichieve.net); same category] Link "1.016M Non-GPUs: Your Chip Stopped Deciding" in the section where the article touches this topic. -->
<!-- internal-link hint: "18x LPDDR Isn't 18 TB/s" -> /18x-lpddr-isnt-18tbs/ [same site (aichieve.net); same category] Link "18x LPDDR Isn't 18 TB/s" in the section where the article touches this topic. -->
## Related reading

- [2,000 Fine-Tunes Cost You 5.5% Throughput](/2000-fine-tunes-one-card-55-throughput/) — more on Major Purchases & Assets
- [1.016M Non-GPUs: Your Chip Stopped Deciding](/your-chip-stopped-deciding/) — more on Major Purchases & Assets
- [18x LPDDR Isn't 18 TB/s](/18x-lpddr-isnt-18tbs/) — more on Major Purchases & Assets
<!-- internal-links:end -->

## Sources

- [1] Smit Kadvani, Kriti Faujdar and Spurthi Tallam, "Twice as Fast, Until It Isn't: Quantized Serving of Mid-Size Open LLMs", arXiv:2611.04380v1, 3 November 2026 — https://arxiv.org/html/2611.04380v1
- [2] Same letter, §3 Table 1 (vLLM 0.6.3, one A100 80GB, Qwen2.5-14B-Instruct) — https://arxiv.org/html/2611.04380v1
- [3] Same letter, §4, single-run standard errors — https://arxiv.org/html/2611.04380v1
- [4] Same letter, §4 Table 2, accuracy against BF16 — https://arxiv.org/html/2611.04380v1
- [5] PyTorch, "Accelerating LLM Inference with GemLite, TorchAO and SGLang", decode throughput table on H100 — https://pytorch.org/blog/accelerating-llm-inference
- [6] PyTorch, model card "pytorch/gemma-3-12b-it-QAT-INT4", latency and MMLU tables — https://huggingface.co/pytorch/gemma-3-12b-it-QAT-INT4
- [7] NVIDIA, H100 Tensor Core GPU product page, specifications table — https://www.nvidia.com/en-us/data-center/h100/
