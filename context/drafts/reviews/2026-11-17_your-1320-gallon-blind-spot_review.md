# Review report — 2026-11-17_your-1320-gallon-blind-spot_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-17_your-1320-gallon-blind-spot_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 8 · citations: 7 · quotes: 0 · sources: 7
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: Backup fuel is regulated by container count, not by generator size, so a site that adds drums or buries a tank can walk itself into a federal spill or underground-tank program without changing its power plan.
SHAPE: Lead names the blind spot and the 1,320-gallon ceiling; At a glance gives the three-line schema; The big picture establishes the rule's age and what changed on the ground; By the numbers carries the figures the prose does not restate; What I'd watch reports where the quiet errors bite and what the next open question is; The catch names the inland limit and the buried-tank trade, with the 66 MW link as the sibling problem.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 792 | 748 |
| sentence length mean | 20.4 | 18.7 |
| sentence length spread (sd) | 10.6 | 8.9 |
| rhythm health (0-1) | 0.587 | 0.817 |
| short sentences (<=8 words) | 14.7% | 14.3% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 8.84 | 9.36 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 53.9 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 10.6 -> 8.9 (kept 84% of the draft's variance)
- hedge density rose: 8.84 -> 9.36 per 1,000 words

## Advisories

- rhythm flattened: sentence-length sd 10.6 -> 8.9 (kept 84% of the draft's variance)
- hedge density rose: 8.84 -> 9.36 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 2, "rhythm_sd": [10.6, 8.9], "rhythm_health": [0.587, 0.817], "filler": [0.0, 0.0], "words": 748, "flesch": 53.9, "score": [true, 0, 1.53], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 2, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [10.6, 8.6], "rhythm_health": [0.587, 0.706], "filler": [0.0, 0.0], "words": 788, "flesch": 53.9, "score": [false, -2, 0.93], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 3, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [10.6, 9.6], "rhythm_health": [0.587, 0.743], "filler": [0.0, 0.0], "words": 793, "flesch": 53.2, "score": [true, 0, 1.25], "critic_fails": 0, "critic_advisories": 0}
```
