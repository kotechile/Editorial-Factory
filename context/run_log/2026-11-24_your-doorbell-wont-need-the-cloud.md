# Run log: smart_home_telemetry news — 2026-11-24 — your-doorbell-wont-need-the-cloud

## Pipeline
Gate: `generation_gate.py --mode news --vertical smart_home_telemetry` → GENERATION OK, exit 0.
Radar: window 2026-10-25 → 2026-11-24; 9 queries (4 web fan-outs across the angles, 4 HN Algolia, 1 home_lifestyle_intel MCP — MCP returned 10 mostly off-vertical rows, dropped 1 out-of-window). Signals file: 5 rows, all in-window with https sources, I60+ (`context/recon_proposals/2026-11-24_smart_home_telemetry_signals.md`).
Seed: `synthesize_topics.py --seed` → rows=3 candidates=0, then re-seeded rows=5 candidates=0 after the row set froze (marker fresh; verify.sh §8 OK). "No valid pair" recorded as input, not verdict.
Judge: de-dup §3.5 killed the obvious synthesis — SmartThings $4.99/100k-calls/Dec-15 was published 2026-11-17 as `your-washer-100000-calls` (Synthesis 9.0), so any pair with it is a retread (N capped 6.0 → 7.4); the Link rename primary is dated 2026-10-02, outside the window. Fresh winner: **HA 2026.11 ships Matter 1.5 cameras + two-way talk** (never published on the desk; only a 7.2 runner-up on 2026-11-03 with a different framing). Single-signal **8.5** (N8.5/A9.0/S8.0). Brief: `2026-11-24_smart_home_telemetry_angle_brief.md`; `--check-briefs` OK (anchors written as plain-parenthesised URLs; both present in the signals file).

## Fact check
`2026-11-24_smart_home_telemetry_verified_brief.md`: 6 rows, all VERIFIED against two hosts (home-assistant.io release notes primary; matteralpha.com corroboration). Gate rulings: no device verdict (Aqara G350 named only as a Matter camera product), no subscription price invented, two-way audio always labelled a Labs preview, HTTPS limit attached to every talk promise. Draft written only from VERIFIED rows; no [NEEDS-SOURCE] survived.

## Draft → rewrite
Draft `2026-11-24_your-doorbell-wont-need-the-cloud_draft.md`, headline "Your Doorbell Won't Need the Cloud" (100/100 STRONG, lead_ok true; scored options: 5 titles rejected at 81 or 6-word-cap). Pre-tune took three passes: Flesch 34.2 → 49.0 → 53.1 → 58.2 (word-choice swaps: microphone→mic, subscription→plan, protocol acronyms dropped: RTSP/RTMP/FLV/HTTP/HTTPS written as plain nouns). Voice gate clean (observer cues in all three interpreting sections).
Review attempt 1 (draft at 52-53): HELD, rewrite landed Flesch 48.5-49.4. After raising the draft to 58.2: **attempt ACCEPTED, hard=0 regressions=0, Flesch 53.8, 713 words**. Post-rewrite audit: one defect fixed by hand — the lead's "a test button" blurred the feature (it is a talk button inside a Labs test feature); corrected. Title, verbatim quote, inline link and section headers all survived.

## Gates and publish
`run_pipeline.py gate`: accessibility ✓ (Flesch 53.8) · shape ✓ · critic ✓ · headline ✓ · sources ✓ · voice ✓ · publish_gate ✓.
`publish.py`: published/2026-11-24_your-doorbell-wont-need-the-cloud.md (kind: news); Supabase row 5ee30216-dce7-4033-8163-5f1c76f5655b; WordPress post 476 (status publish, vertical term 20, kind tag 28 'news', category 5, featured media 475); internal-links block inserted before ## Sources (3 links, same front/category); sitemap.json refreshed; auto-deploy pushed.
Live: https://wellroost.com/your-doorbell-wont-need-the-cloud/ → HTTP 200 first poll with own `<h1>` and a Related-reading block.

## finish
Voice gate now clean for the whole drafts directory (deleted 3 superseded 2026-11-23 drafts whose articles were published: the-human-in-your-agents-loop…, your-200-sqep-fine, your-agent-executes-before-it-verifies). Remaining `finish` failure is the **pre-existing** `scripts/test_illustration_overlay.py` 4-test failure (overlay subject-map/type-placement), same set an earlier 2026-11-24 run documented as not its own; unrelated to this article's media.

## Lessons
host ledger: home-assistant.io, matteralpha.com → fetchable. Pitfall recorded: give the draft ~58 Flesch headroom before Loop 3, or the rewrite HELDs twice.
