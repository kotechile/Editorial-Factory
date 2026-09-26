---
title: "Why Agent Rollbacks Fail"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "A faithfully-restored checkpoint can resume an execution whose states and effects never coexisted in any valid history — checkpoint-and-rollback does not guarantee safe recovery."
date: 2026-09-23
slug: rollback-breaks-execution-continuity
---

<!-- lead -->
A perfect system rollback can trick an Artificial Intelligence (AI) agent into shipping a virus under a clean scan [1]. When a code release fails, the system brings back the bad files but keeps the passing scan in memory. This lets the agent ship the bad code as clean. This is the first attack in a new paper (arXiv:2608.29381) proving that save-and-restore tools do not guarantee a safe fix.

<!-- tension -->
## The Safe Recovery Myth

**Why it matters:** Save-and-restore tools are the quick fix the agent world wants to use right now. Vendors sell them as a core feature, and specialized checkpoint-and-rollback systems tune them just for agents [1]. Long runs build up state and outside actions that cost too much time and money to redo after a crash.

**The big picture:** A correct rollback does not mean a safe start. A restored state can resume a run where the internal memory, rules, and outside actions never lived together at the same time [1]. If a system rolls back a file but not the sent email tied to it, the whole run breaks.

**By the numbers:**
- **5 failure modes:** Missing internal state, mixed-up saves, outside world mismatch, wild random replays, and lost outside actions [1].
- **3 live attacks:** Hacks on Hermes, Cline, and LangGraph let agents skip malware checks, forward private mail, and pay twice [1].
- **1,735 task runs:** Tested across 347 test paths using five different save systems [1].
- **99.5% accuracy:** The paper's test setup accurately spotted these broken runs [1].

<!-- tactical-insight -->
## How to Secure Agent Rollbacks

**The playbook:** Treat a rollback as a partial fix with strict limits, not a magic time machine. Four exact moves close the gap.

- **Map the safe zone:** Know exactly what a save restores. LangGraph saves graph state, Cline and Hermes save files, and E2B saves the whole sandbox [1]. Each tool leaves different parts outside the safe boundary.
- **Make outside actions safe to repeat:** Stop resumed runs from repeating lost outside actions. Use safe-to-repeat keys and an add-only log so a replay cannot charge a credit card twice [1][3].
- **Bind checks to the files:** Tie the scan result to a digital fingerprint (hash) of the exact workspace it checked [1]. A rollback that changes the files will then wipe the passing grade.
- **Stop random drift in replays:** Lock down random seeds, model versions, and tool versions. Log random inputs like timestamps so a restored run acts exactly the same way every time [1].

A setup called ACID-Agent uses Atomicity, Consistency, Isolation, Durability (ACID) rules to score 90.0 on tests. It beats a standard Claude Code setup (75.2) while using 60% fewer tokens [2]. Dropping its failed-step sandbox drops the score by 11.7% because bad data leaks into the next step [2]. 

<!-- nuanced-takeaway -->
## The Cost of Real Safety

**The catch:** Rollbacks are strictly needed, but assuming a perfect restore means a safe start will break your system. The paper shows hacker attacks, but a normal Operating System (OS) crash that re-runs a payment causes the exact same flaw without a bad actor. Building a safe boundary costs real time and code. You need action logs, file hashes, and fixed replays baked deep into the run cycle. Until you plan for these limits, rollbacks will keep bringing back states that never really existed.

<!-- tldr -->
- **The Big Shift:** Save-and-restore tools create a new risk for AI agents. A new study proves a perfect rollback can restore a mixed state where files, choices, and outside actions never lived together.
- **Why It Matters:** If a rollback blindly ties a passing grade to a file it never checked, agents can ship malware, forward private emails, or charge cards twice. This hurts any backend team running agents against live systems.
- **The Winning Moves:**
  - **Map the boundary:** Know if a save restores framework state, files, or a full sandbox to see your exposed parts.
  - **Make actions safe to repeat:** Use unique keys and an add-only log so a resumed run cannot double-charge a payment.
  - **Bind checks to files:** Hash the exact workspace a scan approved so changing the files voids the result.
  - **Force fixed replays:** Lock down random seeds and model versions while logging wild inputs to stop drift.
- **The Catch:** While the shown attacks are malicious, a normal system crash causes the exact same flaws. Teams must build deep fixes like action logs and file hashes instead of slapping them on later.

<!-- internal-links -->

## Sources
[1] "Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback" — arXiv:2608.29381 — https://arxiv.org/abs/2608.29381
[2] "Agentic Transaction: Towards ACID-Compliant Agent Systems" — arXiv:2608.13900 — https://arxiv.org/abs/2608.13900
[3] Diagrid, "Top 5 Mistakes Shipping AI Agents to Production in 2026" (Aug 31, 2026) — https://www.diagrid.io/infrastructure/top-5-mistakes-shipping-agents-production-2026

<!-- linkedin -->
I keep coming back to one thing in a new paper (arXiv:2608.29381): a perfect rollback can restore a mixed state, where files, choices and outside actions never actually lived together.

The bit that stuck with me is that none of the three working attacks - on Hermes, Cline and LangGraph - needed a hacked save file. Agents shipped a virus as clean code, forwarded private mail, and double-charged payments anyway.

My read: this isn't a case for dropping rollbacks. It's a case for treating the recovery zone as a design rule, and I'd want to know where each tool draws it - what sits inside the snapshot and what doesn't, whether outside actions are safe to repeat, whether a passing scan is bound to the exact files it saw, and whether random choices are locked down.

The number I keep circling: ACID-Agent scores 90.0 on tests versus 75.2 for a standard Claude Code setup, on 60% fewer tokens. I could be wrong, but that gap reads like the price of building the boundary properly.

What I'm watching next: whether the cheap save-and-restore tools say anything about their boundary at all. Safe execution is needed. I'm less sure it's the same thing as a clean rollback.

## Gate report
lead: PASS — Delivers the core malware bypass incident in sentence 1 using simple, everyday words and connected sentences.
tension: PASS — Uses standard signposts, frames the shift clearly, and includes a 4-bullet quantitative section with plain vocabulary.
tactical-insight: PASS — Practitioner moves are structured with clean bullets and bold lead-ins, explicitly expanding acronyms like ACID and replacing jargon with plain terms.
nuanced-takeaway: PASS — Honest limitation framed with "The catch:", explaining that normal crashes trigger the same flaws, written in accessible language.
tldr: PASS — Follows the strict 4-part schema using plain English, entirely avoiding dense corporate jargon.
