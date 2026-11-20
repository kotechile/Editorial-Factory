---
title: "Your Error Text Breaks the Repair: 45% vs 84%"
vertical: multi_agent_enterprise_fabric
kind: evergreen
persona: ai_architect
one_big_thing: "An agent at a failure point can only act through the tools it holds, so the repair step printed in a tool's error is a program the agent runs rather than advice it weighs: in 150 widely used MCP servers 949 of 3,001 error messages carry such a step, a terminal command in that slot leaves 45% of credential tasks recovered where the server's own login tool leaves 84%, and a bare wait leaves 6% where naming the call to repeat leaves 88%."
date: 2026-11-18
slug: your-error-text-breaks-the-repair
archetype: evergreen
evergreen: true
meta_title: "Your Error Text Breaks the Repair: 45% vs 84%"
meta_title_source: "derived_from_title"
meta_description: "Your error text breaks the repair it was written to prompt. Of 3,001 error messages found in 150 widely used servers speaking the Model Context Protocol…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-error-text-breaks-the-repair/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "MCP Error Text Breaks Agent Repair. Server rack with red error indicator in a dark server room, lone terminal dark beside it."
image_caption: "MCP Error Text Breaks Agent Repair: A next step the agent cannot run cuts credential recovery from 84% to 45%."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your error text breaks the repair it was written to prompt. Of 3,001 error messages found in 150 widely used servers speaking the Model Context Protocol (MCP), the open standard an agent uses to reach a tool, 949 tell the caller what to do next, and half of those steps need something the server cannot see about the caller [1]. Put a terminal command in that slot and 45% of expired-credential tasks recover; name the server's own login tool instead and 84% do [1]. The 39-point gap comes from a sentence no model was ever asked to weigh.

<!-- tldr -->
## At a glance
- **The shift:** An MCP tool's failure text is part of its contract, not developer notes.
- **The number:** 45% of credential tasks recover on a named command, 84% on a login tool.
- **The risk:** A step the agent cannot run kills a repair its own tools could make.

<!-- tension -->
## The wrong reader

Most MCP servers started as wrappers around a web interface built for software developers, and they kept its error strings word for word [1]. Those strings assume a reader who can open a terminal, change a setting or visit a page. A second reader now arrives who can do none of those things [1]. Credential errors show it: 62 of 67 steps ask for a terminal command, a setting change or a page. Rate limits show it too, where 20 of 30 messages say to wait and never name the call to repeat [1].

A failed call is the one moment when the model knows least, and the message is the only thing the fabric adds [1]. What the agents did with it is the part worth sitting with. They followed it in every model tested, even where the step could not be carried out at all [1]. The authors call this literal compliance: an agent that cannot run the named command gives up on a repair its own tools could make [1].

I went back to the model table three times before I believed the direction. Among the generative pre-trained transformer (GPT) models tested, the loss from an uncallable step grew from 18 points on the older one to 69 on the newest and largest [1]. A capability upgrade made the same sentence more destructive. Better instruction-following did not rescue the run; it carried the instruction out.

## By the numbers
- **949 error messages** told the caller to take a step, and half asked for something the server cannot see [1].
- **88% recovery on rate limits:** Once the message named the call to repeat, at about one extra tool call [1].
- **60 requests per hour:** GitHub's limit for an unauthenticated call [3].

<!-- tactical-insight -->
## Where the fix is written

The rewrite is smaller than the problem suggests. Name a tool instead of a command: the login tool in place of a terminal line took credential recovery from 45% to 84% [1]. Name the call to repeat: on a rate limit, that swap lifted recovery from 6% to 88% [1]. Where the server belongs to someone else, strip the step before the model reads it with a one-sentence prompt, which reached 82% on the same tasks [1].

The standard most teams reach for cannot carry this. Request for Comments (RFC) 9457, the Internet Engineering Task Force (IETF) rule for machine-readable web errors, fixes the error object at five parts: type, status, title, detail and instance [2]. None of the five is an allowed next action. The repair step has to be a part the gateway adds, which is [the same gap that leaves 63% of an agent's rules unmet at the call site](/your-agent-contract-gap-63-unmet/).

The teams closest to this have stopped asking a model to read a fault. They write one answer per failure class into the tool table, so the message names a call instead of describing a condition. That keeps the choice inside the fabric, where the list of tools is known. It leaves the model one job at the failure point, which is to make the named call. A message that only describes a condition hands that choice back to the reader, who has less to go on.

I read this as a schema change rather than a prompt fix. The error object needs a slot for the next action, and that slot has to be filled by the gateway that knows the tool list, not by the server that knows only its own condition.

<!-- nuanced-takeaway -->
## What the sentence cannot buy

The evidence has edges. It covers 150 servers and seven kinds of fault, graded by the Berkeley Function Calling Leaderboard (BFCL) state check, which asks whether the services ended in the right state rather than whether the reply sounded right [1]. A fault outside those classes, or a server that mislabels its own tools, can still point the agent at the wrong call [1].

Nor can a message settle authority. A step that names a tool says the tool exists; it does not say the caller may run it. That permission is a decision the fabric already owns through its own grant checks. Naming a call is the cheap half of the contract, and the half that survives a model change.

What I am watching is the upkeep. Every repair step is a claim about the tool list, and renaming a tool breaks a good message without anyone editing the text. The shape of the fix holds for years; the names inside it do not.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Agent Memory Poisoning" -> /agent-memory-poisoning-write-path/ [same site (aichieve.net); same category; topical overlap: prompt, text] Link "Agent Memory Poisoning" in the section where the article touches prompt, text. -->
<!-- internal-link hint: "Your Router Breaks 275 Rules" -> /your-router-breaks-275-constraints/ [same site (aichieve.net); same category; topical overlap: breaks, written] Link "Your Router Breaks 275 Rules" in the section where the article touches breaks, written. -->
<!-- internal-link hint: "Your Compaction Trap" -> /your-compaction-trap-87-forgeries-survive/ [same site (aichieve.net); same category; topical overlap: text] Link "Your Compaction Trap" in the section where the article touches text. -->
## Related reading

- [Agent Memory Poisoning](/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Your Router Breaks 275 Rules](/your-router-breaks-275-constraints/) — more on Autonomous & Agentic Workflows
- [Your Compaction Trap](/your-compaction-trap-87-forgeries-survive/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources
- [1] Xiaonan Xu et al., "MCP Error Messages Written for Developers Hurt the Most Capable Agents Most" (arXiv:2609.35381v2, 29 September 2026) — https://arxiv.org/html/2609.35381v2
- [2] M. Nottingham, E. Wilde, S. Dalal, "Problem Details for HTTP APIs" (RFC 9457, July 2023) — https://www.rfc-editor.org/rfc/rfc9457.html
- [3] GitHub, "Rate limits for the REST API" (retrieved 18 November 2026) — https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
