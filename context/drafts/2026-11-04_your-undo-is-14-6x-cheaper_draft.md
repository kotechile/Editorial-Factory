---
title: "Your Undo Is 14.6x Cheaper"
vertical: agentic_resilience_failure
kind: evergreen
persona: infra_engineer
one_big_thing: "An agent's recovery is chosen by the class of every action it already committed — idempotent, reversible, compensable or irreversible — and the cost of getting the choice wrong is measured: replaying a task threw away 11.41 finished acts per run against 0.78 for unwinding to the first conflict, at the same answer quality, so the undo is a design decision made per tool, not a button pressed after the failure."
date: 2026-11-04
slug: your-undo-is-14-6x-cheaper
archetype: evergreen
evergreen: true
---

<!-- lead -->
A bookkeeping agent reaches its ninth call and the payment vendor answers with a 504. Three ledger entries are already posted, one customer has been emailed, and a stock reservation is holding goods nobody has ordered yet. The engineer on call has two moves: replay the task from its first step, or walk the four finished steps backwards. A 2026 paper on streaming agents puts a price on that choice, and the price is lopsided. Replaying wastes 11.41 finished acts per run, while unwinding to the first conflict wastes 0.78 [1]. That makes your undo 14.6 times cheaper in thrown-away work, at no cost in the quality of the answer.

<!-- tension -->

## The undo has four classes

The paper's useful move is to stop treating recovery as one ability. It sorts every action into four classes — idempotent, reversible, compensable and irreversible — and shows that the class, not the algorithm, sets what an undo can cost [1].

An idempotent action can run twice and leave the same state, so the undo is nothing. A reversible action can be restored from state you kept, so the undo is one write. A compensable action is already committed somewhere else, so it needs a second and different action to reverse it. A refund is not an un-charge. An irreversible action cannot be taken back at all.

That last class is where the paper stops being tidy. Conflicting irreversible actions make finishing the task impossible, not merely costly, and conflicting compensable actions carry an adjustment cost that no plan avoids [1]. Both are built into the actions themselves, so a smarter planner does not remove them. All a runtime can do is decide where in the sequence the irreversible step sits.

I keep circling how rarely that order is a deliberate choice. A setup agent that opens a firewall rule before it checks the config has put an irreversible step second. The same agent with the rule opened last runs that step only after everything else has worked. Nothing in the model changes between those designs, and the whole gap between a clean unwind and a half-built environment someone fixes by hand sits in that ordering.

The database will not rescue the ordering, and engineers arrive assuming it will. A prepared transaction in PostgreSQL is durable: its state sits on disk, it survives a crash, and any session can commit or roll it back later [4]. But the feature is off until a server setting is raised from zero, and the identifier you hand it must be under 200 bytes, which rules out most run ids a harness generates [4][5]. Even switched on, it covers one database. A two-phase commit, the protocol that settles one transaction across two systems, does not span a payment vendor, a warehouse and an email service.

<!-- By the numbers -->

## By the numbers

- **11.41 against 0.78 — acts thrown away per run:** replaying threw away 11.41 finished acts and unwinding to the first conflict threw away 0.78, across 1,008 runs at 144 per method [1].
- **14 of 45 against 45 of 45 — effects caught before commit:** per-call guards caught 14 of 45 risky effects before they left and left 31 rule-breaking or fixable only after the fact, while a transactional runtime staged and checked all 45 [2].
- **51,200 events — the undo log's ceiling:** a workflow's history is capped at 51,200 events or 50 megabytes, with a warning from 10,240, so the record an undo reads back is finite [3].

<!-- tactical-insight -->

## Where the cost moves

Staging is not free, and the same paper measures the bill with care. The control path takes 22.2% to 23.4% of measured runtime, and the rollback itself is 2.9% of it [2]. Most of the rest is checking that a resumed task can still go on. Token use falls 23.6% to 28.4%, because a run that never commits a doomed step never reasons about it either.

Making every transaction wait for a human is the version most teams would ship. Mean task time rose 5.80 seconds, or 22.7%, which is the number I would quote when someone asks what the control costs [2]. The variant that kills a risky flow before the agent finishes its later steps came out faster than plain execution, at 23.64 seconds against 25.55 [2].

Two effects follow. The undo log is a limited resource: past 51,200 events a long-running agent has to checkpoint, saving a point it can restart from, and begin a fresh run of the workflow [3]. And saying which actions can be undone is a contract question before it is a runtime one. [A durable journal records that a step ran, not whether it can be taken back](/durable-execution-not-a-transaction/), and the class of each tool is what a staging layer reads to decide.

The teams closest to this work put the classification in the tool, not the planner. A tool that declares itself irreversible gets staged and held at the gate. A tool that declares itself idempotent gets retried without ceremony. The planner keeps its plan, and the runtime owns the commit.

<!-- nuanced-takeaway -->

## The catch

My read is that 14.6x is the most useful number here and the easiest to overstate. It comes from a test of mid-task revision, where a user changes the spec while the agent works, not from a test of crash recovery [1]. The unwind was priced against a decision that arrived late, not against a machine that died. Both cases need the same classes, and only one of them was measured.

The quality result cuts the same way. Unwinding did not beat replaying: the gap between 3.07 and 3.17 sits inside the margin of error [1]. The claim is saved work at equal quality, and a piece reporting a quality win has read the table wrong.

The Cordon figures have a narrow scope: 45 risky workflows, five rollback runs, and a runtime built by the people who measured it [2]. The mechanism is checkable, and the direction matches decades of transaction work. The percentages are one team's build on one benchmark list, and nobody has repeated them.

One cost this framing hides is that a compensation is a second write, and it can fail on its own. A refund lands twice. A reservation is released while another run still holds it. Staging before commit is the paper's answer, and it is the part of the design that needs the most care and gets the least.

<!-- tldr -->

## At a glance

**The shift:** Agent recovery is now designed per action class, rather than left to a restart button.
**The number:** Replay threw away 11.41 finished acts per run against 0.78 for unwinding, 14.6 times the waste at equal quality.
**The risk:** The headline test is mid-task revision rather than crash recovery, and a compensation is a second write that can fail too.

## Sources

[1] Zhai, Z., Li, M. and Wang, X. "Revisable by Design: A Theory of Streaming LLM Agent Execution." arXiv:2604.23283v1, 25 April 2026. https://arxiv.org/html/2604.23283v1
[2] "Cordon: Semantic Transactions for Tool-Using LLM Agents." arXiv:2606.17573v1, 16 June 2026. https://arxiv.org/html/2606.17573v1
[3] Temporal. "Workflow Execution Limits." https://docs.temporal.io/workflow-execution/limits
[4] PostgreSQL 18 Documentation. "PREPARE TRANSACTION." https://www.postgresql.org/docs/current/sql-prepare-transaction.html
[5] PostgreSQL 18 Documentation. "Resource Consumption" (`max_prepared_transactions`). https://www.postgresql.org/docs/current/runtime-config-resource.html
