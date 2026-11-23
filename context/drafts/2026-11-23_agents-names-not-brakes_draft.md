---
title: Named, Not Stopped: Your Agent's Missing Brake
vertical: enterprise_ai_governance
kind: news
persona: enterprise_cai
one_big_thing: "The Linux Foundation gave AI agents verifiable names on November 10; Salt Security shipped a stop button thirteen days earlier, because only 17.5% of enterprises can halt a misbehaving agent. Identity shipped first; the brake is still optional."
date: 2026-11-23
slug: agents-names-not-brakes
synthesis: true
sources:
  - https://www.linuxfoundation.org/press/linux-foundation-welcomes-agent-name-service-to-bring-verifiable-identity-and-discovery-to-ai-agents
  - https://salt.security/blog/an-alert-doesnt-stop-an-attack-introducing-autonomous-defense
  - https://salt.security/press-releases/state-of-agentic-ai-and-api-security-2h-2026
---

<!-- lead -->
The tech industry just built AI agents a passport, but almost nobody built the brake. The Linux Foundation has named every AI agent that wants a name: its Agent Name Service, launched this month, lets anyone check an agent's identity over the internet's existing name system, Domain Name System (DNS) [1]. Thirteen days before that launch, Salt Security shipped its stop controls, because only 17.5% of firms can halt a rogue agent on their own [2]. That makes the missing piece plain: 82.5% of firms can now learn an agent's name, yet they still cannot stop it.

<!-- tldr -->
## At a glance
In one 26-day stretch, vendors set a standard for who an AI agent is. Their field data showed few firms can stop one. The trap for buyers is trusting the identity registry to fence the agent it names, because a verified name does not stop anything by itself.

<!-- tension -->
## Identity shipped first, brake shipped second
The order of arrival tells the story. On June 23, the Linux Foundation announced its plan for the Agent Name Service [1]. On October 28, Salt Security rolled out Autonomous Defense, controls that can cut off an agent's tool access [2]. The identity standard then formally launched at the KubeCon conference on November 10, backed by 11 organizations including Cisco, Cloudflare and Salesforce.

Why does the stop side lag? Naming an agent is a paperwork job. Stopping one is a wiring job. A registry only holds records. A stop control must reach the web application firewalls (WAFs) and application programming interfaces (APIs) that the agent touches [2]. Vendors can settle a naming format within weeks. Cutting off a rogue agent means rewiring gear they do not own. Salt's field data shows how thin the stop side is. Only 12.5% of its 383 respondents can trace a full agent path from start to end. Over 60% would need hours or days to rebuild what one agent did yesterday [3].

## By the numbers
- **Seven spec documents:** naming, publication, auditing and monitoring, with no stop control among them [1].
- **11 organizations:** the backers of the identity launch, from Cisco to Salesforce [1].
- **383 practitioners:** the survey base under Salt's 17.5% finding [2].

<!-- tactical-insight -->
## Where the brake lives
Salt's launch shows where its brake sits: outside the model, in the security gear a company already runs — WAFs, API gateways, guardrail policies [2]. Its own research shows why that placement matters: a guardrail spotted a hijacked agent and still could not stop its code from running. The identity camp watches the same gap from the other side. Earlier work said it plainly: the identity layer was never the breach control — [Agent Identity: The Wrong Layer](/agent-identity-missed-the-real-breach/).

Here is what I find hard to square. The chief information officer (CIO) who adopts the registry first owns a nameplate for every agent, yet no nameplate grounds an agent that turns rogue at machine speed. The fastest fix would be one published number: the share of firms that can verify an agent and also stop it on their own. No vendor reports that pair today.

<!-- nuanced-takeaway -->
## The catch
The honest reading cuts both ways. An identity standard thirteen days old has no install base. Eleven backers is intent, not deployment. The same youth applies to Salt's stop button, which works only on gear the customer already owns. And the headline share is my own math, not a published figure: 82.5% is just the flip side of Salt's 17.5%. So the defensible conclusion is narrower than the headline. Buy the fence and the name on the same purchase order, because each is worth little alone.

## Sources
- [1] The Linux Foundation, "Linux Foundation Welcomes Agent Name Service to Bring Verifiable Identity and Discovery to AI Agents", 2026-11-10 — https://www.linuxfoundation.org/press/linux-foundation-welcomes-agent-name-service-to-bring-verifiable-identity-and-discovery-to-ai-agents
- [2] Salt Security, "An Alert Doesn't Stop an Attack: Introducing Autonomous Defense", 2026-10-28 — https://salt.security/blog/an-alert-doesnt-stop-an-attack-introducing-autonomous-defense
- [3] Salt Security, "State of Agentic AI and API Security 2H 2026", 2026-10-13 — https://salt.security/press-releases/state-of-agentic-ai-and-api-security-2h-2026
