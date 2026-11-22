# Run log: your-mowers-313-year-four-battery — 2026-11-21 (yard_robotics evergreen)

## Pipeline
- Gate: generation_gate.py evergreen/yard_robotics → allowed.
- Topic selection: primary_angles #6 (per-acre-year consumables), dropped 2026-10-24 at 7.0 for missing
  fetchable battery/price evidence; re-probe found the anchors: Husqvarna IE support KA-01420 (battery
  2–5 years), Husqvarna NZ blades page (6-8 weeks / 3-4 months), Husqvarna US blade product pages
  ($26.99 Endurance 6-pack, $64.99 Classic), Powered By Moyer parts listing ($313.36 kit, sold out),
  420 iQ price block ($2,599.99 campaign, $3,299.99 MSRP, Out of Stock).
- Candidate table: winner 8.4 (U9/D8/E8/A8); modular-vs-dedicated re-dropped at 6.6 (module reliability
  data still absent on fetchable pages).
- De-dup: nearest prior `2026-10-31_your-mower-pays-back-in-24-years-or-09` (machine vs contract;
  consumables never priced). Cross-corpus checked: 2026-11-06 phone-battery-cycle article (different
  machine class), 2026-10-25 EGO spare-pack (different vertical). No retread.
- Gate: PASS 7 sources / 2 hosts, marker written 18:35 (re-run 18:40 after OEM-terminology edits).
- Draft: readability PASS Flesch 52.9; review HELD 4× (attempt-1 rewrites) — final rejection hard=0
  (flow only) → adopt-and-repair per skills/evergreen_topics.md §6. Hand repair: "40 percent" upper
  claim not earned by the stated middle case → replaced with "a quarter … more if the battery dies
  twice". Gates 8/8 after repair.
- Illustration: first publish skipped it silently (no note in the publish tail); commissioned
  post-publish via ensure_illustration → studio_object on flux-2 (5 credits, task 79a0680d…), render
  review OK (on-topic 1.0), then wp_draft.py --slug … --refresh-live pushed media 454 to post 449.
- Publish: CMS post 449 (publish) + Supabase 6479b8a8 + published/ + sitemap; internal-links block
  (3 links) written to the row.

## Figures (all verified on fetched pages, as of 2026-11-21)
$2,599.99 campaign / $3,299.99 MSRP 420 iQ · 2–5 years battery · $313.36 kit (sold out) ·
6-8 weeks Long Life blades · 3-4 months Endurance · $26.99 Endurance 6-pack · $64.99 Classic.

## Derived arithmetic (recomputed from verified ends)
3–4 Endurance packs/yr × $26.99 → $324–$432 blades/4yr; + one kit $313.36 → $637–$745 ≈ 24.5–28.7%
of $2,599.99 (up to ~41% if the battery dies twice inside the 2–5-year band).

## Environment notes for finish
verify.sh failed on missing pytest/Pillow in the session venv (installed via pip); remaining FAILs are
other runs' artifacts (2026-11-21 outdoor_power_equipment evergreen draft voice cues; test_illustration_overlay
suite; September drafts' accessibility) — none from this article.
