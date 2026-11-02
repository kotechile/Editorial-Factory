# Review report — 2026-11-02_your-192-sessions-stall-the-model-not-the-tools_final.md

- verdict: **HELD — do not publish**
- draft: `2026-11-02_your-192-sessions-stall-the-model-not-the-tools_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 24 · citations: 5 · quotes: 0 · sources: 5

## The reviewer's reading

THROUGH-LINE: An agent runtime's capacity is held by whole sessions, not single calls, so the unit to cap is live jobs per box against a cache budget, and the measured payoff comes from planning agent programs while over-admission lands on the model's writing time because the tool side is where the slack is.
SHAPE: The big picture: fixes the unit with the production trace and the provider's effective-quota example ; By the numbers: lists the four measured effects that quantify the whole-job argument ; What I'd watch: reports the four job-level controls the papers and providers are converging on ; The catch: bounds the gains with field limits and the faster-tools experiment ; At a glance: restates the decision, the number, and the risk.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1011 | 942 |
| sentence length mean | 19.9 | 20.7 |
| sentence length spread (sd) | 8.9 | 9.9 |
| rhythm health (0-1) | 0.866 | 0.712 |
| short sentences (<=8 words) | 9.7% | 9.5% |
| filler per 1,000 words | 1.98 | 0.0 |
| hedge per 1,000 words | 0.99 | 1.06 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.4 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: undefined acronym(s): PASTE

## Flow regressions against the draft

- rhythm health fell 0.866 -> 0.712 (mean 19.9 -> 20.7 words, sd 8.9 -> 9.9) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.866 -> 0.712 (mean 19.9 -> 20.7 words, sd 8.9 -> 9.9) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.9, 9.9], "rhythm_health": [0.866, 0.712], "filler": [1.98, 0.0], "words": 942, "flesch": 54.4, "score": [false, -1, 0.71]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 2, "rhythm_sd": [8.9, 9.7], "rhythm_health": [0.866, 0.761], "filler": [1.98, 1.0], "words": 1003, "flesch": 48.6, "score": [false, -1, -0.46]}
{"attempt": 3, "ok": false, "hard": 5, "regressions": 0, "rhythm_sd": [8.9, 8.0], "rhythm_health": [0.866, 0.969], "filler": [1.98, 0.96], "words": 1045, "flesch": 58.1, "score": [false, -5, 1.86]}
```
