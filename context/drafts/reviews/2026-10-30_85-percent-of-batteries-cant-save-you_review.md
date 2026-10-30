# Review report — 2026-10-30_85-percent-of-batteries-cant-save-you_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-30_85-percent-of-batteries-cant-save-you_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 24 · citations: 7 · quotes: 5 · sources: 7

## The reviewer's reading

THROUGH-LINE: California has built a massive battery fleet, but 85 percent of it sits on the grid's side of the meter where it cannot protect households from growing wildfire power shutoffs.
SHAPE: Lead: Introduces the shutoff scope and the battery location gap. The big picture: Explains why grid batteries don't stop local shutoffs and why costs drive this divide. By the numbers: The hard figures of the outages and the fleet. What I'd watch: Post-event outage durations, the loss of tax credits, and household economics. The catch: A slight dip in retail rates and the stark reality that shutoffs prevent fires. At a glance: Summary of the shift, the number, and the risk.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 907 | 943 |
| sentence length mean | 18.1 | 18.9 |
| sentence length spread (sd) | 9.3 | 9.7 |
| rhythm health (0-1) | 0.996 | 0.933 |
| short sentences (<=8 words) | 19.4% | 16.7% |
| filler per 1,000 words | 2.21 | 0.0 |
| hedge per 1,000 words | 3.31 | 3.18 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 1 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 41.7 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: Flesch 41.7 < floor 50.0 — the long words costing the score, each to be replaced or used once: megawatts, household, percent, battery, shutoff, customers, utility, state's, october, wildfire, counties, medical

## Flow regressions against the draft

- rhythm health fell 0.996 -> 0.933 (mean 18.1 -> 18.9 words, sd 9.3 -> 9.7) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.996 -> 0.933 (mean 18.1 -> 18.9 words, sd 9.3 -> 9.7) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 4, "regressions": 2, "rhythm_sd": [9.3, 6.7], "rhythm_health": [0.996, 0.612], "filler": [2.21, 0.0], "words": 862, "flesch": 54.4, "score": [false, -4, 0.43]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [9.3, 9.7], "rhythm_health": [0.996, 0.933], "filler": [2.21, 0.0], "words": 943, "flesch": 41.7, "score": [false, -1, 1.78]}
```
