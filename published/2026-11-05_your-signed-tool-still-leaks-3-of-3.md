---
title: "Your Signed MCP Tool Still Leaks: 3 of 3"
vertical: agentic_ai
kind: news
persona: ai_architect
one_big_thing: "The MCP trust line is the data each call carries, not the publisher's signature or the list of allowed addresses, and holding that line costs less than resetting the tool between calls."
date: 2026-11-05
slug: your-signed-tool-still-leaks-3-of-3
synthesis: true
sources:
  - https://arxiv.org/abs/2611.06897
  - https://arxiv.org/abs/2611.06585
meta_title: "Your Signed MCP Tool Still Leaks: 3 of 3"
meta_title_source: "derived_from_title"
meta_description: "A correctly signed Model Context Protocol (MCP) tool still leaks private data through an allowed address in 3 of 3 trials, after the signature check and the…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-signed-tool-still-leaks-3-of-3/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "A fiber-optic cable carrying a warm data stream passes through a locked steel security gate in a dark data hall."
image_caption: "Signed MCP Tools Leak Private Data: The trust line is the data each call carries."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

A correctly signed Model Context Protocol (MCP) tool still leaks private data through an allowed address in 3 of 3 trials, after the signature check and the destination policy both pass [2][4]. Two papers published on 4 November measured that trust line from opposite ends. One counted the servers your agents already run on: 9,200 config files in public code repositories, and 5,975 of them point to 5,138 distinct server-and-repo pairs [1]. The other watched a signed tool from a real publisher do what it advertises, then hand private data to an address the rules allow [2].

<!-- tension -->

## The protocol guards the install

The protocol's own security page treats the danger as an install-time problem. Local MCP servers "are binaries that are downloaded and executed on the same machine as the MCP client", it says, and the attacks it lists are a bad startup command in a config file, a payload shipped inside the server, and a local service tricked into answering a hostile name [3]. The fix it requires is consent before the command runs, plus a sandbox — a walled-off space that limits what the process can reach [3]. All of that guards the way in.

The attack in the second paper needs none of it. The release is signed, the publisher is who it claims to be, the address sits on the allowed list, and the tool does its stated job [2]. It also carries protected items from one call into the next, then adds them to a request the rules already cleared [2]. A defence that ties authority to a process and the addresses it may reach cannot see that move, because both the process and the address are fine.

What strikes me here: the authors show why stacking controls did not help. Each baseline ties authority to a different object and so misses a different path: output labels miss items carried over and laundered, and sandboxes miss leaks through allowed addresses [2]. That is why the results do not improve as more controls are stacked. The defence under test blocks a direct transfer in the same run, and still fails the signed release in every trial [2].

The count, meanwhile, grew an audit surface built from identity and capability. Its 284,845 tool records are tagged by how each tool's abilities were learned — seen by probing the server live, or read from a directory, and its provenance fields record where each ability came from [1]. What the count does not hold is the set of arguments in one call. It can tell you that 5,138 server pairs are named somewhere; it cannot tell you which of them hands a customer record to a summary job.

## By the numbers

- **284,845 — tool records:** entries in the release, each tagged as probed live or read from a directory, across 19 linked tables and 78,302 candidate server projects [1].
- **153 — attack runs:** 51 cases run three times each; the data-free fork logged no leak, against 5.9% to 74.5% of runs for the baselines and a stripped-down variant [2].
- **2–28x — cheaper than a reset:** a one-copy call takes 10 to 49 milliseconds, and every runtime still finishes 99 of 99 normal steps [2].

<!-- tactical-insight -->

## The fork caps the data

The control that held ties authority to the items each copy may see, not to the process that owns them. Each call runs in a short-lived copy — a fork — of a process that holds no data. The copy gets only what its target address is cleared for. If hostile code runs anyway, what it can pass on is capped by what its copy was given [2]. The authors call this germline execution, and it stacks with the address rules rather than replacing them: the rules still say where a call may go, and the fork says what may travel [2].

What I find hard to square is the cost. The usual way to clear state between calls is to restart the tool, and forking ahead of time ran 2 to 28 times faster in the reported runs, at 10 to 49 milliseconds per one-copy call [2]. Security work usually arrives with a delay attached; this arrives with a saving, which is why I would raise it in an architecture review rather than a hardening backlog.

The gateway's own surface is the first thing I'd list, and [the tool surface is a release surface](/your-tool-surface-is-a-release-surface/) makes that case. This pair puts the line one level lower: not which tools the gateway shows, but which items each call may carry.

**What I'd watch:** whether the next round of gateways ships a per-call data rule, or one more filter over the same list of addresses.

<!-- nuanced-takeaway -->

## What the proof does not cover

The guarantee is a proof under stated assumptions, not a field result. It holds under explicit assumptions about how well a copy is fenced off and that the starting process holds no data, and a verified sign of a leak exists only for releases that repeat exactly under the authors' replay model [2]. The code is a prototype for unmodified Python MCP servers on an ordinary Linux host [2]. Read the number as a limit on what a class of mechanism can do, not as a certificate for a product.

The count has caveats of its own, and I would not let them vanish into a chart. The 16,165 consuming repos and 78,302 server projects are candidate sets, not live installs, and 3,225 of the 9,200 config files point to no candidate project at all [1]. That gap is a bookkeeping problem, not an incident: an unresolved file is a server whose dependency you cannot name, and a per-call data rule starts with naming it.

None of this makes a signature useless. It still proves who published a release and whether a later build came from them, which is the link that keeps a poisoned package out of production. The finding is narrower and harder to fix than a missing signature: the artifact can be exactly what it claims while the call is not.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> /durable-execution-not-a-transaction/ [same site (aichieve.net); same category; topical overlap: context, model, protocol, tool] Link "Durable Execution Is Not a Transaction" in the section where the article touches context, model, protocol. -->
<!-- internal-link hint: "Your 60% Drop Isn't the Model" -> /your-60-drop-isnt-the-model/ [same site (aichieve.net); same category; topical overlap: context, model, protocol] Link "Your 60% Drop Isn't the Model" in the section where the article touches context, model, protocol. -->
<!-- internal-link hint: "Answer Field First Costs 38.15 Points" -> /answer-field-first-costs-38-points/ [same site (aichieve.net); same category; topical overlap: model, tool] Link "Answer Field First Costs 38.15 Points" in the section where the article touches model, tool. -->
## Related reading

- [Durable Execution Is Not a Transaction](/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
- [Your 60% Drop Isn't the Model](/your-60-drop-isnt-the-model/) — more on Autonomous & Agentic Workflows
- [Answer Field First Costs 38.15 Points](/answer-field-first-costs-38-points/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

**The shift:** The MCP trust line moved from the signed artifact to the data each call carries.
**The number:** 3 of 3 trials leaked past a correct signature and an allowed address.
**The risk:** The guarantee is a proof under assumptions, on a prototype, not a certificate.

## Sources

[1] MCP-Eco: A Linked Dataset of MCP Servers, Consumers, and Development Activity, 2026-11-04 — https://arxiv.org/abs/2611.06897
[2] Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains, 2026-11-04 — https://arxiv.org/abs/2611.06585
[3] Model Context Protocol specification, Security Best Practices (version 2025-06-18) — https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices
[4] Meta MCPGuard-Dynamic repository, the runtime defence tested in the same run — https://github.com/facebook/mcpguard-dynamic
