---
title: "Your Compaction Trap: 87% of Forgeries Survive"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "Consent is a property of the harness's data model: text gets forged, a typed protocol state does not."
date: 2026-10-29
slug: your-compaction-trap-87-forgeries-survive
synthesis: true
sources:
  - https://arxiv.org/abs/2610.29869
  - https://arxiv.org/abs/2610.37461
---

<!-- lead -->
A coding agent that runs long enough will compact its own talk. It writes a summary, drops the original, and carries that summary forward as memory. A study posted on 21 October found a trap in that step. It sits in five widely used open-source harnesses: pi, opencode, Cline, Aider and OpenHands. Each one flattens the typed conversation into a single string before the summary is written, tagging messages with labels like `[User]:`. Once the roles live in text, a forged user turn survives compaction as a real instruction. Those forgeries survive 87% to 100% of the time in the five, and 0% in four harnesses that keep messages role-typed: Codex, Gemini CLI, Qwen Code and Continue [1].

<!-- tension -->

## The big picture:

What strikes me here is how plain the failure is. A long session outgrows its window, so every harness that writes a summary must decide what it keeps. Five of the nine the authors tested keep the words and lose the roles. A label is cheap and a typed message is not. So the summary that saves the session becomes the place where an attacker's sentence reads as the user's own. No prompt can undo that, because the loss happens in code before a model sees it [1].

The second half of the trap is what happens when a person is asked to say yes. An audit of ten agent runtimes, posted on 15 October, found no approval record that a third party could check [3]. Four of the eight runtimes with measurable binding also let the arguments change after the approval was given.

<!-- tactical-insight -->

## By the numbers

- **87% to 100% — Forged approvals surviving compaction:** the rate across pi, opencode, Cline, Aider and OpenHands, against 0% for the four role-typed tools. The forged turn travels as far as a ~908,000-token window [1]
- **13 of 50 — Tasks changed without the yes:** airline tasks where a standard agent changed a booking without the confirmation it was told to get. The same test found 29 of 128 task-runs with Claude Haiku 5.5, and none for the protocol-typed agent [2]
- **4 of 8 — Runtimes with post-approval changes:** how many of the eight runtimes with measurable binding let the arguments move after the approval was given [3]
- **45% — Extra approvals for the same harm:** a gate ranked by failure risk times cost lands at 5.82% harmful runs, against 7.02% for a router that weighs the same factors, while sending far more work to a person [4]

## What I'd watch:

I keep circling the fact that the fix in the first paper is a serializer change, not a security program. Escaping the role labels before the messages are joined is the stated remedy [1]. The role-typed tools never had the defect at all. That is a line of code, and I expect it to spread once teams read their own compaction path.

- **Role-typed serializers.** Keep each message as a typed object, or escape the labels, and a forged turn has nothing to copy.
- **Protocols checked at definition.** The second paper rejects an agent subclass that could bypass its parent's protocol, a behavioral form of the rule most teams already apply to classes [2].
- **Loss made visible.** The Agent Sandbox project caps tool output at 30,000 Unicode code points by default in its 22 October release [5]. It also returns cut flags for stdout and stderr, so a trim is machine-readable rather than silent. Compaction has no such flag, and that gap is the whole defect.
- **Approval as runtime state.** Cloudflare's agent workspace now pauses a run with a call to `ctx.interrupt()` [6]. It resumes only when the app answers with an explicit yes, and the wait survives a deploy.

The older question of what an agent's records can prove reads well beside this. [An agent's logs are not evidence](/agent-audit-trail-not-evidence/) until something outside the agent ties them to the call they describe.

<!-- nuanced-takeaway -->

## The catch

My read is that the numbers are stronger on the defect than on the remedy. Both anchor papers are preprints posted in the last three weeks, and neither has been peer reviewed [1]. The attack is a lab setup. The authors report no field case, so 87% is a floor across five named tools rather than a rate for the installed base. The role split rests on nine harnesses in total.

The approval leg is weaker. A trusted approval card lifts the catch rate from 0.30 to 0.98, with 15 models acting as approvers [3]. It also turns away 16% of harmless near misses, mostly because of a placeholder in the authors' own test material. Flooding the approval path still works 0.45 to 0.60 of the time. No approval can stop a step the policy already allows. The cost of routing more work to a person comes from a simulation that assumes its own fixes work [4].

<!-- tldr -->

## At a glance

- **The Big Shift:** Five open-source coding harnesses lose the record of who said what when they compact a session. A forged approval is carried forward as memory 87% to 100% of the time, while four harnesses that keep messages role-typed hold at 0%.
- **Why It Matters:** Consent stored as text can be forged, and an agent that cannot tell a summary from an instruction will act on the forgery. The same missing type shows up with no attacker at all. On 50 airline tasks, a standard agent skipped a required confirmation 13 times, and the benchmark's own score did not see most of those.
- **What I'd Watch:** whether the fix travels as code rather than as policy.
  - **Role-typed serializers:** keep each message as a typed object, or escape the role labels, so a summary cannot hold a line that reads as the user's.
  - **Protocol state at dispatch:** offer only the tools the current step allows, and reject the rest before they act. That stopped all 13 changes in the paper's test.
  - **Cut flags on tool output:** the sandbox project now reports when it trims a result, a habit compaction has not picked up.
- **The Catch:** both papers are unreviewed preprints, the attack ran in a lab, and the 16% false-refusal rate is partly an artifact of the test material. A typed protocol limits what an agent can do, not what it grasps, and 50 tasks is a small sample.

## Sources

[1] Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents — https://arxiv.org/abs/2610.29869
[2] Concordat: Typed Sessions for LLM Agents — https://arxiv.org/abs/2610.37461
[3] Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization — https://arxiv.org/abs/2610.21063
[4] CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents — https://arxiv.org/abs/2610.36570
[5] kubernetes-sigs/agent-sandbox v1.0.8 release notes — https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v1.0.8
[6] Cloudflare Computer v0.7.0 changelog — https://developers.cloudflare.com/changelog/post/2026-10-26-computer-durable-javascript/
