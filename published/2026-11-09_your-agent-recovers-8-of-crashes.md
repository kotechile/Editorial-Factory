---
title: "Your Agent Recovers 8% of Crashes"
vertical: agentic_ai
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
one_big_thing: "What a crashed agent resumes from is the state its tools actually touched, not the transcript: chat-only recovery restores 8% of shell-heavy tasks, a disk snapshot 28% to 42%, and a full save on every turn costs 3.78x at 96 sandboxes per host — so the runtime has to sort turns by their OS effects and pay the write only where state changed."
date: 2026-11-09
slug: your-agent-recovers-8-of-crashes
meta_title: "Your Agent Recovers 8% of Crashes"
meta_title_source: "derived_from_title"
meta_description: "Your agent recovers 8% of crashes when the runtime rebuilds it from the chat log alone. That log holds what the model said, not what its tools changed on the…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-agent-recovers-8-of-crashes/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "A hot-swap drive bay pulled halfway out of a server rack, its status light glowing amber in a dark data hall."
image_caption: "Your Agent Recovers 8% Of Crashes: Chat-only resume keeps the model's words, not the files or jobs its tools changed."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

Your agent recovers 8% of crashes when the runtime rebuilds it from the chat log alone. That log holds what the model said, not what its tools changed on the machine. The process that comes back no longer matches the disk it was writing to [1]. Three 2026 studies measure that gap, and one shows what it costs to close.

<!-- tldr -->

## At a glance

- **The shift:** A crashed run resumes from the sandbox, not from its transcript.
- **The number:** 3.78x — the cost of a full save on every turn at 96 sandboxes.
- **The risk:** Save too much and the write stalls the run; too little and it resumes broken.

<!-- tension -->

## What a resume actually restores

Three studies landed in 2026. Crab, from Hong Kong University of Science and Technology, came out on 30 April as a save-and-restore layer for agent sandboxes [1]. DeltaBox, from Shanghai Jiao Tong University, followed on 21 May with a cheaper way to save [2]. AgentRewind, from a team at Tsinghua and the Chinese Academy of Sciences, arrived in August with paired saves so a run can step back to an earlier point [3].

An agent in a sandbox runs on the operating system (OS), so the OS sees every change it makes. The agent writes files, installs packages, and leaves background jobs running. A chat log keeps the turns of the conversation. A disk snapshot keeps files but loses the running jobs. Only a save that includes running processes brings the whole machine back, and that is the costly one.

My read is that the task, not the model, sets how much must come back. On SWE-bench, the software engineering (SWE) benchmark where most turns edit files, a disk snapshot was enough for every run Crab tested. On Terminal-Bench, where agents start services and leave them running, a disk snapshot brought back 28% to 42% of tasks and the chat log alone 8% to 13% [1].

| State captured | What comes back | Bring-back rate, command-line tasks | Cost at 96 sandboxes per host |
|---|---|---|---|
| Chat log | Model turns only | 8% to 13% | Lowest |
| Disk snapshot | Files, packages | 28% to 42% | Cheap on file-only work |
| Full state, every turn | Files and live jobs | 100% | 3.78x slower |
| Sorted turns | Whatever the turn changed | 100% | 87% of turns skipped |

## By the numbers

- **3.78x slower:** A full save on every turn costs that much more, measured across 96 sandboxes sharing one host's disk [1].
- **87% skipped:** Up to that share of agent turns change neither processes nor files, so they need no save [1].
- **14 milliseconds:** A change-only save lands that fast, against seconds for a full copy [2].

<!-- tactical-insight -->

## Where runtime teams are going

I've been watching three research teams split the problem into two cheaper parts: a save that is rare, and a save that is small.

- **Crab sorts turns by what they change on the OS.** A Linux tracing hook called eBPF, short for extended Berkeley Packet Filter, sees system calls without touching the agent. It tags each turn as no save, files only, process only, or both [1]. The save runs during the model's own wait. With 64 sandboxes on one host, the save delay a user sees stayed at 0.44% of task time at the 95th percentile (the point where the slowest 5% of turns begin). The next turn does not start until the save lands [1].
- **DeltaBox makes the save small.** It stores only what changed since the last save and rolls back by starting from a frozen master process [2]. A save lands in 14 milliseconds and a rollback in 5, against hundreds of milliseconds to seconds for a full copy [2]. What I find hard to square is how soon both of those costs became ordinary.
- **AgentRewind pairs context with environment.** It records matched pairs so an agent can return to an earlier pair with a short note about what the failed attempt taught it [3]. Its benchmark, MettleBench, chains related requirements into one long task, and baseline success across seven models ranged from 28.0% to 73.2% [3]. Long runs fail often enough that recovery becomes a design choice.
- **Temporal, a workflow engine, shows why the journal cannot hold state.** It replays a run from its event journal, a log of every step [4]. That journal caps out at 51,200 events or 50 megabytes (MB), with a warning from 10,240 events or 10 MB [4]. Agent text plus tool output hits those bytes before the event cap, so state has to live outside the journal and the journal has to point to it.

<!-- nuanced-takeaway -->

## The catch

A full save is not the villain. The Crab test found it works well on SWE-bench, where turns mostly edit files and a disk save is cheap; its cost shows up on command-line-heavy work at high density [1]. A code-editing agent in one container is not in the same spot as a Terminal-Bench agent.

Sorting turns still needs a view most runtimes lack. An app framework sees tool calls, and the OS sees state changes, but neither alone can tell whether a turn's effect matters for recovery [1]. That is why the fix has to sit outside the agent, in the layer that runs the sandbox.

The part I keep circling is the contract that does not exist yet. A journal that records that a step ran does not say what that step changed, which is [the missing state in agent tool contracts](/durable-execution-not-a-transaction/). The studies infer it from OS effects after the run, which works, but the tool interface stays silent about the state each call touches.

Agents that mostly edit files get nearly everything back from a disk save, so the cheap answer is right for them. Agents that work at the command line start services and leave processes running; a chat log brings back about one task in twelve. The real choice for command-line agents is between paying for a save on every turn and sorting the turns that need one.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "68 Loops Your Runtime Never Stopped" -> /agent-loop-bound-not-a-budget/ [same site (aichieve.net); same category; topical overlap: agent, runtime] Link "68 Loops Your Runtime Never Stopped" in the section where the article touches agent, runtime. -->
<!-- internal-link hint: "Tool-List Budget: How Many Tools One Agent Can Hold" -> /agent-tool-count-ceiling/ [same site (aichieve.net); same category; topical overlap: agent, crashes] Link "Tool-List Budget: How Many Tools One Agent Can Hold" in the section where the article touches agent, crashes. -->
<!-- internal-link hint: "60.7% of Agent Deletes Ask Nobody" -> /your-agent-deletes-ask-nobody/ [same site (aichieve.net); same category; topical overlap: agent] Link "60.7% of Agent Deletes Ask Nobody" in the section where the article touches agent. -->
## Related reading

- [68 Loops Your Runtime Never Stopped](/agent-loop-bound-not-a-budget/) — more on Autonomous & Agentic Workflows
- [Tool-List Budget: How Many Tools One Agent Can Hold](/agent-tool-count-ceiling/) — more on Autonomous & Agentic Workflows
- [60.7% of Agent Deletes Ask Nobody](/your-agent-deletes-ask-nobody/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

- [1] Wu, Chang, Cao, Gao and Wang, "Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes," arXiv:2604.28138, 30 April 2026 — https://arxiv.org/html/2604.28138v1
- [2] Dong, He, Hou, Du, Xu, Yu and Xia, "DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback," arXiv:2605.22781, 21 May 2026 — https://arxiv.org/html/2605.22781v1
- [3] Zhuang, Chen, Duan, Zheng, Li and Zhang, "AgentRewind: Recoverable Execution for Long-Horizon LLM Agents," arXiv:2608.14380, 14 August 2026 — https://arxiv.org/html/2608.14380v1
- [4] Temporal, "Workflow Execution limits," platform documentation — https://docs.temporal.io/workflow-execution/limits

## Gate report

lead — PASS — Opens on the 8% figure in sentence one, plain words, no preamble.
tension — PASS — Timeline and study sequence are clear, SWE is expanded, table and bullets keep it scannable, first-person read present.
tactical-insight — PASS — Observations use bold lead-ins and no commands; eBPF, p95, and MB are anchored in place, first-person cue present.
nuanced-takeaway — PASS — Honest limitation stays self-contained, no cold closing concept, first-person cue present.
tldr — PASS — Three-line shift/number/risk schema under 50 words, plain English, no tactical recap.
