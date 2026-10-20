---
title: "Your Trace Won't Prove 92.5 Points"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A trace is a claim about state, not a photograph of it: the harness decides which facts survive into the record and the agent trusts the record over the environment, so a green trace certifies internal consistency and not the state it names."
date: 2026-10-20
slug: your-trace-wont-prove-925-points
synthesis: true
sources:
  - https://arxiv.org/abs/2610.25947
  - https://arxiv.org/abs/2610.26632
---

<!-- lead -->
A coding agent marks a step done that never took effect, and it does not go back — in one set of experiments, the model kept going in 53 to 100 percent of cases like that [1]. In another, when the fact behind a step could no longer be looked up again, success fell to chance: a gap of 92.5 percentage points between a fact that can be re-read and one that cannot [2]. Your trace won't prove either state.

The record a gate reads is written by the tool that ran, trimmed by the harness that decides what survives, and believed by the model that reads it.

<!-- tension -->

## The big picture:

Observability was built on one premise. The trace observes the system, so a clean trace means a clean run.

Two papers posted on 19 October remove the premise from both ends. The first shows that when an action fails silently, the agent's own log outweighs the environment. The second shows that the log is written before the model ever reads it, by a context policy that decides which facts live on.

What strikes me here is how little either failure needs a bad actor. The tool reports success, the harness drops an old turn to save context, and the model reads both and proceeds.

The two failures meet in the same place. A trace is not a picture of state. It is a claim about state, written by three parties, and a gate that reads it is reading an argument.

**The harness half.** The second paper treats the context window as a policy, not a setting. It drops old turns, sums them up, or replays the model's own earlier reasoning. The question is when that choice changes whether the task is solved [2].

The answer turns on one property: whether the fact can be recovered somewhere else. When it can, the model looks it up again and pays nothing. When it cannot, success drops to chance. The two penalties differ by 92.5 percentage points, with a 90 percent confidence interval of 89.5 to 95.5, and a pre-registered replication on a second provider's model found the same contrast [2].

On one public agent benchmark, the gap between two harnesses narrowed when old turns were summed up rather than dropped. That single change, plus the harness's own invitation to keep notes, recovered 86 percent of a 63-point gap.

The same setup without the note-taking recovered 43 percent, and adding the provider's replay of the model's earlier reasoning recovered the rest. Those are shares of one counted run per configuration and game, and the authors say so [2].

**The record half.** The first paper varies the observation, the logged action and an explicit success claim, one at a time [1]. In all 12 setups of four models across three environments, the record had a larger average pull on the agent's next commitment than the observation did.

After a step that claimed success and did not take effect, the model still stopped, advanced or purchased in 53 to 100 percent of cases [1]. The contradiction was already inside the model.

Probes on middle layers separated failed steps from successful ones on unseen apps, tasks and goals, with scores of 0.77 to 1.00, where 0.5 is a coin flip [1]. A veto placed there lifted task success by 18.7 points in one live environment, and by 5.0 and 5.1 in two others, at 0.04 to 2.0 percent added serving latency [1].

## By the numbers

- **92.5 percentage points — Lost state:** the penalty when a needed fact cannot be looked up again, against no penalty when it can, with a 90 percent interval of 89.5 to 95.5 [2].
- **86% of 63 points — Harness share:** summing up old turns plus a note-taking invitation recovered most of the gap between two harnesses; without the notes the same change recovered 43 percent [2].
- **53% to 100% — Post-failure commitment:** models still acted on a step that claimed success and did not take effect, in every setup tested [1].
- **54.3% — Green traces with errors:** across 1,828 traces from nine benchmark setups of multi-agent systems, 54.3 percent of successful traces carried a local error that something absorbed [3].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to where the checks sit. Both papers put the useful test before the next action, not after the run.

- **Re-observability as a test:** the harness result gives one question a clean yes or no. If this turn were dropped, could the agent rebuild the fact from a tool call, a file or a note? A suite that answers no for a fact it leans on is testing a trace, not a task [2].
- **A veto inside the loop:** the middle-layer check runs before the model commits and needs no extra pass through the network. That is the design worth watching, because the correction lands where the decision is made instead of in a review queue [1].
- **Evidence that stays valid:** a separate system carries each judgement with the evidence view it was made from. It found 36 binding faults that a hash-only check missed, with nothing in the system's behaviour changing [4].
- **The price of reading traces:** Laminar put its trace reader at frontier-level detection on the vendor's own 523-trace benchmark, at 23 times lower cost [5]. Cheap reading makes a full sweep affordable. It does not make the trace neutral.
- **A caution on cheap graders:** Red Hat benchmarked typed decision models against judges and classifiers on guardrail tasks. The decision model came fourth on prompt injection at 86.35 percent, behind a general model at 89.31 percent and a small classifier at 89.01 percent, and slower than both [6]. Cheaper and typed is not automatically better.

<!-- nuanced-takeaway -->

## The catch

My read is that the idea here is stronger than any single number under it.

The harness shares come from one counted run per configuration and game, on one model across four games, and the authors say the replay share rests on a single run [2]. The veto's gains are measured under injected silent failures, in three environments, not in a live product [1]. It also needs a look inside the model, which a team calling a hosted service does not get. The authors' own caveat is the sharpest one: gates calibrated on offline states did not carry over to live runs [1].

There is an easy over-read I want to avoid, since none of this says traces are useless or that the model is lying. The mechanism is duller and worse: a step fails quietly, a status field reports success, and the next decision treats the report as fact.

The part I keep circling is that the fix costs so little. One question about re-observability, asked of every fact a run leans on, is cheaper than another dashboard.

<!-- tldr -->

## At a glance

- **The Big Shift:** two papers posted on 19 October show that an agent's trace is a claim rather than an observation. The harness decides which facts survive into it, and the model trusts the record over the environment when the two disagree.
- **Why It Matters:** a passing trace certifies that the record agrees with itself, not that the run reached the state it names, so a release gate built on trace review measures the wrong object.
- **What I'd Watch:** whether teams start asking, of each fact a run leans on, whether it could be rebuilt if the turn holding it were dropped.
  - **Re-observability check:** a test that drops the turn holding a fact and asks the agent to recover it from another tool or file.
  - **In-loop veto:** a check placed before the next action, on the signal the model already carries, instead of a review after the run.
  - **Evidence-bound judgement:** a stored verdict that keeps the evidence view it was made from, so the verdict can be retired when the evidence moves.
- **The Catch:** the harness figures are single-run point estimates, the veto needs a view inside the model that a hosted service does not expose, and offline calibration did not transfer to live runs.

## Sources

[1] Khezresmaeilzadeh, T., Azizi, S. A., Baghaei Potraghloo, E., Kamal, M., Pedram, M. "Claim Laundering: When Agent Decision Models Trust Records Over Reality." arXiv:2610.25947, submitted 2026-10-19. https://arxiv.org/abs/2610.25947
[2] Lencevicius, R. "When the harness decides success: state that cannot be re-observed." arXiv:2610.26632, submitted 2026-10-19. https://arxiv.org/abs/2610.26632
[3] Huang, Y., Narechania, A., Sinha, A. "MASIF: Implicit Failures for Process Observability in Multi-Agent Systems." arXiv:2610.25852, submitted 2026-10-19. https://arxiv.org/abs/2610.25852
[4] "AgentEval: Evidence-Bounded Assessment of Stateful Agents." arXiv:2610.21177, submitted 2026-10-15. https://arxiv.org/abs/2610.21177
[5] Kim, R. "flow-1: Frontier trace intelligence at 1/20th of the cost." Laminar, 2026-10-02. https://laminar.sh/blog/flow-1
[6] Geada, R., Misiura, M., Cyril, S. "Benchmarking AI decision models against traditional guardrails." Red Hat Developer, 2026-10-02. https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails
