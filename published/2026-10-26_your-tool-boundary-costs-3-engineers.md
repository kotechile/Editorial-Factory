---
title: "Your Tool Boundary Costs 3 Engineers"
vertical: agentic_ai
persona: ai_architect
archetype: evergreen
evergreen: true
one_big_thing: "A service boundary is a purchase, not a convenience: Segment spent 3 full-time engineers keeping 140+ of them alive, a monolith-to-microservices case study bought its five boundaries with a 20% effort premium, so a boundary has to buy an independent scaling profile or an independent change cadence — and in an agent runtime the unearned ones bill the context window too."
date: 2026-10-26
slug: your-tool-boundary-costs-3-engineers
meta_title: "Your Tool Boundary Costs 3 Engineers"
meta_title_source: "derived_from_title"
meta_description: "Segment spent 3 full-time engineers just keeping its software alive. Then it folded more than 140 separate services into one, and shipped 46 improvements to…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-tool-boundary-costs-3-engineers/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "The Tool Boundary Tax. A modular mechanical assembly unlatching into separate components on a brushed steel surface."
image_caption: "The Tool Boundary Tax: Unearned service boundaries drain engineering time."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

Segment spent 3 full-time engineers just keeping its software alive. Then it folded more than 140 separate services into one, and shipped 46 improvements to shared code the next year against 32 before [1][2][3]. The gap between those two counts is what an unneeded boundary costs, and it is the same bill a team takes on when it splits the tool layer for an agent.

Your team faces the same call at a smaller scale. Splitting a program into separate services means each piece gets its own release process and its own pager. So an agent runtime wired to a dozen Model Context Protocol (MCP) servers raises a plain question: how many pieces of the tool layer get their own release, and what does each one have to buy? MCP is an open standard for handing an AI assistant a set of tools.

<!-- tension -->

## The big picture:

The same trade has been priced from both ends. The two readings disagree in a way that matters. One team pulled five business tasks out of a twelve-year-old system of 280K lines of code and ran them as separate services. Their maintenance backlog then grew on a slope 89.76% smaller than the old single system's [4][5]. The same paper records the bill: overall development cost rose by more than 20%, because a spread-out system costs more to build and run [4].

My read is that neither result proves the other wrong. Neither study asked whether small services are good. Both priced a split, one from the invoices and one from the interest on that mess.

Teams pick these cuts on two tests. When teams chose which part to pull out, the top test was whether it needed to scale on its own. That was named by 40 of 53 staff (75.5%). The top reason to split at all was easier upkeep and change, at 43 of 53 (81.1%) [6][7]. Scaling is a question about load. Upkeep is a question about time.

<!-- tactical-insight -->

## What I'd watch:

Four signals separate a split that earns its keep from one that only adds another release process. I look for them in every design review that crosses this desk.

- **Change cadence:** a piece that always ships with everything else is a library wearing a network hop. The bill for that hop is the on-call rota behind it. Segment's improvement count moved once a change to one shared library stopped needing 140+ releases [3].
- **Resource profile:** combined, Segment's outbound destinations scaled more easily. One large pool of workers soaked up spikes that the small, chatty services used to page on [1]. A split sold on its own scaling is a claim to test, not a starting point.
- **Discovery cost:** every MCP server adds a tool list the model has to find before it can call anything. Anthropic's own engineers put the saving from loading only what a task needs at 98.7%, in a fleet built from dozens of servers [9]. That is a vendor measuring its own set-up, so I read it as a direction rather than a test of your estate.
- **Where the seam lands:** most surveyed teams cut along a business job rather than the old wiring [7]. Our earlier note on [how many tools one agent can hold](/agent-tool-count-ceiling/) makes the same point from the other side, since a job-shaped seam usually fits inside one context window.

## By the numbers

- **$407,940 — a year of engineers:** three full-time staff at the 2025 median software wage of $135,980 each [8]. That is the wage line a needless split shows up on.
- **50.9% — one service at a time:** 27 of the 53 staff surveyed split work piece by piece rather than all at once [7]. It is the path that keeps a split easy to undo.
- **52.8% — seams cut by business job:** 28 of 53 teams chose the cut by what the service does for the business, not by how the old system was wired [7].
- **98.7% — the vendor's token cut:** Anthropic reports token use for the tool list falling from 150,000 to 2,000 when only the needed ones load. That is a claim about its own set-up rather than an outside test [9].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Your Tool Boundary Costs 3 Engineers</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">one service at a time</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="152" height="18" rx="4" fill="#818cf8"/>
  <text x="402" y="84" fill="#f1f5f9" font-size="13" font-weight="600">50.9%</text>
  <text x="456" y="84" fill="#64748b" font-size="11">([7])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">seams cut by business job</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="158" height="18" rx="4" fill="#818cf8"/>
  <text x="408" y="132" fill="#f1f5f9" font-size="13" font-weight="600">52.8%</text>
  <text x="462" y="132" fill="#64748b" font-size="11">([7])</text>
  <!-- Row 3 -->
  <text x="20" y="180" fill="#e2e8f0" font-size="13" font-weight="500">the vendor&#x27;s token cut</text>
  <rect x="240" y="166" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="166" width="296" height="18" rx="4" fill="#818cf8"/>
  <text x="546" y="180" fill="#f1f5f9" font-size="13" font-weight="600">98.7%</text>
  <text x="600" y="180" fill="#64748b" font-size="11">([9])</text>
</svg>

<!-- nuanced-takeaway -->

## The catch

The evidence is thinner than the trust in either camp, and three limits matter more than the two big results. The maintenance study tracks a single system, however well it was measured. One case with two teams, one language and one path of migration is a strong example of how it works and a weak guess at the size of the gain [4][5]. The survey covers 53 people, 41 of them working in Brazil, so it reports how one group works rather than a global rule of design [6][7].

Segment's move also cost something the post names plainly. The small services had been a way to fence off faults and ship on their own, and folding them together traded that fence for speed [1]. My read is that this is the honest shape of the call. You are picking which fault you can live with, not removing one.

Neither source gives a break-even count, and I would distrust any piece that supplied one. The number of splits follows from how many scales and speeds a team truly runs. That is why the same design can fit one company and be pure overhead at the next.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Answer Field First Costs 38.15 Points" -> /answer-field-first-costs-38-points/ [same site (aichieve.net); same category; topical overlap: costs, tool] Link "Answer Field First Costs 38.15 Points" in the section where the article touches costs, tool. -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> /durable-execution-not-a-transaction/ [same site (aichieve.net); same category; topical overlap: tool] Link "Durable Execution Is Not a Transaction" in the section where the article touches tool. -->
<!-- internal-link hint: "Long Context Is Not Memory" -> /agent-memory-tiering-l1-l4/ [same site (aichieve.net); same category; topical overlap: engineers] Link "Long Context Is Not Memory" in the section where the article touches engineers. -->
## Related reading

- [Answer Field First Costs 38.15 Points](/answer-field-first-costs-38-points/) — more on Autonomous & Agentic Workflows
- [Durable Execution Is Not a Transaction](/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
- [Long Context Is Not Memory](/agent-memory-tiering-l1-l4/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent runtimes are being split into fleets of MCP servers, which turns a tool list into a set of separate services with release processes and on-call duties. It is the same call product teams had to re-open.
- **Why It Matters:** A split that does not buy its own scale or its own speed of change is pure overhead. One case measured it at 3 full-time engineers, the other at a 20% cost rise.
- **What I'd Watch:** where the next split lands, and whether anyone prices it before the release processes appear.
  - **Change cadence:** a piece whose code always ships with another team's code is a library with a network hop.
  - **Resource profile:** whether the claimed need to scale is measured or assumed, since one large pool often soaks up the spikes.
  - **Discovery cost:** each new server adds tools the model must load before it can call anything.
- **The Catch:** the strongest numbers come from a single case study and a small survey, and folding services together buys speed with the fault fence you gave up.

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
