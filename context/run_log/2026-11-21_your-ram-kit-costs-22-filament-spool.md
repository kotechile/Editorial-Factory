# Run log — 2026-11-21 — your-ram-kit-costs-22-filament-spool (personal_microeconomics_tinkering_tax, NEWS)

## Pipeline
- STEP 0 gate: `generation_gate.py --mode news --vertical personal_microeconomics_tinkering_tax` → GENERATION OK.
- Radar (window 2026-10-22 → 2026-11-21): home_lifestyle_intel MCP (10 items, mostly off-vertical housing/energy — all dropped as out-of-beat), 3 web fan-outs, 2 HN Algolia sweeps, dated-page checks. **4 signal rows** in `2026-11-21_personal_microeconomics_tinkering_tax_signals.md`; out-of-window items (Tom's 500% piece 08-17, noted.lol 10-17, archy.net 02-15) carried as Dated background.
- `synthesize_topics.py --seed` → **rows=4 candidates=0** — the §2.5 threshold-class blind spot (a spot-market stock indexed daily ⨂ a daily aggregate index share no archetype tokens). Recorded as input; the pair was asserted by the Judge.
- Judge (`..._angle_brief.md`): Synthesis **E8.4/A8.8/S8.5 → 8.6**. Anchor 1 = Tom's Hardware RAM price index (dateModified 2026-11-17); Anchor 2 = SpoolHound Filament Price Index (read 2026-11-21). Emergent thesis: the hobby's cost centre moved from consumables to memory — $474 kit ≈ 22 spools at the $20.99 U.S. PLA median. De-dup named `your-cheap-board-costs-385` (same vertical, 11-07 — Pi repricing; distinct leg: filament deflation absent there) and sibling `your-128gb-laptop-2319-memory-bill` (11-03, workstation front); novelty held 8.4 for the adjacency.
- Fact check (`..._verified_brief.md`): 6 VERIFIED (each anchor fetched, verbatim cells), 2 DERIVED (the 22-spool division; labelled in the brief), 1 FLAGGED (out-of-window 500% background used as framing only). Dual-anchor gate PASS (2 hosts + 1 corroborator).
- Draft → pre-tune: 2 rounds of fixes (citation-tag hygiene ×3, inline link added, U.S.-bullet rewrite, matrix table for the kit prices, RAM/DDR5 glosses, five markers, figure-budget fixes). Critic PASS, accessibility PASS, shape ok, headline **100/100 STRONG** ("Your RAM Kit Costs 22 Spools", 28 chars) with `lead_ok` true.
- Loop 3 (`run_pipeline.py review`): **HELD attempt 1** — rhythm regressions (mean 18.2→19.5, health 0.987→0.894), boilerplate cue; rewrite itself sound. Hand fix: the reviewer's At-a-glance box counted 53 words (em-dash tokens) → trimmed to 40. `_final.md` written.
- Gate (`run_pipeline.py gate`): **8/8 ok** — accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate.

## Publish
- `publish.py` → Supabase row **3271526c-d09e-4eb1-9210-551b9e946743**; WP post **1813** on cms.giniloh.com, published in the two-call vertical sequence (vertical term 27, kind tag 43 news, category 4 Money & Wealth, featured media 1812); 3 generated internal links written back to the row; sitemap refreshed; auto-deploy committed.
- Reader: https://giniloh.com/your-ram-kit-costs-22-filament-spool/ → **200** with own `<h1>` "Your RAM Kit Costs 22 Spools", hero image + og:image present.
- Calendar row appended (≤900 chars). Lessons: pitfall (finish/pytest venv defect) + 2 host records via `scripts/learn.py`.

## Open items
- `run_pipeline.py finish` still exits 1: cron venv lacks pytest (worked around with PATH=/usr/bin); `scripts/test_illustration_overlay.py` fails 4 tests under system python on a PIL/numpy version difference — pre-existing, environment-dependent, unrelated to this article.
- The generated Related-reading block again includes single-token picks ("costs", "rate") — recorded, not stripped (same front, same hub).
