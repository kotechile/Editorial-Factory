# Review report — 2026-11-23_your-agent-executes-before-it-verifies_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-23_your-agent-executes-before-it-verifies_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 13 · citations: 5 · quotes: 0 · sources: 5
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The load-bearing layer of an agent runtime is the deterministic gate between the model and the tool, because the cheapest check placed before execution removes most of the measured harm at almost no latency cost.

SHAPE: lead: state the gap and its price in one breath; At a glance: one plain paragraph naming subject, reader, and finding; tension: the three studies in evidence order — harm ceiling, guardrail result, verify-before-retry — then the architecture reason the cheap layer wins; By the numbers: three figures the prose does not restate, placed after the mechanism; tactical: what the closest teams actually shipped — profiles, postconditions, the 24-to-3 gate/judge ratio; catch: the gate buys stability not correctness, 37.33% is a floor, and blocking unsafe actions is not the same as safe tasks.

NOT YET EARNED: the closing's link to tool contracts introduces a concept the body never built — cut it or bridge it; "What I keep circling" is a borrowed cue and must be replaced; the tension section's fourth paragraph re-explains what the tactical section shows better — trim it and give the space to the 24-to-3 ratio's meaning.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 860 | 862 |
| sentence length mean | 18.7 | 20.4 |
| sentence length spread (sd) | 8.7 | 9.1 |
| rhythm health (0-1) | 0.952 | 0.831 |
| short sentences (<=8 words) | 11.1% | 18.5% |
| filler per 1,000 words | 2.33 | 1.16 |
| hedge per 1,000 words | 2.33 | 2.32 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 52.8 (FAIL) |
| sections restating the through-line | 2 | 2 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- tactical-insight --> carries no first-person sentence — it currently opens "The verify-before-retry study adds the second half of the gate, after the call. When a tool call may only half-complete, the agent checks outside stat…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words
- accessibility gate: undefined acronym(s): TS — a brand or system name with no known full form cannot be glossed: DROP the all-caps token and write the plain noun instead ('the chipmaker', 'the GPU maker', 'the agency'). Do not invent an expansion and do not answer with a comma appositive — the gate reads both as an undefined acronym.

## Flow regressions against the draft

- rhythm health fell 0.952 -> 0.831 (mean 18.7 -> 20.4 words, sd 8.7 -> 9.1) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.952 -> 0.831 (mean 18.7 -> 20.4 words, sd 8.7 -> 9.1) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [8.7, 9.1], "rhythm_health": [0.952, 0.831], "filler": [2.33, 1.16], "words": 862, "flesch": 52.8, "score": [false, -2, 0.21], "critic_fails": 0, "critic_advisories": 1}
```
