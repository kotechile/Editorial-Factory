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
---

<!-- lead -->

Your agent recovers 8% of crashes when the runtime rebuilds it from the chat log alone. That log holds what the model said, not what its tools did to the machine, so the process that comes back no longer matches the disk it was working on [1]. Three 2026 studies measure that gap, and one of them shows what closing it costs.

<!-- tldr -->

## At a glance

- **The shift:** A crashed run resumes from sandbox state, not from its transcript.
- **The number:** 3.78x — the cost of a full save on every turn at 96 sandboxes.
- **The risk:** Save too much and the write stalls the run; too little and it resumes broken.

<!-- tension -->

## What a resume actually restores

The evidence landed in one year, in three pieces. A Hong Kong University of Science and Technology group published Crab on 30 April 2026, a save-and-restore layer for agent sandboxes [1]. A Shanghai Jiao Tong University team published DeltaBox on 21 May, which makes the save itself cheap [2]. In August, a Tsinghua group published AgentRewind, which pairs two saves so a run can step back to an earlier point [3].

An agent in a sandbox is an operating-system actor, and the OS (the layer that owns files and processes) sees every change it makes. The agent writes files, installs packages and leaves background jobs running. A chat log keeps the turns of the conversation. A disk snapshot keeps the files but loses the running jobs. Only a save of process state brings the whole machine back, and that is the costly one.

My read is that the task, not the engine, sets how deep the hole is. On the software engineering (SWE) benchmark called SWE-bench, where turns mostly edit files, a disk snapshot was enough for all of the runs Crab tested. On Terminal-Bench, where agents start services and leave them up, a disk snapshot brought back 28% to 42% of tasks and the chat log alone 8% to 13% [1].

| State captured | What comes back | Restore success, shell-heavy tasks | Cost at 96 sandboxes per host |
|---|---|---|---|
| Chat log | Model turns only | 8% to 13% | Lowest |
| Disk snapshot | Files, packages | 28% to 42% | Cheap on file-only work |
| Full state, every turn | Files and live jobs | 100% | 3.78x slower |
| Sorted turns | Whatever the turn changed | 100% | 87% of turns skipped |

## By the numbers

- **3.78x slower:** A full save on every turn, measured across 96 sandboxes sharing one host's disk [1].
- **87% skipped:** Up to that share of agent turns change neither process nor disk state, so they need no save [1].
- **14 milliseconds:** One diff-based save of a sandbox, against seconds for a full copy of it [2].

<!-- tactical-insight -->

## What the runtime teams are doing

The Crab team stopped guessing which turns matter. A tracing layer called eBPF, a Linux hook that sees system calls without touching the agent, sorts every turn into one of four kinds: no save, files only, process only, or both [1]. The same runtime runs the save during the model's own wait. That kept the 95th percentile (p95, the slowest 5% of turns) of exposed save delay at 0.44% of task time, with 64 sandboxes on a host. It also holds the next turn until the save lands.

Making the save cheap matters as much as making it rare. DeltaBox saves only what changed since the last save and rolls back by forking a frozen template process. A save takes 14 milliseconds and a rollback 5, against the hundreds of milliseconds to seconds a full copy needs [2]. What I find hard to square is how recently both of those costs passed as normal.

The third study moves the save up a level. AgentRewind records matched pairs of agent context and environment, then lets the agent return to an earlier pair with a short note about what the failed attempt taught it [3]. Its benchmark, MettleBench, chains related requirements into one long task. Baseline success ranged from 28.0% to 73.2% across seven models, so a long run fails often enough to make recovery a design choice.

Workflow engines carry a second, harder limit. Temporal rebuilds a run by replaying its history, and it caps that history at 51,200 events or 50 megabytes (MB), with a warning from 10,240 events or 10 MB [4]. A few hundred turns of agent text with tool output attached reaches those bytes long before it reaches that event count. The state has to live outside the journal, and the journal has to hold references to it.

<!-- nuanced-takeaway -->

## The catch

A full save is not the villain here. The same Crab test found it works well on SWE-bench, where turns almost only edit files and a disk save is cheap; its cost shows up on shell-heavy work at high density [1]. An agent that edits code in one container is not in the same hole as a Terminal-Bench agent.

Sorting turns also needs a view most runtimes lack. An application framework sees tool calls. The OS sees state changes. Neither one alone can tell whether a turn's effect matters for recovery [1]. That is why the fix sits in a host-side runtime: nothing inside the agent's own config can make this call.

The part I keep circling is the contract that does not exist yet. A journal that records a step ran does not say what that step changed, which is [the missing state in agent tool contracts](/durable-execution-not-a-transaction/). The studies here infer it from OS effects after the run, which works, but the tool interface stays silent about the state each call touches.

So the decision follows the task mix in front of you. If your agents mostly edit files, a disk save brings back nearly everything and the cheap answer is right. If they start services and leave processes running, a chat log buys a resume of about one task in twelve, and the real choice is between paying for a save on every turn and sorting the turns that need one.

## Sources

- [1] Wu, Chang, Cao, Gao and Wang, "Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes," arXiv:2604.28138, 30 April 2026 — https://arxiv.org/html/2604.28138v1
- [2] Dong, He, Hou, Du, Xu, Yu and Xia, "DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback," arXiv:2605.22781, 21 May 2026 — https://arxiv.org/html/2605.22781v1
- [3] Zhuang, Chen, Duan, Zheng, Li and Zhang, "AgentRewind: Recoverable Execution for Long-Horizon LLM Agents," arXiv:2608.14380, 14 August 2026 — https://arxiv.org/html/2608.14380v1
- [4] Temporal, "Workflow Execution limits," platform documentation — https://docs.temporal.io/workflow-execution/limits
