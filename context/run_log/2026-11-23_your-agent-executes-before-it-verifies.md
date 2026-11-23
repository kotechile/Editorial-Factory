# Run log — 2026-11-23 agentic_ai evergreen — your-agent-executes-before-it-verifies

## Topic selection
- Gate: `scripts/generation_gate.py --mode evergreen --vertical agentic_ai` → GENERATION OK.
- First candidate (tool-shortlist size, RAG-MCP 43.13% vs 13.62%) **refused by hand**: whole-corpus grep
  surfaced `published/2026-10-07_agent-tool-count-ceiling.md` (multi_agent_enterprise_fabric, 2026-10-07)
  already arguing the mechanism, down to the same two figures. Cross-vertical de-dup caught what the
  per-vertical `check_dedup` could not.
- Winner: **the gate before the act** — founder pillar (`founder-voice.md` §3: "hard deterministic
  verification gate before taking an external action"), zero prior coverage (`verification gate`,
  `deterministic gate`, `guardrail`, `pre-execution` greps returned nothing in `published/`).
  Brief scores: U9 D8 E8 A9 → 8.6.

## Evidence (evergreen gate PASS, 2026-11-23T17:36)
| row | figure | source |
|---|---|---|
| 1 | 65% fewer harmful tool invocations, +~10% benign completion | aclanthology.org 2026.findings-acl.1850 (ToolSafe, ACL 2026 Findings) |
| 2 | 74.83% no-guard realised-harm ceiling (449/600) | arxiv.org/html/2607.21642v2 (CARE) |
| 3 | 37.33% harm, 84.99% F1, 0.34 ms static profile | same CARE paper |
| 4 | verify-only 58%→80% task success, dupes 42%→20% | arxiv.org/html/2608.02645v1 |
| — | gates fired 24 vs judges 3, no reversal | arxiv.org/html/2609.31937v1 (prose anchor, [5]) |
- Matcher lesson: the BoR paper (2605.24660) TOC collides on small integers — "3,251 tools", "20K
  tokens", "6 percentage points" all evidenced on the table of contents; only "200 tokens" lands.
  Not used in the end (topic refused), recorded here for the next tool-fabric brief.

## Review / gates
- Loop 3 attempt 1 HELD: hard=2 (tactical-insight first-person cue missing from the rewrite's own
  output detection; "TS-Guard" introduced by the rewrite and unglossable) + the rewrite **dropped the
  earned inline link** to `/durable-execution-not-a-transaction/`. Hand-repaired the held file
  (restored link, dropped "named TS-Guard", re-worded imperatives "Start with…" / "check the proposed
  action…", cue "I keep coming back to…"), promoted to `_final.md`.
- `run_pipeline.py gate`: 8/8 OK (accessibility 51.6 Flesch, headline 100 STRONG, lead_ok True).
- Reviewer rewrite also moved one By-the-numbers citation tag inside the period; harmless.

## Persistence
- `publish.py`: CMS post 1828 (publish), media 1827 (featured), Supabase row 39fe3453-313a-4940-8110-c52e8652ebfe
  (links written back), sitemap refreshed, auto-deploy pushed.
- Front verified live: aichieve.net/your-agent-executes-before-it-verifies/ → 200 with body
  (first probe 404 at ~1 min = build lag; 200 at ~5 min).
- `publish.py` printed "0 internal link(s)" — same known counting artifact as the OTIF run (it counts
  the generated block's links, and inline links don't register); the artifact carries 1 earned inline
  link + a 3-link Related-reading block, both live.
- Host lesson recorded: aclanthology.org → fetchable (learn.py --kind host).
