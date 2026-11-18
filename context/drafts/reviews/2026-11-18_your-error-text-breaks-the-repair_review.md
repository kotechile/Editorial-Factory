# Review report — 2026-11-18_your-error-text-breaks-the-repair_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-18_your-error-text-breaks-the-repair_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 19 · citations: 3 · quotes: 0 · sources: 3
- reader-side critic: 2 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: An agent can only repair a failed tool call through the tools it already holds, so error text that names a terminal command or a bare wait is a broken instruction — and the gap between naming a command and naming a tool is the entire margin between failure and recovery.
SHAPE: Lead: state the argument and the core numbers ; At a glance: three-line box with shift, number, risk ; The big picture: establish the mismatch between developer-written errors and agent capabilities, with the credential and rate-limit evidence ; By the numbers: three figures that prove the mechanism, placed after the mechanism is explained ; What I'd watch: where the fix lives — naming tools not commands, the RFC 9457 gap, and how teams closest to this are writing the answer ; The catch: the edges of the evidence and the upkeep problem, with the authority caveat.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 840 | 864 |
| sentence length mean | 18.4 | 18.3 |
| sentence length spread (sd) | 8.8 | 9.2 |
| rhythm health (0-1) | 0.847 | 0.866 |
| short sentences (<=8 words) | 7.5% | 11.6% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 3.57 | 4.63 |
| abstraction per 1,000 words | 1.19 | 1.16 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 60.1 (PASS) |
| sections restating the through-line | 2 | 2 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- hedge density rose: 3.57 -> 4.63 per 1,000 words

## Advisories

- hedge density rose: 3.57 -> 4.63 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 1, "rhythm_sd": [8.8, 9.2], "rhythm_health": [0.847, 0.866], "filler": [0.0, 0.0], "words": 864, "flesch": 60.1, "score": [true, 0, -0.48], "critic_fails": 2, "critic_advisories": 0}
{"attempt": 2, "ok": false, "hard": 3, "regressions": 0, "rhythm_sd": [8.8, 8.6], "rhythm_health": [0.847, 0.839], "filler": [0.0, 0.0], "words": 837, "flesch": 58.6, "score": [false, -3, -0.07], "critic_fails": 2, "critic_advisories": 0}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.8, 8.8], "rhythm_health": [0.847, 0.847], "filler": [0.0, 0.0], "words": 840, "flesch": 58.6, "score": [false, -1, -0.71], "critic_fails": 1, "critic_advisories": 0}
```
