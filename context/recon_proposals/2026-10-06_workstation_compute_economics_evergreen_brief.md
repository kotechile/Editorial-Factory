# Evergreen Brief: workstation_compute_economics — 2026-10-06

**Archetype:** evergreen
**Vertical:** workstation_compute_economics
**Persona:** infra_engineer
**Decision the reader is facing:** Whether to fine-tune an open-weights model on local hardware and retire a per-token API bill, or keep renting a model by the token — a decision that bites the moment a narrow, high-volume extraction or classification task's monthly API line crosses the point where a rig and its electricity amortize inside a year.
**Durability:** The decision rule does not expire — a fixed VRAM floor plus a recurring electricity cost is compared against a variable per-token fee, so the *method* (estimate monthly tokens, price them against the cheapest hosted model of the same family, compare to the rig's annualized capex + power) stays true for years. The figures are as of 2026-10-06: the QLoRA VRAM floors (Hugging Face, technical doc), the US average retail electricity price (EIA, 2024 data year, re-issued annually), the RTX 5090 power spec (NVIDIA product page), and the two per-token rates below (vendor pricing pages, re-priced on the vendor's schedule — re-check each before quoting).
**De-dup:** Nearest prior artifact for this vertical in the last 180 days is the news brief 2026-10-06_workstation_compute_economics_verified_brief.md and its published output 2026-10-06_local-ai-payback-cloud-gpu-spread — a build-versus-rent thesis whose denominator is a per-GPU-hour cloud-rental rate (RTX 5090 street prices, getdeploying H100 medians, Micron contract prices) for *inference and agent loops*. This piece prices a per-token API fee for a *fine-tuning* decision and carries a different set of anchors (QLoRA VRAM floors, electricity cents/kWh, GPU watts, two per-token rate cards); none of the news piece's anchors or its "which cloud row" thesis appears here, and no prior fine-tuning/VRAM-floor brief or article exists for this vertical in the window. Cross-vertical, 2026-10-06_cloud-repatriation-break-even is a server-repatriation thesis on a different vertical.
**Thesis:** Fine-tuning versus renting a model by the token is settled by your monthly token volume priced against the *cheapest hosted model of the same family* — not against the frontier rate — so a team that quotes the frontier per-token price to justify a rig has priced its own conclusion, and the honest question is whether the task fits a 33B-class open model on one 24 GB card at the cost of a few watts.

**Lead:** `founder-voice.md` §3 `workstation_compute_economics` bullet 3 — *Local LLM Fine-Tuning & Open-Weights Economics* ("fine-tuning an open-weights 8B–14B model … eliminates recurring commercial API token bills while preserving absolute IP confidentiality") — restated against the vertical's own `primary_angles` line *"local llm fine-tuning hardware requirements vs commercial api per-token fees"* (`context/verticals.json`), grounded in the field note in `customer-truth.md` §workstation_compute_economics anecdote 3 (a legal-tech startup at $14,200/month of commercial API calls fine-tuned a local Qwen-2.5-14B on a 4× RTX 4090 rig for $1,100 of compute and $180/month of power). Demand corroboration only: persona `infra_engineer` wants "real numbers, caveats, reproduction details," and `gsc_analyzer.py --vertical workstation_compute_economics --export-md` returned 0 striking-distance queries (impressions too thin on a young site to be a signal, and per `skills/evergreen_topics.md` §2 that never vetoes a lead).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Hugging Face — Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA | https://huggingface.co/blog/4bit-transformers-bitsandbytes | 2026-10-06 | 33B — a 33B-parameter model QLoRA fine-tunes on a single 24GB GPU, and a 65B model on a single 46GB GPU: the fine-tuning VRAM floor is far above the inference floor most buyers budget for | measured (technical doc) |
| 2 | Anthropic — Claude API pricing (top-tier model rate card) | https://www.anthropic.com/pricing | 2026-10-06 | $10 per MTok input and $50 per MTok output — the frontier per-token rate that teams quote in the denominator to justify a rig | vendor claim (stated price) |
| 3 | Together AI — Pricing (cheap hosted open-model tier) | https://www.together.ai/pricing | 2026-10-06 | $0.30 per 1M input and $1.20 per 1M output — MiniMax M3, the hosted open-model rate that shrinks the same break-even by roughly two orders of magnitude | vendor claim (stated price) |
| 4 | US Energy Information Administration — Electricity Profile (state data, 2024) | https://www.eia.gov/electricity/state/ | 2026-10-06 | 12.68 cents per kilowatthour — the US average retail electricity price, the recurring cost of running a local rig 24/7 | measured |
| 5 | NVIDIA — GeForce RTX 5090 product page (specifications) | https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ | 2026-10-06 | 575 W — the RTX 5090's total graphics power (on a 1000 W required system supply), the load side of the electricity math | measured (spec sheet) |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Fine-tune or rent by the token: the VRAM floor and the volume threshold for an open-weights model | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Developer hardware debt: pricing the compile-and-test wait in loaded salary | 8 | 8 | 5 | 8 | 7.3 | dropped — no fetchable *primary* anchor for "minutes lost per day"; every figure on offer is a vendor or trade claim, and the load-bearing claim would rest on an unfetchable number |
| Local media rendering (NVENC) vs cloud render nodes | 7 | 7 | 6 | 7 | 6.8 | dropped — the cloud-render side of the comparison is dynamically priced (JS-rendered instance tables) so fewer than three HTML primaries survive the fetch gate |
| What a local inference box actually costs to run (the power line) | 7 | 8 | 7 | 6 | 7.1 | dropped — a unit-conversion piece with a single measured anchor and no decision beyond arithmetic |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=5 hosts=5 decision="sha1:7b1aa75d8d" dedup="matched a prior artifact: 2026-10-06_workstation_compute_eco" window_days=180 checked_at=2026-10-06T19:33:13+00:00 -->
<!-- evergreen-gate:end -->
