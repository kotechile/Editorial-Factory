# Run log — 2026-11-17 workstation_compute_economics (EVERGREEN)

**Artifact:** `published/2026-11-17_19-minutes-your-spots-real-bill.md` — "19 Minutes: Your Spot Discount's Real Bill"
**Track:** evergreen (`skills/evergreen_topics.md`), slot `30 19 * * 2`, vertical `workstation_compute_economics`, persona `infra_engineer`, surface aichieve.net.

## Topic provenance
Re-opened candidate from the 2026-11-10 brief's own table ("Checkpoint interval from measured failure and write cost", 7.4, dropped because "no fetchable primary states the machine-failure rate the interval formula needs"). This run found fetchable primaries that carry the failure counts (arXiv 2410.18124v1's 840-interruption GPT-3 example; the Llama 3 paper's 466/419 interruption census) and the vendor mechanics (Google Spot 91% ceiling, preemptible 24-hour cap with a 30-second shutdown period, Azure's 30-second eviction notice). Axes: U9 / D9 / E9 / A9 → 9.0.

Candidates refused: branch-circuit continuous-load ceiling (8.8 — `2026-10-13_panel-upgrade-80-percent-test` already argues the 80% rule, and the energy-bill half is in `2026-10-06_fine-tune-vs-rent-by-token` and `2026-10-24_your-homelab-heat-pays-back-45-cents`); ECC memory (7.2 — no fetchable per-GPU-day corruption rate); PCIe lane budget (7.3 — intel.com 403, amd.com slugs unresolved, and `2026-10-27_two-sparks-cost-3048-more-cable` prices link bandwidth).

## Gates
- Evergreen gate PASS first run: `rows=5 fetched=5 sources=5 hosts=3` (arxiv.org, cloud.google.com, learn.microsoft.com), de-dup `matched a prior artifact: 2026-11-10_your-gpu-starves-at-5-9`.
- Draft: accessibility PASS (Flesch 58.3 on the published artifact), `readability_critic` ok, `article_shape` ok, headline 100/100 STRONG with `lead_ok` true, `check_social_voice` clean.
- Frontend review: `article_reviewer.py` held all three attempts with **hard=0** (flow regressions only: rhythm sd 9.7→8.1, hedge 0→1.14). Attempt 3 adopted and hand-repaired: the rewrite had **deleted the one inline internal link** and turned "My read" into "My reading", and it had **renamed the tension H2 to a 7-word header** ("The Rule That Prices The Lost Hours"), over the six-word cap. Header re-cut to "The Rule Sets The Bill".
- `review_audit.py` PASS after the repairs (13 figures / 5 citations / 5 sources). Full `run_pipeline.py gate`: 8/8 ok.

## Arithmetic checked by hand
- 3.09 h failure gap = 1,296 h ÷ 419 unexpected interruptions.
- 19 min = √(2 × 185.4 min × 1 min); 43 min at a five-minute write; 61 min at ten — all recomputed before the draft.
- 91% ceiling and Meta's >90% effective training time kept as two separate sourced claims, never multiplied into a "cost per useful hour" figure.

## Publish
`scripts/publish.py` → Supabase row **3907732a-424d-45e4-86ec-b5fb85166e83** (HTTP 201), WordPress post **1758** (status publish, category 2 "Major Purchases & Assets", vertical term 23 → aichieve.net, kind tag 44 `evergreen`, featured media **1757**). One repair after publish: the rewrite's 7-word H2 was re-cut in the artifact, the Supabase row and the CMS body (`wp_draft.py --slug … --refresh-live`, post kept published), then a redeploy was triggered.

**Known display quirk (not a defect):** the push summary prints "0 internal link(s)" for this slug; the CMS body and the rendered front both carry the earned inline link (`/local-ai-payback-cloud-gpu-spread/`) plus the three generated Related-reading links.
