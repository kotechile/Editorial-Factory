---
title: "Your Agent's Contract Gap: 63% Unmet"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "A sandbox and a call-site contract are two different controls at two different boundaries; the second is where trust leaks, and checking it costs about a millisecond."
date: 2026-10-26
slug: your-agent-contract-gap-63-unmet
synthesis: true
sources:
  - https://arxiv.org/abs/2610.24545
  - https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/
image_path: "context/assets/illustrations/your-agent-contract-gap-63-unmet/featured.jpg"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "The Agent Contract Gap. A small mechanical assembly with a solid perimeter and an unlatched internal gate resting on a steel desk."
image_caption: "The Agent Contract Gap: Why 63% of agent call rules are unmet by code."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A study of 496 call sites in 40 open-source agent systems found 63% of the rules those calls depend on unmet. Only 5.3% of sites met their whole contract [1]. It landed the month Microsoft made its execution containers available to all, and the month Nvidia open-sourced its own agent runtime. Both tools limit what an agent's workload can touch. That gap sits inside the sandbox, at the point where the code reads one model reply. The one place it was measured puts the fix at about 1.5 milliseconds and zero tokens [2].

<!-- tension -->

## The big picture:

Two controls landed in the same month, and they answer different questions. A sandbox sets what the workload can reach: which files, which web addresses, which programs it may start. A contract sets what the code will accept from each model reply before it acts on it.

The study is blunt about the second one. Code enforces 78% of the rules these systems need. But 67% of the rules written into a prompt are only asked of the model, never checked [1]. Most of that promise is a polite request inside a string a model can ignore, and injected text can overwrite it.

The clearest case is a guard that ships today. The Gemini command-line tool has an optional policy check that asks a model whether a tool call breaks a rule. The code then allows the call when the reply is empty, will not parse, or the request fails. Five of its six exit paths let the call through [1]. The model is asked the right question and the code does not enforce the answer. My read is that this is the normal shape of the problem, not one vendor's bug. A check exists, so the call site looks guarded in review.

What the vendors shipped this month is real, and it sits somewhere else. Microsoft Execution Containers (MXC) carry a written policy that can hold generated output, plugins, tools, the harness, or the whole agent. That policy sits outside the workload, so the agent cannot widen its own access [3]. Nvidia's OpenShell checks policy on every file access, system call and network connection inside the kernel, and keeps real credentials out of the sandbox [4]. Both are right about their own claim, which Microsoft puts plainly: an agent cannot be its own security authority [3].

## By the numbers

- **63% — Rules left unmet:** Of the rules each call site depends on, 63% went unmet across 496 sites in 40 systems, and people checked the analysis with 17,428 judgments [1].
- **5.3% — Whole contracts met:** 82% of call sites check before and after the call, yet only 5.3% meet the whole contract those checks exist to serve [1].
- **73% — Replies no person sees:** Of the replies that drive a decision, 73% are read only by the program or by another model, so no user sees them first [1].
- **1.50 ms — A code check:** Checking an action against live state took 1.50 milliseconds at zero tokens, against 17.73 seconds for a model judge. One bad call costs a median of 22,400 tokens to repair [2].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to the mismatch between what teams buy and what they measure. A sandbox can be bought, has a menu of backends, and maps to a diagram. A short list of checks per call site is none of those things, which is why it tends to go unwritten.

- **The activity report as a running log:** MXC's learning mode blocks access it did not grant and logs which files and web addresses a workload tried to use. I'd want to know whether teams read that report once, to tune a policy, or keep reading it to see what their agent keeps attempting.
- **Rules mined instead of written:** One paper here pulls rules from the docs for the tools a model may call. It then tightens them against real traces, lifting error detection from 37.0 to 58.3 on one model [5]. That removes most of the work behind a check per call site.
- **The case neither control covers:** Across 13,598 skills that each passed a safety scan, 612 formed unsafe chains. In 13.7% of those chains, every skill had already been called safe by a single-skill scanner [6]. Clean parts in a permitted sandbox still allow a bad handoff.
- **Whether a vendor publishes a result:** This window holds a launch post, a repository and a policy guide, and no public number for what a sandbox does to task success.

<!-- nuanced-takeaway -->

## The catch

I could be wrong about the size of the prize, because the study reads code rather than live failures. Its 63% compares the code against a contract that a separate agent drew from a plain description of each unit's job. Three reviewers then corrected that yardstick: a stricter one would lift the figure, a looser one would cut it. The authors also ran the work with model-based agents before people checked each step, so the method carries part of the weakness it names.

Two limits sit on the other side. Some of those gaps are accepted risk rather than oversight, since a team may know a call site is weak and ship it anyway. A code check can be wrong too, turning away good replies or letting bad ones past. What the window does not hold is any measure showing that a sandbox closes the call-site gap. The honest claim is that these are two controls at two boundaries, not that the newer one fails.

<!-- tldr -->

## At a glance

- **The Big Shift:** Microsoft made its execution containers available to all on 7 October and Nvidia open-sourced a runtime that enforces policy itself the same month, while a study of 496 call sites in 40 agent systems found 63% of the rules those calls depend on unmet.
- **Why It Matters:** A sandbox limits what the workload can reach, but it does not decide whether one reply is safe to act on, and 73% of the replies that drive a decision never reach a person who could catch them.
- **What I'd Watch:**
  - **Rule coverage as a release metric:** The share of call sites whose checks before and after the call are enforced in code, counted per system rather than inferred from the fact that a check exists.
  - **Rules mined from docs:** Rules pulled from the docs for the tools a model may call and tightened against real traces, which makes a check per call site cheap enough to write.
  - **Chained skills:** Sequences where every part passed a single-skill scan and the whole chain still reaches an unsafe step.
- **The Catch:** The 63% comes from an audit of open-source code against a drawn-up reference, some gaps are deliberate, and no vendor has published what a sandbox does to this number.

## Sources

[1] When Code Becomes an LLM Call: An Empirical Study of Call-Site Contracts in Agentic Systems — https://arxiv.org/abs/2610.24545

[2] StateMirror: Pre-Execution Detection of Hallucinated Tool Calls in Coding Agents — https://arxiv.org/abs/2610.32648

[3] Microsoft Execution Containers: Policy-driven containment for AI agents, Windows Developer Blog, 7 October 2026 — https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/

[4] Nvidia OpenShell repository — https://github.com/NVIDIA/OpenShell

[5] Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors — https://arxiv.org/abs/2610.25552

[6] Detecting Insecure Compositions of Clean Agent Skills via Capability-Flow Graph Analysis — https://arxiv.org/abs/2610.32155

## Gate report
lead: PASS — sentence 1 carries the 63% figure and the contract gap, no preamble.
tension: PASS — the two boundaries are defined and kept apart, with both anchors primary and cited.
tactical-insight: PASS — observer cues present, no instructions to the reader, four observations bulleted.
nuanced-takeaway: PASS — reference-dependence, accepted risk and check error all stated; ends on substance.
tldr: PASS — four slots, both legs visible in The Big Shift, plain definitions in the watch sub-bullets.
hand-tune: removed a frontier-added link to a page the article never cited, restored the 22,400-token recovery figure, restored the third allow path in the guard example, and re-voiced the closing sentence out of second-person instruction.
