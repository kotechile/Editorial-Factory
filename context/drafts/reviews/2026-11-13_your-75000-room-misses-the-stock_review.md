# Review report — 2026-11-13_your-75000-room-misses-the-stock_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-13_your-75000-room-misses-the-stock_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 18 · citations: 9 · quotes: 0 · sources: 9
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The $75,000 retirement cap is sized by salary and therefore cannot touch a stock position, so the only lever on concentrated equity is a sale planned far in advance under Rule 10b5-1, not a deposit schedule.
SHAPE: Lead: set the two Thursday documents side by side and name the unit mismatch; At a glance: three labelled lines giving the shift, the number, and the risk; The Cap Is Written in Salary: establish the timeline once, then explain why the cap's salary-shaped formula excludes shares; By the numbers: three figures the prose does not restate; What a Plan Can't Schedule: explain Rule 10b5-1's cooling-off clock and why it cannot be started mid-crisis; The catch: the honest smaller reading of Thursday's fall and the cap's real but limited value.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 866 | 859 |
| sentence length mean | 19.5 | 16.6 |
| sentence length spread (sd) | 10.0 | 8.2 |
| rhythm health (0-1) | 0.891 | 0.9 |
| short sentences (<=8 words) | 20.0% | 19.1% |
| filler per 1,000 words | 1.15 | 1.16 |
| hedge per 1,000 words | 5.77 | 5.82 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 63.2 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: undefined acronym(s): NVIDIA

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 10.0 -> 8.2 (kept 82% of the draft's variance)

## Advisories

- rhythm flattened: sentence-length sd 10.0 -> 8.2 (kept 82% of the draft's variance)

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [10.0, 10.2], "rhythm_health": [0.891, 0.775], "filler": [1.15, 1.16], "words": 864, "flesch": 61.3, "score": [false, -1, -0.95], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [10.0, 8.2], "rhythm_health": [0.891, 0.9], "filler": [1.15, 1.16], "words": 859, "flesch": 63.2, "score": [false, -1, 0.03], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [10.0, 10.0], "rhythm_health": [0.891, 0.891], "filler": [1.15, 1.16], "words": 861, "flesch": 61.1, "score": [false, -1, -0.03], "critic_fails": 0, "critic_advisories": 0}
```
