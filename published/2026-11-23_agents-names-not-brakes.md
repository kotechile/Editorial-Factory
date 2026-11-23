---
title: "Your Rogue Agent: 82.5% Can't Stop It"
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
meta_title: "Your Rogue Agent: 82.5% Can't Stop It"
meta_title_source: "derived_from_title"
meta_description: "The industry just built AI agents a passport, but left the brake as an option. The Linux Foundation has named every AI agent that wants a name: its Agent…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/agents-names-not-brakes/featured.jpg"
image_style: "paper_collage"
image_model: "nanobanana"
image_alt: "AI Agents Got Names, Not Brakes. Cut-paper passport standing beside a flat emergency-stop button with a torn, disconnected cable on a dark"
image_caption: "AI Agents Got Names, Not Brakes: Only 17.5% of firms can halt a rogue agent — identity shipped first, the brake didn't."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The industry just built AI agents a passport, but left the brake as an option. The Linux Foundation has named every AI agent that wants a name: its Agent Name Service (ANS) gives an agent a verifiable identity over the internet's existing name system, the Domain Name System (DNS) [1]. Thirteen days before that launch, Salt Security shipped its stop controls, because its survey shows only 17.5% of firms can halt a rogue agent on their own [2]. The other 82.5% — my math, the flip side of Salt's figure — can learn an agent's name but cannot be sure it gets stopped. The missing half is not a name. It is a stop button.

<!-- tldr -->
## At a glance
Over 26 days, the industry set a standard for naming AI agents and, apart from it, a tool for stopping them. This piece is for security buyers who run AI agents. The finding: the identity standard's own papers contain no stop control, so a verified name fences nothing.

<!-- tension -->
## The Name Shipped, the Brake Lagged

The order of arrival tells the story. On June 23, the Linux Foundation announced its plan for the Agent Name Service [1]. On October 28, Salt Security rolled out Autonomous Defense, controls that can cut off an agent's tool access [2]. On November 10, at the KubeCon conference, the identity standard formally launched, backed by 11 groups including Cisco, Cloudflare and Salesforce [1].

What I keep circling is the order of those dates. It is not an accident, and the spec shows why. The full ANS standard runs to seven documents: naming, registration, DNS publication, public log auditing, integrity monitoring, and agent-to-agent sign-in [1]. Read that list twice. Not one of the seven documents is an authorization or containment control. The standard built to know every agent has no part built to stop one.

The gap has a mechanical reason. Naming an agent is a paperwork job: a registry holds records, and a consortium can settle a record format in months. Stopping an agent is a wiring job. A stop control has to reach the web application firewalls (WAFs), the application programming interface (API) gateways and the guardrail policies on gear the standard's authors do not own [2]. That is why the two halves shipped thirteen days apart, from two different camps.

Salt's field data measures how thin the wiring side is. The firm surveyed 383 security practitioners for its State of Agentic AI and API Security report, and the answers describe firms that can see their agents but not hold them back [3].

## By the numbers
- Only 12.5% of the 383 practitioners surveyed can trace a full agent path from instruction to outcome [3].
- More than 60% would need hours or days of manual work to rebuild what one agent did the previous day [3].
- 49.8% reported an agent taking an action nobody intended or authorized [2].

<!-- tactical-insight -->
## The number nobody publishes

Salt's launch shows where the brake has to live: outside the model, in the security gear a company already runs. Its Autonomous Defense workflows revoke agent and Model Context Protocol (MCP) tool access, push blocking rules to WAFs and API gateways, and restore guardrail settings [2]. That placement is honest about the problem, and it is also the limit. The brake works only on gear the customer already owns.

The identity camp watches the same gap from the other side. The ANS backers build the layer that answers "who is this agent," and our earlier work argued that this layer was never the breach control — what happens after the answer arrives is ([Agent Identity: The Wrong Layer](/agent-identity-missed-the-real-breach/)).

What I am watching next is a number no vendor reports today: the share of firms that can verify an agent's identity and also stop it without human help. Salt publishes the stop share alone, 17.5%. The Linux Foundation publishes adoption intent alone, 11 groups. Neither publishes the pair, and the pair is the only figure that would tell a buyer whether the two launches are meeting up or just running side by side.

<!-- nuanced-takeaway -->
## The catch

Both halves are younger than a quarter. An identity standard that launched only this month has no install base worth counting, and 11 backers is intent, not a live fleet [1]. Salt's stop button is two weeks older and inherits a different limit: it can act only through the firewalls and gateways the customer already has [2]. The 82.5% in the headline is not Salt's published number either — it is the flip side of Salt's 17.5%, and it should be read as arithmetic, not survey data.

My reading: the narrow conclusion is the defensible one. The name and the brake are worth little apart, because a verified identity with no containment can only watch, and a stop control with no identity swings blind. The buyer who needs both the name and the brake now should put them on one purchase order, and should ask any vendor who claims otherwise for the one number that would settle it — how many agents you can name, and how many you can stop.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Kill Switch Misses Half Your Agents" -> /kill-switch-misses-half-your-agents/ [same site (aichieve.net); same category; topical overlap: agents, built] Link "Kill Switch Misses Half Your Agents" in the section where the article touches agents, built. -->
<!-- internal-link hint: "Agent Identity: The Wrong Layer" -> /agent-identity-missed-the-real-breach/ [same site (aichieve.net); same category; topical overlap: agents] Link "Agent Identity: The Wrong Layer" in the section where the article touches agents. -->
<!-- internal-link hint: "An Agent's Logs Aren't Evidence" -> /agent-audit-trail-not-evidence/ [same site (aichieve.net); same category; topical overlap: agent's] Link "An Agent's Logs Aren't Evidence" in the section where the article touches agent's. -->
## Related reading

- [Kill Switch Misses Half Your Agents](/kill-switch-misses-half-your-agents/) — more on Mental Models & Strategy
- [Agent Identity: The Wrong Layer](/agent-identity-missed-the-real-breach/) — more on Mental Models & Strategy
- [An Agent's Logs Aren't Evidence](/agent-audit-trail-not-evidence/) — more on Mental Models & Strategy
<!-- internal-links:end -->

## Sources
- [1] The Linux Foundation, "Linux Foundation Welcomes Agent Name Service to Bring Verifiable Identity and Discovery to AI Agents", 2026-11-10 — https://www.linuxfoundation.org/press/linux-foundation-welcomes-agent-name-service-to-bring-verifiable-identity-and-discovery-to-ai-agents
- [2] Salt Security, "An Alert Doesn't Stop an Attack: Introducing Autonomous Defense", 2026-10-28 — https://salt.security/blog/an-alert-doesnt-stop-an-attack-introducing-autonomous-defense
- [3] Salt Security, "State of Agentic AI and API Security 2H 2026", 2026-10-13 — https://salt.security/press-releases/state-of-agentic-ai-and-api-security-2h-2026
