---
title: "Agent Memory Poisoning: Guard the Write, Not the Prompt"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "A persistent-memory agent's real attack surface is the memory write path, not the prompt: a guardrail sitting at the model never sees a poisoned memory that fires days later, so the control belongs at the store boundary — validate every write, scope it per user, and screen what the retrieval path promotes into trusted context."
date: 2026-10-07
slug: agent-memory-poisoning-write-path
archetype: evergreen
evergreen: true
---

<!-- lead -->
One plain repository file was enough to take over a coding agent's memory. Cisco's researchers looked at a shipping coding agent. The first 200 lines of its memory files were loaded straight into the system prompt [3]. So one poisoned write stayed live across every project, every session, and every reboot. Nobody had to break the model. They only had to write to its memory.

<!-- tension -->

## The big picture:

Memory makes an agent worth running. It is also the one part a prompt filter never inspects.

A filter at the model reads each input once. A memory write works in two steps. The agent stores text now. Later, in a new session, it reads that text back as trusted context.

The industry's own risk list named this in 2026. The Open Worldwide Application Security Project (OWASP) filed Memory and Context Poisoning as entry ASI06 of its Top 10 for Agentic Applications [5]. The pattern is easy to state. The content arrives once, and the system keeps trusting it.

The measured numbers are large. One study pushed a payload into the memory store of top agents about 98% of the time. That stored entry fired again later in about 60% of runs [1]. A second study hit over 95% injection and 70% attack success with plain user queries alone [2]. No special access was needed.

The first paper names the cause. The attacks work, it says, because of "the lack of security-focused memory governance" [1]. My read: that is a missing control at the storage layer, not a weak model.

This is not just a lab result. Microsoft watched it happen in the wild. In one 60-day window of email traffic, it found more than 50 memory-poisoning prompts, tied to 31 companies across 14 industries [4].

## By the numbers

- **98% — Memory injection rate:** One study planted a payload in the memory store of top agents in about 98% of trials, and the stored entry fired later in about 60% of them [1].
- **95% — Query-only attack:** A second study reached over 95% injection and 70% attack success with plain user queries alone, and no special access [2].
- **200 lines — Memory read as orders:** A shipping coding agent loaded the first 200 lines of its memory files straight into the system prompt, so one write became a trusted order [3].
- **50 prompts — Found in the wild:** Microsoft logged over 50 memory-poisoning prompts from 31 companies across 14 industries in 60 days [4].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that every fix in the sources sits at the store, not at the prompt. The study that measured the 98% rate also built a defense. It calls it Agentic Memory Sentry, and it has two parts: a policy for what may be saved, and a screen for what comes back out [1]. Both act on the memory layer. That is the layer a prompt filter cannot see.

The teams closest to this are moving in three ways. I'd watch which one sticks.

- **A checked write path:** Every memory save passes a check first. Injected orders, secrets, and edits to protected fields get blocked or set aside. The write is the moment trust is granted, so it is the cheapest place to say no.
- **A retrieval screen:** Content pulled back out of memory gets checked again before it enters the context window. This is the control that would have caught the coding-agent case above [3].
- **Per-user scope:** Memory keyed to one user stops a poisoned entry from spilling into other people's sessions. It shrinks the blast radius even when a write slips through.

So where will operators draw the line? On one view, memory is just another database. It gets a guarded write path, checks, and per-tenant scope. On the other, a team bolts on a memory feature, lets the model write to it freely, and ships a surface nobody tested.

<!-- nuanced-takeaway -->

## The catch

The headline rates come from lab tests, run under tight conditions. The second study says as much in its own framing [2]. Read them as a ceiling on how easy the attack is, not as the rate to expect on your own traffic.

Every defense costs something. A write check that is too strict throws away useful memory, which is a real failure even when it is a safe one. A retrieval screen adds delay to a path that runs on every turn.

The work is also young. The researchers who found the coding-agent flaw closed one path, and they say so. The wider question is still open: how many other tools still treat stored memory as trusted orders? [3]

My read is that the mechanism is the part that lasts. A record the agent re-reads as truth will keep being worth attacking. And it will keep being cheaper to guard at the write than to chase at the prompt. I could be wrong about where the line lands. But leaving the write path open and hoping the model behaves is not a design I would defend.

<!-- tldr -->

## At a glance

- **The Big Shift:** An agent's memory is now a named attack surface. A poisoned write is read back later as trusted context, so the flaw lives in the store, not in the prompt.
- **Why It Matters:** A prompt filter reads one input once. Memory is re-read on every later turn. That gap let labs hit about 98% injection, and let a live campaign reach 31 companies in 60 days.
- **What I'd Watch:** Whether teams guard the memory store the way they guard a database. The controls in the evidence all sit at the store:
  - **A checked write path:** A check on every memory save that blocks or sets aside injected content before it is stored.
  - **A retrieval screen:** A second check on content leaving memory, before it enters the context window.
  - **Per-user scope:** Memory keyed to one user, so a poisoned entry cannot spread into other sessions.
- **The Catch:** The attack rates come from lab tests, and every defense costs something. A strict write check discards useful memory, and a retrieval screen adds delay on every turn.

## Sources
[1] George Torres, Sharad Shrestha and Satyajayant Misra, "When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents" (arXiv:2607.06595, submitted 2026-07-06) — the GhostWriter attack (98% injection, ~60% activation) and the Agentic Memory Sentry defense (https://arxiv.org/abs/2607.06595)
[2] "Memory Poisoning Attack and Defense on Memory Based LLM-Agents" (arXiv:2601.05504) — the MINJA (Memory Injection Attack) query-only attack, over 95% injection and 70% attack success (https://arxiv.org/html/2601.05504v2)
[3] Idan Habler and Amy Chang, "Identifying and remediating a persistent memory compromise in Claude Code", Cisco Blogs, 2026-04-01 — the first 200 lines of memory loaded into the system prompt, persistence across sessions and reboots, and the v2.1.50 fix (https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code)
[4] Microsoft Defender Security Research Team, "Manipulating AI memory for profit: the rise of AI Recommendation Poisoning", Microsoft Security Blog, 2026-02-10 — over 50 prompts from 31 companies across 14 industries in 60 days (https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning)
[5] Idan Habler, "Memory Is a Feature. It Is Also an Attack Surface", OWASP GenAI Security Project, 2026-05-13 — the ASI06 Memory and Context Poisoning entry in the Top 10 for Agentic Applications (https://genai.owasp.org/2026/05/13/memory-is-a-feature-it-is-also-an-attack-surface)
