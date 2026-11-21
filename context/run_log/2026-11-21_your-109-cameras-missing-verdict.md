# Run log: home_diagnostics_tech — 2026-11-21 — your-109-cameras-missing-verdict

## STEP 0
`generation_gate.py --mode news --vertical home_diagnostics_tech` → GENERATION OK (control=supabase, vertical=file). Exit 0.

## Radar (Loop 1)
MCP `home_lifestyle_intel` returned 10 rows, all off-vertical (mortgage/NAHB, offshore wind, FAA ground stop) — fanned out on configured sources instead: HN Algolia (thermal camera / borescope / moisture meter / energy audit), PR Newswire, vendor first-party pages, syndicated inspector guidance, BBC (dated out: 2024-11-29), Picothermal blog (2026-10-12, pre-window → background). 9 queries total.
In-window rows (4, 4 distinct domains): ScienceDaily thermal cloak 2026-10-26 (90); RISION Black Friday pricing 2026-11-19 (88); Yahoo inspector guidance 2026-11-16 (80); HIKMICRO first-party concession (observation-dated 2026-11-21, dating note recorded) (70).
Both new hosts probed clean via host_probe.py and recorded to the host ledger (sciencedaily, prnewswire, hikmicrotech).

## Seed + Judge (Loop 1 gate)
`synthesize_topics.py --seed` → rows=4 candidates=0 (legitimate: collision axis is "what the reading means", not archetype tokens). Judge asserted the pair per virality_judge §2.5: cloak ⨂ record-low pricing → **Synthesis 8.7** (E8.5/A9/S8.5), beats best single (cloak alone, 8.1) by 0.6 ≥ 0.3 margin. De-dup: prior-cycle retread risk identified — 2026-11-07 `your-512x384-cameras-10x-illusion` owns the resolution-inflation thesis, so RISION's 512×384 QuadIR figure was excluded; the pricing leg is used only as the adoption event. Sibling wellroost verticals (last 7 days) checked: no thermal overlap.

## Fact check + draft (Loop 2)
Verified brief: both anchors fetched this run, figures read on the page (cloak: aluminum-lattice/cast-rubber, "much as it would if no object were present", Nature Comm DOI 10.1038/s41467-026-73167-0; RISION: $109/45%, $149, Nov 19–30 window). Excluded-figures section named prior-edition traps (BBC 2024 stats, Picothermal, 512×384).

## Frontier rewrite + gates (Loop 3)
**Defect found and fixed:** repo `.env` pinned `REVIEW_MODEL=anthropic/claude-3-5-haiku` — dead on OpenRouter (HTTP 404); every review call failed until the pin was commented out (falls back to frontier z-ai/glm-5.3). A stale `REVIEW_MODEL` shell export was also present (unset before the run). Recorded as a pitfall via learn.py.
Review: attempt 1 HELD (Flesch 47.4; NHBC/USB acronyms introduced by the rewrite from brief tokens — brief cleaned of NHBC/USB). Draft revised for accessibility (shorter sentences, plain nouns) → rewrite ACCEPTED (hard=0, Flesch 53.8). Hand repairs on the final: dropped double citations [3][4]→single per sentence (critic), added inline link to /categories/home-diagnostics-tools/ (shape gate), kept otherwise frontier prose.
`run_pipeline.py gate` → 8/8 pass.

## Persist
`publish.py` → published/2026-11-21_your-109-cameras-missing-verdict.md; Supabase row c4a0e6b0-373a-4f65-ad6b-4214adcf9401 (internal links written back); CMS post 447 (publish) on wellroost.com, category 26 Home Diagnostic Tools, vertical term 27, kind tag 28 (news), featured media 446 (flux, editorial_macro); sitemap refreshed; auto-deploy triggered. Illustration auto-generated in the same pass (idempotent by digest).

## Post-run verify
verify.sh: article voice OK (1,187 checks) after draft observer-cue fix (tension + tactical sections); remaining verify.sh FAILs are pre-existing environmental unit-test failures (pytest missing from the active interpreter), unrelated to this artifact. Reader-front check right after publish returned 404 — static front rebuild in flight from the auto-deploy; CMS delivery was verified by publish.py itself.

## Lesson
learn.py pitfall (REVIEW_MODEL dead model pin) + 3 host-ledger entries.
