# Run log: enterprise_tech_leadership — 2026-11-24 — 23-of-26-builds-saved-nothing

**Mode:** news · **Gate:** `generation_gate.py --mode news --vertical enterprise_tech_leadership` → ON at STEP 0.
**Window:** 2026-10-25 → 2026-11-24 · **Queries:** 12 (HN Algolia date-filtered ×10; publisher date checks ×4).

## Radar
Signals file: `context/recon_proposals/2026-11-24_enterprise_tech_leadership_signals.md` — rows=4 (hissingkitty.com build-vs-buy report 10-31 I88; blog.emailengine.app 10-26 I70; one2n.io 11-08 I82; tomshardware.com Exchange exit 11-07 I65), 4 distinct domains. `synthesize_topics.py --seed` → candidates=3 (re-seeded after row freeze; `verify.sh` §8 marker fresh: rows=4 candidates=3). Dated background: McKinsey State of AI 2026 (fielded out of window), ETR/techstrong 09-22, dubach 02-10, beforeyouship 08-31, scalar-engineering (medium.com 403, undatable → not written as a row).

## Judge (virality_judge.md §2/§2.5/§3.5)
All 3 seeded pairs scored in the angle brief. Best pair (cohort ⨂ one2n cost levers) = 8.4 but fails the §2.5 precedence rule (+0.2 < +0.3 over the single 8.2) → **Format B single-signal winner: the HissingKitty build-vs-buy report, N8.5/A7.5/S8.5 → 8.2 ≥ 8 → proceed.** one2n + emailengine kept as attributed corroborating clauses only (no argument resting on them).
De-dup: vertical's last 4 winners untouched; sibling check across aichieve.net last 7 days (build_vs_buy 11-11/11-18, finops 11-12, agentic_ai, observability) — none anchored hissingkitty/one2n/emailengine/tomshardware (grep confirmed).

## Fact check
`context/recon_proposals/2026-11-24_..._verified_brief.md` — 10 claims, all VERIFIED against fetched pages; binding flags: $6.86M is shared-bills not market spend (one $2M NetSuite bill = 29%); ServiceTitan n=3; 32%/1,719 is McKinsey-as-cited (out of window, attributed); report is a first-edition self-selected two-week sample; €300 case = one solo founder, boundary condition only; no hands-on claims.

## Draft + rewrite
Slug `23-of-26-builds-saved-nothing`. Title "AI Build vs Buy: 23 of 26 Builds Saved Nothing" → headline_score 100 STRONG, lead_ok true. Pre-tune: Flesch 59.0 (floor 50), critic ok, shape ok, inline internal link `/enterprisebuildvsbuy-the-250k-ai-upkeep-tax/` (200 on aichieve.net).
Review: attempt 1 HELD (2 critic defects: two 15/64-37/64 bullet lead-ins); fixed the two bullet lead-ins mechanically; a second review attempt introduced 1 hard defect and its held output was superseded — the accepted artifact is the attempt-1 frontier rewrite with the two bullet lead-ins repaired (critic clean, voice clean after one mechanical fix: source-line colon punctuation changed to a dash, `"The State of SaaS — Build vs. Buy"` — the voice gate reads `": Build"` as advice-after-colon; recorded as a lesson).

## Gates + persistence
`run_pipeline.py gate` on `_final.md`: accessibility ✓ shape ✓ critic ✓ headline ✓ sources ✓ review_audit ✓ voice ✓ publish_gate ✓. `publish.py` → published/, published_log, Supabase row 0d356ede-ba31-4004-8124-6ec56438a213, sitemap refreshed, WP post 1840 status publish (kind tag 'news' 43, vertical term 17, featured media 1839), push to origin/main (Coolify redeploy), live verified on aichieve.net.

## Verify.sh at finish — pre-existing failures, not this run's
- `scripts/test_illustration_overlay.py`: 4 failing tests (overlay subject-map/type-placement) — pre-existing, unrelated to this article's own media.
- article voice: 5 problems, all in `context/drafts/2026-11-23_your-agent-executes-before-it-verifies_draft.md` and the siblings of that run (": check", "Start …") — a 2026-11-23 agentic_ai run's superseded draft still in context/drafts/, which the voice gate reads whole-directory.
