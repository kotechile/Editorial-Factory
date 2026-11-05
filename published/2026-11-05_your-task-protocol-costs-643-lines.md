---
title: "Your Task Protocol Costs 643 Lines"
vertical: agentic_ai
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
one_big_thing: "An agent-to-agent hop keeps its state in one of three places — nowhere, a handle you store and check on every call, or a task object the protocol owns — and the task costs a measured 643 extra lines, six coordination steps against two, and a 37-state machine with 11 flaws a compliant attacker can use, so it is worth buying only when the work must outlive the call."
date: 2026-11-05
slug: your-task-protocol-costs-643-lines
meta_title: "Your Task Protocol Costs 643 Lines"
meta_description: "Building the same agent hand-off as a task protocol instead of a tool call cost 643 extra lines of code, three times the coordination steps, and a 37-state machine."
image_path: "context/assets/illustrations/your-task-protocol-costs-643-lines/featured.jpg"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "Your Task Protocol Costs 643 Lines. Rack-mounted task object module with a 37-position state selector track and latching connector rails."
image_caption: "Your Task Protocol Costs 643 Lines: The bill for state that outlives the call."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Building the same agent hand-off twice cost 643 extra lines of code because a task protocol turns one call into a small state machine that owns the fact between calls [1]. The tool version came to 1,255 lines and the task version to 1,898, which the authors put at about 51% more [1]. The task version also ran six coordination steps per interaction against two, and this one has 37 states and 76 transitions [1][2]. That is not a case against it. It is the bill for a choice the protocol makes for you, and that choice is where the fact lives between two calls.

<!-- tension -->

## Three places to keep the fact

The Model Context Protocol (MCP) removed the session. The current spec says the protocol has no state handle and no session, so a server cannot tie one call to the next through the connection [3]. Any state that has to survive is a handle: a string the server returns from a creation tool, which the model passes back on the next call [3]. That is the middle option, and most teams land there without naming it. What I keep circling is that it is also the option almost nobody writes down in a design review.

A handle is a name, not a permission. The spec's rule is that the server checks the caller against the handle on every call. An open handle works like a password, so it needs high entropy and a fixed lifetime [3]. Its worked example puts the rule in the tool description, with baskets that expire after 24 hours of inactivity, so the model can see the expiry when it decides to keep state [3]. The cost is not storage. It is that each reuse runs the check again, and each expiry becomes a path the model has to notice.

A task protocol puts that state on the wire. A2A gives the callee a lasting object with a life cycle, so a call can ask a question back, stream as it runs, be watched, or leave a file behind after the caller has stopped waiting [1]. The price is plain in the comparison: ten coordination parts against four, six steps per interaction against two, and about half again the code [1]. It is also plain in the size of the spec, which a Purdue team turned into a machine of 37 states and 76 transitions before attacking it [2].

Then the line moved, and most comparisons are older than the move. The July 2026 MCP revision adds a round trip inside a tool call: the call can come back asking for input, and the client resends the answers plus any state the server handed it [3][4]. It is a breaking change, because it replaces the old pattern of server-initiated requests [4]. So the question that used to need a task now fits inside a tool call. What is left is time, which is why a task is for work that outlives the call: the problem that [durable execution treats as a contract rather than a transaction](/durable-execution-not-a-transaction/), not as a retry.

## By the numbers

- **51% — Code premium:** The task version of one hop needed 1,898 lines against 1,255, counted with cloc over Python and Java source, excluding configuration [1].
- **11 — Spec flaws:** Turning A2A into a state machine surfaced 11 protocol-level flaws that a fully compliant attacker can use with no implementation bug, including context injection through unprotected identifiers and credential harvesting across delegation chains [2].
- **24 hours — Handle lifetime:** The MCP spec's example states a handle's retention inside the creation tool's description, so the model can read the expiry before it keeps state [3].

<!-- tactical-insight -->

## Where the hop owners land

What I keep coming back to is that the three options fail in different places, and the failure is what to size. A plain tool call fails by forgetting, which the caller sees at once. A handle fails by expiring under a run that paused, or by being read as a permission when it is only a name, which the caller sees later. A task fails by collecting states nobody drew, which the caller sees when a resumed task arrives in a shape the app never handled.

The teams closest to this pick by time, not by feature lists. A hop that ends inside one call is a tool, even when it asks a question mid-call, because the round trip keeps the state with the asker and needs no shared store [4]. A hop that has to survive a restart, hand work to a person for an hour, or send a file after the caller has moved on is a task, and the 37-state machine is then the thing being secured, not a detail of the vendor [2][3]. My read is that the hard work sits in the middle case, where a handle's expiry and its per-call check are the whole design.

There is a quieter cost in the task version that the line count hides. The formal study found that the delegated path is where identity is lost between hops, which is the same fault a handle invites when it is reused as a password [2][3]. Neither protocol removes that risk. One puts the check in your code on every call, and the other puts it in a life cycle the application has to draw, and both are work the architect owns.

<!-- nuanced-takeaway -->

## The catch

The comparison is one team's build of one task. Two of its four agents call a language model, the pair was tested on 30 prompts, and the multi-turn finding came from reading the specs rather than from running a question loop [1]. Lines of code are a proxy for how much surface you coordinate, never a measure of run cost, and the formal study bounds what the protocol allows rather than what any shipped server does [2].

What I find hard to square is how cleanly the numbers read as a verdict when they are really a price list. Paying 643 lines and three times the steps is cheap if the other path is a life cycle your callers will lean on for years, and it is dear if you only needed a question answered two calls ago. The choice is not which protocol is better. It is how long the fact has to live.


<!-- tldr -->

## At a glance

- **The shift:** MCP dropped the session and now round-trips a question inside a tool call, so asking back no longer needs a task.
- **The number:** 643 — the extra lines the task version of one hop needed.
- **The risk:** Without a handle's expiry and per-call check, the cheaper wire quietly turns state into a password.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> /durable-execution-not-a-transaction/ [same site (aichieve.net); same category; topical overlap: agent, protocol, state] Link "Durable Execution Is Not a Transaction" in the section where the article touches agent, protocol, state. -->
<!-- internal-link hint: "Your Undo Is 14.6x Cheaper" -> /your-undo-is-14-6x-cheaper/ [same site (aichieve.net); same category; topical overlap: agent, costs, task] Link "Your Undo Is 14.6x Cheaper" in the section where the article touches agent, costs, task. -->
<!-- internal-link hint: "60.7% of Agent Deletes Ask Nobody" -> /your-agent-deletes-ask-nobody/ [same site (aichieve.net); same category; topical overlap: agent, because] Link "60.7% of Agent Deletes Ask Nobody" in the section where the article touches agent, because. -->
## Related reading

- [Durable Execution Is Not a Transaction](/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
- [Your Undo Is 14.6x Cheaper](/your-undo-is-14-6x-cheaper/) — more on Autonomous & Agentic Workflows
- [60.7% of Agent Deletes Ask Nobody](/your-agent-deletes-ask-nobody/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

[1] Predoaia, Vu, Barmpis, Kolovos and García-Domínguez, "A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems", University of York, arXiv:2607.23884v1, 26 Jul 2026 — https://arxiv.org/html/2607.23884v1
[2] Lotfi, Rahman, Karim and Bertino, "A2ABreak: Systematic Security Analysis of the A2A Protocol", Purdue University and UT Dallas, arXiv:2609.10871v1, 09 Sep 2026 — https://arxiv.org/html/2609.10871v1
[3] Model Context Protocol specification 2026-07-28, "Server Features: Tools", including the Stateful Tools guidance and the Input Required result — https://modelcontextprotocol.io/specification/2026-07-28/server/tools
[4] Model Context Protocol specification 2026-07-28, "Multi Round-Trip Requests" — https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr
