# Review report — 2026-11-25_your-egress-bill-six-times-storage_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-25_your-egress-bill-six-times-storage_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 30 · citations: 4 · quotes: 1 · sources: 4
- reader-side critic: 5 holding defect(s), 6 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: Object storage is billed on two meters — per GB-month to keep data, per GB to move it — so the exit meter, not the storage list price, decides the bill for any workload that serves, and the vendors who abolished egress priced it back into storage.

SHAPE: lead — the $41/$492 bill as the hook and thesis in one; At a glance — one plain paragraph naming the subject, the reader, the finding; tension — the two-meter mechanism across AWS and Google's rate cards, including the tier ladder and the page layout that buries egress; By the numbers — three figures the prose does not restate; tactical — the 2 TB/4 TB crossover worked across all four vendors, then the egress-to-storage ratio as the decision rule; catch — free egress as repricing and lock-in arithmetic, plus the ceilings on both free offers.

NOT YET EARNED: nothing material — the draft supports its claims; the At a glance box must be rebuilt to the new single-paragraph schema, and the closing link to a prior article should stay as a link, not a new concept. Watch that "75% more" stays a comparison, not an effect size, and that the 100 GB free tier stays an allowance, not a share of the bill.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 995 | 984 |
| sentence length mean | 20.6 | 21 |
| sentence length spread (sd) | 11.2 | 11.2 |
| rhythm health (0-1) | 0.631 | 0.615 |
| short sentences (<=8 words) | 15.9% | 13.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 46.2 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The free-egress offer is also a statement about where your data lives. Exit fees are small per gigabyte and enormous as lock-in: moving 50 TB between …". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words
- accessibility gate: Flesch 46.2 < floor 50.0 — the long words costing the score, each to be replaced or used once: storage, transfer, gigabyte, workload, example, allowance, vendors, standard, movement, duration, gb-month, million
- accessibility gate: undefined acronym(s): AWS, GB, TB — a brand or system name with no known full form cannot be glossed: DROP the all-caps token and write the plain noun instead ('the chipmaker', 'the GPU maker', 'the agency'). Do not invent an expansion and do not answer with a comma appositive — the gate reads both as an undefined acronym.

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 3, "regressions": 0, "rhythm_sd": [11.2, 11.2], "rhythm_health": [0.631, 0.615], "filler": [0.0, 0.0], "words": 984, "flesch": 46.2, "score": [false, -3, -0.13], "critic_fails": 5, "critic_advisories": 6}
```
