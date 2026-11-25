# Run derivation: agentic_resilience_failure — 2026-11-25 (news)

**Slug:** `agent-detector-precision-66-days` · **Title:** "91% Precision, 66 Days Late: Agent Failures Nobody Sees"
**Angle Type:** Synthesis (E9 A9 S9 → 9.0), beats best single-signal ~8.7 by margin — Winner: detection tooling is measured on the visible failure class while the median real incident runs 66 days before disclosure.
**Anchors:** [1] Agent Incident Ledger snapshot 2026-11-10 (66-day median; 13-day handler lag; 21/66 outsider-first; 141,006-run review miss; ~481M transcripts) — https://www.manifold.security/blog/how-long-ai-agent-incidents-take-to-come-to-light · [2] Apsis arXiv 2611.28469 2026-11-21 (91% precision / 84% recall; 861 issues / 13 frameworks; 135-workflow benchmark; 36 unknown bugs).
**Support:** OpenAI Workspace Agent 9h42m critical outage, two updates, no RCA (status RSS 2026-11-12 + HostTracker mirror) · Anthropic 2026-11-13 double incident 4h29m, scheduled tasks skipped (Maxenius) · RecordRoute 2611.33022 (86% exact-step) · ~25 OpenAI status incidents in 30 days.

## Course of the run
- Gate ON (generation_control). Queries: arXiv API fan-out, HN Algolia, OpenAI/Anthropic status records, web search; 9 signal rows, 7 in-window primaries.
- Seeder: `rows=9 candidates=0` (measurement-on-measurement pair — §2.5 blind case, documented); Judge asserted the pair directly.
- Review: frontier rewrite HELD ×5 (Flesch inflation on every attempt: 45.1 / 46.1 / 47.5 / 46.6 / attempt 2 of a 3-attempt run reached 54.1 PASS but carried 3 critic defects + hedge regression). Resolution: attempt-2 text of the 3-attempt run adopted, reviewer's NOT-YET-EARNED list applied by hand (At a glance trimmed; count-heading renamed; [3]/[4] split to one tag per sentence; hedges → labelled first-person cues; internal link restored), then all mechanical gates re-run green on the `_final.md`.
- Gate battery: accessibility · shape · critic · headline 100/100 · sources · review_audit · voice · publish_gate — all ok.
- Persisted: WP post **1855** (publish, category 9, term 15, kind tag 43 `news`), featured media **1854**, Supabase row 59f0aeb1-d019-4df5-a42f-6142ab3ded13 (internal links written back), sitemap refreshed, auto-deploy committed+pushed.

## Open item
Reader front aichieve.net served 404 immediately after publish (static HTML; debounced rebuild from the auto-deploy push). CMS verified `publish` with the internal-links block in the body. Verify the reader page post-rebuild before considering delivery done.
