# Review report — 2026-11-24_your-backup-tier-holds-a-365-day-lease_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-24_your-backup-tier-holds-a-365-day-lease_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 7 · citations: 5 · quotes: 1 · sources: 5
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A backup's storage class must be picked on its restore-time requirement, not its list price, because the cheapest tier's real costs — a 365-day minimum-storage clock and a 15-hour rehydration ceiling — are paid on the restore side.

SHAPE: lead — states the thesis and both clocks in three sentences; At a glance — one plain paragraph naming the subject and the finding; tension (chronology of the price screen vs the clocks) — shows why the cheap price is a loan against restore time; By the numbers — three one-metric bullets after the mechanism is explained; tactical — what teams running cold storage actually do, the two-hop staging pattern, and where the question bites next; catch — durability vs restore behaviour, the missing divisor (restore frequency), and the decision rule.

NOT YET EARNED: the draft's "retrieval bills per gigabyte" is asserted without a figure or citation — keep it qualitative or drop the specificity; "batches your restore behind paying work" is an inference, label it as reading not vendor claim; the "two-hop staging pattern" is presented as observed practice but has no source — present it as the pattern teams converge on, not measured fact; the link to the prior node article is fine but the sentence around it must parse standalone.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 667 | 675 |
| sentence length mean | 20.1 | 20.9 |
| sentence length spread (sd) | 9.1 | 9.6 |
| rhythm health (0-1) | 0.616 | 0.794 |
| short sentences (<=8 words) | 5.6% | 5.9% |
| filler per 1,000 words | 4.5 | 4.44 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 53.2 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: undefined acronym(s): GB, TB — a brand or system name with no known full form cannot be glossed: DROP the all-caps token and write the plain noun instead ('the chipmaker', 'the GPU maker', 'the agency'). Do not invent an expansion and do not answer with a comma appositive — the gate reads both as an undefined acronym.

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [9.1, 9.6], "rhythm_health": [0.616, 0.794], "filler": [4.5, 4.44], "words": 675, "flesch": 53.2, "score": [false, -1, 1.48], "critic_fails": 0, "critic_advisories": 0}
```
