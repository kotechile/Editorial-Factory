# Verified Brief: workstation_compute_economics — 2026-10-06 (EVERGREEN track)

Archetype: evergreen. Topic = the fine-tune-versus-rent-by-the-token decision: the VRAM floor for
local fine-tuning, the recurring electricity cost of a rig, and the two ends of the hosted
per-token ladder that set the denominator. Every external claim below traces to a source the
evergreen gate fetched live and confirmed contains the cited figure (5/5 rows verified on 5 hosts,
`<!-- evergreen-gate: -->` marker in
`context/recon_proposals/2026-10-06_workstation_compute_economics_evergreen_brief.md`).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Fine-tuning hardware floor | QLoRA fine-tunes a **33B** parameter model on a single **24GB** GPU, and a **65B** model on a single **46GB** GPU | VERIFIED | https://huggingface.co/blog/4bit-transformers-bitsandbytes | "This method enables 33B model finetuning on a single 24GB GPU and 65B model finetuning on a single 46GB GPU." |
| 2 | Same floor, headline framing | The method fits "a **65B** parameter model on a single **48GB** GPU" while preserving 16-bit fine-tuning quality | VERIFIED | https://huggingface.co/blog/4bit-transformers-bitsandbytes | "…reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance." |
| 3 | Hosted rate — top tier | The top-tier hosted model costs **$10** per MTok input and **$50** per MTok output | VERIFIED | https://www.anthropic.com/pricing | "Prompt caching Read $0.25 / MTok Write $12.50 / MTok Input $10 / MTok Output $50 / MTok" |
| 4 | Hosted rate — cheap open tier | Hosted **MiniMax M3** costs **$0.30** per 1M input and **$1.20** per 1M output tokens | VERIFIED | https://www.together.ai/pricing | "Price per 1M tokens Batch API price Model Input output MiniMax M3 $0.30 $0.06 (cached) $1.20" |
| 5 | Electricity price | The US average retail electricity price is **12.68 cents** per kilowatthour (2024 data year) | VERIFIED | https://www.eia.gov/electricity/state/ | "U.S. average retail price per kilowatthour is 12.68 cents" |
| 6 | Rig power draw | The **RTX 5090** draws **575 W** total graphics power and asks for a **1000 W** system supply | VERIFIED | https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ | "Total Graphics Power (W) 575 Required System Power (W) (5) 1000" |
| 7 | Field note (internal, not a gate row) | A legal-tech team at **$14,200/month** of commercial API calls fine-tuned a local Qwen-2.5-14B model on a 4x RTX 4090 rig for **$1,100** of compute and **$180/month** of power | VERIFIED (our own field note, `context/growth_os/customer-truth.md` §workstation_compute_economics Anecdote 3) | (internal — attributed in the article as our field notes, never presented as an external statistic) | "…spending $14,200/month on commercial LLM API calls. Fine-tuning a local open-weights Qwen-2.5-14B model on a single 4x RTX 4090 rig cost $1,100 in initial compute and $180/month in electrical power…" |

**Derived arithmetic (labelled as arithmetic in the article, never as a source figure — built only
from rows 3–6):**
- A 575 W card run continuously for a year draws 575 x 8,760 = **5,037 kilowatthours**; at
  12.68 cents that is **$638.69/year**, about **$53/month**.
- $638.69 of electricity, priced against the cheap tier's **$1.20 per 1M output tokens**, is about
  **532 million output tokens** a year; against the top tier's **$50 per 1M output tokens** it is
  about **13 million** — a roughly **42x** swing from the denominator alone.
- The same $638.69 buys about **2.13 billion input tokens** at the cheap tier's **$0.30 per 1M
  input**, versus about **64 million** at the top tier's **$10 per 1M input**.
- The two input rates are themselves a **33-fold** spread (10 / 0.30 = 33.3) — the "denominator"
  the article describes as a 33-times gap.

## Gate rules applied
- 6/6 external claims VERIFIED against the fetched primary page (rows 1–6); 0 REMOVED, 0 FLAGGED.
  Row 7 is our own field note, carried with attribution and never presented as a third-party stat.
- Hosts: huggingface.co (rows 1–2, one page cited for two figures — the 24/46GB floor and the 48GB
  16-bit headline), anthropic.com (row 3), together.ai (row 4), eia.gov (row 5), nvidia.com (row 6).
- No synthesis: single-signal evergreen topic; the dual-anchor gate does not apply.
- Boundary caution for drafting: rows 3 and 4 are *stated vendor prices* that the vendors re-price
  (so the draft dates them "as of October 2026"); row 5 is a 2024-data-year average the EIA
  re-issues annually; row 6 is a product spec. The derived arithmetic must be presented as the
  writer's arithmetic on those figures, never as a figure any source stated.
- De-dup: nearest prior artifact is the news brief
  `2026-10-06_workstation_compute_economics_verified_brief.md` and its published output
  `2026-10-06_local-ai-payback-cloud-gpu-spread` (build-vs-rent on a per-GPU-hour cloud rate). This
  piece's denominator is a per-token API fee for a *fine-tuning* decision and shares none of the
  news piece's anchors.
