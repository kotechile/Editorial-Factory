# Review report — 2026-11-11_your-rate-limit-1-39-a-second_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-11_your-rate-limit-1-39-a-second_draft.md` · attempt kept: 3 of 3
- figures in the ledger: 16 · citations: 6 · quotes: 0 · sources: 6
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A vendor's rate limit is a request budget sold as a plan ladder, but the page size — how many records each request carries — is the free multiplier that decides whether a nightly sync finishes before the ladder's modest multiples ever matter.
SHAPE: Lead: states the core equation and the hidden multiplier; At a glance: three-line summary of shift, number, risk; The big picture: establishes the bucket mechanics and why the ladder's multiples are small against page size; By the numbers: the key figures in bullet form after the mechanism is explained; What I'd watch: the tactical questions — where batching lives, the offset ceiling, and patience; The catch: the honest limits of the page-size lever and when the ladder is the right purchase.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 842 | 843 |
| sentence length mean | 17.4 | 17.1 |
| sentence length spread (sd) | 7.6 | 7.2 |
| rhythm health (0-1) | 0.959 | 0.867 |
| short sentences (<=8 words) | 11.4% | 8.9% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.9 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The page-size lever stops at the endpoint's own ceiling, and some work never batches. A webhook — a call the vendor makes to your server when somethin…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Flow regressions against the draft

- rhythm health fell 0.959 -> 0.867 (mean 17.4 -> 17.1 words, sd 7.6 -> 7.2) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.959 -> 0.867 (mean 17.4 -> 17.1 words, sd 7.6 -> 7.2) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 3, "regressions": 1, "rhythm_sd": [7.6, 7.1], "rhythm_health": [0.959, 0.844], "filler": [0.0, 0.0], "words": 833, "flesch": 56.9, "score": [false, -3, -0.92], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 2, "rhythm_sd": [7.6, 6.0], "rhythm_health": [0.959, 0.524], "filler": [0.0, 0.0], "words": 794, "flesch": 57.8, "score": [false, -1, -3.48], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [7.6, 7.2], "rhythm_health": [0.959, 0.867], "filler": [0.0, 0.0], "words": 843, "flesch": 54.9, "score": [false, -1, -0.74], "critic_fails": 0, "critic_advisories": 1}
```
