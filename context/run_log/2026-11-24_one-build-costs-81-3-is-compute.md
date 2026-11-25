# Run detail — 2026-11-24 — workstation_compute_economics (evergreen) — one-build-costs-81-3-is-compute

## What ran
- STEP 0 gate: generation OK (supabase control, vertical file).
- Lead: `primary_angles` beat 2, "the developer hardware debt index and lost compilation hours" — the one angle in this vertical never priced (de-dup against 2026-10-06 capex-vs-rent, 2026-10-06 fine-tune-vs-token, 2026-10-20 render billing, 2026-11-10 storage feed, 2026-11-17 spot/checkpoint; cross-vertical 2026-10-21_your-ci-bill-232-hours prices CI compute, not the developer's wait).
- Anchors: Gallup/Mark interview (23m15s, 81.9%), GitHub engineering build-cost experiment ($150k/$75 loaded cost; 92-min build = $2.94 compute vs $77.94 dev, 26.5x), Buildkite/Elastic Kibana case (3h → 55min, 70%).
- Evergreen gate PASS 19:36 (5 rows, 3 hosts). Review: 1 attempt HELD (hard=1: missing first-person cue in nuanced-takeaway) — adopted the held rewrite (regressions=0, rhythm improved) and repaired by hand; re-added the gpu-compute tool inline link the rewrite had dropped.
- Gate battery: all pass. Published: Supabase row 5c6791b8, WP post 1852 (status publish), sitemap refreshed, auto-deploy pushed. Live on aichieve.net verified: title, og:image, 1024x576 hero derivative, 3 Related-reading links, kind tag evergreen.

## Derived figures (arithmetic on verified ends)
- 26.5x = 77.94 / 2.94. One build total $80.88.
- 5 waits/day x 20 min x 21 days = 35 h/mo = $2,625 at $75/h (reader-replaceable assumption, labelled).
- Re-entry tax: 5 x 23.25 min x 21 d = 40.7 h = $3,052.
- Halved wait saves 17.5 h = $1,312/mo; $3,500 box pays back in ~2.7 months.

## Notes
- incredibuild.com (State of Build Times survey) unreachable to the gate fetcher — figure not citable from it (recorded as pitfall).
- Featured image: overlay title text is the pipeline's own deterministic composite over a text-free base render; base render reviewed clean.
