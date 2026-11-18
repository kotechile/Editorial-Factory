# Run log — 2026-11-18 · multi_agent_enterprise_fabric · EVERGREEN

**Article:** `your-error-text-breaks-the-repair` — "Your Error Text Breaks the Repair: 45% vs 84%"
**CMS:** post 1779 on aichieve.net (status publish) · Supabase row `366e509d-fcec-479b-ac28-3fd41c617db7`
**Artifact:** `published/2026-11-18_your-error-text-breaks-the-repair.md`
**Brief:** `context/recon_proposals/2026-11-18_multi_agent_enterprise_fabric_evergreen_brief.md` (gate PASS: rows=8 fetched=8 sources=3 hosts=3)

## Topic selection

The vertical has published 13 pieces and its durable space is dense: durable execution, tool-count ceiling,
stale grants, consume-once approval, cost meters, stale-basis writes, interface shape, aggregate caps,
approval defaults, the deterministic cut, planner portability, the exit predicate, and today's news piece on
tool identity and version. Candidates refused by hand this run (scores in the brief's table): risky fallback
(8.5 — spent by `2026-11-17_your-warning-leaves-701-wrong`), protocol versioning (8.2 — today's news),
OfficePrism scoring rules (7.8 — the news Judge scored it 7.4), CoAgent concurrency control (8.4 — the
2026-10-21 brief and `agent-writes-stale-basis` own the anomaly catalogue), reversibility classes (8.2 —
`2026-11-04_your-undo-is-14-6x-cheaper`), guardscope coverage (7.7), the ERP bus (7.0, fourth round).

What remained was the one half of the failure boundary nothing had read: the text a tool returns when it
fails. Anchored on `primary_angles` "MCP anti-corruption layer", persona `ai_architect` wants ("MCP
contracts", "microservice RPC boundaries"), founder-voice §3 bullet 2 (the gateway that isolates stochastic
reasoning), customer-truth Anecdote 3 (the insurer's MCP gateway in front of a mainframe).

## Evidence

| # | Source | Figure |
|---|---|---|
| 1–6 | arXiv:2609.35381v2 (Xu et al., 29 Sep 2026) | 949 of 3,001 messages in 150 MCP servers carry a step; 62 of 67 credential steps ask for a terminal command; 45% recovered vs 84% naming the login tool; 6% vs 88% on rate limits; 18→69 points with capability; 15,120 runs, five GPT models, BFCL state check |
| 7 | RFC 9457 §3.1 | five members (type, status, title, detail, instance), none an allowed next action |
| 8 | docs.github.com rate limits | 60/hour unauthenticated, 5,000/hour authenticated |

## Gates and repair

Evergreen gate PASS on the second attempt: the first draft of rows 1 and 6 led with comma-grouped numbers
("3,001", "15,120"), which the matcher splits into stray tokens ("3"/"001", "15"/"120") and verified on the
wrong sentence; leading with the ungrouped figure fixed the audit trail.

Frontier review held three attempts. Attempt 1 had hard=0 with one flow regression (hedge density) but two
critic defects (At-a-glance over 50 words, a bullet packing two figures); attempts 2 and 3 were worse (hard=3,
hard=1). Per the skill, attempt 1 was adopted and repaired by hand: the At-a-glance box trimmed, the numbers
bullets split to one metric each, "My reading is that" replaced with a first-person verb the observer-cue
matcher reads, and one imperative ("…: make the named call") rewritten to reported speech after the voice
gate flagged it.

Final battery: accessibility, shape, critic, headline (100/100, lead_ok), sources, review_audit, voice,
publish_gate — all pass. Flesch 59.8.

## Persistence

`scripts/publish.py` wrote the artifact, the published log, the Supabase row, the sitemap (auto-deploy to
origin/main), one featured image (media 1778), three generated internal links before `## Sources`, and the CMS
post at status publish with the vertical term (16) and the `evergreen` kind tag (44). The reader-side verifier
counted the inline internal link as present in the body; the front reported 0 internal links at verification
time because the static rebuild had not completed (see the post-run check).
