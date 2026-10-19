---
title: "Answer Field First Costs 38.15 Points"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "A tool schema is an instruction the decoder enforces token by token: put the working field before the answer field, check that the engine can compile and constrain your schema, and treat a clean parse as no proof that the call reasoned."
date: 2026-10-19
slug: answer-field-first-costs-38-points
archetype: evergreen
evergreen: true
---

<!-- lead -->
Put the answer field ahead of the reasoning field in a tool schema, and the decoder writes the answer first. Every JSON (JavaScript Object Notation) mode reply in one 2024 study did that, and its reasoning scores fell [1]. On that study's Last Letter task, an open model lost 38.15 points in that format, while only 0.148% of outputs failed to parse [1]. That shortfall costs accuracy, and the parse rate never shows it.

<!-- tension -->

## The big picture:

A decoder that is held to a schema does not read the schema the way a person does. It turns the schema into a rule set, then blocks every token the rules forbid, one step at a time. The field order you write becomes the order the model writes in [1][2].

I keep coming back to how quiet that is. The call returns clean JSON, and the parser shows green.

Nothing in the logs says the working was skipped, because no field asked for it.

Two studies measure the cost, and they seem to disagree until you read the schema.

The first ran five model families on reasoning and sorting tasks. It found that looser formats scored higher, and JSON mode did worst in most cases.

The cause was not subtle. The answer field came before the reason field, so the model answered straight away instead of working through the problem [1].

The second study went the other way. It built a test of 9,558 real schemas, drawn from function signatures, service APIs (application programming interfaces), Kubernetes configs and a public schema library, then ran six engines against them [2].

On its own quality test, the constraint did no harm. A school maths set scored 83.7% under XGrammar against 80.1% with no constraint, and Guidance reached 83.8% [2].

Both results hold. What separates them is what the schema let sit inside its fields.

A schema with one answer field and no room for working removes the working. A schema with a steps list keeps it, and the rule set then only strips bad output [2].

The engines are the other half, and they are less alike than the marketing implies. Across the official schema test suite, Llamacpp failed to compile 37 groups, Outlines 42, Guidance 25 and XGrammar 3 [2]. A failed compile means the schema is refused before a single token is written.

Compiling is not the same as obeying. XGrammar let through outputs that broke the schema in 38 test groups, against 8 for Outlines, 7 for Llamacpp and 1 for Guidance [2].

An engine can be quick, compile almost anything, and still pass bad data in a shape the next service will reject.

Then there are the size limits, which no schema file warns you about. On OpenAI's strict output mode, one schema may hold up to 1,000 enum values in total, and a single word list above 250 values is capped at 15,000 characters [3].

The total length of names, definitions and fixed values cannot pass 120,000 characters [3]. A domain model that outgrows those numbers does not fail at design time. It fails as a refused request in production.

## By the numbers

- **38.15 points — Format accuracy gap:** an open model on the Last Letter task in JSON format, with a 0.148% parse-error rate that looked healthy [1].
- **100% — Answer-first replies:** every JSON-mode reply in the same study put the answer key before the reason key, so the model answered rather than reasoned [1].
- **38 groups — Bad data let through:** XGrammar accepted outputs that broke the schema in 38 test groups, against 8 for Outlines, 7 for Llamacpp and 1 for Guidance [2].
- **83.7% vs 80.1% — Maths accuracy:** a schema-constrained run against an unconstrained one on the study's quality test, which shows a schema with room for working does not cost accuracy [2].

<!-- tactical-insight -->

## What I'd watch:

I've been reading these two papers against each other for a week. What strikes me is how little of this shows up in a runtime's dashboards; teams watch speed and token spend.

Almost nobody watches whether the schema survived the engine.

- **Where the working field sits:** the order a schema declares is the order the model writes in. A schema that opens with steps and closes with the final answer keeps the working. One that opens with the answer removes it [1].
- **Whether the engine took the schema:** a refused schema is a request that fails before any output. The compile step is a release step, and it belongs in a test suite rather than in a hope [2].
- **Whether the engine holds both edges:** some engines are too strict and reject valid outputs. Some are too loose and accept invalid ones. The failure counts differ by engine and by schema feature [2].
- **What the parse rate hides:** a green parser measures syntax. The accuracy gap in the first study sat behind a 0.148% parse rate, so the parse rate is not the metric that catches this [1].
- **Where the size limit bites:** enum counts and total string length have hard caps on the strict subset, and a large domain model can cross them with no local warning [3].

**What I'm watching next:** whether field order becomes a reviewed item in agent runtimes, the way a database migration is reviewed. The evidence says it acts like one.

<!-- nuanced-takeaway -->

## The catch

The strongest number here has the shortest shelf life. The 100% answer-first result comes from one 2024 study of one chat model, and field order is a model habit, not a law of physics. A newer model may do its working inside a single text field before it writes, which would blunt the effect without changing the schema.

The engine figures drift with every release too. Those compile and loose-constraint counts are a snapshot of six engines tested against one set of schemas in early 2025 [2]. A team reading this a year from now should run the test suite against its own engine rather than trust the table.

The counter-evidence has an honest limit as well. The 83.7% result shows that a constraint did not lower accuracy when the schema left room for working. It does not show that every schema does that, and the study's authors built the tasks to test the question [2].

My read is that both papers describe one mechanism from two sides. The schema is the second prompt, and it is the one nobody proofreads.

<!-- tldr -->

## At a glance

- **The Big Shift:** two studies show that the tool schema an agent decodes against acts as an instruction, not a formatting detail. Field order set the order of the model's output, and six engines disagreed sharply on which schemas they could compile or obey.
- **Why It Matters:** a schema that puts the answer before the working removes the working. One 2024 study measured a 38.15-point accuracy gap on a task where more than 99.8% of outputs parsed cleanly, so the damage never shows up in a parse-rate dashboard.
- **What I'd Watch:** whether teams start reviewing field order and engine coverage as release items, and what a schema test suite finds in their own engine.
  - **Working field first:** the schema declares the order the model writes in. A steps field ahead of the final answer keeps the working in view.
  - **Compile coverage:** whether the engine accepts the schema at all. An engine that refuses it fails the request before any token is written.
  - **Too loose:** an engine that takes a schema but also accepts bad output. The reply then parses and still breaks the contract downstream.
- **The Catch:** the field-order result is a 2024 snapshot of one model, and the engine counts come from early 2025. A test that left room for working found no loss at all, so the schema text decides which finding applies.

## Sources
[1] Tam, Wu, Tsai, Lin, Lee & Chen — "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models," arXiv:2408.02442v2 [cs.CL] (2024-08-05, rev. 2024-10-07) — https://arxiv.org/html/2408.02442v2
[2] Geng, Cooper, Moskal, Jenkins, Berman, Ranchin, West, Horvitz & Nori — "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models," arXiv:2501.10868v1 [cs.CL] (2025-01-18, rev. 2025-02-27) — https://arxiv.org/html/2501.10868v1
[3] OpenAI — "Structured Outputs" API guide (limits on enum size and total string size, retrieved 2026-10-19) — https://platform.openai.com/docs/guides/structured-outputs
