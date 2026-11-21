# Run log: yard_robotics news — 2026-11-21 — your-robot-costs-775-a-month

**Track:** news (Sat 10:30 UTC slot). Generation gate: ON (STEP 0 exit 0).
**Window:** 2026-10-22 → 2026-11-21. 14 queries; 7 in-window rows on 7 distinct domains (intensities 88/86/80/78/70/66/65) → `context/recon_proposals/2026-11-21_yard_robotics_signals.md`.
**Seed step:** `synthesize_topics.py --seed` → rows=7 candidates=0 (structural: no archetype in the PATTERNS registry scopes to yard_robotics; not a domain-mix artifact). Legitimate "no valid pair"; Judge asserted the pair per skills/virality_judge.md §2.5.

**Winner (synthesis, composite 8.9 = E9.0/A8.5/S9.0, beats best single ≈7.5 by ≥0.3):** Yarbo storefront regular ladder (https://www.yarbo.com, observed 2026-11-21: $9,299 top bundle, 0% APR $774.92/mo ×12; $7,299 entry; $8,199 mower tier; Y40P $7,799) ⨂ MowBook pricing guide (updated 2026-11-03, https://www.mowbook.co/blog/lawn-care-pricing-guide: 1-acre monthly-billed $300–$520/mo). Thesis: year one of financing the full modular bundle costs more per month than the landscaping contract it replaces; payback only closes in year two+ and only if the machine replaces BOTH mowing and snow. Corroborating owner record (row #2, gamma.app): 80–90% of storms cleared, street-plow berms not cleared.

**De-dup (§3.5):** prior vertical artifacts checked (10-25 Yarbo review, 10-31 FCC news, 10-31 payback evergreen, 11-07 canopy evergreen, 11-08 acreage review) + sibling wellroost verticals last 7 days (outdoor_power recall/importer, snow shovels) — no overlap; figures $774.92/$300–$520/$9,299 unanchored anywhere in published/.

**Fact check:** `context/recon_proposals/2026-11-21_yard_robotics_verified_brief.md` — 12 rows: 11 VERIFIED (2 labeled DERIVED from printed endpoints), 1 FLAG. Flag: yarbo.com is mid-Black-Friday sale — 4-in-1 product page prints $7,399 sale ($616.58/mo) vs homepage $9,299 regular; article uses the REGULAR ladder consistently, never mixed. Dual-anchor gate PASS (5 VERIFIED leg A, 4 VERIFIED leg B). MowBook curl hits a Vercel bot wall; the web_extract fetch is the record (fetch issue, not sourcing defect).

**Draft:** `context/drafts/2026-11-21_your-robot-costs-775-a-month_draft.md`, 858 words, Flesch 57.8, headline 100/100 STRONG lead_ok true ("Your Robot Costs $775 a Month").

**Frontier rewrite** (`run_pipeline.py review`): 1 attempt → HELD (hard=1: nuanced-takeaway without a first-person sentence; rhythm 6.1→7.0, health 0.795, Flesch 56.9, 676 words). Hand repair per the hold rule: added the observer cue ("would I still write the check in month fourteen…"); reviewer's NOT-YET-EARNED note (motive claim) already recast as observation by the rewrite. Promoted to `_final.md`.

**Gate battery** (`run_pipeline.py gate`): accessibility ok, shape ok, critic ok (0 holding, 2 advisories), headline 100/100, sources ok, review_audit ok, voice ok, publish_gate ok — all pass.

**PERSISTED** (`run_pipeline.py publish`): Supabase row `cc02693c-f10f-447f-a9ef-49de3a356fe6` (link block written back); WordPress post **439** on cms.wellroost.com, status publish via the two-call vertical sequence, category 22 "Yard Robots & Automation", vertical term 23, kind tag 28 "news", featured media **438** (img 200); sitemap refreshed; auto-deploy pushed. Reader surface https://wellroost.com/your-robot-costs-775-a-month/ answered 404 on first poll (documented front-rebuild lag), **200** on the next with its own `<h1>` and the $774.92 body figures.

**Internal links:** scorer's generated pick noted in the publish log; the body's earned inline link is the hand-placed `/categories/yard-robotics/` hub. No social distribution and no LinkedIn/Reddit copy (channels removed 2026-10-06).

**Open items:** none blocking; the sale/regular price vintage on yarbo.com will drift after Black Friday — a future re-read of the live ladder is a new price as of a new date, not a correction.
