# Run log — 2026-11-26 evergreen run, home_ops_execution — hvac-maintenance-plan-math

## Gate (STEP 0)
`generation_gate.py --mode evergreen --vertical home_ops_execution` → GENERATION OK (control=supabase, vertical=file).

## Topic selection
From the vertical's own `primary_angles` ("annual preventative maintenance vendor contracts") +
founder-voice §3 "The Enterprise Home Ops Playbook" + customer-truth Anecdote 3 (the $7,500
compressor quote). GSC striking-distance file had 0 candidates (not a veto per §2). No Judge, no
30-day window — evergreen track.

## Evergreen gate
Brief: context/recon_proposals/2026-11-26_home_ops_execution_evergreen_brief.md
- 5 rows / 3 hosts (fixr.com, thisoldhouse.com, onetonline.org). Composite 8.9 (U9/D9/E9/A8) → winner; runner-ups dropped (sewer-scope: no fetchable cost anchor; R-410A rider: expires < 90 days → news track).
- Gate FAIL 1st run: row 3 was figure-free prose (warranty-claim condition) → figure_absent. Rewrote rows 2–3 to lead with the figures ($75–$200 tune-up; $75–$150 agreement) → PASS, marker written 19:04.
- De-dup: `2026-11-29`-window nearest prior `2026-10-29_11-degrees-kills-the-compressor-quote` (diagnostics, not plan-purchase economics); cross-corpus grep clean (4 cross-vertical hits, none HVAC plans).
- Note: gate evidence windows for rows 2/3 sit on the first "$75" token, not the agreement-plan sentence — the plan-price sentence exists verbatim on the page (eyeballed in the fetched text); recorded per casebook row-crafting guidance.

## Draft → review
- Draft written with one earned inline link ([11-degree delta-T…](/11-degrees-kills-the-compressor-quote/), curl 200), frontmatter kind/archetype/evergreen set.
- Pre-tuned: readability_critic (enumeration fix — numbered items need bold lead-ins), accessibility (HVAC gloss at first use; Flesch 50.2→52.6), article_shape, headline 100/100.
- Review attempt 1 HELD hard=2: both observer-cue checks. The rewrite HAD cues but in forms the regex misses: "My own reading" (regex needs "My reading"/"My read") and the catch cue had been dropped. Adopted attempt by hand: "My reading, held loosely…" and "What I find hard to argue with…". Cues then present in all three sections, no boilerplate.
- `article_reviewer` voice checker + verify.sh §9: adopted file passes.

## Gates
`run_pipeline.py gate --file …_final.md` → 8/8 PASS (accessibility 52.6, shape, critic, headline 100, sources, review_audit, voice [22 pre-existing corpus-wide], publish_gate).

## Persistence
- `scripts/publish.py` → published/2026-11-26_hvac-maintenance-plan-math.md; internal-links block inserted before ## Sources (3 links: Tools & Equipment hub, Insurance Bill Beats Property Tax, 3 Days to Kill Your Deposit); Supabase row a847d482-e87d-4b18-a9bd-e99d9c0c3295 enriched.
- CMS post 491 status publish, kind tag evergreen (term 29), vertical term 18, category 3 Tools & Equipment, featured media 490.
- Delivery verified: front 404 for ~90 s (static build in flight), then 200 with title, hero + -1024x576 derivative, 3 internal links, 2 inline links (11-degrees + Related reading).

## Open items
- verify.sh repo-wide `finish` fails on OTHER runs' artifacts (2026-11-26 angle-brief anchor misses; test_illustration_overlay failures; 22 corpus voice problems) — pre-existing, not this artifact; this file's gates are green.
- Sewer-scope cadence still blocked on a fetchable cost anchor (angi/bobvila 403 the verifier).
