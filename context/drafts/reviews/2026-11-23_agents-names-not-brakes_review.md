# Review report — 2026-11-23_agents-names-not-brakes_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-23_agents-names-not-brakes_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 8 · citations: 3 · quotes: 0 · sources: 3
- reader-side critic: 0 holding defect(s), 2 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The industry gave AI agents verifiable names before it gave enterprises a way to stop them, and the identity standard's own specification contains no stop control — so buyers must not mistake the registry for a brake.

SHAPE: lead — the argument in one breath, with the derived 82.5% framed as the complement of Salt's 17.5%; At a glance — one plain paragraph naming subject, audience, finding; The big picture (tension/chronology) — the timeline stated once (June 23 intent → October 28 stop controls → November 10 launch), then the mechanism: naming is paperwork, stopping is wiring, and the ANS spec's seven documents cover identity and monitoring but no containment; By the numbers — the survey figures the prose does not restate; What I'd watch (tactical) — where the brake actually lives (WAFs, gateways, guardrails), the gap between the two camps, and the number no vendor publishes; The catch — both launches are young, the 82.5% is my arithmetic not Salt's, and the narrow conclusion.

NOT YET EARNED: the draft's "a guardrail spotted a hijacked agent and still could not stop its code from running" is not in the verified brief — cut it. The internal link is kept as the author's own prior work, but the claim behind it must stay at the level the brief supports (A4: no ANS document is an authorization or containment control). The 82.5% must stay labelled as derived.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 579 | 844 |
| sentence length mean | 14.9 | 19.8 |
| sentence length spread (sd) | 8.8 | 10.6 |
| rhythm health (0-1) | 0.778 | 0.644 |
| short sentences (<=8 words) | 38.9% | 18.4% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 1.73 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 41.2 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: Flesch 41.2 < floor 50.0 — the long words costing the score, each to be replaced or used once: identity, control, security, standard, publishes, november, foundation, launched, agent's, organizations, watching, containment

## Flow regressions against the draft

- rhythm health fell 0.778 -> 0.644 (mean 14.9 -> 19.8 words, sd 8.8 -> 10.6) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.778 -> 0.644 (mean 14.9 -> 19.8 words, sd 8.8 -> 10.6) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.8, 10.6], "rhythm_health": [0.778, 0.644], "filler": [0.0, 0.0], "words": 844, "flesch": 41.2, "score": [false, -1, -0.03], "critic_fails": 0, "critic_advisories": 2}
```
