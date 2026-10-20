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
image_path: "context/assets/illustrations/your-trace-wont-prove-925-points/featured.png"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Why AI Agents Trust Bad Logs. A modular mechanical assembly with a severed connector displaying a green indicator light."
image_caption: "Why AI Agents Trust Bad Logs: Models trust flawed records over actual state."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A coding agent logs a step as complete when it failed silently, and in 53 to 100 percent of tested cases the model acts on that claim [1]. The record behind that decision is an argument, not a photograph: the tool writes it, the harness trims it, and the model believes it. Your trace won't prove the state that cost 92.5 points.

<!-- tension -->

## The big picture:

Monitoring rests on one premise. A clean trace means a clean run.

Two papers posted on 19 October break that premise from both ends. The first shows that when a step fails quietly, the agent trusts its own log over the environment [1]. The second shows that a context policy edits the log before the model reads it, choosing which facts survive [2].

What strikes me here is how little either failure needs a bad actor. The tool claims success and the harness drops an old turn to save room. The model reads both and moves on.

A trace is not a photograph of system state. It is a claim about state, written by three parties.

**The harness half.** The second paper treats the context window as a policy, not a setting. That policy drops old turns, sums them up, or replays the model's past reasoning.

The question is whether a dropped fact can be recovered. When the model can look it up again, nothing is lost. When it cannot, success falls to a coin flip.

The gap between those two outcomes is 92.5 percentage points, spanning 89.5 to 95.5 at 90 percent confidence [2]. A second provider's model showed the same split in a pre-registered repeat.

On one public benchmark, summing up old turns instead of dropping them closed 43 percent of a 63-point gap between two harnesses [2]. Adding an invitation to keep notes pushed that recovery to 86 percent.

Those are shares of one counted run per setup, and the authors say so.

**The record half.** The first paper varies the observation, the logged action and a success claim, one at a time, across three environments [1]. In all 12 setups, the record pulled the agent's next move harder than the observation did.

After a step claimed success and did not take effect, the model still stopped, advanced or bought in 53 to 100 percent of cases [1]. The conflict was already inside it.

Probes on middle layers told failed steps from successful ones on apps, tasks and goals the model had not seen. Those scores ran 0.77 to 1.00, where 0.5 is a coin flip [1].

A veto placed there lifted task success by 18.7 points in one live setting. It added 5.0 and 5.1 points in two others, at 0.04 to 2.0 percent extra serving latency [1].

## By the numbers

- **92.5 points — Lost state:** success falls to a coin flip when a needed fact cannot be looked up again, against no loss when it can [2].
- **86% of 63 points — Harness share:** summing up old turns plus a note-taking invitation recovered most of the gap between two harnesses. Without the notes, the same change recovered 43 percent [2].
- **53% to 100% — False commitment:** models acted on a step that claimed success and did not take effect, in every setup tested [1].
- **54.3% — Green traces with errors:** across 1,828 traces from nine multi-agent benchmark runs, 54.3 percent of successful traces carried a local error that something absorbed [3].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to where the checks sit. Both papers put the useful test before the next action, not after the run.

- **Re-observability as a test:** the harness result gives one question a clean yes or no. If this turn were dropped, could the agent rebuild the fact from a tool call or a file? A suite that answers no for a fact it leans on is testing the trace, not the task [2].
- **A veto inside the loop:** the middle-layer check runs before the model commits, with no extra pass through the network. I expect this one to spread, because the fix lands where the decision is made instead of in a review queue [1].
- **Evidence that stays valid:** a separate system keeps each judgement beside the evidence view it came from. It found 36 binding faults that a hash-only check missed, with nothing in the system's own behaviour changing [4].
- **The price of reading traces:** Laminar puts its trace reader level with a top commercial model on the vendor's own 523-trace benchmark, at 23 times lower cost [5]. Cheap reading makes a full sweep affordable. It does not make the trace neutral.
- **A caution on cheap graders:** Red Hat tested typed decision models against judges and classifiers on guardrail tasks. The decision model came fourth on prompt injection at 86.35 percent, behind a general model at 89.31 percent and a small classifier at 89.01 percent [6]. Cheaper and typed is not automatically better.

<!-- nuanced-takeaway -->

## The catch

My read is that the idea is stronger than any single number under it.

The harness shares come from one counted run per setup, on one model across four games, and the authors say the replay share rests on a single run [2]. The veto's gains are measured under injected silent failures, in three environments, not in a live product [1]. It also needs a look inside the model's middle layers, which a team calling a hosted service does not get.

The sharpest limit is the authors' own. Gates calibrated on offline states did not carry over to live runs [1].

There is an easy over-read I want to avoid, since none of this says traces are useless or that the model lies. The mechanism is duller and worse: a step fails quietly, a status field reports success, and the next decision treats the report as fact.

The part I keep circling is that the fix costs so little. Asking whether a fact could be rebuilt, for every fact a run leans on, costs less than another dashboard.

<!-- tldr -->

## At a glance

- **The Big Shift:** two papers posted on 19 October show that an agent's trace is a claim, not an observation. The harness decides which facts survive into it, and the model trusts the record over the environment when the two disagree.
- **Why It Matters:** a passing trace certifies that the record agrees with itself, not that the run reached the state it names, so a release gate built on trace review measures the wrong object.
- **What I'd Watch:** whether teams start asking, of each fact a run leans on, whether it could be rebuilt if the turn holding it were dropped.
  - **Re-observability check:** a test that drops the turn holding a fact and asks the agent to recover it from another tool or file.
  - **In-loop veto:** a check placed before the next action, on the signal the model already carries, instead of a review after the run.
  - **Evidence-bound judgement:** a stored verdict that keeps the evidence view it was made from, so the verdict can be retired when the evidence moves.
- **The Catch:** the harness figures are single-run point estimates, the veto needs a look inside the model that a hosted service does not expose, and offline calibration did not transfer to live runs.

## Sources

[1] Khezresmaeilzadeh, T., Azizi, S. A., Baghaei Potraghloo, E., Kamal, M., Pedram, M. "Claim Laundering: When Agent Decision Models Trust Records Over Reality." arXiv:2610.25947, submitted 2026-10-19. https://arxiv.org/abs/2610.25947
[2] Lencevicius, R. "When the harness decides success: state that cannot be re-observed." arXiv:2610.26632, submitted 2026-10-19. https://arxiv.org/abs/2610.26632
[3] Huang, Y., Narechania, A., Sinha, A. "MASIF: Implicit Failures for Process Observability in Multi-Agent Systems." arXiv:2610.25852, submitted 2026-10-19. https://arxiv.org/abs/2610.25852
[4] "AgentEval: Evidence-Bounded Assessment of Stateful Agents." arXiv:2610.21177, submitted 2026-10-15. https://arxiv.org/abs/2610.21177
[5] Kim, R. "flow-1: Frontier trace intelligence at 1/20th of the cost." Laminar, 2026-10-02. https://laminar.sh/blog/flow-1
[6] Geada, R., Misiura, M., Cyril, S. "Benchmarking AI decision models against traditional guardrails." Red Hat Developer, 2026-10-02. https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails

## Gate report

lead PASS — opens on the measured behaviour and names both anchors' figures early.
tension PASS — the fusion is stated where neither paper states it, with a first-person cue.
tactical-insight PASS — five observed checks, each attributed, none reader-directed.
nuanced-takeaway PASS — carries the single-run limits, the hosted-model limit and the authors' calibration caveat.
tldr PASS — four slots, both legs and the fusion under The Big Shift.
hand-tune note — attempt 1 passed at Flesch 50.7 with a re-cut title; the hand-set 100/100 title was restored, five claims were re-tied to their sources, and the body was tuned without dropping a figure, a name or a citation.
