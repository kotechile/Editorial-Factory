# Review report — 2026-11-25_your-mcp-mandate-ships-100-wrong-tool-risk_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-25_your-mcp-mandate-ships-100-wrong-tool-risk_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 14 · citations: 4 · quotes: 1 · sources: 4
- reader-side critic: 2 holding defect(s), 8 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: Google's February 1, 2027 MCP mandate lands on a protocol whose tool catalog still cannot prove which tool belongs to which provider — so the deadline standardizes the front door while leaving the tool list ungoverned.

SHAPE: lead — the two facts in collision, mandate and measured failure; At a glance — one plain paragraph naming subject, audience, finding; tension — chronology in strict order (Nov 16 study → Nov 24 announcement → Feb 1, 2027 enforcement → Apr 1, 2027 billing), then the scope split: Google governs sign-in, nobody governs the tool list; By the numbers — figures the prose does not restate; tactical — the corroborating research (ads census, recovery audit), then what the people closest to it are doing next; catch — the failure needs an attacker-run server, so governed-only tenants sit outside it, and the risk is the open catalog, not the protocol.

NOT YET EARNED: the draft's "often points to the wrong vendor" generalizes the 100% figure beyond its condition (C10: exact name copy, copied description, compatible schema) — must be conditioned. "Hides ads from you" overstates the 9.3% labeled figure. The tactical section mixes reporting with playbook advice; it should report what researchers and teams are doing. The gains/split paragraph asserts vendor wins without evidence — cut or soften. Recovery figures (54 partial, 45 failed) can be added from the brief to earn "almost never undoes a bad run."

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 674 | 845 |
| sentence length mean | 20.9 | 23.0 |
| sentence length spread (sd) | 9.6 | 12.6 |
| rhythm health (0-1) | 0.53 | 0.358 |
| short sentences (<=8 words) | 13.3% | 17.6% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 1.48 | 1.18 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 40.5 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The mandate and the study test different parts of one stack. Google governs who may sign in, what gets logged, and what needs a human's sign-off [1]. …". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words
- accessibility gate: Flesch 40.5 < floor 50.0 — the long words costing the score, each to be replaced or used once: servers, november, mandate, measured, february, workspace, description, google's, protocol, attacker, provider, researchers
- accessibility gate: undefined acronym(s): GPT, MCP, REST — a brand or system name with no known full form cannot be glossed: DROP the all-caps token and write the plain noun instead ('the chipmaker', 'the GPU maker', 'the agency'). Do not invent an expansion and do not answer with a comma appositive — the gate reads both as an undefined acronym.

## Flow regressions against the draft

- rhythm health fell 0.53 -> 0.358 (mean 20.9 -> 23.0 words, sd 9.6 -> 12.6) — vary sentence length and break any run-on past 40 words

## Advisories

- figure not in the draft or the brief: 20 — confirm it is the source's own
- rhythm health fell 0.53 -> 0.358 (mean 20.9 -> 23.0 words, sd 9.6 -> 12.6) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 3, "regressions": 1, "rhythm_sd": [9.6, 12.6], "rhythm_health": [0.53, 0.358], "filler": [0.0, 0.0], "words": 845, "flesch": 40.5, "score": [false, -3, -1.2], "critic_fails": 2, "critic_advisories": 8}
```
