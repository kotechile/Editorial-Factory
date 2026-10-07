---
title: "Durable Execution Isn't a Transaction: Who Tracks the State the Tool Contract Can't Describe?"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "A durable journal and an MCP gateway each record half of a transaction nobody defined — the missing artifact is the task's state footprint plus the effect's declared semantics, carried across the tool boundary."
date: 2026-10-07
slug: durable-execution-not-a-transaction
synthesis: true
sources:
  - https://arxiv.org/abs/2610.03140
  - https://arxiv.org/abs/2609.15397
---

<!-- lead -->
Across 98,291 tools published by registered Model Context Protocol (MCP) servers, the metadata an agent sees can almost never say whether a call can be undone. The one risk field is set on 65.8% of those tools, but it means something on just 12.9% of them, and only 3.1% actually declare a destructive operation [1]. Three weeks earlier, a different team measured the other end of the same boundary and found the orchestrator does not record which state a task read or wrote — a gap that let one coding agent silently overwrite a sibling's work in a four-task software-engineering evaluation [2]. Neither paper cites the other.

<!-- tension -->

## The big picture:

Two pieces of infrastructure are supposed to make agents safe to point at production systems, and each one assumes the other is already solved.

The durable execution layer journals that a step ran and lets you replay it. The gateway layer catalogues which tools exist and who may call them. Neither carries a transaction: the journal does not know what state a task touched, and the tool contract does not know whether a call can be reversed.

What strikes me here is how symmetrical the blind spot is. Tapio Mraz and his co-authors at Delft University of Technology and Ververica put it plainly — orchestrators track control flow, the order tasks run in, but not data flow, the state each task reads and writes [2]. The anomaly that follows is mundane. Two workers edit the same shared test file, the plan assumed their write sets were disjoint, and one overwrote the other without a warning.

Flip to the other side and a separate team found the same emptiness in reverse. Measured across 98,291 tools from an official registry snapshot, the MCP annotation vocabulary is emitted widely and describes almost nothing a recovery protocol needs [1]. There is no status endpoint, no compensation contract, no rule saying whether two calls can be reordered.

## By the numbers

- **12.9% — Where the risk hint applies:** the destructive-operation hint is set on 65.8% of the 98,291 tools measured, but it is only meaningful on tools that are not read-only, and just 3.1% assert an actual destructive call [1].
- **98,291 — Tools in the census:** a full snapshot of the MCP registry taken on 27 July 2026, covering 18,688 distinct servers; 4,838 remote servers answered with at least one tool, a median of 11 each, and no tool was ever called [1].
- **1 of 8 — Boundary capabilities the interface can express:** for the eight recurring effect anomalies the paper catalogues, only idempotence is partly expressible in the standard annotations; the other seven capabilities are absent [1].
- **4 tasks × 2 models × 4 topologies × 5 runs — Evidence behind the orchestrator gap:** a Django refactor from a public coding benchmark was run under sequential, uncoordinated, task-ordered and conflict-ordered plans, and a repaired conflict-ordered plan fixed the failures at comparable token cost [2].

<!-- tactical-insight -->

## What I'd watch:

Both teams reached for the word "interface" from opposite ends of the same wire, which is why I read this as one missing object rather than two complaints.

The contract paper ends by saying the missing layer is a reusable transactional contract at the tool boundary, not another recovery mechanism [1]. The database-systems paper asks for external systems to expose transactional interfaces so an orchestrator can stage, validate and revert effects, and for each task to carry a footprint of everything it read and wrote [2]. Put together, the footprint is what makes the contract checkable, and the contract is what makes the footprint meaningful.

- **Where the vocabulary lands first:** the MCP specification now has a formal extensions process, and I'd want to know whether a compensation contract arrives as an extension or as a second, competing convention per vendor.
- **Whether the harness records the footprint:** the footprint has to be captured where tool calls are executed, which is the harness, not the planner. An orchestrator that infers footprints from a plan will miss the conflicts that emerge mid-execution.
- **How the two halves get priced:** a durable journal is already a line item, and agent registries are joining it. I'm watching whether anyone sells the pair as one product, because the papers argue they only work as one.

<!-- nuanced-takeaway -->

## The catch

The honest limit is that both measurements describe what is declared, not what is implemented. The census says so itself: tools may enforce stronger guarantees internally, such as deduplication or idempotency keys, than any annotation surfaces — and that safety stays unusable to a runtime that only sees the interface [1].

There is a second caveat. The orchestrator-side evidence is four coding tasks on two Claude models, not production write-backs into an enterprise system of record, and the paper states its broader agenda as a vision with open questions rather than a finished design [2]. So what is documented here is a contract gap at the boundary and a demonstrated anomaly in the small. I could be wrong that the gap survives contact with a real enterprise fabric; the way to find out is to watch whether a footprint starts appearing in traces next to the tool spans.

<!-- tldr -->

## At a glance

- **The Big Shift:** Two papers submitted three weeks apart measured the same missing object from opposite ends: an orchestrator that orders tasks but never records which state they read and wrote [2], and a tool interface that cannot declare whether an effect occurred, can be undone, or must be ordered against a concurrent caller [1]. Neither cites the other.
- **Why It Matters:** Durable execution records that a step ran, not what it changed. A gateway catalogues which tools exist, not what calling one commits you to. Teams that buy either expecting transactional safety get half a contract, and the failure it misses is a silent overwrite or a repeated posting into a system of record.
- **What I'd Watch:** I'm watching where the two halves get written down, because whoever ships the contract sets the vocabulary everyone else implements.
  - **The annotation route:** whether a compensation and outcome contract arrives as a formal extension of the tool protocol or as a per-vendor convention, which decides whether it is portable.
  - **The harness trail:** whether the state a task read and wrote starts showing up in traces beside each tool call, since the harness is the only place that can observe it.
  - **The combined purchase:** whether the journal and the registry get sold, and bought, as one thing — the papers treat them as a single interface.
- **The Catch:** The census reads declared metadata, not behaviour, so a tool with internal deduplication still looks undeclared [1]; and the orchestrator-side evidence is four coding tasks rather than a live enterprise workflow, with the wider design left as open questions [2].

## Sources

[1] *When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent–Tool Boundary* — arXiv:2609.15397, submitted 14 September 2026 (registry census snapshot 27 July 2026; artifact: github.com/flame-stream/mcp-annotation-census). https://arxiv.org/abs/2609.15397

[2] *Tracking State Footprints: How Agents Can Transact* — Mraz, Şerban, Psarakis, Kulahcioglu Ozkan and Katsifodimos, Delft University of Technology and Ververica, submitted 2 October 2026 (PVLDB 20(1)). https://arxiv.org/abs/2610.03140
