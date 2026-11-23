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
The industry just built AI agents a passport and left the brake as an option. On November 10, the Linux Foundation launched the Agent Name Service (ANS), an open standard that lets any AI agent carry a verifiable identity over the internet's existing name system, the Domain Name System (DNS) [1]. Thirteen days earlier, Salt Security had shipped its stop controls, and its survey explains the hurry: only 17.5% of firms can automatically halt an agent that goes wrong [2]. The other 82.5% — my arithmetic, the flip side of Salt's own figure — can now learn a rogue agent's name and still cannot stop it.

<!-- tldr -->
## At a glance
Over 26 days, the industry standardized what an AI agent is named and, separately, how one gets stopped. This piece concerns security buyers running AI agents. The finding: the identity standard's specification contains no stop control, so a verified name fences nothing.

<!-- tension -->
## The big picture: a name in weeks, a brake in someone else's rack

The timeline lands in one order. On June 23, the Linux Foundation announced its intent to build the Agent Name Service [1]. On October 28, Salt Security rolled out Autonomous Defense, controls that can cut off an agent's tool access [2]. On November 10, at the KubeCon conference, the identity standard formally launched, backed by 11 organizations including Cisco, Cloudflare and Salesforce [1].

The order is not an accident, and the specification shows why. The complete ANS standard runs to seven documents, covering domain-anchored naming, registration and versioning, DNS publication, public log auditing, integrity monitoring, and agent-to-agent authentication [1]. Read that list again. Naming, publishing, auditing, watching. Not one of the seven documents is an authorization or containment control. I counted the document titles twice before accepting that the standard whose job is to know every agent has no document whose job is to stop one.

The gap has a mechanical reason. Naming an agent is a paperwork job: a registry holds records, and a consortium can settle a record format in months. Stopping an agent is a wiring job. A stop control has to reach the web application firewalls (WAFs), the application programming interface (API) gateways and the guardrail policies on gear the standard's authors do not own [2]. That is why the two halves shipped separately, thirteen days apart, from different organizations.

Salt's field data measures how thin the wiring side is. The company surveyed 383 security practitioners for its State of Agentic AI and API Security report, and the results describe firms that can see their agents but not restrain them [3].

## By the numbers
- Only 12.5% of the 383 practitioners surveyed can trace a full agent path from instruction to outcome [3].
- More than 60% would need hours or days of manual work to rebuild what one agent did the previous day [3].
- 49.8% reported a confirmed or suspected case of an agent taking an unintended action [2].

<!-- tactical-insight -->
## What I'd watch: the number nobody publishes

Salt's launch shows where the brake has to live: outside the model, in the security equipment a company already runs. Its Autonomous Defense workflows revoke agent and Model Context Protocol (MCP) tool access, push blocking rules to WAFs and API gateways, update guardrail policies and restore posture settings [2]. That placement is honest about the problem — a stop control is only as good as the gear it can reach — and it is also the limit. The brake works on what the customer already owns.

The identity camp is watching the same gap from the other side of it. The ANS backers are building the layer that answers "who is this agent," and our earlier reporting argued that this identity layer was never the breach control — the breach control is what happens after the answer arrives ([Agent Identity: The Wrong Layer](/agent-identity-missed-the-real-breach/)).

What I am watching next is a number no vendor reports today: the share of firms that can verify an agent's identity and also stop it without human help. Salt publishes the stop share alone, 17.5%. The Linux Foundation publishes adoption intent alone, 11 organizations. Neither publishes the pair, and the pair is the only figure that would tell a buyer whether the two launches are converging or just parallel.

<!-- nuanced-takeaway -->
## The catch

Both halves are younger than a quarter. An identity standard launched on November 10 has no install base worth counting, and 11 backers is intent rather than deployment [1]. Salt's stop button is two weeks older and inherits a different constraint: it can only act through the firewalls and gateways the customer already has [2]. The 82.5% in the headline is not Salt's published number either — it is the complement of Salt's 17.5%, and it should be read as arithmetic, not survey findings.

My reading, held loosely: the narrow conclusion is the defensible one. The name and the brake are worth little apart, because a verified identity with no containment is a witness and a containment control with no identity is a tripwire. The buyer who needs both this year should put them on the same purchase order, and should ask any vendor claiming otherwise for the one number that would settle it — how many agents you can name, and how many you can stop.

## Sources
- [1] The Linux Foundation, "Linux Foundation Welcomes Agent Name Service to Bring Verifiable Identity and Discovery to AI Agents", 2026-11-10 — https://www.linuxfoundation.org/press/linux-foundation-welcomes-agent-name-service-to-bring-verifiable-identity-and-discovery-to-ai-agents
- [2] Salt Security, "An Alert Doesn't Stop an Attack: Introducing Autonomous Defense", 2026-10-28 — https://salt.security/blog/an-alert-doesnt-stop-an-attack-introducing-autonomous-defense
- [3] Salt Security, "State of Agentic AI and API Security 2H 2026", 2026-10-13 — https://salt.security/press-releases/state-of-agentic-ai-and-api-security-2h-2026
