# Verified Brief: workstation_compute_economics — 2026-10-27 (evergreen: multi-LoRA serving economics)

Source of truth for the article `2000-fine-tunes-one-card-55-throughput`. Every row was fetched
through the same path the push uses (`scripts/citation_hub_dossier.fetch_source`), and every figure
below was read inside its own sentence on the page, not just matched as a digit.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| E1 | serving scale | One graphics card can hold a fleet of 2,000 task adapters at once, not one model per card | VERIFIED | https://arxiv.org/html/2311.03285v1 | "Remarkably, S-LoRA can serve 2,000 adapters simultaneously, maintaining minimal overhead for the added LoRA computation." |
| E2 | throughput cost of scale | Going from 5 adapters to 2,000 on one A100 80GB moves throughput from 8.05 to 7.61 requests a second (a 5.47% loss; write it as 5.5%, never as "5x" or as a per-model figure) | VERIFIED | https://arxiv.org/html/2311.03285v1 | Table 3 (caption: "The hardware is a single A100 (80GB)"): "S1 5 8.05 2.04 0.88 100 7.99 OOM 0.25 1000 7.64 OOM - 2000 7.61 OOM -" |
| E3 | the naive path breaks | The baseline that copies adapters per batch held 2.04 requests a second with 5 adapters and ran out of memory at 100 | VERIFIED (dated to the study's 2023–24 stack — see FLAG-2) | https://arxiv.org/html/2311.03285v1 | Same Table 3 row: "5 8.05 2.04 0.88 100 7.99 OOM 0.25" |
| E4 | authors' own summary | The paper claims up to 4x the throughput of a serving system with naive LoRA support (3.95x in Table 3's 5-adapter row) and up to 30x over the PEFT library | VERIFIED | https://arxiv.org/html/2311.03285v1 | "Compared to state-of-the-art libraries such as HuggingFace PEFT and vLLM (with naive support of LoRA serving), S-LoRA can improve the throughput by up to 4 times and increase the number of served adapters by several orders of magnitude" / "When compared to the state-of-the-art parameter-efficient fine-tuning library, Huggingface PEFT, S-LoRA can enhance throughput by up to 30x" |
| E5 | where the limit actually sits | Adapter count scales with host memory, not with card memory | VERIFIED | https://arxiv.org/html/2311.03285v1 | "We will show that S-LoRA can efficiently scale the number of adapters, limited only by the available main memory." |
| E6 | adapter size vs base size | A published adapter is 13.6 MB against a 14.48 GB base model — under a thousandth of its size | VERIFIED (vendor claim — platform operator's own post, sizes as listed on the model hub) | https://huggingface.co/blog/multi-lora-serving | "predibase/magicoder is 13.6MB, which is less than 1/1000th the size of mistralai/Mistral-7B-v0.1, which is 14.48GB." |
| E7 | thirty adapters, three percent | Loading 30 adapters adds about 3% to the memory the base model already occupies | VERIFIED (vendor claim; FLAG-1 on the page's RAM/VRAM wording) | https://huggingface.co/blog/multi-lora-serving | "In relative terms, loading 30 adapters into RAM results in only a 3% increase in VRAM." |
| E8 | the overhead rule of thumb | An adapter costs roughly 1% of the base model's storage and memory | VERIFIED (vendor claim) | https://huggingface.co/blog/multi-lora-serving | "These adapters typically only add about 1% of storage and memory overhead compared to the size of the pre-trained LLM while maintaining the quality compared to fully fine-tuned models." |
| E9 | the card in the benchmark | The benchmarked card is an 80 GB A100 with over 2 terabytes a second of memory bandwidth | VERIFIED (vendor specification) | https://www.nvidia.com/en-us/data-center/a100/ | "The A100 80GB debuts the world's fastest memory bandwidth at over 2 terabytes per second (TB/s) to run the largest models and datasets." / "Combined with 80GB of the fastest GPU memory" |
| E10 | why an adapter is small | A rank-16 adapter on a 4096-wide weight matrix in a 7B model trains under 1% of the original parameter count | VERIFIED | https://arxiv.org/html/2405.09673v2 | "As an example, applying a r=16 LoRA adapter to a 7B weight matrix with d=k=4096 trains <1% of the original parameter count." |
| E11 | quality cost of low rank | Low-rank adapters underperform full fine-tuning on code and math | VERIFIED | https://arxiv.org/html/2405.09673v2 | Section 4.1 heading: "Target-domain performance: LoRA at low ranks underperforms full finetuning" |
| E12 | where quality is not lost | On a general instruction mix the same method is on par with full fine-tuning | VERIFIED | https://arxiv.org/html/2405.09673v2 | Section 4.4 heading: "For the Tülu-v2-mix dataset, LoRA is on par with full finetuning" |
| E13 | what low rank buys | Low-rank adapters forget less of the source domain | VERIFIED | https://arxiv.org/html/2405.09673v2 | Section 4.2 heading: "LoRA forgets less than full finetuning" |

## Derived arithmetic the drafter may use (recompute, never copy from this line)

- Throughput loss 5 → 2,000 adapters: (8.05 − 7.61) ÷ 8.05 = **5.47%** → write "5.5%".
- Speed-up over the naive baseline at 5 adapters: 8.05 ÷ 2.04 = **3.95x** (the paper's "up to 4x").
- 30 adapters × 13.6 MB = **408 MB**, which is 2.82% of a 14.48 GB base model — the page's "3%" and
  its "13.6MB" agree, so either may be quoted but not as an independent second measurement.
- 100 adapters × 13.6 MB = **1.36 GB** = 1.7% of an 80 GB card.
- 2,000 adapters × 13.6 MB = **27.2 GB** of host memory. 2,000 copies of the 14.48 GB base model
  would be **28,960 GB**. That ratio — 27.2 GB against 28.96 TB — is the article's core comparison.

## FLAGs the drafter must respect

- **FLAG-1 (wording, E7):** the post says adapters loaded "into RAM" produce "a 3% increase in VRAM".
  It conflates the two. Write it as the operator's own sentence and treat 3% as a vendor claim about
  the base model's memory footprint, never as a measured VRAM reading.
- **FLAG-2 (datedness, E3):** the 100-adapter out-of-memory result belongs to the baseline the study
  built against in 2023 — "a serving system with naive support of LoRA serving". Modern serving stacks
  do batch adapters natively (vLLM documents `max_loras`, `max_lora_rank` and `max_cpu_loras` as server
  arguments). The article must date that failure and must not claim today's default stack runs out of
  memory at 100 adapters.
- **FLAG-3 (generality, E1-E4):** all throughput figures are Llama-class 7B/13B/30B models on A100
  40 GB and 80 GB cards with synthetic request traces (power-law adapter popularity). They are a
  benchmark of a serving design, not a promise for any particular model or traffic mix.
- **FLAG-4 (quality, E11-E13):** low-rank adapters are not free. The same study finds them weaker than
  full fine-tuning on code and math and merely on par on a general instruction mix, while forgetting
  less. A "twenty models on one card" plan has to carry that quality difference explicitly.
