# Review report — 2026-11-17_your-warning-leaves-701-wrong_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-17_your-warning-leaves-701-wrong_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 43 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 0 holding defect(s), 9 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: Detection already works, but advice does not change an agent's fault rate; only a deny path that withholds the failed result does.
SHAPE: Lead: the core contrast in one paragraph ; At a glance: the shift, number, risk in three lines ; The big picture: two fault classes, one finding ; By the numbers: the measured facts that prove the gap ; What I'd watch: what the deny path costs and who owns it ; The catch: the trade in coverage and scope limits.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1134 | 1145 |
| sentence length mean | 18.4 | 18.1 |
| sentence length spread (sd) | 10.6 | 11.0 |
| rhythm health (0-1) | 0.807 | 0.831 |
| short sentences (<=8 words) | 23.7% | 26.2% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.88 | 0.87 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.7 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: undefined acronym(s): API — a brand or system name with no known full form cannot be glossed: DROP the all-caps token and write the plain noun instead ('the chipmaker', 'the GPU maker', 'the agency'). Do not invent an expansion and do not answer with a comma appositive — the gate reads both as an undefined acronym.

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 2, "regressions": 0, "rhythm_sd": [10.6, 10.6], "rhythm_health": [0.807, 0.807], "filler": [0.0, 0.0], "words": 1137, "flesch": 54.0, "score": [false, -2, 0.0], "critic_fails": 0, "critic_advisories": 9}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [10.6, 11.0], "rhythm_health": [0.807, 0.831], "filler": [0.0, 0.0], "words": 1145, "flesch": 54.7, "score": [false, -1, 0.2], "critic_fails": 0, "critic_advisories": 9}
{"attempt": 3, "ok": false, "hard": 2, "regressions": 0, "rhythm_sd": [10.6, 9.1], "rhythm_health": [0.807, 0.914], "filler": [0.0, 0.0], "words": 1128, "flesch": 55.0, "score": [false, -2, 0.85], "critic_fails": 0, "critic_advisories": 9}
```
