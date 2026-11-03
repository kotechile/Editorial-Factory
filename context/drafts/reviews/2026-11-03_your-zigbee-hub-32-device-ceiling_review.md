# Review report — 2026-11-03_your-zigbee-hub-32-device-ceiling_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-03_your-zigbee-hub-32-device-ceiling_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 12 · citations: 8 · quotes: 3 · sources: 8

## The reviewer's reading

THROUGH-LINE: A Zigbee mesh's device limit is a firmware child-table budget — 32 plus 15 per mains-powered router — so a full network is solved with a plug, not a bigger antenna.
SHAPE: Lead: names the silent table and the formula ; The ceiling is a table: sets the ZHA 32-child arithmetic against Zigbee2MQTT's 20/21 arithmetic and reconciles the gap as firmware ; The numbers that don't move: isolates the timeout and noise-floor figures the prose does not restate ; Where the next router goes: reports the docs' cheap fixes and the reversed purchase order ; The catch: separates capacity from coverage and forces two different repairs for the same symptom ; At a glance: condenses shift, number, risk.
NOT YET EARNED: The 40-device stall point is arithmetic inference, not a documented threshold; the 12-device contrast is author judgment. Keep them as reading, not as source fact.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 827 | 757 |
| sentence length mean | 21.5 | 19.0 |
| sentence length spread (sd) | 8.5 | 8.4 |
| rhythm health (0-1) | 0.752 | 0.931 |
| short sentences (<=8 words) | 5.9% | 13.9% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 2.42 | 2.64 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 52.5 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 4, "regressions": 1, "rhythm_sd": [8.5, 9.1], "rhythm_health": [0.752, 0.743], "filler": [0.0, 0.0], "words": 773, "flesch": 51.4, "score": [false, -4, -0.95]}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [8.5, 8.4], "rhythm_health": [0.752, 0.931], "filler": [0.0, 0.0], "words": 757, "flesch": 52.5, "score": [true, 0, 1.3]}
```
