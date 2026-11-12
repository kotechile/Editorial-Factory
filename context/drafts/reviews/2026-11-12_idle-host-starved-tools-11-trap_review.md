# Review report — 2026-11-12_idle-host-starved-tools-11-trap_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-12_idle-host-starved-tools-11-trap_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 21 · citations: 5 · quotes: 0 · sources: 5
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: An agent host that looks idle at the 11% median is actually a burst machine, and the levers that fix it are scheduler work budgets and role-pooled cores, not more cores sized to the average.
SHAPE: Lead: state the trap in one concrete image ; At a glance: the shift, the number, the risk in three lines ; The big picture: why the host is on the critical path and why the burst shape matters ; By the numbers: the figures that prove the burst and the fix ; What I'd watch: the two scheduler levers and what they cost ; The catch: what the evidence does not yet cover and what to measure next.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1112 | 1115 |
| sentence length mean | 19.5 | 19.6 |
| sentence length spread (sd) | 8.4 | 8.3 |
| rhythm health (0-1) | 0.701 | 0.698 |
| short sentences (<=8 words) | 4.3% | 4.3% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.9 | 0.9 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 58.8 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [8.4, 8.8], "rhythm_health": [0.701, 0.666], "filler": [0.0, 0.0], "words": 1030, "flesch": 58.6, "score": [false, -1, -0.32], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [8.4, 8.3], "rhythm_health": [0.701, 0.698], "filler": [0.0, 0.0], "words": 1115, "flesch": 58.8, "score": [true, 0, -0.02], "critic_fails": 0, "critic_advisories": 1}
```
