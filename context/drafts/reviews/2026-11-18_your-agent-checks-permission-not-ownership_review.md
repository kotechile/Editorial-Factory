# Review report — 2026-11-18_your-agent-checks-permission-not-ownership_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-18_your-agent-checks-permission-not-ownership_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 18 · citations: 3 · quotes: 2 · sources: 3
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A multi-agent fabric checks what a caller may do but never who owns the tool or which version is live, and two papers published the same day show that gap fails in both directions: an impostor server wins the call, and a stale memory writes to a dead interface.
SHAPE: Lead: two concrete failures, one shared missing check ; At a glance: the shift, the number, the risk in three lines ; The big picture: the protocol boundary, the two papers, the timeline ; By the numbers: the three figures the prose does not restate ; What I'd watch: Metabase's naming fixes and what the papers ask for next ; The catch: the limits of both studies and the cheaper repair.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 919 | 942 |
| sentence length mean | 18.6 | 18.8 |
| sentence length spread (sd) | 9.4 | 9.3 |
| rhythm health (0-1) | 0.957 | 0.941 |
| short sentences (<=8 words) | 22.2% | 23.9% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 2.18 | 2.12 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 55.5 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [9.4, 9.3], "rhythm_health": [0.957, 0.941], "filler": [0.0, 0.0], "words": 942, "flesch": 55.5, "score": [true, 0, -0.09], "critic_fails": 0, "critic_advisories": 1}
```
