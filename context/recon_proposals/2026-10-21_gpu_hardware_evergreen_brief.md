# Evergreen Brief: gpu_hardware — 2026-10-21
**Archetype:** evergreen
**Vertical:** gpu_hardware
**Persona:** infra_engineer
**Decision the reader is facing:** Your cluster is power-capped and demand is rising — buy another card, or cap the cards you already own, and at what percentage of rated power does the cap stop paying for itself in latency?
**Durability:** The mechanism is the shape of a GPU's power-performance curve — energy per inference is U-shaped in the operating point (GPU × power cap) because board power rises superlinearly with clocks on top of a fixed floor — not a product generation, so the rule survives hardware refreshes. Figures are as of: NVIDIA spec pages read 2026-10-21; the three measurements as of their own publication dates (20 May 2026, 23 Aug 2026, 10 Sep 2026); the electricity price as of EIA's 2025 annual average.
**De-dup:** `2026-10-14_prefill-decode-two-pool-gap` is this vertical's nearest prior evergreen artifact, and it argued the serving topology (split prefill and decode into two pools). This piece does not re-argue the split — it takes a disaggregated deployment as given and settles where the power cap goes, a lever that artifact never touches. Cross-vertical checked and differentiated: `2026-10-06_rack-power-density-ceiling-build-before-you-buy` (nhil_infrastructure_ops) argues facility capacity — air cooling's ~40 kW rack line, the utility feed, the building project; this piece stays inside the watt already provisioned. Also checked `2026-10-21_your-68k-tokens-cost-every-step` (this vertical, energy per token set by the agent's own KV history — a workload property, not an operating-point choice) and `2026-10-07_gpu-hour-price-set-by-memory` (rental price of a card, not what you do with the watt).
**Thesis:** Energy per inference is U-shaped in the operating point, so under a fixed power budget the cheapest capacity is a calibrated power cap rather than another card — but the cap's number has two floors: a per-card-type constant near 45% of rated power that transfers, and a per-deployment ceiling near 80% of natural draw that only a tail-latency-gated calibration on your own stack can find.

**Lead:** The vertical's own beat (`primary_angles`: "inference economics") crossed with the founder's standing position in `context/growth_os/founder-voice.md` §3 — "the metric that matters is tokens generated per dollar per watt; peak theoretical TFLOPS on a spec sheet is vendor marketing" — and `customer-truth.md`'s gpu_hardware anecdote 1 (a $28,000 → $9,500 monthly bill from serving-stack changes, not hardware). The material came from the arXiv intel feed: three independent 2026 measurement papers that all treat GPU power caps as a control knob, plus the vendor spec pages that price the watt, plus the government price of a kWh.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Apartsin & Aperstein, "The Joule Point: an Energy-Optimal Operating Point for AI Inference" (arXiv:2609.27926, 23 Aug 2026) | https://arxiv.org/abs/2609.27926 | 2026-10-21 | 43 to 46 per cent of a large GPU's rated power — the cap that minimises energy per inference, cutting it by roughly a quarter to a third at ~1.2x slower per request | measured |
| 2 | Kim, Yoo, Ryu, Ha, Lee & Ryu, "Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving" (arXiv:2609.11133v1, 10 Sep 2026) | https://arxiv.org/html/2609.11133v1 | 2026-10-21 | +20.4% tokens/J at +3.5% mean end-to-end latency versus +8.6% at +5.2% for NVIDIA's Max-Q profile, on 8x B200 serving a 480B MoE (FP8) under agentic load | measured |
| 3 | Hankendi, Shahout, Yu & Coskun, "PALS: Power-Aware LLM Serving for Mixture-of-Experts Models" (arXiv:2605.21427, 20 May 2026) | https://arxiv.org/abs/2605.21427 | 2026-10-21 | 26.3% — the energy-efficiency improvement from treating GPU power caps as a first-class knob inside vLLM, with 4x to 7x fewer QoS violations under power constraints | measured |
| 4 | NVIDIA, H100 Tensor Core GPU product page | https://www.nvidia.com/en-us/data-center/h100/ | 2026-10-21 | 700W — maximum thermal design power of the SXM part (350-400W for the PCIe part), i.e. the rated power a cap is expressed against | vendor claim |
| 5 | NVIDIA, DGX B200 system product page | https://www.nvidia.com/en-us/data-center/dgx-b200/ | 2026-10-21 | 14.3 kW — maximum system power for an 8-GPU node, i.e. ~1.79 kW of facility load per GPU once CPU, memory and networking are counted | vendor claim |
| 6 | U.S. Energy Information Administration, "Prices and factors affecting prices" (Energy Explained) | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | 2026-10-21 | 13.41¢ per kWh — the 2025 U.S. average commercial retail price, the rate that converts a saved kilowatt into dollars | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Where to put the power cap: at a fixed power budget, the cheapest capacity is a calibrated cap on the cards you own, not another card — and the two papers' numbers differ because they measure from different baselines | 9 | 8 | 9 | 9 | 8.8 | **winner** |
| Rack power provisioning: how many accelerators a kW envelope buys and what the cooling mode changes | 8 | 9 | 7 | 7 | 7.8 | dropped — the mechanism (air cooling's 40 kW line, the utility feed) is already argued in `published/2026-10-06_rack-power-density-ceiling-build-before-you-buy.md` under nhil_infrastructure_ops; re-running it here is the cross-vertical retread §3 refuses |
| Porting cost off NVIDIA: what a non-NVIDIA accelerator saves on capex versus what the stack rewrite costs | 8 | 8 | 5 | 7 | 7.1 | dropped — no measured porting-cost anchor fetches: the promising papers are PDF-only and the vendor support matrices state capability, not cost |
| Second-hand accelerator resale and depreciation curves | 7 | 6 | 5 | 7 | 6.2 | dropped — no retrievable primary price series, and the value half-lives inside ~90 days (news, not evergreen) |

## Notes the drafting stage must carry

- **The two headline percentages are measured from different baselines and must never be presented as one number.** The Joule Point is a fraction of a card's *rated* power (43-46% of the 700 W class); the phase-decoupled controller's winning setpoint is a fraction of *natural draw* under load (~80%). A sentence that equates them ships a claim neither paper makes.
- **Both large wins are Mixture-of-Experts results.** 2609.11133 states plainly that an exploratory dense-model comparison recovers roughly 5x less, so the article scopes the big numbers to MoE serving and says what a dense stack should expect.
- **The vendor profile is the counter-example, not the recommendation.** Max-Q's realised gain was +8.6% tokens/J at +5.2% mean latency, and it applies one setting to prefill and decode GPUs that sit in opposite hardware regimes.
- **The gotcha with a number:** a cap near 65% of natural draw held throughput within tolerance while pushing ITL-p99 past the SLO in the large majority of repeated runs; adding a tail-latency criterion moved the accepted setpoint to 80% and restored 100% SLO compliance at +22.4% tokens/J. The calibration target is a latency cliff, not an energy minimum.
- **The money is small next to the card, and the article should say so.** At 13.41¢/kWh, one kW run flat for a year costs $1,174.72; a 14.3 kW DGX B200 node costs $16,798.44 a year at full draw, so a 20.4% energy saving is ≈$3,427 per node-year — real, but a rounding error against the hardware, which is exactly why the cap has to be sold as *capacity at fixed power*, not as a power bill saving.
- **Arithmetic to recompute from the two verified endpoints after the frontier rewrite:** 14.3 kW ÷ 8 GPUs = 1.79 kW per GPU; 700 W × 8 = 5.6 kW of GPU-only draw inside a 14.3 kW node; a 32.3% three-day energy saving on a 14.3 kW node = 4.62 kW ≈ $5,426 a node-year.

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=6 hosts=3 decision="sha1:311cc2cc89" dedup="matched a prior artifact: 2026-10-14_prefill-decode-two-pool" window_days=180 checked_at=2026-10-21T18:32:40+00:00 -->
<!-- evergreen-gate:end -->
