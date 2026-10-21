# Verified Brief: gpu_hardware — 2026-10-21

Claim extraction from `2026-10-21_gpu_hardware_angle_brief.md` (Angle Type: Synthesis). Every row below was fetched from its own primary URL during this run. Both anchors carry ≥2 VERIFIED claims → **Dual-Anchor Gate PASS**.

**Fetch record.** Signal A's full text was retrievable (arXiv HTML, 88,298 chars of extracted text) and is quoted from the paper's own body and figure captions. Signal B's HTML is not served in this environment; its claims are verified against the paper's own abstract as returned by the arXiv API for `id_list=2610.22863` and served verbatim on `https://export.arxiv.org/abs/2610.22863` (5,358 chars, abstract present). **Drafter ruling: Signal B may be cited only for what its abstract states** — no figure, sample or mechanism beyond those rows may be attributed to it.

## Leg A — The Token-Energy Law (anchor 1)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| A1 | Energy model form | GPU-board energy per useful output token is an affine function of two byte/time coordinates — shared dense-weight bytes, private KV bytes, and realized decode time — with coefficients calibrated per model and hardware/runtime configuration | VERIFIED | https://arxiv.org/abs/2610.28576 | `e_gross,σ = c_σ + α_σ q_w + β_σ q_KV + P_τ,σ τ + u_σ` … "`e_gross,σ` is GPU-board energy in joules per useful output token. The coefficients `α_σ`, `β_σ`, and `P_τ,σ` describe effective energy responses to weight demand, KV demand, and time" |
| A2 | Model accuracy | All evaluated condition means from 374 held-out energy executions are within 3.73% of measurement | VERIFIED | https://arxiv.org/abs/2610.28576 | "All evaluated condition means from 374 held-out energy executions are within 3.73% of measurement." |
| A3 | Private KV reads per output | Each request processes its own private, materialized KV history; an output attending L historical records incurs K_KV × L logical read bytes plus one new-record write — i.e. the read is per output token, not once per request | VERIFIED | https://arxiv.org/abs/2610.28576 | "Each request processes its own private, materialized KV history. Let K_KV denote the constant byte size of one complete KV record … An output attending L historical records incurs K_KV L logical read bytes and is aligned with one new-record write." |
| A4 | History raises energy | Mean measured energy increases with attended history in every plotted series | VERIFIED | https://arxiv.org/abs/2610.28576 | "Mean energy increases with history in every plotted series." (Fig. 9 caption); abstract: "longer attended histories increase private KV demand" |
| A5 | Test envelope | Three dense models (Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3), BF16 weights and KV, FlashAttention, **full-history attention**, NVIDIA GH200 (144 GB HBM3e per device, 700 W per-GPU power limit) and GB300 (1,300 W per-GPU limit), vLLM 25.09 runtime | VERIFIED | https://arxiv.org/abs/2610.28576 | "All experiments use BF16 weights and KV state, FlashAttention, and full-history attention. The GH200 platform is a dual-GPU node with 144-GB HBM3e per device … a fixed 700-W power limit per GPU. The GB300 experiments use … a fixed 1,300-W power limit per GPU" |
| A6 | Batching amortises weights only | Larger tested batches lower measured mean energy at matched model, platform and history — the shared-weight term amortises, the private KV term does not | VERIFIED | https://arxiv.org/abs/2610.28576 | "Larger tested batches have lower measured mean energy at matched model, platform, and history settings." (against A3: KV bytes are per request) |

## Leg B — KV residency in production agentic workloads (anchor 2)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| B1 | Trace base | Four production Microsoft M365 workload traces (Deep Research, Enterprise Assistant, Coding Agent, Enterprise Chat) spanning more than 121 million model calls | VERIFIED | https://arxiv.org/abs/2610.22863 | "We characterize four production Microsoft M365 workload traces (Deep Research, Enterprise Assistant, Coding Agent and Enterprise Chat) spanning more than 121 million model calls." |
| B2 | Context growth inside a session | In Deep Research the application issues 89% of model calls and the median context grows from about 10K to 68K tokens by the 30th call | VERIFIED | https://arxiv.org/abs/2610.22863 | "In Deep Research, the application issues 89% of model calls and the median context grows from about 10K to 68K tokens by the 30th call." |
| B3 | Prefix-cache share | About 80% of context tokens are served from the prefix cache | VERIFIED | https://arxiv.org/abs/2610.22863 | "About 80% of context tokens are served from the prefix cache." |
| B4 | Capacity ceiling and retention time | One 99th-percentile Deep Research session exceeds the 80 GB HBM of an NVIDIA H100, and holding all live sessions at their peak needs an estimated 501.8 TB of HBM, although inference occupies only 5.6% of that retention time | VERIFIED | https://arxiv.org/abs/2610.22863 | "one 99th-percentile Deep Research session exceeds the 80 GB HBM of an NVIDIA H100, and holding all live sessions at their peak needs an estimated 501.8 TB of HBM, although inference occupies only 5.6% of that retention time." |
| B5 | Clock as a lever | A one-hour idle cap cuts the ceiling 3.6x while raising the share of calls that recompute context only from 4.07% to 4.53% | VERIFIED | https://arxiv.org/abs/2610.22863 | "a one-hour idle cap cuts this ceiling by 3.6x while raising the share of calls that recompute context only from 4.07% to 4.53%." |
| B6 | Eviction quality at tight budgets | At one tenth of the busiest hour's demand, LRU eviction makes 63% of Deep Research calls recompute and clairvoyant furthest-next-use 31%, where multi-resolution retention (demoting the LRU session's KV state to int4) lowers it to 13.6% | VERIFIED | https://arxiv.org/abs/2610.22863 | "at one tenth of the busiest hour's demand, LRU eviction makes 63% of Deep Research calls recompute and clairvoyant furthest-next-use 31%, whereas multi-resolution retention (MRR), which demotes the LRU session's KV state to int4, lowers this to 13.6%." |
| B7 | Placement limit | When the next call reaches a different deployment, cached-context reuse drops from 89% to 29%; treating KV state as deployment-local raises the recompute floor under unlimited memory from 5.4% to 20.2% | VERIFIED | https://arxiv.org/abs/2610.22863 | "when the next call reaches a different deployment, cached-context reuse drops from 89% to 29%, and treating KV state as deployment-local raises the recompute floor under unlimited memory from 5.4% to 20.2%." |
| B8 | Estimate's own limitation | The capacity arithmetic uses the public Llama-2-70B KV layout as a stand-in for confidential production models | VERIFIED | https://arxiv.org/abs/2610.22863 | "With the public Llama-2-70B KV layout standing in for confidential models …" |

## Corroborating rows (not anchors)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| C1 | Cache hits are a prefill lever | A remote KV tier left median time-to-first-token unchanged but raised the 16k-token p99 from 3.96 s to 17.3 s; a remote hit took 0.88 s against 0.31 s to recompute the prompt; a hit only pays above B\* = 2.53 GB/s, and a fixed per-hit cost means prompts shorter than about 17k tokens cannot beat recompute at any bandwidth | VERIFIED | https://arxiv.org/abs/2610.21500 | "Enabling the remote tier (LMCache with a Valkey store) left median time-to-first-token unchanged but raised the 16k-token p99 from 3.96 s to 17.3 s … a remote hit took 0.88 s against 0.31 s to recompute the prompt … a hit pays off only if the tier delivers more than B\* = sR (2.53 GB/s …)" |
| C2 | Power lives in the memory path | Toggling all HBM2-internal bank-group bus signals costs 29.4% more power than holding them constant, and an engineered pattern draws 23.6% more across 36 chips than the highest-power-consuming JEDEC-specified loop — so a vendor/spec loop is not a ceiling; the new model predicts power at 7.6–8.1% MAPE and matches HBM3E memory power on three H200 GPUs within 2.4% to 5.3% | VERIFIED | https://arxiv.org/abs/2610.14244 | "toggling all HBM2-internal bank group bus signals causes 29.4% higher power consumption than keeping them constant … an access pattern that yields 23.6% higher power consumption on average across 36 tested HBM2 chips than the highest-power-consuming JEDEC-specified current measurement loop … 7.6 -- 8.1% mean absolute percentage error" |
| C3 | Agents run at batch one | Agent trajectories are sequentially dependent and run at effective batch one, so per-token decode latency dominates completion time; a 2% per-step failure rate erases a 2x decode advantage over a 20-step trajectory | VERIFIED | https://arxiv.org/abs/2610.07094 | "agent trajectories are sequentially dependent, run at effective batch one, and make per-token decode latency (TPOT) the dominant term in task completion time … a 2% per-step failure rate erases a 2x decode advantage for a 20-step agent" |
| C4 | Retention representation changes the power line | Hot-in-HBM / cold-in-HBF tiering hosts 24x more concurrent sessions per GPU and cuts read power by 7.6 kW per 8-GPU node versus serving all KV from flash | VERIFIED | https://arxiv.org/abs/2609.25782 | "hosting 24x more concurrent sessions per GPU … our design also cuts read power by 7.6 kW per 8-GPU node relative to serving all KV from flash" |

**Status totals:** 18 claims VERIFIED, 0 FLAGGED, 0 REMOVED. No claim in this brief required a secondary source.

## Authorised desk arithmetic (label as arithmetic, print the inputs)

1. **Retention is roughly eighteen times the time actually spent producing tokens.** 100 ÷ 5.6 = 17.9. Inputs: B4's 5.6% share of retention time. Write it as "about eighteen times", never as a measured ratio.
2. **Median context grows about seven-fold inside a session.** 68K ÷ 10K = 6.8. Inputs: B2. Write "about seven times", and keep both endpoints ("from about 10K to 68K tokens").
3. **501.8 TB is about 6,273 H100-class cards' worth of HBM.** 501.8 × 10¹² ÷ 80 × 10⁹ = 6,272.5. Inputs: B4's 501.8 TB and the 80 GB card. Use it once, labelled as desk arithmetic, and never as a purchase recommendation — it is a peak-retention figure, not a fleet size.

No other sum, difference, ratio or interval is authorised.

## Gate rulings for the drafter (do not violate)

1. **Attribute each leg to its own paper.** Signal B never measures energy; Signal A never measures a workload. The sentence that fuses them is the desk's reading and is written as such.
2. **Never write that a prefix-cache hit reduces decode reads.** B3 measures prefill reuse; A3 says the decode read is K_KV × L per output token. The honest sentence is that the cache spares the recompute and keeps the history resident to be re-read on every later step. C1 corroborates the "prefill lever" framing.
3. **501.8 TB is an estimate, not a measurement.** Say "estimated", and name B8's stand-in (the public Llama-2-70B KV layout) when the number appears in a load-bearing sentence.
4. **5.6% is a share of retention time, not a cache hit rate and not capacity utilisation.** Do not convert it into "94.4% idle capacity".
5. **68K is a median at the 30th call in Deep Research only** — not all four workloads, not a mean, not a worst case.
6. **The energy figures are GPU-board energy per output token** for dense, full-history decoding at BF16 on three 7B–14B models. They exclude host, network and facility power, and do not generalise to mixture-of-experts models or sparse attention.
7. **3.73% is the worst-case held-out condition-mean error** over 374 executions — not an average, and not a bound for other configurations.
8. **Batching still helps.** A6 says larger batches lower measured mean energy at matched history. The claim is that batching does not shrink the per-request KV read — never that batching is useless.
9. **C2 is HBM2.** Name the generation, and carry its HBM3E validation as a microbenchmark on three H200 GPUs, not as a serving-workload result.
10. **No claim about what vendors charge or should charge.** The piece's claim is that a session's unit cost rises with its own age; a price list that quotes one number per token cannot express that.
11. **B7 is placement, not time.** The 89% → 29% drop is caused by the next call landing on a different deployment.
12. Cite only URLs already written into `context/recon_proposals/2026-10-21_gpu_hardware_signals.md` (all five anchors/corroborations above are present there).

## Dual-Anchor Gate

Leg A: 6 claims VERIFIED (A2, A3, A4 carry the argument). Leg B: 8 claims VERIFIED (B2–B6 carry it). Both legs primary, both dated inside 2026-09-21 → 2026-10-21. **PASS.**
