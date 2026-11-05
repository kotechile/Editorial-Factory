---
title: "Your Signed Tool Still Leaks: 3 of 3"
vertical: agentic_ai
kind: news
persona: ai_architect
one_big_thing: "The MCP trust line is the data each call carries, not the publisher's signature or the list of allowed addresses, and holding that line costs less than resetting the tool between calls."
date: 2026-11-05
slug: your-signed-tool-leaks-in-3-of-3-trials
synthesis: true
sources:
  - https://arxiv.org/abs/2611.06897
  - https://arxiv.org/abs/2611.06585
---

<!-- lead -->

On 4 November two papers measured the same trust line from opposite ends, after both counted what a single agent tool call actually carries. One inventoried the Model Context Protocol (MCP) estate your agents already run on: 9,200 config files in public repositories, and 5,975 of them point to 5,138 distinct server-and-repo pairs [1]. The other took a correctly signed tool from a real publisher, one that does what it says, and showed it passing private data to an address the rules allow — in 3 of 3 trials, past the best runtime defence yet shipped, running in the same process [2][4]. Your signed tool still leaks in 3 of 3 trials, and not one field in that count records what the tool was allowed to see.

<!-- tension -->

## The check looks at the publisher

My read starts with the protocol's own security page. It treats the danger as a problem at install time. Local MCP servers "are binaries that are downloaded and executed on the same machine as the MCP client", it says, and the attacks it lists are a bad startup command in a config file, a payload shipped inside the server, and a local service tricked into answering a hostile name [3]. The fix it requires is consent before the command runs, plus a sandbox [3]. All of that guards the way in.

The attack in the second paper needs none of it. The release is signed, the publisher is who it claims to be, the address sits on the allowed list, and the tool does its stated job [2]. It also carries protected items from one call into the next, then adds them to a request the rules already cleared [2]. A defence that ties authority to a process and the addresses it may reach cannot see that move, because both the process and the address are fine.

The authors put it plainly. Each baseline ties authority to a different object and so misses a different path: output labels miss items carried over and laundered, and sandboxes miss leaks through allowed addresses [2]. That is why the results do not improve as more controls are stacked. The defence under test blocks a direct transfer in the same run, and still fails the signed release in every trial [2].

The count, meanwhile, grew an audit surface built from identity and capability. Its 284,845 tool records are tagged by how each tool's abilities were learned — seen by probing the server live, or read from a directory — and its provenance fields keep the two apart [1]. What it does not hold is the set of arguments in one call. A count can tell you that 5,138 server pairs are named somewhere; it cannot tell you which of them hands a customer record to a summariser.

## By the numbers

- **284,845 — tool records:** entries in the release, each tagged as probed live or read from a directory, across 19 linked tables and 78,302 candidate server projects [1].
- **153 — attack runs:** 51 cases run three times each; the data-free fork logged no leak, against 5.9% to 74.5% of runs for the baselines and a stripped-down variant [2].
- **2–28x — cheaper than a reset:** a one-copy call takes 10 to 49 milliseconds, and every runtime still finishes 99 of 99 normal steps [2].

<!-- tactical-insight -->

## Where the fork sits

The control that held ties authority to the items each copy may see, not to the process that owns them. Each call runs in a short-lived copy forked from a process that holds no data, and the copy gets only what its target address is cleared for; if hostile code runs anyway, what it can pass on is capped by what its copy was given [2]. The authors call this germline execution, and it stacks with the address rules rather than replacing them: the rules still say where a call may go, and the fork says what may travel [2].

What I find hard to square is the cost. The usual way to clear state between calls is to restart the tool, and forking ahead of time ran 2 to 28 times faster in the reported runs, at 10 to 49 milliseconds per one-copy call [2]. Security work usually arrives with a delay attached; this arrives with a saving, which is why I would raise it in an architecture review rather than a hardening backlog.

The gateway's own surface is the first thing to list, and [the tool surface is a release surface](/your-tool-surface-is-a-release-surface/) makes that case. This pair puts the line one level lower: not which tools the gateway shows, but which items each call may carry. The open question on the vendor side is whether the next round of gateways ships a per-call data rule, or one more filter over the same list of addresses.

<!-- nuanced-takeaway -->

## What the proof does not cover

The guarantee is a proof under stated assumptions, not a field result. It holds under explicit assumptions about how well a copy is fenced off and that the starting process holds no data, and a verified sign of a leak exists only for releases that repeat exactly under the authors' replay model [2]. The implementation is a prototype for unmodified Python MCP servers on stock Linux [2]. Read the number as a limit on what a class of mechanism can do, not as a certificate for a product.

The count has caveats of its own, and I would not let them vanish into a chart. Its 78,302 server projects and 16,165 consuming repos are candidate sets, not counts of live installs, and 3,225 of the 9,200 files point to no candidate project at all [1]. That gap is a bookkeeping problem, not an incident: an unresolved file is a server whose dependency you cannot name, and naming it is step one for any per-call data rule.

None of this makes a signature useless. It still proves who published a release and whether a later build came from them, which is the link that keeps a poisoned package out of production. The finding is narrower and harder to fix than a missing signature: the artifact can be exactly what it claims while the call is not.

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
