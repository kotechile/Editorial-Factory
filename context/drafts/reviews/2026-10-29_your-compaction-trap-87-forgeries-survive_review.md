# Review report — 2026-10-29_your-compaction-trap-87-forgeries-survive_final.md

- verdict: **ACCEPTED**
- draft: `2026-10-29_your-compaction-trap-87-forgeries-survive_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 21 · citations: 6 · quotes: 0 · sources: 6

## The reviewer's reading

THROUGH-LINE: When an AI coding assistant flattens its session history into plain text to save space, it strips away the structural boundaries that separate user commands from forged inputs, allowing attackers to hijack the session.
SHAPE: Lead: introduces the data-loss flaw in session compression; Tension: explains why structural types matter more than prompts; Tactical: details the survival rates of forgeries and unauthorized changes; Watch: highlights code-level fixes like strict protocols and output caps; Catch: notes the lab-only nature of the attack and the flaws in approval models; TLDR: summarizes the argument.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1016 | 1115 |
| sentence length mean | 15.5 | 18.5 |
| sentence length spread (sd) | 5.1 | 5.3 |
| rhythm health (0-1) | 0.38 | 0.502 |
| short sentences (<=8 words) | 6.1% | 0.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 1.97 | 0.9 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 52.4 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 5, "regressions": 0, "rhythm_sd": [5.1, 4.8], "rhythm_health": [0.38, 0.341], "filler": [0.0, 0.0], "words": 887, "flesch": 45.4, "score": [false, -5, 0.19]}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [5.1, 5.3], "rhythm_health": [0.38, 0.502], "filler": [0.0, 0.0], "words": 1115, "flesch": 52.4, "score": [true, 0, 1.62]}
```
