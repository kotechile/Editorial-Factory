# Review report — 2026-11-10_your-5-gate-breaks-at-261_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-10_your-5-gate-breaks-at-261_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 13 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A gate's false-positive rate is set by how often it is consulted, so any eval that can be stopped early needs an interval valid at every look or a sample size fixed in advance.
SHAPE: At a glance states the gate's promise, the proof, and the operational consequence; The big picture connects Miller's 2010 peeking result to Molas's 2025 Bayesian simulation and the 2026 optstop framework; By the numbers isolates the two measured costs; What I'd watch separates the two fixes and flags the near-zero safeguard; The catch narrows the 57–97% and 26.1% claims to the settings that produced them, then closes on the sampling schedule.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 893 | 845 |
| sentence length mean | 17.1 | 16.5 |
| sentence length spread (sd) | 7.2 | 6.6 |
| rhythm health (0-1) | 0.875 | 0.714 |
| short sentences (<=8 words) | 16.7% | 14.9% |
| filler per 1,000 words | 2.24 | 2.37 |
| hedge per 1,000 words | 2.24 | 3.55 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 50.5 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm health fell 0.875 -> 0.714 (mean 17.1 -> 16.5 words, sd 7.2 -> 6.6) — vary sentence length and break any run-on past 40 words
- hedge density rose: 2.24 -> 3.55 per 1,000 words

## Advisories

- rhythm health fell 0.875 -> 0.714 (mean 17.1 -> 16.5 words, sd 7.2 -> 6.6) — vary sentence length and break any run-on past 40 words
- hedge density rose: 2.24 -> 3.55 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 2, "rhythm_sd": [7.2, 6.6], "rhythm_health": [0.875, 0.714], "filler": [2.24, 2.37], "words": 845, "flesch": 50.5, "score": [true, 0, -2.2], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 2, "ok": false, "hard": 2, "regressions": 3, "rhythm_sd": [7.2, 5.6], "rhythm_health": [0.875, 0.569], "filler": [2.24, 1.16], "words": 863, "flesch": 49.3, "score": [false, -2, -2.11], "critic_fails": 1, "critic_advisories": 0}
{"attempt": 3, "error": "frontier returned no text (finish_reason=length)"}
```
