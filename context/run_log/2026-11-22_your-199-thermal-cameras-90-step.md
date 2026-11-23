# Run detail: home_diagnostics_tech REVIEW — 2026-11-22 — your-199-thermal-cameras-90-step

Review run (`skills/review_comparison.md`, Sun 15:00 UTC slot, registry `review_cadence 0 15 * * 0`). Not the news sweep, not evergreen: no 30-day window, no virality Judge. Gate at STEP 0: `generation_gate.py --mode review --vertical home_diagnostics_tech` → exit 0.

## Subject selection

Prior review runs: borescopes 11-01, outlet testers 11-08. Moisture meter (10-25) and slab leak (11-07) went evergreen. Remaining admissible subject: the thermal-imager buying decision (primary_angles #1/#6), newly acute because Black Friday cut the class to $109–$239 (PR Newswire 2026-11-19).

Products chosen from evidence, with live cart records on 2026-11-22:
- RISION Magic (AF01) — $109.00 cart (rendered banner $119.00 vs $139.00 list) — IN STOCK
- RISION Magic Pro (AF02) — $199.00 cart (rendered $229.00 vs $299.00) — IN STOCK
- Thermal Master P3 Lite (P2 Max) — $239.00 (og meta + variants 23900 vs compare-at 26900) — ships early/mid Dec

**Refused on stock, not taste:** Topdon TC001 ($289.00) and TC001 Mini ($139.00) — both carry the server-rendered sold-out badge on topdon.us (three renders each). §2 admissibility.

## Gate trail

- Review gate PASS on attempt 2: first run failed on (a) Shopify split-glyph page — the gate fetcher sees no `$119.00` in the rendered page text (prices live only in markup the fetcher skips), and (b) the concatenated-price bug when the Price cell carried "($119.00 (regular $139.00)" ($1,190,013,900). Fixed by citing the Shopify variant JSON endpoints (`....js`) as the price source of record with Figure `10900` / `19900` (cents) and moving list figures to the note; second run PASS: rows=8 fetched=8, products=3, hosts=2 (rision.com ×4 URLs, thermalmaster.com), marker 2026-11-22T15:05:41Z.
- Brief second-header failure avoided: header row must read `| Product | Price | Source | Note |` (the parser keys on both words).
- `context/source_quality.json`: added `rision.com` and `thermalmaster.com` to primary_hosts (maker's own page is the price source of record).

## Fact check

11 rows in `2026-11-22_home_diagnostics_tech_review_verified_brief.md`: maker cart records ×3 (incl. the $50.00 macro-lens variant and $289.00 kit variant), manufacturer-claimed specs ×4, owner report ×1, vendor announcement ×1. Key rulings: cart record beats rendered banner ($109/$199 match RISION's own Nov 19 press release; banners $119/$229 may revert after Nov 30 — stated, dated); every headline resolution is an upscale (320×240, 512×384 ×2) over 160×120 / 256×192 natives — the 11-07 news thesis stated in one line, not re-argued; no independent measured review of these units was fetchable, so all sensitivity/accuracy/range figures are labelled manufacturer claims; Topdon refusal documented.

## Draft and rewrite

Draft 1,058 words, all gates PASS after two pre-tune passes (figure budget, one citation per sentence, observer cues in tension/tactical, acronym expansions "universal serial bus (USB-C)", "infrared (IR)", "RISION (the phone thermal-camera brand)").
Loop 3: attempt 1 REJECT (1 critic defect: [2]×2 in one sentence; Flesch 50.0 at 1,094 words) → HELD file repaired by hand: restored the two acronym expansions the rewrite dropped (the known rewrite class), split the double citation, three small Flesch re-voices (49.9 → PASS). Final: 1,094 words, all 8 gates PASS (accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate). Furniture grep before push: price matrix (Fails at column), By the numbers, `## What we did not test`, situation table, calculator + hub links — all present.

## Publish

Supabase article id `52ccb0a8-ad9a-42a6-ae31-26c4beb5b5e0` (metadata.wordpress written back). WordPress post **463** on cms.wellroost.com, status publish, category 26, vertical term 27, kind tag 30 (review), featured media **462** (flux-2/pro, 2,400×1,350). Internal links: the generator produced none for this topic (no live page qualified — block written empty, stated, not filled). Sitemap.json refreshed; auto-deploy committed and pushed.

**Alt-text truncation found and fixed (the recurring class):** the director's composed alt was cut mid-phrase ("…infrared lens"). Rewritten in the sidecar AFTER the last render as a 144-character complete sentence, PATCHed to media 462 over REST (read-back verified), reconciled into the row's `metadata.illustration.alt_text` and `metadata.wordpress.media_alt`, then the wellroost front was force-rebuilt (`ci: re-trigger frontend build` commit to kotechile/wellroost) and the live page serves the corrected alt.

**Reader surface:** https://wellroost.com/your-199-thermal-cameras-90-step/ — 404 on the first two probes, 200 on the third (build), with its own `<h1>`, `## What we did not test`, og:image derivative 200, corrected hero alt.

No social distribution and no LinkedIn/Reddit copy (channel removed 2026-10-06).

## Open items

(a) The review gate's fetcher cannot see Shopify rendered prices at all on these two storefronts — any future RISION/topdon/Thermal Master brief must cite the `.js` variant endpoint (or the og meta) as the price source of record.
(b) thermalmaster.com's Black Friday discount was not live on the P3 Lite page ($239.00 stands); re-check before the next run cites it.
(c) `bash scripts/verify.sh` still red on the pre-existing snow-blower draft voice defect and the 4 illustration-overlay test failures (unrelated to this run).
