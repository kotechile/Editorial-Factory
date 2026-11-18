---
title: "Your Agent Checks Permission, Not Ownership: 100%"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
kind: news
synthesis: true
sources:
  - https://arxiv.org/abs/2611.21577
  - https://arxiv.org/abs/2611.20922
one_big_thing: "A fabric binds every tool call to a name and remembers it by its argument shape, and neither is an identity — an impostor server that copies the name, description and field list wins the call on three of five clients, and an agent whose own memory predates one silent interface change succeeds 0.23 of the time against 0.63 for an agent that never saw the older version, so server identity and version have to be matched at the call, outside the model."
date: 2026-11-18
slug: your-agent-checks-permission-not-ownership
meta_title: "Your Agent Checks Permission, Not Ownership"
meta_description: "An agent repeats a call it made last week, the field has been renamed, and the tool stores an empty meeting. The same week, an impostor tool won every trial on three of five clients."
image_path: "context/assets/illustrations/your-agent-checks-permission-not-ownership/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Your Agent Checks Permission, Not Ownership. Server module slid out from a rack of identical modules, its exposed hardware revealing a"
image_caption: "Your Agent Checks Permission, Not Ownership: Stale interfaces and impostor tools win when the call record lacks ownership."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
An agent books a meeting for two colleagues. The calendar service renamed one field from attendees to guests a week earlier, and because nothing errored, the agent now sends a call the service reads as empty. It stores an event with nobody in it, and the agent reports the meeting booked. In the same week, a server run by nobody you hired copied one tool's name, description and argument list, and three of five commercial AI clients sent 100% of their 50 trials to that impostor instead. The first failure is a stale interface; the second is a fake one; both happen because the fabric checks permission at the door and never checks ownership of the tool behind it.

Both failures skip the same check. A multi-agent fabric verifies what a caller may do, and never verifies who owns the tool or which version of it is live. Ownership is a field the call record does not carry, and what a record carries is what it can prove — [durable execution without a transaction](/durable-execution-not-a-transaction/) is the same gap one layer down. The practical effect is plain: server identity and version have to be matched at the call itself, from a record the model neither writes nor remembers.

<!-- tldr -->
## At a glance
- **The shift:** Tool metadata is both the pick-list and an unchecked claim.
- **The number:** 0.23 of tasks succeed when memory outlives one change [2].
- **The architectural rule:** Match server and version at the call, not at discovery.

<!-- tension -->
## The check the fabric skips

Both papers appeared on 16 November, and they cover the two ends of one boundary. The Model Context Protocol (MCP) lets a client gather tools from several servers into one flat list. For each tool the client sees a name, a short description and an input schema — the argument list the model must fill. The model picks on those three strings alone.

The protocol's own wording gives the game away. Tool metadata is "not, by itself, necessarily bound to a verified provider identity". The misbinding study turns that line into a test: one real data server, one hostile server that advertises only tools with chosen fields, twelve mixes of name, description and schema, and fifty trials for each mix.

The split follows the metadata, not the model. An exact name collision with an unrelated description and an argument list that did not fit produced almost no wrong-server calls: 0.00 to 0.02 across five clients. Add the copied description and a matching argument list, and the same name reached a wrong-server rate of 1.00 on OpenAI's flagship model, on Qwen3.7 Max and on DeepSeek's V3, and 0.84 on Gemini 2.5 Pro. Anthropic's Claude Sonnet 5 held its direct rate to 0.06 and asked for a clarification in 0.94 of trials. That looks like caution until you see its binding stability of 0.00: it never picked a server at all.

The name was never the weapon. The three fields together were. An unrelated name, with a description that claimed authority and a matching argument list, still reached 0.50 on DeepSeek V3 and 0.42 on Gemini 2.5 Pro.

The other end needs no attacker. An agent that has called a tool keeps that call in chat history, in memory files, in retrieved notes and in saved skills. A server can swap tool definitions mid-session, and a service can accept the old request while ignoring fields it does not know. The change arrives with no error at all. I read the stale-memory table twice before I believed the direction: an agent with out-of-date experience got the task right 0.23 of the time, against 0.63 for one that never saw the old interface.

<!-- By the numbers -->
## By the numbers
- **0.23 of tasks:** Success for an agent whose saved memory outlived one silent change [2].
- **1.00 of failed runs:** After an untyped field rename, the share whose last reply still said done [2].
- **0.84 of trials:** Gemini 2.5 Pro's calls to an impostor that copied a tool's fields [1].

<!-- tactical-insight -->
## What I'd watch

Metabase rebuilt its own MCP server this month, and each fix in the post is a naming fix. By version 63, four different tools could run a query, so the rebuild covers the same ground with 10 of its 24 tools, ships nothing that removes a record, and makes a bad reference fail out loud. The team's own line belongs above an architect's desk: "A wrong name errors loudly; a wrong id that exists resolves to the wrong column silently."

What I'm watching is whether clients go the rest of the way. The misbinding paper asks for signed tool manifests, stable server-bound identifiers and schema hashes — a fingerprint of the field list — all enforced on the client side rather than in a prompt. A client that shows a model a tool, but not which server owns that tool, has moved the ambiguity rather than removed it.

<!-- nuanced-takeaway -->
## The catch

Both studies are one controlled harness each, so read their rates as proof that the failure exists, not as field numbers. The misbinding work measures a single toy data-fetching task, in a sandbox where no real data moved. The memory study runs six models over a handful of interface changes, and it leaves the current docs one search away.

That last detail points to a cheaper repair than a registry. Adding the current docs to the agent's memory file lifted its stale-memory success from 0.72 to 0.89. A version tag alone lifted it to 0.77. Memory that still matches the live interface reaches 1.00. Neither closes the gap, and both need docs that spell out the answer, which is exactly what the failing cases lack.

Neither paper argues against permission checks. The misbinding paper says its mechanism answers an earlier question than permission does. My reading is that most fabrics never ask that earlier question out loud — and until they do, the door is locked while the wrong tool walks through it.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your 78.3% Silent Cap Breach" -> /your-783-silent-cap-breach/ [same site (aichieve.net); same category; topical overlap: agent, checks] Link "Your 78.3% Silent Cap Breach" in the section where the article touches agent, checks. -->
<!-- internal-link hint: "OpenAI just made the agent loop a commodity" -> /openai-just-made-the-agent-loop-a-commodity/ [same site (aichieve.net); topical overlap: agent, checks, permission] Link "OpenAI just made the agent loop a commodity" in the section where the article touches agent, checks, permission. -->
<!-- internal-link hint: "60.7% of Agent Deletes Ask Nobody" -> /your-agent-deletes-ask-nobody/ [same site (aichieve.net); same category; topical overlap: agent] Link "60.7% of Agent Deletes Ask Nobody" in the section where the article touches agent. -->
## Related reading

- [Your 78.3% Silent Cap Breach](/your-783-silent-cap-breach/) — more on Autonomous & Agentic Workflows
- [OpenAI just made the agent loop a commodity](/openai-just-made-the-agent-loop-a-commodity/)
- [60.7% of Agent Deletes Ask Nobody](/your-agent-deletes-ask-nobody/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources
- [1] Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani, "When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents", 2026-11-16 — https://arxiv.org/abs/2611.21577
- [2] Zhen Xu, Hang Yin, Zitao Zhang, Kevin Zhao, Xuefeng Liu, "Experience Rot: Experienced Agents Fail Where Novices Succeed", 2026-11-16 — https://arxiv.org/abs/2611.20922
- [3] Aleksandr Lesnenko, "Rebuilding the Metabase MCP server: lessons for MCP tool design", Metabase Engineering, 2026-11-17 — https://www.metabase.com/blog/mcp-tool-design-lessons
