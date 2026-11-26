# Run log: agentic_ai news — your-multi-agent-fan-out-bills-3-8x (2026-11-26)

## Topic derivation
- Radar window 2026-10-27 → 2026-11-26, 9 queries (arXiv API, HN Algolia, 2 web corroborations). 6 signals ≥ 60, all dated from publisher's own date fields.
- Seed: `synthesize_topics.py --seed` → `rows=6 candidates=0` (measurement ⨂ launch collision shares no archetype tokens; skill's documented "no valid pair" branch). Judge asserted the pair under §2.5 and answered seeded inputs in the brief's runner-ups.
- Judge: synthesis #2 (launch ⨂ equal-cost study) E9/A9/S9 → 9.0; beats best single-signal (8.5) by 0.5 — precedence rule satisfied. De-dup: prior 30-day theses were memory-tier close-out (11-23) and subagent identity/authority (11-12); fan-out economics is new.
- Anchors: Perplexity Multiagent launch 2026-11-17 (first-party, fetched); arXiv 2611.33893 2026-11-25 (HTML body fetched; every figure verbatim: 1–5 pp, 2.6–3.8×, equal-cost, one-sentence probe, 75% on atlas, GPT-6.1 shrink). Corroborations: 2611.34327 (82% lower cost), 2611.33242 (CypherMAS), Bespoke coordination bench (2-of-3 fixes discarded). Dual-anchor gate passed (3 + 4 VERIFIED).

## Production
- Draft: Flesch went through three hand-tunes (24.2 → 42.9 → 52.9); fixes: one citation tag per sentence (bullet block merged by the parser until periods added), heading with "nine" read as a promise (renamed), GPT/HN glosses, title re-cut to `Your Agent Fan-Out Bills 3.8×: 16 Agents, One Price Tag` (100 STRONG with body, lead_ok).
- Loop 3 (humanize_one): 1 attempt, verdict FAIL at Flesch 46.1; hand-repaired to PASS (Flesch 50.0): stripped its `## Gate report` block (would have published), restored exact paper model names (GPT-5.6 Sol / GPT-6.1 Sol via "Generative Pre-trained Transformer (GPT)" expansion for the acronym gate), removed the duplicated inline link + imperative tail the rewrite added to the catch.
- Review (article_reviewer): two full re-runs, both HELD on its OWN output — attempt 1 emptied the nuanced-takeaway section entirely; attempt 2 dropped the tension section's first-person cue. The reviewer's critique of the standing final was otherwise "nothing unearned" (plus a dsh note — grounded: the paper itself names "dsh, DeepSeek's open-source agent harness"; gloss added). The standing `_final.md` passes `review_audit.py --draft --final` directly (PASS, 2 advisories: filler density rose, boilerplate cue "my read is that").
- Gate battery (`run_pipeline.py gate`): all 8 ok — accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate. Post-push re-score: `publish_gate --slug` → PASS.

## Persistence
- `publish.py`: Supabase row 380c8a97-4cbd-46de-8911-0fa0a3ee0b3a; CMS post 1877 (publish, two-call sequence), vertical term 14, kind tag 43 (`news`), featured media 1876; sitemap refreshed; auto-deploy commit 796394d.
- `metadata.synthesis` was absent from the row (known parse_draft gap) — PATCHed to true and read back.
- Reader: aichieve.net 404 for ~4 min (static build lag), then 200 with correct `<h1>`, hero image, inline link to agent-failure-topology-not-model, At a glance, Related reading. Sitemap `public: false` is the stale-scan artifact; delivery verified on the page.
- Unrelated sibling work (calendar row, knowledge jsonl, run-log file) committed separately (79ba682) BEFORE the publish pass so the auto-deploy commit carries only this run's files. A sibling `enterprise_ai_finops` run started mid-pass; its untracked brief files were left untouched.
