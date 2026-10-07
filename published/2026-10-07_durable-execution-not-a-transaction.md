---
title: "Durable Execution Is Not a Transaction: The Missing State in Agent Tool Contracts"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "A durable journal and an MCP gateway each record half of a transaction nobody defined — the missing artifact is the task's state footprint plus the effect's declared semantics, carried across the tool boundary."
date: 2026-10-07
slug: durable-execution-not-a-transaction
synthesis: true
sources:
  - https://arxiv.org/abs/2610.03140
  - https://arxiv.org/abs/2609.15397
meta_title: "Durable Execution Is Not a Transaction: The Missing State…"
meta_title_source: "derived_from_title"
meta_description: "Across 98,291 tools built for the Model Context Protocol (MCP), an AI agent rarely knows if it can undo a mistake."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/durable-execution-not-a-transaction/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "A dark logic board bypassed by a glowing amber fiber optic relay in a moody, hazy data vault."
image_caption: "AI agents and their tool contracts currently lack a shared mechanism to track data footprints, leaving a dangerous gap in execution safety."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Across 98,291 tools built for the Model Context Protocol (MCP), an AI agent rarely knows if it can undo a mistake. The standard risk flag appears on 65.8% of those tools. Yet it only matters on 12.9% of them, and just 3.1% warn of a true, lasting change [1].

Three weeks earlier, a second team found that task planners fail to track the exact data a step touches. That blind spot let one coding agent silently wipe out a sibling's work in a software test [2]. Neither paper cites the other.

<!-- tension -->

## The big picture:

Two systems try to make agents safe for live work, and each assumes the other handles the hard part.

The durable log records that a step ran, so you can replay it. The gateway lists which tools exist and who may call them. Neither one creates a safe, complete exchange.

The log ignores what data changed. The tool contract ignores whether a call can be reversed.

What strikes me here is how perfectly the two gaps mirror each other. Oto Mraz and his team at Delft University of Technology point out that planners track the order tasks run in. But they ignore the actual data each task touches [2].

The resulting failure is mundane. Two workers edit the same shared file, the plan assumes their changes will not clash, and one wipes out the other without a warning.

From the other side, a separate team found the same empty space. Measured across an official list of 98,291 tools, the MCP tags say almost nothing a recovery system needs [1].

There is no status check. There is no rule for undoing a call, and no guide for reordering two calls.

## By the numbers

- **12.9% — Risk flags that matter:** The risk hint sits on 65.8% of the 98,291 tools measured. It only counts for tools that change data, so just 3.1% flag a true, lasting change [1].
- **98,291 — Tools measured:** A July 2026 snapshot of the tool list covered 18,688 separate servers. Of those, 4,838 servers answered with at least one tool [1].
- **1 of 8 — Rules the tags can state:** The researchers grouped eight common failures. Only one ability, running the same call safely twice, is partly shown in the standard tags [1].
- **4 tasks × 2 models × 4 topologies × 5 runs — Planner-gap evidence:** A public coding test showed that tracking read and write clashes fixes silent failures across four plan setups [2].

<!-- tactical-insight -->

## What I'd watch:

Both research teams reached for the word "interface" from opposite ends of the same wire. My read is that this points to one missing part, not two separate complaints.

The contract paper argues for one shared rule set at the tool boundary [1]. The database paper asks outside systems to expose those rules, so a planner can stage, check, and revert changes [2].

Put together, the data footprint makes the contract checkable, and the contract makes the footprint useful.

- **Where the terms land:** The MCP rules have a formal way to add new ones. I am watching whether a rollback rule arrives as an official addition or as a vendor's own rule.
- **Whether harnesses record footprints:** The data a tool reads and writes has to be captured at the run harness, not the planner. Planners that guess data changes from a plan will miss live clashes.
- **How the halves get priced:** Durable logs are already their own product, and agent tools lists are joining them. I am watching to see if anyone sells the pair as one system.

<!-- nuanced-takeaway -->

## The catch

The honest limit is that both measurements describe what developers state, not what systems actually do.

The report notes that a tool may run stronger safety checks inside itself, like filters that drop repeat calls, and never show them in the public tags [1]. That safety stays hidden to a run engine that only reads the public rules.

The planner evidence rests on small coding tasks with Claude models. It is not a live write to a company database, and the paper frames its wider goals as an open vision rather than a finished design [2].

I could be wrong that this gap survives contact with a real enterprise network. The test I would apply: whether read and write records start showing up in logs next to each tool call.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "OpenAI just made the agent loop a commodity" -> https://giniloh.com/openai-just-made-the-agent-loop-a-commodity/ [same site (giniloh.com); topical overlap: agent, model, tool, tools] Link "OpenAI just made the agent loop a commodity" in the section where the article touches agent, model, tool. -->
<!-- internal-link hint: "Planner-as-Router: Fold the Model Choice Into the Plan" -> https://giniloh.com/planner-as-router-fold-the-model-choice-into-the-plan/ [same site (giniloh.com); same category; topical overlap: agent, model] Link "Planner-as-Router: Fold the Model Choice Into the Plan" in the section where the article touches agent, model. -->
<!-- internal-link hint: "MCP Skills Extension" -> https://giniloh.com/mcp-skills-extension/ [same site (giniloh.com); same category; topical overlap: agent] Link "MCP Skills Extension" in the section where the article touches agent. -->
## Related reading

- [OpenAI just made the agent loop a commodity](https://giniloh.com/openai-just-made-the-agent-loop-a-commodity/)
- [Planner-as-Router: Fold the Model Choice Into the Plan](https://giniloh.com/planner-as-router-fold-the-model-choice-into-the-plan/) — more on Autonomous & Agentic Workflows
- [MCP Skills Extension](https://giniloh.com/mcp-skills-extension/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Two research papers published three weeks apart found the same missing piece in agent systems. Planners fail to record the data tasks read and write [2], and tool interfaces cannot declare if an action actually happened or can be undone [1].
- **Why It Matters:** Durable logs track that a step ran, not what it changed. Gateways list available tools, not the risks of calling them. Teams buying either system for safety get an incomplete deal, risking silent data loss in their core databases.
- **What I'd Watch:** I am watching where these two halves get set in stone, because whoever ships the contract sets the terms everyone else uses.
  - **The rule route:** Whether a rollback rule arrives as a formal tool protocol addition or a vendor's own rule.
  - **The harness trail:** Whether the data a task reads and writes starts appearing in logs beside each tool call.
  - **The combined purchase:** Whether the log and the tool list merge into one product.
- **The Catch:** The report measures public tags, so a tool with hidden internal safety checks still looks undeclared [1]. The planner evidence also rests on small coding tests rather than live enterprise workflows [2].

## Sources

[1] *When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent–Tool Boundary* — arXiv:2609.15397, submitted 14 September 2026 (registry census snapshot 27 July 2026; artifact: github.com/flame-stream/mcp-annotation-census). https://arxiv.org/abs/2609.15397

[2] *Tracking State Footprints: How Agents Can Transact* — Mraz, Şerban, Psarakis, Kulahcioglu Ozkan and Katsifodimos, Delft University of Technology and Ververica, submitted 2 October 2026 (PVLDB 20(1)). https://arxiv.org/abs/2610.03140

## Gate report

- **lead:** PASS — Delivers the core news immediately in plain English, citing both papers, while breaking down complex sentences to improve readability and keeping paragraphs under 3 sentences.
- **tension:** PASS — Clearly contrasts the two missing halves of the transaction problem using short, active sentences and a clear first-person transition. Paragraphs strictly capped at 1-3 sentences.
- **tactical-insight:** PASS — Avoids playbook commands, frames the next steps as industry observations ("I am watching whether..."), and uses clear bullet points.
- **nuanced-takeaway:** PASS — Accurately caveats the limitations of the research (declared vs. implemented, small-scale vs. enterprise) with a clear first-person reflection. Plain vocabulary used to boost Flesch score.
- **tldr:** PASS — Strictly follows the 4-part Smart Brevity schema under a standalone "At a glance" H2, providing a clean 30-second executive summary.

<!-- post-rewrite figure audit (2026-10-07) -->
- Reverted a frontier-introduced wrong author name ("Tapio Mraz" → **Oto Mraz**, the paper's first author).
- Replaced the lossy "a reusable, two-way deal" with "one shared rule set" (the source's claim is a transactional contract at the tool boundary).
- No new unsourced numbers: every figure in the body (98,291 / 65.8% / 12.9% / 3.1% / 18,688 / 4,838 / 1 of 8 / 4×2×4×5 runs / July 2026) is in the verified brief.
- Hand-tuned for the Flesch floor: split every sentence over ~20 words and swapped multi-syllable generic words for shorter ones; facts, [n] citations, markers and the ## Sources list untouched.
