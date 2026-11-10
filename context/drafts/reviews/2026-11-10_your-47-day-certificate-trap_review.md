# Review report — 2026-11-10_your-47-day-certificate-trap_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-10_your-47-day-certificate-trap_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 14 · citations: 3 · quotes: 0 · sources: 3
- reader-side critic: 0 holding defect(s), 2 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A sealed enclave's certificate renewal rate is set by an outside calendar, so unattended issuance inside the fence is a capacity decision, not a housekeeping one.
SHAPE: lead: name the trap and the calendar that sets it ; At a glance: the shift, the one figure, the operational risk ; tension: the four-rung schedule, the validation-data rung, why revocation pushes issuers ahead, and what an air gap removes ; By the numbers: the arithmetic of an assumed 500-certificate estate at three rungs ; tactical-insight: what teams are building and the first rung that lands on an unowned workload ; nuanced-takeaway: what the rule does and does not bind, and where the real cost sits

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 856 | 862 |
| sentence length mean | 15.6 | 15.7 |
| sentence length spread (sd) | 7.6 | 7.6 |
| rhythm health (0-1) | 0.829 | 0.838 |
| short sentences (<=8 words) | 21.6% | 21.6% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 3.5 | 3.48 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 52.5 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "None of this binds a private authority. The baseline requirements cover public certificates, and an enclave may keep issuing 398-day internal certific…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [7.6, 7.6], "rhythm_health": [0.829, 0.818], "filler": [0.0, 0.0], "words": 841, "flesch": 53.0, "score": [false, -1, -0.13], "critic_fails": 0, "critic_advisories": 2}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [7.6, 7.6], "rhythm_health": [0.829, 0.838], "filler": [0.0, 0.0], "words": 862, "flesch": 52.5, "score": [false, -1, 0.08], "critic_fails": 0, "critic_advisories": 2}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [7.6, 7.6], "rhythm_health": [0.829, 0.819], "filler": [0.0, 0.0], "words": 842, "flesch": 53.0, "score": [false, -1, -0.12], "critic_fails": 0, "critic_advisories": 2}
```
