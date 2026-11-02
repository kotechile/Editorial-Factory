---
title: "Your Gateway's 104-Minute Trap"
vertical: enterprise_ai_governance
kind: news
persona: enterprise_cai
one_big_thing: "Federal guidance now tells firms to run every agent call through one watched gateway, which puts both the watching and the model keys in a single box — and five days after that guidance landed, the most widely used open-source gateway shipped a booby-trapped build that read the keys the box exists to hold, so how the gateway was built is now a governance question, not a buying detail."
date: 2026-11-02
slug: your-gateway-was-malicious-for-104-minutes
synthesis: true
sources:
  - https://www.nist.gov/document/keypracticesforincidentreadinessandresponseinsuperintelligence-trainingandevaluation
  - https://docs.litellm.ai/blog/security-incident-oct-21-2026
meta_title: "Your Gateway's 104-Minute Trap"
meta_title_source: "derived_from_title"
meta_description: "For 104 minutes on 21 October, the Python Package Index served a booby-trapped build of LiteLLM, the open-source gateway many firms place between agents and…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-gateway-was-malicious-for-104-minutes/featured.jpg"
image_style: "paper_collage"
image_model: "nanobanana"
image_alt: "Cut-paper server rack panel with a key turned in its keyhole, beside a torn paper lens disc on a steel table."
image_caption: "LiteLLM's 104-Minute Trap: Model keys sat inside a poisoned build for 104 minutes."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
For 104 minutes on 21 October, the Python Package Index served a booby-trapped build of LiteLLM, the open-source gateway many firms place between agents and model makers. Anyone who pulled it got a trap: code that read the model keys the gateway holds [1]. Five days earlier, the National Institute of Standards and Technology (NIST), the National Security Agency (NSA), and the Cybersecurity and Infrastructure Security Agency (CISA) told firms to route agent network access through one monitored gateway [2]. Neither paper mentions the other. Read side by side, they describe a control that puts the watching you want and the keys a thief wants in one place.

LiteLLM is not a niche tool. Datadog puts it at about 23 million downloads a week, and the bad build tried to read the model keys the proxy stores so it can call providers for a customer [3][4]. LiteLLM's own report says the release went out through three engineers' GitHub accounts, most likely by way of stolen command-line tokens, and that the files were built from a lookalike copy of the project rather than the real one [1]. The source tag on GitHub was clean. The build was not. That gap is the leak: code that ran on every machine which pulled the package, in a place where the keys to every model sit.

<!-- tension -->

## The big picture:

The federal paper is voluntary, and it aims at labs that train or test very able agents on long tasks, not at a firm running a dozen workflow bots [2].

Its network rule still fits any buyer, because it is the one line a small team can act on this week: keep agent access to a strict allowlist, and send what is left through a gate you watch [2]. That is the design most governance teams have been building toward. The LiteLLM case is the first hard test of it.

What I keep circling is the trade inside that rule. A gateway earns its place by taking every model call, so it holds the keys for every model in the estate, and it is the one process that can see each tool call an agent makes. One box holds both the view and the keys. That is why the control works, and why one bad build reached 23 million weekly installs [3].

The paper covers the view. It says nothing about how the box itself was built, who could rebuild it, or what stops a hijacked build from arriving as a normal update. A line about supply chains sits in its opening list of general habits, but no numbered practice asks an operator to check the build of the path it watches through [2].

The evidence rule has the same blind spot. Practice 3.3 says agents must not be able to reach the watch process or its logs, and practice 5.3 asks for logs that cannot be quietly changed, with reliable timestamps, full enough to rebuild what an agent did, which tools it called and why a control let it [2]. Both are sound. Neither survives the LiteLLM payload, which ran as soon as Python started in a bad environment, whether or not anyone imported the package [4]. A log written by a process that was already taken at startup is not evidence. It is a record kept by the intruder.

That is the part I cannot close with the paper as written.

## By the numbers

- **104 minutes — Python index window:** LiteLLM 1.107.0 sat on the Python Package Index from 11:39 to 13:23 coordinated universal time (UTC) on 21 October, carrying a key stealer and a loader for remote code [1].
- **23 million — weekly downloads:** Datadog's count for the proxy, which is why a two-hour window mattered [3].
- **154 minutes — container tag window:** the release stayed live on the `latest`, `main-latest`, and `main-stable` image tags from 11:46 to 14:20 UTC, so a cluster pulling a moving image label stayed open longer than a laptop running pip [1].
- **Ten practices, five stages — paper scope:** the federal paper sets ten voluntary practices across preparing, spotting, responding, recovering and reporting, and none of them names the build record of the gateway itself [2].

<!-- tactical-insight -->

## What I'd watch:

- **A fix list, not a patch:** LiteLLM's own advice starts with pinning version 1.106.2 and deleting the dropped files by hand, because removing the package folder does not remove them [1]. Microsoft's write-up adds one incident response rule: do not start Python inside a suspect environment, since that runs the payload again [4]. No vulnerability number was issued, because a bad build is not a software flaw [5].
- **The rebuild line:** the project revoked the tokens involved, removed all but one user from its GitHub group, and cut the trusted links between the public store and the code host [1]. That repair tells me the control that failed was identity on the build system, not identity on the agent.
- **Who was spared:** buyers on the private enterprise release were not affected, because they pull from a separate store [1]. The largest estates sat behind the paid line, while self-hosted teams on the open-source proxy took the hit.
- **The missing clock:** reporting is practice 9, and the ten practices name a duty to notify without naming a period for keeping the records that would make a notice true [2]. When a case like this lands, the retention rule in the reader's own book decides what can be rebuilt afterwards. That is a separate call from the gateway purchase, and [what an agent's logs can actually prove](/agent-audit-trail-not-evidence/) is where it starts.

<!-- nuanced-takeaway -->

## The catch

The strongest objection is that this is one vendor's release failure, and it does not follow that a gateway is the wrong design. My read: that objection is right about the design and wrong about the risk. A gateway is still the only place where every tool call can be seen before it runs, and the option of each team holding its own model keys spreads the same secrets over a wider surface with less to watch. The earlier argument that [the tool surface is a release surface](/your-tool-surface-is-a-release-surface/) still holds. This case moves that concern one layer down, to the binary itself.

Two limits are worth carrying. The paper is voluntary and was written for frontier training runs — long, expensive tests of very able models — so treating it as a compliance bar overstates what it is; a bank that borrows practice 1.5 is borrowing a habit, not obeying a law. And the paid line held: the private store was unaffected, so the case fell hardest on teams that picked the open-source route because they wanted to read the code. They could read the source and still not see the build.

What I cannot settle from these two papers is whether a watched gateway can ever be checked by the team that installs it, given that the build line, the package index and the image tags are three trust points, each with its own keys. The paper treats the gateway as a given. The case treats it as a supply chain. Until a practice names the second thing, the gateway's own build process is the part of an AI governance plan that no governance paper covers.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "OpenAI just made the agent loop a commodity" -> /openai-just-made-the-agent-loop-a-commodity/ [same site (aichieve.net); topical overlap: agents, build, minutes, model] Link "OpenAI just made the agent loop a commodity" in the section where the article touches agents, build, minutes. -->
<!-- internal-link hint: "Agent Identity: The Wrong Layer" -> /agent-identity-missed-the-real-breach/ [same site (aichieve.net); same category; topical overlap: agents, october] Link "Agent Identity: The Wrong Layer" in the section where the article touches agents, october. -->
<!-- internal-link hint: "Kill Switch Misses Half Your Agents" -> /kill-switch-misses-half-your-agents/ [same site (aichieve.net); same category; topical overlap: agents, firms] Link "Kill Switch Misses Half Your Agents" in the section where the article touches agents, firms. -->
## Related reading

- [OpenAI just made the agent loop a commodity](/openai-just-made-the-agent-loop-a-commodity/)
- [Agent Identity: The Wrong Layer](/agent-identity-missed-the-real-breach/) — more on Mental Models & Strategy
- [Kill Switch Misses Half Your Agents](/kill-switch-misses-half-your-agents/) — more on Mental Models & Strategy
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

**The shift:** Guidance now sends every agent call through one watched gateway, and that gateway's own release line was what got hijacked.
**The number:** 104 minutes on the Python index, at about 23 million weekly downloads.
**The risk:** The box trusted to watch the agents holds every model key, and no practice covers how it was built.

## Sources

[1] LiteLLM, "Contained: Oct 21, 2026 LiteLLM release v1.107.0 Compromised" — https://docs.litellm.ai/blog/security-incident-oct-21-2026
[2] NIST CAISSI, NSA SISC and CISA, "Key Practices for Incident Readiness and Response in Super Intelligence Training and Evaluation", PP-26-4396, October 2026 — https://www.nist.gov/document/keypracticesforincidentreadinessandresponseinsuperintelligence-trainingandevaluation
[3] Datadog Security Labs, analysis of the LiteLLM 1.107.0 compromise, 21 October 2026 — https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker
[4] Microsoft Security Blog, "Inside the LiteLLM 1.107.0 supply chain compromise: Credential theft through Python startup hooks", 23 October 2026 — https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks
[5] BerriAI, "[SECURITY] litellm 1.107.0 compromised", issue 47826, 21 October 2026 — https://github.com/BerriAI/litellm/issues/47826
