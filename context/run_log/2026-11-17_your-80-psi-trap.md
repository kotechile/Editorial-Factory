# Run-log detail — 2026-11-17 your-80-psi-trap (evergreen, smart_home_telemetry)

## Pipeline
STEP 0 `generation_gate.py --mode evergreen --vertical smart_home_telemetry` → GENERATION OK (control=supabase, vertical=file).
`run_pipeline.py start` → persona pro_homeowner, surface wellroost.com, no-repeat titles 2026-11-17 / 11-10 / 11-03.

## Candidate search (what was probed and refused before the winner)
- GSC: `gsc_analyzer.py --vertical smart_home_telemetry --export-md` → **0** opportunities (young site, thin impressions). Bonus signal only, never a veto.
- Intel MCP: `home_lifestyle_intel_client.py --recent 30` → 12 rows, all news (Redfin mortgage, Canary permitting, Wirecutter product guides). No durable lead on the telemetry beat; unused.
- Corpus greps: `pressure-reducing|pressure reducing valve|expansion tank|static pressure` across `published/` + `context/recon_proposals/` → no hit at all. Nearest neighbours by keyword: `2026-11-07_slab-leak-listener-misses-one-in-six` (home_diagnostics_tech — prices a $100–$250 pressure *test* as leak location), `2026-11-01_your-3000-psi-washers-11-gpm-trap` (outdoor_power_equipment).
- Refused candidates: Thread border-router capacity (role table 32 routers / 511 end devices, openthread.io fetches cleanly) — same capacity-arithmetic shape as the 2026-11-03 Zigbee piece, 7.9; HA recorder 10-day default — re-scored from 2026-11-10, still 7.9 on evidence (one project's docs, no bytes/day figure); IoT VLAN + mDNS — third refusal, 6.7; pressure-decay leak test — cross-vertical retread of 11-07, 7.2.

## Host probes (fixed UA `EditorialFactorySourceVerifier/1.0`)
- FETCH: `up.codes/s/design-of-building-waterdistribution-system` (9,985 chars, §604.8 + Table 604.4), `up.codes/s/excessive-water-pressure` (3,944, §608.2), `up.codes/s/thermal-expansion-control` (3,035, P2903.4), `epa.gov/watersense/showerheads` (10,375), `epa.gov/watersense/statistics-and-facts` (7,565), `home-assistant.io/integrations/recorder/` (20,615), `data.home-assistant.io/docs/statistics/` (6,262), `openthread.io/guides/thread-primer/node-roles-and-types` (11,630), `threadgroup.org`, `github.com/openthread/openthread`.
- UNREACHABLE: `zurn.com`, `cashacme.com`, `watts.com` (all PRV manufacturers), `codes.iccsafe.org/s/...` (returns a 293-char premium shell, no section text), `codelibrary.amlegal.com` (NYC 604.8, 85 psi variant), `epa.gov/watersense/leaks`, `usgs.gov` water-pressure page, `support.ecobee.com`, `energy.gov/energysaver/thermostats`, `docs.netgate.com` (untested — VLAN candidate refused before probing).
- Matcher trap fixed: row 1 first written as "80 psi (552 kPa) static — …" evidenced on Table 604.4's "Shower head 2.5 gpm at 80 psi" (the page's first standalone `80`). Re-led on `552 kPa —`, which lands on §604.8 itself. Verified with `figure_evidence` before re-running the gate.

## Brief → gates
5 rows, 5 sources, **2 hosts** (up.codes ×3, epa.gov ×2), de-dup marker `2026-11-10_smart_home_telemetry_ev…`.
Scores: U8 / D8 / E8 / A9 → 8.2.
`gate-brief` PASS; marker re-run twice (row edit + marker strip) — final `checked_at 2026-11-17T19:07:31+00:00`.

## Draft → review → gate
Draft 1,081 words. Hand fixes before Loop 3: At-a-glance labels restored to The shift / The numbers / The risk; one figure per By-the-numbers bullet; 3 citation tags in one sentence split (1/sentence); ASSE/CSA/T&P acronyms removed or spelled; Flesch 46.6 → 58.3 by word swaps (not sentence splits).
Frontier (`run_pipeline.py review`, deepseek-v4-pro): a near no-op — it changed one label ("The numbers"→"The number"), **deleted the inline internal link** (shape HOLD) and **introduced the imperative "Start with the valve…"** (voice HOLD), and dropped the 80 psi bullet from By the numbers. All four repaired by hand; also corrected "twenty years" (2011→2024 is 13) and "a licensed engineer" → "a plan stamped by a registered design professional" (§608.2's actual permission).
Final: 8/8 gates (accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate). Headline 100/100 STRONG, lead_ok True.

## Persistence + defects
- `publish.py` created WP post **421** on wellroost.com (category 5 Smart Home & Security, vertical term 20, kind tag 29 evergreen), Supabase row `524a0572-8125-4f27-bba8-0ad7e41493ef`, sitemap refreshed, auto-deploy pushed.
- **Defect: the publish shipped hero-less** (no `image_path` in the artifact, no illustration directory). Cause: the illustration pass in that run did not complete; the note was outside the captured tail. Repaired in-run: `illustration_creator.py published/…md --apply` → technical_isometric on nano-banana-pro (2400×1350, 18 credits) → `wp_draft.py --slug your-80-psi-trap --reimage` → media **423** uploaded and set as featured_media → **draft→publish toggle** to fire the front rebuild → front 200 with `-1024x576` hero + og:image.
- Rendered front verified: hero `<img>` with alt, og:image = the `-1024x576` derivative, 4 site-relative links (inline `/water-leak-monitor-rate-threshold/` + generated camera, category hub, mower).

## verify.sh state after this run (what is mine and what is not)
- Mine, fixed in-run: the draft kept the reviewer's imperative sentence (`Start with the valve…`) after I repaired only the `_final.md`; `verify.sh` scans every file in `context/drafts/`, so it failed the voice check on the draft. Both files now carry "The valve is the narrower half of the code."
- Pre-existing, NOT mine: `scripts/test_illustration_overlay.py` — 4 of 28 tests fail (`4 failed, 24 passed`), reproduced on a clean checkout of the overlay code, last touched by commit 4a28e00 (2026-11-06, "place the type on the quietest part of the frame"). Diagnosis: that commit added `weight = 0.25 + 0.75 * texture` to `_subject_map`, which is right for a smooth lit *ground* (the turnstile header) and wrong for a smooth *subject* — the test's bright document on a dark desk scores 0.24 where the test demands >0.6. The four failing tests encode the behaviours the weighting broke, so a green build needs a discriminator between "smooth surface" and "smooth object", not a threshold tweak. Left alone deliberately: the overlay heuristic decides where type lands on every header, and a blind edit at the end of a cron run is a worse risk than a documented red test.
- The `access: VERDICT: FAIL` lines on 2026-09/10/11 artifacts are reported per-artifact and do not fail the build; `article voice: OK — 1139 checks`, `sitemap 385 in sync`, `registry 33 verticals in sync` all green.
