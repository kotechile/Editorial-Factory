# Review report — 2026-11-27_roofers-fight-the-15-year-roof-clock_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-27_roofers-fight-the-15-year-roof-clock_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 6 · citations: 4 · quotes: 4 · sources: 4
- reader-side critic: 1 holding defect(s), 2 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The FORTIFIED program's new 15-year age cap is a narrow paperwork rule, but the industry fight over it is really about whether insurers will turn a certificate's expiry into a reason to drop or reprice older roofs.
SHAPE: lead — the accusation and the one date that matters, stated once; At a glance — one plain paragraph naming subject, audience, finding; tension — the chronology in strict order, then the gap between what the rule says and what each side fears, proven by Florida's history; By the numbers — two figures the prose does not restate, after the mechanism is explained; tactical — what the carriers and the program itself are doing now, the undocumented-roof trap, and the reinsurance link; catch — both sides are right about different things, and the contractor's 32-year-old roof shows the test his argument will face is a certificate, not a storm.
NOT YET EARNED: nothing new needed — every claim is in the brief; the risk is repetition of the Jan 1 date (fix: state once in lead) and long-noun density sinking the Flesch score (fix: one full mention per term, short words after).

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 784 | 857 |
| sentence length mean | 13.1 | 19.2 |
| sentence length spread (sd) | 5.9 | 10.6 |
| rhythm health (0-1) | 0.413 | 0.918 |
| short sentences (<=8 words) | 27.3% | 18.2% |
| filler per 1,000 words | 2.55 | 1.17 |
| hedge per 1,000 words | 3.83 | 2.33 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 37.6 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: Flesch 37.6 < floor 50.0 — the long words costing the score, each to be replaced or used once: shingle, insurers, fortified, certificate, florida, bulletin, designation, discount, asphalt, insurance, premium, institute

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [5.9, 10.6], "rhythm_health": [0.413, 0.918], "filler": [2.55, 1.17], "words": 857, "flesch": 37.6, "score": [false, -1, 6.32], "critic_fails": 1, "critic_advisories": 2}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [5.9, 7.2], "rhythm_health": [0.413, 0.693], "filler": [2.55, 1.32], "words": 759, "flesch": 48.8, "score": [false, -1, 3.4], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [5.9, 8.4], "rhythm_health": [0.413, 0.902], "filler": [2.55, 1.26], "words": 791, "flesch": 45.7, "score": [false, -1, 5.23], "critic_fails": 1, "critic_advisories": 0}
```
