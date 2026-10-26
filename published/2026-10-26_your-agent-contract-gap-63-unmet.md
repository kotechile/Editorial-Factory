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
meta_title: "Your Agent's Contract Gap: 63% Unmet"
meta_title_source: "derived_from_title"
meta_description: "Amid a vendor push to lock down AI workloads, 63% of the rules an agent depends on go unmet at the call site. This contract gap sits inside the sandbox…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-agent-contract-gap-63-unmet/featured.jpg"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "The Agent Contract Gap. Modular containment block with an unlatched inspection gate resting on a metal workbench."
image_caption: "The Agent Contract Gap: Why sandboxes miss trust leaks at the call site."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Amid a vendor push to lock down AI workloads, 63% of the rules an agent depends on go unmet at the call site [1]. This contract gap sits inside the sandbox, right at the boundary where the code reads a model reply before acting on it. While Microsoft and Nvidia just shipped runtimes that limit what a workload can touch, the call-site fix costs about 1.5 milliseconds and zero tokens [2].

<!-- tension -->

## The big picture:

Two controls landed in the same month, and they answer entirely different questions. A sandbox dictates what the workload can reach, while a contract sets what the code will accept from a model reply before acting.

The recent study is blunt about that second boundary. Code enforces 78% of the rules these systems need. But 67% of the rules written into a prompt are only asked of the model, never checked [1]. Most of a prompt's promise is a polite request a model can ignore, and injected text can overwrite it. The clearest case is the Gemini command-line tool, which asks a model if a tool call breaks a rule but then allows the call if the reply is empty, fails to parse, or the request fails. Five of its six exit paths let the call through [1].

My read is that this represents the normal shape of the problem rather than one vendor's bug. A check exists, so the call site looks guarded in review, yet the code never actually enforces the answer.

What Microsoft and Nvidia shipped this month is real, but it sits somewhere else entirely. Microsoft Execution Containers (MXC) carry a written policy outside the workload, ensuring the agent cannot widen its own access [3]. Nvidia's OpenShell checks policy on every file access, system call and network connection inside the kernel, and keeps real credentials out of the sandbox [4].

Both validate Microsoft's core claim: an agent cannot be its own security authority [3].

## By the numbers

- **63% — Rules left unmet:** Across 496 sites in 40 systems, 63% of the rules each call site depends on went unmet, with the work checked step by step in 17,428 human judgments [1].
- **5.3% — Whole contracts met:** Only 5.3% of call sites meet the whole contract their checks exist to serve, despite 82% checking state before and after a call [1].
- **73% — Blind model replies:** Programs or other models read 73% of the replies that drive a decision, meaning no human user sees them first [1].
- **1.50 ms — Fast code checks:** Checking an action against live state took 1.50 milliseconds at zero tokens, against 17.73 seconds for a model judge [2]. One bad call costs a median of 22,400 tokens to repair [2].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to the mismatch between what teams buy and what they measure. A sandbox can be bought, has a menu of backends, and maps cleanly to an architecture diagram. A short list of checks per call site is none of those things, which explains why it tends to go unwritten.

- **The activity report as a running log:** MXC's learning mode blocks access it did not grant and logs which files and web addresses a workload tried to use. I'd want to know whether teams read that report once to tune a policy, or keep reading it to see what their agent keeps attempting.
- **Rules mined instead of written:** One paper here pulls rules from the documentation for the tools a model may call. It then tightens them against real traces, lifting error detection from 37.0 to 58.3 on one model [5]. That removes most of the manual work behind a check per call site.
- **The case neither control covers:** Across 13,598 skills that each passed a safety scan, 612 formed unsafe chains. In 13.7% of those chains, every skill had already been called safe by a single-skill scanner [6]. Clean parts in a permitted sandbox still allow a bad handoff.
- **Whether a vendor publishes a result:** This launch window holds a blog post, a repository, and a policy guide, yet no public number details what a sandbox actually does to task success.

<!-- nuanced-takeaway -->

## The catch

I could be wrong about the exact size of the prize, because the study reads code rather than live failures. Its 63% compares the code against a contract that a separate agent drew from a plain description of each unit's job. Three reviewers then corrected that yardstick, meaning a stricter reviewer would lift the figure while a looser one would cut it. 

The authors also ran the work with model-based agents before people checked each step, so the method carries part of the weakness it names.

Two limits sit on the other side. Some of these gaps are accepted risk rather than oversight, since a team may know a call site is weak and ship it anyway. A code check can be wrong too, turning away good replies or letting bad ones past. What the window does not hold is any measure showing that a sandbox closes the call-site gap. The honest claim is that these are two controls at two boundaries, not that the newer one fails. Where that points is the step rather than the model, which is the case made in [Your Agent's Next Step](/gate-the-step-not-the-model/).

<!-- tldr -->

## At a glance

- **The Big Shift:** Microsoft made its execution containers available to all on 7 October and Nvidia open-sourced a runtime that enforces policy itself the same month, while a study of 496 call sites in 40 agent systems found 63% of the rules those calls depend on unmet.
- **Why It Matters:** A sandbox limits what the workload can reach, but it does not decide whether one reply is safe to act on, and 73% of the replies that drive a decision never reach a person who could catch them.
- **What I'd Watch:**
  - **Rule coverage as a release metric:** The share of call sites whose checks before and after the call are enforced in code, counted per system rather than inferred from the fact that a check exists.
  - **Rules mined from docs:** Rules pulled from the docs for the tools a model may call and tightened against real traces, which makes a check per call site cheap enough to write.
  - **Chained skills:** Sequences where every part passed a single-skill scan and the whole chain still reaches an unsafe step.
- **The Catch:** The 63% comes from an audit of open-source code against a drawn-up reference, some gaps are deliberate, and no vendor has published what a sandbox does to this number.


<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Retry Is the Bug: An Agent's Costliest Failure Mode" -> /retry-is-the-failure-amplifier/ [same site (aichieve.net); same category; topical overlap: agent, agent's, study] Link "Retry Is the Bug: An Agent's Costliest Failure Mode" in the section where the article touches agent, agent's, study. -->
<!-- internal-link hint: "Your Agent's Next Step" -> /gate-the-step-not-the-model/ [same site (aichieve.net); same category; topical overlap: agent, agent's, study] Link "Your Agent's Next Step" in the section where the article touches agent, agent's, study. -->
<!-- internal-link hint: "68 Loops Your Runtime Never Stopped" -> /agent-loop-bound-not-a-budget/ [same site (aichieve.net); same category; topical overlap: agent, found] Link "68 Loops Your Runtime Never Stopped" in the section where the article touches agent, found. -->
## Related reading

- [Agent Memory Poisoning](/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Retry Is the Bug: An Agent's Costliest Failure Mode](/retry-is-the-failure-amplifier/) — more on Autonomous & Agentic Workflows
- [Your Agent's 84,000-Write Mistake](/agent-writes-stale-basis/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

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
