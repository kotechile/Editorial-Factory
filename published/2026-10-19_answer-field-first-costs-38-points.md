---
title: "Answer Field First Costs 38.15 Points"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "A tool schema is an instruction the decoder enforces token by token: put the working field before the answer field, check that the engine can compile and constrain your schema, and treat a clean parse as no proof that the call reasoned."
date: 2026-10-19
slug: answer-field-first-costs-38-points
archetype: evergreen
evergreen: true
meta_title: "Answer Field First Costs 38.15 Points"
meta_title_source: "derived_from_title"
meta_description: "Put the answer field before the reasoning field in a tool schema, and the model writes the answer first. In one 2024 study, an open model lost 38.15 points…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/answer-field-first-costs-38-points/featured.png"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Answer Before Reasoning. Modular mechanical assembly featuring a heavy metal output casing placed in front of sequential"
image_caption: "Answer Before Reasoning: Why asking for the answer first breaks LLM reasoning."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Put the answer field before the reasoning field in a tool schema, and the model writes the answer first. In one 2024 study, an open model lost 38.15 points on a string task when it ran in JavaScript Object Notation (JSON) mode [1]. Just 0.148% of its outputs failed to parse [1]. The syntax was clean. The work behind it was gone.

<!-- tension -->

## The big picture:

A decoder held to a schema does not read the schema. It turns it into a rule set, then blocks every word (token) the rules forbid, step by step. The field order you write sets the order the model writes in [1][2].

I keep coming back to how quiet that is. The call returns clean data, and the parser shows green.

Nothing in the logs says the model skipped its working, because no field asked for it.

Two studies measure the cost, and they seem to clash until you read the schema.

The first ran five models on reasoning and sorting tasks. Looser formats scored higher, and JSON mode did worst in most cases [1]. The cause was plain. The answer key came before the reason key, so the models answered without thinking [1].

The second study built a test of 9,558 real schemas, drawn from service endpoints, system configs and code libraries [2]. It ran six engines against them.

Where a schema left room for step-by-step work, scores held. A school math set scored 83.7% under XGrammar, against 80.1% with no rule set [2].

Both results hold. What splits them is whether the schema gave the model space to think.

The engines are the other half, and they act nothing alike. On the official schema test suite, Llamacpp failed to compile 37 groups, Outlines 42, Guidance 25 and XGrammar 3 [2]. A failed compile means the system rejects the schema before it writes a word.

Compiling is not the same as obeying. XGrammar let through broken outputs in 38 test groups, against 8 for Outlines, 7 for Llamacpp and 1 for Guidance [2].

An engine can run fast, take any schema, and still hand bad data to the next service.

Size limits bite too. On OpenAI's strict mode, one schema may hold up to 1,000 enum values in total [3]. A single word list above 250 values is capped at 15,000 characters [3].

Names, definitions and fixed values together cannot pass 120,000 characters [3]. A large domain model then fails as a refused request in live systems, with no warning at design time.

## By the numbers

- **38.15 points — Format gap:** an open model lost this much on a string task in JSON mode, while only 0.148% of its outputs failed to parse [1].
- **100% — Answer-first replies:** every JSON-mode reply in the first study put the answer key before the reason key, so the model guessed rather than worked [1].
- **38 groups — Bad data passes:** XGrammar accepted outputs that broke the schema rules in 38 test groups, against 1 for Guidance [2].
- **83.7% vs 80.1% — Math scores:** a run held to a schema beat an open run on the study's quality test, so a schema with room for working does not cost accuracy [2].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 172" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Answer Field First Costs 38.15 Points</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">Answer-first replies</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#818cf8"/>
  <text x="550" y="84" fill="#f1f5f9" font-size="13" font-weight="600">100%</text>
  <text x="604" y="84" fill="#64748b" font-size="11">([1])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Math scores</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="251" height="18" rx="4" fill="#818cf8"/>
  <text x="501" y="132" fill="#f1f5f9" font-size="13" font-weight="600">83.7%</text>
  <text x="555" y="132" fill="#64748b" font-size="11">([2])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

I've been reading these two papers against each other for a week. What strikes me is how little of this shows up in the usual dashboards. Teams watch speed and token spend, but rarely check if the schema survived the engine.

- **Where the working sits:** the schema sets the writing order. A schema that opens with a steps field and closes with the final answer keeps the work in view [1].
- **Whether the engine took the schema:** a refused schema fails the request before any output. The compile step is a release gate, not a given [2].
- **How strict the engine is:** some engines reject good outputs, while others accept broken ones. The counts swing by engine and by schema feature [2].
- **What the parse rate hides:** a green parser only measures syntax. The big gap in the first study sat behind a 0.148% parse rate [1].
- **Where the size limit bites:** enum counts and total string lengths have hard caps in strict modes. A growing domain model can cross them and fail in live systems [3].

What I'm watching next: whether field order gets reviewed in agent codebases the way a database migration does. The evidence says it needs the same care.

<!-- nuanced-takeaway -->

## The catch

The strongest number here has the shortest shelf life. The 100% answer-first result comes from one 2024 study of one chat model. Field order is a model habit, not a law of physics. A newer model may do its working inside one text block before it writes, which would blunt the effect without changing the schema.

The engine figures drift with every release too. Those compile counts are a snapshot of six engines tested in early 2025 [2]. A team reading this a year from now would need to run the test suite against its own engine.

The other side has a limit too. The 83.7% result shows a rule set did not lower scores when the schema left room for working [2]. It does not show that every schema does that.

My read is that both papers describe one pattern from two sides. The schema is a second prompt, and it is the one nobody proofreads.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> /durable-execution-not-a-transaction/ [same site (aichieve.net); same category; topical overlap: model, tool] Link "Durable Execution Is Not a Transaction" in the section where the article touches model, tool. -->
<!-- internal-link hint: "Planner-as-Router: Fold the Model Choice Into the Plan" -> /planner-as-router-fold-the-model-choice-into-the-plan/ [same site (aichieve.net); same category; topical overlap: costs, model] Link "Planner-as-Router: Fold the Model Choice Into the Plan" in the section where the article touches costs, model. -->
<!-- internal-link hint: "Tool-List Budget: How Many Tools One Agent Can Hold" -> /agent-tool-count-ceiling/ [same site (aichieve.net); same category; topical overlap: tool] Link "Tool-List Budget: How Many Tools One Agent Can Hold" in the section where the article touches tool. -->
## Related reading

- [Durable Execution Is Not a Transaction](/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
- [Planner-as-Router: Fold the Model Choice Into the Plan](/planner-as-router-fold-the-model-choice-into-the-plan/) — more on Autonomous & Agentic Workflows
- [Tool-List Budget: How Many Tools One Agent Can Hold](/agent-tool-count-ceiling/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** two studies show that a tool schema acts as an instruction, not a formatting detail. Field order sets the order the model writes in, and engines disagree on which schemas they compile or obey.
- **Why It Matters:** a schema that puts the answer before the work forces the model to skip its thinking. One 2024 study measured a 38.15-point drop on a task where just 0.148% of outputs failed to parse, so the usual dashboards miss it.
- **What I'd Watch:** whether teams start reviewing field order and engine coverage before release.
  - **Working field first:** the schema sets the writing order. A steps field ahead of the final answer keeps the work in view.
  - **Compile coverage:** whether the engine takes the schema at all. A refused schema fails the request at once.
  - **Too loose:** an engine that takes a schema and also accepts bad output. The reply parses and still breaks the next service.
- **The Catch:** the field-order result is a 2024 snapshot of one model, and the engine data comes from early 2025. A newer model may reason differently, so the schema text decides which finding applies.

## Sources
[1] Tam, Wu, Tsai, Lin, Lee & Chen — "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models," arXiv:2408.02442v2 [cs.CL] (2024-08-05, rev. 2024-10-07) — https://arxiv.org/html/2408.02442v2
[2] Geng, Cooper, Moskal, Jenkins, Berman, Ranchin, West, Horvitz & Nori — "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models," arXiv:2501.10868v1 [cs.CL] (2025-01-18, rev. 2025-02-27) — https://arxiv.org/html/2501.10868v1
[3] OpenAI — "Structured Outputs" API guide (limits on enum size and total string size, retrieved 2026-10-19) — https://platform.openai.com/docs/guides/structured-outputs

## Gate report
lead — PASS — the loss and the parse rate land in the first three sentences, with JSON expanded on first use.
tension — PASS — plain-language mechanism, short paragraphs, first-person cue, a "By the numbers" block with four cited bullets.
tactical-insight — PASS — five observations under "What I'd watch:", no instruction to the reader, first-person cue.
nuanced-takeaway — PASS — states the shelf life of the figures and the limit of the counter-evidence, ends on a labelled reading.
tldr — PASS — the four-slot schema with three defined sub-bullets under "What I'd Watch:".
access — see the check below.
