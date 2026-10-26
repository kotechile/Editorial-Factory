---
title: "Your Tool Boundary Costs 3 Engineers"
vertical: agentic_ai
persona: ai_architect
archetype: evergreen
evergreen: true
one_big_thing: "A service boundary is a purchase, not a convenience: Segment spent 3 full-time engineers keeping 140+ of them alive, a monolith-to-microservices case study bought its five boundaries with a 20% effort premium, so a boundary has to buy an independent scaling profile or an independent change cadence — and in an agent runtime the unearned ones bill the context window too."
date: 2026-10-26
slug: your-tool-boundary-costs-3-engineers
---

<!-- lead -->

Segment had 3 full-time engineers spending most of their time keeping its service estate alive, which is why the team folded more than 140 services into one and then shipped 46 shared-library fixes a year later against 32 before [1][2][3]. That is what an unneeded boundary costs, and it is now the call in front of your team, because an agent runtime wired to a dozen Model Context Protocol (MCP) servers is the same shape at smaller scale: how many pieces of the tool layer get their own deploy, and what each one has to buy.

<!-- tension -->

## The big picture:

The same trade has been priced from both ends, and the two readings disagree in a useful way.

One team went the other way. They pulled five business processes out of a twelve-year-old system of 280K lines of code and ran them as separate services. After that, their technical debt grew on a slope 89.76% smaller than the old monolith's [4][5]. The same paper records the bill: their overall development cost rose by more than 20%, because a spread-out system costs more to build and run [4].

My read is that neither result refutes the other, which is why the argument keeps starting over around a question that was never the right one. Neither study asked whether microservices are good. Both priced a boundary, one from the invoices and one from the interest on the debt.

What engineers actually pick for is narrower than the debate suggests. When they chose which part to cut out, the top test was whether it needed to scale on its own, named by 40 of 53 (75.5%). The top reason to split at all was easier upkeep and change, at 43 of 53 (81.1%) [6][7]. Scaling is an argument about load. Upkeep is an argument about time.

<!-- tactical-insight -->

## What I'd watch:

Four signals tell a boundary that earns its keep from one that only adds a deploy pipeline, and I look for them in every architecture review that crosses this desk.

- **Change cadence:** a piece that ships in lockstep with everything else is a library wearing a network hop, and the bill for that hop is the on-call rota behind it. Segment's fix rate moved once a shared-library change stopped needing 140+ deploys [3].
- **A resource profile that truly conflicts:** combined, Segment's endpoints scaled more easily, because one large pool of workers soaked up spikes that the small, chatty services used to page on [1]. A boundary sold on "we need to scale it on its own" is a claim to test, not a starting point.
- **Discovery cost:** every MCP server adds tool definitions the model has to find before it can call anything. Anthropic's own engineers report that loading only the definitions a task needs cut token use from 150,000 to 2,000, a 98.7% saving, in a fleet built from dozens of servers [9]. That number is a vendor measuring its own set-up, so read it as a direction rather than a test of your estate.
- **Where the seam lands:** most surveyed teams cut along a business job, at 28 of 53 (52.8%), rather than along how the old system was wired [7]. Our earlier note on [how many tools one agent can hold](/agent-tool-count-ceiling/) makes the same point from the other side, since a job-shaped seam usually fits inside one context window.

## By the numbers

- **$407,940 — a year of engineers:** three full-time engineers at the 2025 median software-developer wage of $135,980 each [8], which is the wage line an unneeded boundary shows up on.
- **50.9% — one service at a time:** 27 of the 53 surveyed engineers split work piece by piece rather than all at once [7], the path that keeps a split easy to undo.
- **52.8% — seams cut by business job:** 28 of 53 teams chose the cut by what the service does for the business, not by how the old system was wired [7].
- **98.7% — the vendor's token cut:** Anthropic reports 150,000 tokens of tool definitions falling to 2,000 when only the needed ones load, a claim about its own pattern rather than an outside test [9].

<!-- nuanced-takeaway -->

## The catch

The evidence is thinner than the confidence in either camp, and three limits matter more than the two headline results.

The debt study is one system, however well it was measured. A single case with two teams, one language and one path of migration is a strong example of the mechanism and a weak estimate of the size of the gain [4][5]. The survey is a sample of 53 people, 41 of them working in Brazil, so it reports how one group of engineers works rather than a global law of design [6][7].

Segment's move also cost them something the post names plainly. The small services had been a way to fence off failures and ship on their own, and folding them together traded that fence for speed [1]. My read is that this is the honest shape of the call: you are picking which failure you can live with, not removing one.

Neither source gives a break-even count, and I would distrust any piece that supplied one. The number of boundaries follows from how many truly separate scales and speeds a team has, which is why the same design can fit one company and be pure overhead at the next.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent runtimes are being split into fleets of MCP servers, which turns a tool list into a set of service boundaries with deploy pipelines and on-call duties, the same call product teams had to re-open.
- **Why It Matters:** A boundary that does not buy a separate scale or a separate speed of change is pure overhead, and it was measured at 3 full-time engineers in one case and at a 20% cost rise in the other.
- **What I'd Watch:** where the next split lands, and whether anyone prices it before the deploy pipelines appear.
  - **Change cadence:** a boundary whose code always ships with another team's code is a library with a network hop.
  - **Resource profile:** whether the claimed need to scale is measured or assumed, since one large pool often soaks up the spikes.
  - **Discovery cost:** each new server adds definitions the model must load before it can call anything.
- **The Catch:** the strongest numbers come from a single case study and a small survey, and folding services together buys speed with the failure fence you gave up.

## Sources
[1] Segment Engineering, "Goodbye Microservices: From 100s of problem children to 1 superstar," Alexandra Noonan, 10 July 2018. https://segment.com/blog/goodbye-microservices/
[2] Same post, on-call and velocity sections. https://segment.com/blog/goodbye-microservices/
[3] Same post, shared-library improvement count. https://segment.com/blog/goodbye-microservices/
[4] Lenarduzzi, Saarimäki and Taibi, "Does Migrating a Monolithic System to Microservices Decrease the Technical Debt?", arXiv:1902.06282v3, 4 July 2020. https://arxiv.org/html/1902.06282v3
[5] Same paper, case description and scaling section. https://arxiv.org/html/1902.06282v3
[6] Nogueira, Felizardo, Amaral et al., "Insights on Microservice Architecture Through the Eyes of Industry Practitioners," arXiv:2408.10434v1, 19 August 2024. https://arxiv.org/html/2408.10434v1
[7] Same paper, extraction criteria and migration process. https://arxiv.org/html/2408.10434v1
[8] O*NET OnLine, Software Developers (15-1252.00), 2025 median wages. https://www.onetonline.org/link/summary/15-1252.00
[9] Anthropic Engineering, "Code execution with MCP: Building more efficient agents," 4 November 2025. https://www.anthropic.com/engineering/code-execution-with-mcp
