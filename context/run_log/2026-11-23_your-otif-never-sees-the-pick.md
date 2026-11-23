# Run log: sales_order_service_level_otif — 2026-11-23 — your-otif-never-sees-the-pick

## Chain
gate: `generation_gate.py --mode news --vertical sales_order_service_level_otif` → GENERATION OK.
Radar: `supply_chain_intel` MCP sweep (10 items) + 6 web fan-outs; 7 in-window rows kept (2 sponsored rows downgraded to friction/corroboration; Meta row dropped — HTTP 403 bot wall).
Seeder: `synthesize_topics.py --seed` → **rows=7 candidates=0** ("no valid pair" — the legs collide on *where service is made* (store vs DC), no archetype tokens; recorded as input, pair asserted per virality_judge.md §2.5).
Judge: **Synthesis 8.65** (E8.5/A9.0/S8.5) vs best single 8.26 (Walmart speed alone) — margin +0.39 ≥ 0.3, synthesis takes it.
De-dup §3.5: own artifacts (pallet-price, $3.79, four-sigma, Kroger) argued different theses; sibling grep over aichieve.net last 7 days + `grep -ril "sub-30|on-shelf availability|23% year"` over published/ → clean.

## Anchors
- A: Walmart Q3 FY27 earnings call (2026-11-19, Motley Fool transcript) + SEC-filed release: sub-30 deliveries "almost 3x"; 60% of US households in 30 min with "a 15-minute pick time in the store"; store-fulfilled +40%, expedited +50%, >80% of US e-comm orders store-fulfilled; US e-comm +23% (global +17%); inventory $70.6B (+8.1%).
- B: Target Q3 2026 earnings highlights page (2026-11-18): OSA +1 full ppt YoY incl. most frequently purchased items; AI tools "help teams improve availability and keep shelves stocked"; store comps +4.6%, digital +9.8%.
- Fact check: 8 VERIFIED + 2 corroborations + 2 DERIVED, 0 REMOVED, 0 FLAGGED; dual-anchor gate PASS. 10 rulings in the verified brief.

## Draft → frontier → gates
Draft 748 words, Flesch 51.5 PASS (two earlier cuts failed: Flesch 30/41, undefined-OTIF, headline hook/word-count), headline **"Your OTIF Never Sees the Pick"** 100/100 STRONG. Earned inline link `/same-day-race-undoes-route-optimization/` (200).
Reviewer attempt 1 HELD (reviewer replaced "What I find…" cues with cue patterns its own detector rejects); re-run attempt 1 ACCEPTED (hard=0, Flesch 51.3, 744 words). Gate battery 8/8. publish_gate PASS pre-push.

## Persistence
published/2026-11-23_your-otif-never-sees-the-pick.md; Supabase **af0d596e-b698-422a-8eff-29c61ed69824** (metadata.synthesis absent post-push → PATCHed true); WP post **1825** (publish, category 10, vertical term 41, kind tag 43 'news'); generated Related block justified on loose tokens but same-category ("deliveries, store" / "order" / "walmart") — left as generated. Featured media **1824** (long_lens_industry, flux-2): alt arrived headline-glued + truncated → rewritten to a complete sentence, reconciled across sidecar featured.json, artifact image_alt/caption, media 1824 PATCH (read back), row metadata.
**Overlay defect found and fixed:** the subhead line rendered mid-word-truncated ("…15-minute stor" clipped at the image edge). Re-typed locally with `illustration_overlay.apply_to_slug(force_copy=…)` (hook ≤88 chars, "The 30-minute promise assumes a 15-minute pick past the scorecard"), pixels verified by vision — no truncation, no garble, no brand mark. New bytes (405,719, sha256 e03e54d1…) copied into the CMS uploads dir (full + 6 regenerated derivatives, ownership www-data), served sha256 == staged sha256.
Reader: https://aichieve.net/your-otif-never-sees-the-pick/ 404×4 → 200 (auto-deploy lag ~2 min); h1 correct, og:image = featured jpg, earned link present.

## Lessons
- `article_reviewer.py` on this driver rewrites the draft's "I find / I would watch" cues into "What I keep coming back to / What I am watching" — forms its own first-person detector does not match — so attempt 1 HELDs on a healthy draft; a second identical run passed. Watch for convergence; if it recurs, the driver needs the cue-family list shared with the model.
- `illustration_overlay` lets a hook up to 88 chars render past the image edge — the wrapper does not wrap the hook line; keep hooks ≤ ~72 chars.
- verify.sh run-log 900-char gate flagged a sibling run's row (home_infrastructure 2026-11-23, 1002 chars) — trimmed to 863; the detail lives in its run_log file. Not this run's defect.
- Hosts recorded fetchable: fool.com, corporate.target.com, sec.gov.
