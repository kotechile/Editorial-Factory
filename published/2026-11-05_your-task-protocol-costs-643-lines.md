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
image_alt: "Task Protocol Costs 643 Lines. Two robot arms pass a sealed tote while a loop of gated check stations curves behind."
image_caption: "The same hand-off, carried two ways: a direct pass, or a long chain of gated stations."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
In your agent stack, one job moves from one service to another, and what carries it is paid for every year after. A published comparison built the same hand-off twice and found that the task-protocol version costs 643 extra lines of code [1]. That premium is not waste. A task protocol turns one request into a state machine that holds execution state between calls, and the bill is what owning that state costs [1].

<!-- tldr -->

## At a glance

- **The shift:** The July 2026 MCP revision lets a tool call ask a question mid-call.
- **The numbers:** 643 extra lines, six coordination steps against two, a 37-state machine.
- **The architectural rule:** A task protocol only for work that outlives the call.

<!-- tension -->

## Three Ways to Manage Agent State

I read the three documents in one sitting, and the difference between them is not a feature list. All three options are documented patterns, and what separates them is where the state sits between two calls.

1. **In-call round trips.** The Model Context Protocol (MCP) removed the session. The current spec has no session and no state handle, so a server cannot tie one call to the next through the connection [3]. Anything the work needs must travel inside the call. The July 2026 revision adds multi round-trip requests (MRTR), which let the server ask for more input before it answers [4].

2. **Server-issued state handles.** A handle is a string that a server returns from a create call, and the caller passes it back on the next request [3]. A handle is a name, not a permission. The spec requires the server to check the caller against the handle on every call, so an open handle needs high entropy and a fixed lifetime [3]. Its worked example keeps a shopping-basket handle for 24 hours without use. It writes that expiry into the tool description, so the model can read it before it keeps state [3].

3. **Full task protocols.** Google's Agent-to-Agent (A2A) protocol gives the receiving agent a lasting task object with its own lifecycle [1]. A call can ask a question back, stream while it runs, be watched, or leave a file behind after the caller has stopped waiting [1].

The price of the task protocol is counted, not estimated. The same hop as a task protocol took 1,898 lines against 1,255, counted by the line-count tool (cloc) over Python and Java [1]. The authors put that at about 51% more code [1]. The handshake grew from four parts to ten, and one interaction from two steps to six [1]. The Purdue University team that turned the A2A spec into a state machine before attacking it counted 37 states and 76 transitions [2].

| Pattern | State location | Overhead | Failure mode | Best for |
| :--- | :--- | :--- | :--- | :--- |
| **In-call round trip (MCP)** | Client, inside the call | 1,255 lines, 4 parts, 2 steps | Dropped connection loses the prompt | Synchronous questions |
| **State handle (MCP)** | Server store, behind a token | Cheap per call, plus a lifetime | Token expires, or is read as a permission | Sessions under 24 hours |
| **Task protocol (A2A)** | Protocol layer, 37 states | 1,898 lines, 10 parts, 6 steps | Unhandled states, lost identity | Jobs that outlive the call |

That table is the whole argument in one screen. The overhead column is what you pay up front, and the failure column is what you are still debugging at two in the morning.

The July 2026 MCP revision is what makes the handle option cheaper than it looks. It puts a round trip inside a tool call. The call returns asking for input, and the client resends the answers plus any state the server handed it [4]. That is a breaking change, because it replaces the older pattern of server-initiated requests [4]. A question that once needed a task object now fits inside one tool call, which leaves the task protocol with the work that outlives the connection. That is the case where [durable execution](/durable-execution-not-a-transaction/) starts: a resumed run rather than a repeated call.

## By the numbers

- **51% more code:** One hop took 1,898 lines as a task against 1,255 as a tool call, counted with cloc over Python and Java [1].
- **11 — Spec flaws:** Turning A2A into a state machine surfaced 11 protocol flaws that a compliant attacker can use with no implementation bug [2].
- **24 hours — Handle lifetime:** The MCP spec's worked example expires a basket handle after 24 hours without use [3].

<!-- tactical-insight -->

## How Each Pattern Fails in Production

The three options fail in different places, and the failure is the thing to size. A plain tool call fails by forgetting, so the answer never arrives and the caller knows at once. A handle fails later, either by expiring under a run that paused or by being read as a permission when it is only a name. A task protocol fails by collecting states nobody drew, and the caller finds out when a resumed task arrives in a shape the app never handled [2].

The teams closest to this problem choose by time, not by feature lists. A hop that ends inside one call is a tool, even when it asks a question in the middle. The round trip keeps the state with the asker, so no shared store is needed [4]. A hop that must survive a restart, hand work to a person for an hour, or send a file later is a task. The 37-state machine is then the asset being secured, not a vendor detail [2]. My read is that the hard work sits in the middle case, where the handle's expiry and its per-call check are the whole design.

There is a quieter cost that the line count hides. The formal study found that identity is lost between delegated hops [2]. A reused handle invites the same fault, because a handle that works like a password was never a permission [3].

<!-- nuanced-takeaway -->

## The catch

That study is one team's build of one task. Two of its four agents call a language model, and the pair was tested on 30 prompts. The multi-turn finding came from reading the specs, not from running a question loop [1]. Lines of code measure how much surface you coordinate, never what a run costs. The formal study bounds what the protocol allows, not what a shipped server does [2].

What I find hard to square is how cleanly those numbers read as a verdict when they are really a price list. Paying 643 lines and three times the steps is cheap if the other path is a lifecycle your callers will lean on for years. It is dear if you only needed a question answered two calls ago. The choice is not which protocol is better; it is how long the state has to live.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "$915M Illusion: Your AI Judge Moves" -> /buying-ai-quality-when-the-score-belongs-to-the-judge/ [same site (aichieve.net); topical overlap: another, every, moves, paid] Link "$915M Illusion: Your AI Judge Moves" in the section where the article touches another, every, moves. -->
<!-- internal-link hint: "Your Undo Is 14.6x Cheaper" -> /your-undo-is-14-6x-cheaper/ [same site (aichieve.net); same category; topical overlap: agent, costs, task] Link "Your Undo Is 14.6x Cheaper" in the section where the article touches agent, costs, task. -->
<!-- internal-link hint: "68 Loops Your Runtime Never Stopped" -> /agent-loop-bound-not-a-budget/ [same site (aichieve.net); same category; topical overlap: agent, every] Link "68 Loops Your Runtime Never Stopped" in the section where the article touches agent, every. -->
## Related reading

- [$915M Illusion: Your AI Judge Moves](/buying-ai-quality-when-the-score-belongs-to-the-judge/)
- [Your Undo Is 14.6x Cheaper](/your-undo-is-14-6x-cheaper/) — more on Autonomous & Agentic Workflows
- [68 Loops Your Runtime Never Stopped](/agent-loop-bound-not-a-budget/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

- [1] Predoaia, Vu, Barmpis, Kolovos and García-Domínguez, "A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems", University of York, arXiv:2607.23884v1, 26 Jul 2026 — https://arxiv.org/html/2607.23884v1
- [2] Lotfi, Rahman, Karim and Bertino, "A2ABreak: Systematic Security Analysis of the A2A Protocol", Purdue University and UT Dallas, arXiv:2609.10871v1, 09 Sep 2026 — https://arxiv.org/html/2609.10871v1
- [3] Model Context Protocol specification 2026-07-28, "Server Features: Tools", including the Stateful Tools guidance and the Input Required result — https://modelcontextprotocol.io/specification/2026-07-28/server/tools
- [4] Model Context Protocol specification 2026-07-28, "Multi Round-Trip Requests" — https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr
