# Run log — 2026-11-18 · multi_agent_enterprise_fabric (news)

**Window:** 2026-10-19 → 2026-11-18 · **Mode:** news (`0 11 * * 3`) · **Persona:** ai_architect · **Surface:** aichieve.net
**Artifact:** `2026-11-18_your-agent-checks-permission-not-ownership` — "Your Agent Checks Permission, Not Ownership: 100%"

## 1. Radar

31 query shapes: 10 arXiv API sweeps sorted `submittedDate` desc across the vertical's six `primary_angles`
(saga/compensating, multi-agent rollback, MCP, MCP+tool+agent, ERP+agent, tool-schema/context-poisoning,
durable execution, multi-agent orchestration+enterprise, agent fabric/mesh/gateway, agent interoperability/A2A),
1 arXiv `id_list` batch pulling full abstracts for 14 candidates, 14 Hacker News Algolia `search_by_date` pulls
bounded at epoch floor 2026-10-19 with a points ≥ 8 floor, 2 web fan-outs on the MCP tool-design and
enterprise-integration beats, and 4 first-party fetches (metabase.com blog; arXiv HTML full text for
2611.21577 and 2611.20922). 129 in-window arXiv hits screened, ~60 read at title level, 14 abstracts read in
full, 2 paper bodies read in full. 8 rows kept at Intensity 72–95.

HN was thin on this beat in the window (mostly Show HN repos); its one substantive find — Metabase's
2026-11-17 MCP-server rebuild — is a first-party engineering post and became the friction leg.

## 2. Judge

**Synthesis** of two papers published the same day, both read from their own HTML bodies:

- **Leg A** — arXiv:2611.21577, *When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based
  AI Agents* (Anbiaee, Dadkhah, Ghorbani), 2026-11-16.
- **Leg B** — arXiv:2611.20922, *Experience Rot: Experienced Agents Fail Where Novices Succeed* (Xu, Yin, Zhang,
  Zhao, Liu — UChicago / eBay / UFlorida), 2026-11-16.

Scores E=9.0 A=9.0 S=9.2 → **9.1**. Best single-signal candidate: Leg B alone at **8.8** (N capped 8.0 for
adjacency to `2026-10-28_your-60-drop-isnt-the-model`, which already established on this front that the tool
interface's shape decides outcomes) → margin **0.3**, meeting §2.5.

The collision: Leg A shows the fabric cannot tell *whose* tool it calls (an impostor that copies name +
description + schema wins the call); Leg B shows it cannot tell *which version* it calls (the agent's own
correct memory becomes the wrong call after a silent change). One missing step — no identity resolution at
invocation — and the only check either system performs is permission.

**Seeder:** `synthesize_topics.py --seed` → `rows=8 candidates=1`, and the one mechanical candidate (#3 Metabase
⨂ #7 guardscope, governance_x_runtime) was scored in the brief at **7.0** and refused: one leg is design intent
with no measurement, the other measures kernel-level action paths rather than tool identity. Both legs here sit
on `arxiv.org`, so the token layer cannot see the pair — the documented measurement-axis blind spot, recorded
as input.

Runner-ups answered in the brief: Leg A alone 8.7, Leg B alone 8.5 (capped), SECCARD/A2A Agent Cards 8.2
(same thesis one layer up), Reversibility Classes 7.8 (**retread** of `2026-11-04_your-undo-is-14-6x-cheaper`
on the same front — that piece already graded actions into idempotent/reversible/compensable/irreversible),
code-mode vs decision layers 7.6, OfficePrism 7.4, Metabase alone 6.9.

**De-dup §3.5:** prior 30 days of this vertical checked thesis by thesis (planner-vs-model, done-without-proof,
router-275-constraints, deletes-ask-nobody, stale-basis, replay, tool-surface-release, signed-tool, subagent).
This piece's object is the *invocation binding*, which none of them argues. Sibling front check (aichieve.net,
last 7 days): `2026-11-18_your-transcript-says-done` (agentic_resilience_failure) is about verification of
completion claims; no overlap.

## 3. Fact check

`2026-11-18_multi_agent_enterprise_fabric_verified_brief.md`: **16 rows — 16 VERIFIED, 0 FLAGGED, 0 REMOVED**,
with 12 binding rulings. Figures taken from the papers' own tables (Table II; Tables 4 and 5), never from the
abstracts. Dual-anchor gate PASS: Leg A 7 rows, Leg B 6 rows, friction 3 rows.

Rulings that mattered downstream: 1.00 is **three of five** clients, never five; Claude's 0.94 clarification
comes with binding stability 0.00 and is not a defence; 0.23 stands against 0.63 (novice), not against 1.00
(valid experience); "reports done" is a share **of failed runs**; Metabase is friction and may anchor nothing.

## 4. Draft → frontier

Draft 881 → 907 words after the title words were brought into the lead; Flesch 42.4 → **54.4** by word-choice
substitution (no sentence-splitting for score). Headline candidates scored with `headline_score.py`; "Your Agent
Checks Permission, Not Ownership: 100%" scored **100/100** with `lead_ok` true (core 6 words, 49 chars). Two
candidate titles were refused at 62 and 81. Accessibility gate failed twice on the way (undefined `GPT`,
unglossed jargon) and was repaired by naming OpenAI's flagship model without the acronym.

`article_reviewer.py` (deepseek-v4-pro): **attempt 1 ACCEPT — hard=0, regressions=0, rhythm 0.957 → 0.941,
Flesch 55.5, 942 words.**

**Hand audit after the PASS (required, since ACCEPT is not critic-clean) found two real regressions the gates
could not see:** the rewrite had **deleted the earned inline internal link** to
`/durable-execution-not-a-transaction/`, and it had **dropped the 0.63 comparator**, leaving "does worse than
one that never saw the old interface" as an unsupported comparative. Both restored; the At-a-glance third line
was re-cut from "The risk" to "The architectural rule". The 1.00 bullet was tightened to name its condition
(untyped field rename) so the figure is not read as a universal rate.

## 5. Gates

`run_pipeline.py gate` **8/8**: accessibility (Flesch 53.5, floor 50), shape, critic, headline, sources
(3 sources / 2 hosts, all fetched), review_audit, voice (1 pre-existing problem elsewhere, another run's draft),
publish_gate. `publish_gate --slug` PASS again on the published artifact.

## 6. Persistence and the defects repaired in-run

- `scripts/publish.py` wrote `published/`, `context/published_log.md`, Supabase row
  `d109914d-78f6-401b-9203-7187eedaff96`, the sitemap and WordPress post **1765** (publish; category 9
  "Autonomous & Agentic Workflows", vertical term 16 → aichieve.net, kind tag 43 `news`, featured media 1764).
- **Defect 1 — alt text was the overlay headline glued to a clipped phrase** ("…its exposed hardware revealing
  a", 128 chars). Recovered the director's own clean revision-1 sentence, shortened to 111 chars, and
  reconciled across the sidecar (rev 3), the artifact's `image_alt`, media 1764, the Supabase row's
  `metadata.illustration.alt_text` and `metadata.wordpress.media_alt`.
- **Defect 2 — the generated Related-reading block was justified on incidental tokens alone** ("agent",
  "checks", "permission") and included an off-vertical piece. Curated to three same-vertical on-thesis pages
  (`/your-tool-surface-is-a-release-surface/`, `/stale-grants-travel-the-graph/`,
  `/your-signed-tool-still-leaks-3-of-3/`, all probed 200) and written to the artifact, the Supabase row and
  post 1765 **after** the push, so no `--refresh-live` could regenerate it.
- **Defect 3 — the reader front served the pre-repair build.** The CMS PATCH does not fire the front's rebuild
  hook, so the published artifact was committed and pushed to `origin/main` (`72b6bdb`) to trigger the Coolify
  deploy; the page then served the corrected alt and the curated block.

## 7. Verification

- Front `https://aichieve.net/your-agent-checks-permission-not-ownership/` **200**, `<h1>` "Your Agent Checks
  Permission, Not Ownership: 100%", hero carries the corrected alt, `og:image` =
  `…/uploads/2026/11/your-agent-checks-permission-not-ownership-featured.jpg`, 4 site-relative links (earned
  inline + 3 curated), body carries 0.63, 0.23 and "100% of their 50 trials".
- CMS REST read-back: post 1765 publish, featured media 1764, media alt = the 111-char sentence.

## 8. Lessons recorded

`scripts/learn.py` — see §8 of this run's report: (a) a same-day pair of arXiv papers can be the strongest
collision of a window and still seed `candidates=0`, because the seeder needs two source domains; (b) an
ACCEPT from `article_reviewer.py` can silently drop an inline internal link *and* a comparator figure, so the
hand audit must diff the final against the draft for links and numbers.
