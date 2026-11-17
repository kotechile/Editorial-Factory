# Run log — 2026-11-17 · smart_home_telemetry · `your-washer-100000-calls`

**Track:** NEWS (window 2026-10-18 → 2026-11-17), registry `cadence` `0 12 * * 2`, Tue 12:00 UTC slot.
**Artifact:** `published/2026-11-17_your-washer-100000-calls.md` — "Your Washer Now Costs 100,000 Calls"
**CMS:** post 417 on wellroost.com (status publish), media 420, vertical term 20, kind tag 28.
**Synthesis:** 9.0 (E9 / A9 / S9); strongest single-signal alternative 8.65 (margin 0.35 ≥ 0.30 precedence).

## Step 0 — generation gate
`python3 scripts/generation_gate.py --mode news --vertical smart_home_telemetry` → EXIT 0,
`GENERATION OK (ok): vertical 'smart_home_telemetry' news mode is ON. [control=supabase, vertical=file]`.

## Step 1 — Radar (19 queries)
- 8 date-agnostic web fan-outs across the six configured sources and five primary angles
  (Home Assistant release, Matter/Thread, ultrasonic flow meters, panel CT clamps, cloud shutdowns,
  Hackaday, appliance subscriptions, CT-clamp guides).
- 1 Hacker News Algolia `search_by_date` sweep on the window epoch (`home assistant`, 30 hits) —
  which is where the AUX-2 launch (2026-11-11), the SmartThings integration-change post (2026-11-06)
  and the EcoFlow discussion (2026-10-22) surfaced.
- 1 intelligence-MCP pull (`home_lifestyle_intel_client.py --recent 30 --format signals`): 10 rows,
  all off-beat (three Wirecutter product guides, Remodelista interiors, a permitting piece, a
  Microsoft 365 outage). None used — the MCP returns home-lifestyle feed after all.
- 6 primary fetches (HA AUX-2 post, The Verge hands-on, SmartThings community post, GitHub discussion,
  SmartThings blog, HA 2026.11 release), 2 Discourse `.json` date lookups, 1 README fetch.

**Dropped at Stage 1, not softened:**
- SmartThings' June 2026 API announcement (out of window) and the `$4.99` figure that sits in legacy
  boilerplate on the same blog — the in-window documents are the 2026-10-30 pricing post, the
  2026-11-04 launch and the 2026-11-04 HA migration post.
- HACS → Marketplace: published 2026-10-27 as `your-hubs-4292-project-blind-spot`; excluded from
  this piece entirely (2026.11 appears only for its action-history feature, and in the end was not cited).
- EcoFlow's ask to `ha-ef-ble` (2026-10-01, HN 2026-10-22) — event predates the window.
- Belkin Wemo / Devolo / Wink / Insteon / Nest 1st–2nd gen / Dropcam: out of window.
- Matter 1.5 and 1.5.1 (2025-11, 2026-03-31): out of window; the "Matter 2.0" pages that rank are
  undated SEO with no first-party record.
- SPAN / Schneider / Leviton panel cost guides: undated marketing pages; the $8,000–$15,000
  service-upgrade figure appears in no primary document.

## Step 2 — seed
`python3 scripts/synthesize_topics.py --seed …signals.md` → `rows=7 candidates=0`. The pair collides
on a *when* and a *who-pays* (a subscription deadline against a one-time hardware price), not on
archetype vocabulary — the documented blind spot. Judge asserted the pair under `virality_judge.md`
§2.5; the zero-candidate result is recorded in the brief's runner-ups as input, not verdict.

## Step 3 — Judge
Winner (synthesis): **SmartThings meters the cloud path to your appliances by the call and sets a
15 December cutoff; Nabu Casa sells a $69 box for the physical port, eight days later.**
The emergent claim neither document states: the spec that now decides a household's running cost is
not "works with my hub" but "which of the device's ports answers without an account".
Scores: E 9.0 / A 9.0 / S 9.0 → 9.0. Best single-signal candidate: 8.65 (row 2 alone).

## Step 4 — Fact check (dual-anchor gate)
Leg A VERIFIED ×5: 2026-11-04 launch and the free/paid table (blog 2026-10-30); 2 December release,
15 December cutoff, paid Developer Plan required; 100,000 calls/month + 10 OAuth apps, per account;
country lockout clause; SSE included in the plan. Leg B VERIFIED ×3 (+1 negative): $69/€59 and the
port list; "hellish proprietary cloud" pitch and 1–2 W draw; The Verge's $69 + ESP32 concession and
the untested serial feature; the box's complete job list contains no appliance path.
Plus R1 (LocalThings: no cloud account, 30-second polling, single maintainer) and R3 (2026.11 action
history). **FLAGGED and barred from printing: the `$4.99/month` boilerplate — SmartThings publishes
no rate for the Developer Plan, and "a rate the announcement never prints" became a load-bearing beat.**
Derived arithmetic labelled as ours: 100,000 ÷ 30 = ~3,330/day; a 30-second poll = 2,880 calls/day = 86%.

## Step 5 — Draft
Title scored 100/100 STRONG (`headline_score.py`), `lead_ok: True` after "washer" and "costs" were
put in the first paragraph verbatim (the title's content-word check reads the lead only).
Pre-Loop-3 gate: Flesch 61.1, `readability_critic` ok, `article_shape` ok, voice clean. Fixes made
during drafting: "$69 (€59)" split out of one bullet lead-in; a three-prepositional-phrase sentence
in the allowance paragraph rewritten; the 15 December date removed from the lead so the timeline is
stated once (paragraph 2 of `<!-- tension -->`).

## Step 6 — Frontier rewrite
`run_pipeline.py review` → `article_reviewer.py`, attempt 1: **ACCEPT**, hard=0 regressions=0,
rhythm 8.6→8.7, Flesch 61.4, 867 words. `context/drafts/reviews/…_review.md` kept.
**The rewrite dropped the one inline internal link** (it flattened `[utility meter's own hourly rows](/your-meter-bills-from-hourly-rows/)`
to plain text). `review_audit` cannot see links, so the audit still passed; `article_shape` holds
`min_body_inline_links`. Restored by hand before the gate.

## Step 7 — Gate
`run_pipeline.py gate --file …_final.md`: accessibility ok · shape ok · critic ok · headline ok ·
sources ok · review_audit ok · voice ok (4 pre-existing failures elsewhere in the directory) ·
publish_gate ok. All eight green.

## Step 8 — Persistence
`python3 scripts/publish.py …_final.md` → published/, `published_log.md`, Supabase row
`3100b089-50cd-4943-af87-2701a5dc0f14`, `sitemap.json` refreshed, CMS post **417** created with
status=publish, vertical term 20, kind tag 28 (`news`), 7,269 chars of body, 152-char excerpt.
Internal links stamped site-relative (3): the article's own category hub, `cloud-update-bricked-the-fridge-local-first`,
`your-hubs-4292-project-blind-spot`, plus the hand-written `your-meter-bills-from-hourly-rows` in the close.
Verified on the CMS: all four hrefs present in the delivered HTML.

## Step 9 — Illustration (one re-commission)
First render: `component_assembly` on nano-banana-pro, 18 credits. The overlay's three-line headline
collided with the two-line hook and the third title line read grey-on-grey — legible per the 6.0-vs-5.5
contrast measurement, not legible per the eye. Re-commissioned with `--style editorial_macro` on flux
(5 credits, revision 3) for a composition with an empty top-right; overlay re-run (quality 88),
`wp_draft.py --slug … --reimage` switched the post to media **420** and removed the superseded 419/416.
**Alt text repair:** the director's alt was truncated at 140 chars *and* opened with the headline —
both banned in `illustration_director.md` §5. Rewritten to
"A washer's recessed network port in macro beside a small black bridge box with two RJ45 sockets."
(96 chars, one pixel sentence), patched into `featured.json`, the published artifact and the final,
and pushed to the attachment (verified alt on media 420). `illustration_creator.py --check` clean.

## Step 10 — Verification of the shipped artifact
- `https://wellroost.com/your-washer-100000-calls/` → **200** (404 immediately after publish, while
  the static build redeployed; live after the auto-deploy).
- Reader HTML carries the four internal links and the figures (100,000 ×8, 3,330, 2,880, 86%).
- CMS post 417: featured_media 420, image bytes 383,072 as served, alt set, kind tag `news`.

## Lessons recorded
1. `scripts/learn.py --kind pitfall` — the frontier rewrite drops the single inline internal link;
   `review_audit` passes it because it compares figures, citations, quotes and source lines only.
2. `scripts/learn.py --kind pitfall` — the art director's `alt_text` is cut at 140 characters mid-word
   and prefixed with the headline; check it before the push and rewrite to one complete pixel sentence.
