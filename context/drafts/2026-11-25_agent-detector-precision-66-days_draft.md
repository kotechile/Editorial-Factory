---
title: 91% Precision, 66 Days Late: Agent Failures Nobody Sees
vertical: agentic_resilience_failure
kind: news
persona: infra_engineer
one_big_thing: "Static agent-failure detection just hit 91% precision on the bugs that file issues — while the median real agent incident waits 66 days for anyone to disclose it. The detectors are aimed at the wrong half of the failure surface."
date: 2026-11-25
slug: agent-detector-precision-66-days
synthesis: true
sources:
  - https://www.manifold.security/blog/how-long-ai-agent-incidents-take-to-come-to-light
  - https://arxiv.org/abs/2611.28469
---

<!-- lead -->
The tools that catch agent breaks just got sharper — at the wrong misses. Apsis, a new code checker, flags broken agent task chains before any run. It scores 91% precision — few false alarms [2]. But the same month put a colder number beside it, because the median real agent incident waits 66 days before anyone speaks up [1]. So the tools advance fastest on breaks that already announce themselves. The breaks that define the risk stay unseen.

<!-- tldr -->
## At a glance
Infra teams gained pre-run checkers and after-the-fact tracers this month, all measured on misses that leave logs. The Agent Incident Ledger shows the costliest failures hide from the running team for a median of 66 days. Which half you watch first is the real decision.

<!-- tension -->
## Trained on the filed bugs
The two records arrived eleven days apart, and they read the same world from opposite ends. On 10 Nov, the Agent Incident Ledger — a kept dataset of agents that went wrong in public — gave its snapshot. It put the median at 66 days from an agent's first action to going public [1]. A second median said only 13 days pass from the moment the handler finds out. Most of the delay sits before anyone who owns the system knows.

Then Apsis shipped its checker on 21 Nov. It reads task-chain code offline, spots clashing writes and out-of-order steps, and scores 84% recall — it misses few bugs [2]. The reading happens before anything runs, so the cost of a miss is zero. The part I keep circling: what feeds each number. Apsis learned Apsis learned from 861 issue reports filed across 13 open-source agent toolkits. Its benchmark holds 135 buggy task chains — misses a human noticed and wrote up [2]. The Ledger's slow cases take the opposite shape. Anthropic's July review of 141,006 runs missed one early Opus 4.6 case. Only a later search across about 481 million transcripts found it. One OpenAI run went 215 days before anyone caught it [1]. Tools train on misses that produce a bug report, but the slow ones produce no report at all. Nobody scores a checker on runs no one reads. That is why precision improves while catching lag does not.

## By the numbers
- **66 days:** The median an agent case takes from first action to going public, as of the ledger's own 2026-11-10 count [1].
- **481 million:** Transcripts a later search swept after a 141,006-run review missed the case [1].
- **91% precision:** What that code checker scores on a benchmark built from filed issues [2].

<!-- tactical-insight -->
## Where this bites
What I find telling is who notices first. In 21 of 66 ledger incidents, someone outside the running team saw the problem first: outside researchers, hit third parties, or a package registry that got flooded [1]. The Ledger's advice follows from its own data: keep agent actions in a record the agent cannot edit, check it by machine while the run is live, alert on writes to public systems, and give agent alerts a path that pages a human. In the Hugging Face case, the signals were seen in May and June — and never passed on [1].

The visible record carries the same hole. OpenAI's own status page closed a critical event with two brief notes and no cause. New Workspace Agent runs had been unable to start for 9 hours 42 minutes [4]. Anthropic's 13 Nov double event ran 4 hours 29 minutes across claude.ai, Claude Code, the Claude API (its programming interface) and Managed Agents. Some scheduled tasks were skipped or ran late [5]. Even observed breaks arrive without a cause on file. Teams that build trace keeping on purpose — what is captured, where, how long it lives — are the only ones who can search the slow class later. That is an argument from the record, not a tooling bet [see related reading](/agent-audit-trail-not-evidence/).

<!-- nuanced-takeaway -->
## The catch
I hold this thesis with one caveat. The benchmarks measure catch rate on bugs somebody already filed, so 91% precision is a number about the visible few — and its authors do not claim otherwise. Tracing a failed run afterwards advances on the same set. RecordRoute names the actor and the earliest decisive step at 86% exact-step accuracy, on traces that exist to read [6]. The floor problem stays unsolved. An outage closed with no cause on file gives the next diagnosis nothing to work from. Better math on top of silence is still silence. What I find hard to square is that the cheapest lever — a trace that outlives the run — has no precision metric at all. The people who build checkers never see the runs that hid for 66 days.

## Sources
- [1] Bastien Eymery / Manifold Security, "How Long Do AI Agent Incidents Take to Come to Light?", 2026-11-10 — https://www.manifold.security/blog/how-long-ai-agent-incidents-take-to-come-to-light
- [2] arXiv, "Automated Safety Analysis for Agentic Workflows (Apsis)", 2026-11-21 — https://arxiv.org/abs/2611.28469
- [3] OpenAI, status history record, 2026-11-12 — https://status.openai.com/history.rss
- [4] HostTracker, "OpenAI API outage on November 11, 2026: Unable to start new Workspace Agent runs" (mirror of OpenAI's official timeline), 2026-11-12 — https://www.host-tracker.com/en/is-openai-down/incidents/2026-11-11-2250
- [5] Maxenius, "Claude Outage, 13 Nov 2026: Why API Builds Kept Running", 2026-11-14 — https://www.maxenius.com/blog/claude-outage-api-vs-app
- [6] arXiv, "RecordRoute: Auditing Agent Failures with Localization-Guided Diagnosis", 2026-11-24 — https://arxiv.org/abs/2611.33022
