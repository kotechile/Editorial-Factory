---
title: Your Planner Is Not Your Model: 6.4 Points
vertical: multi_agent_enterprise_fabric
kind: news
persona: ai_architect
one_big_thing: "In an agent fabric the workflow is a portable artifact with its own measured quality: a plan written by one model added 6.4 points to four other models, while a plan from a stronger author subtracted 2.5, so who writes the plan matters more than which model runs it."
date: 2026-11-11
slug: your-planner-is-not-your-model
image_path: "context/assets/illustrations/your-planner-is-not-your-model/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Your Planner Is Not Your Model. Central planning console with fiber conduits fanning to server racks in a darkened data hall."
image_caption: "Your Planner Is Not Your Model: Who writes the plan matters more than which model runs."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

A workflow outlives the model that wrote it, and on a new benchmark that is worth about 6.4 points to whichever model runs it. The plan became a model output because recent harnesses let one model split a task among helper agents and dispatch them while the run is happening [1]. WorkflowArena handed 145 long, open-ended tasks to nine models and recorded every handoff, then ran a second test in which one model writes the plan and four others do all the work [1]. Plans from Opus raised all four; plans from Astra, which scores higher on its own than any of them, lowered two in the static setting, where the written plan runs unchanged [1]. The plan is the part of your fabric that accumulates.

<!-- tldr -->

## At a glance

- **The shift:** Orchestration is now measured on its own, apart from task completion.
- **The number:** Opus's plans added 6.4 points to other models; Astra's lost 2.5 [1].
- **The risk:** Effort alone re-authors the plan — calls per task rose 67% [1].

<!-- tension -->

## The plan travels without its author

The premise is that the plan has become an output. Recent agent harnesses let a model split a task among helper agents and write the workflow that keeps them in order [1]. The shape of the work is therefore decided while the run is happening, not by the person who built the system [1]. The benchmark makes that shape visible: every handoff passes through a recorded interface, so each finished task can be read next to the plan that produced it [1].

The results are modest and uneven. The best setup completed 36.95% of tasks in full, and the spread by field is wide — software engineering at 29.41%, legal work at 9.09% [1]. What separates the systems is not only how many tasks they finish but how they split the work. At high effort, Opus and Sonnet average 0.86 and 0.76 workflow calls per task, and each call carries 5.55 and 6.14 helper agents [1]. Astra and Sol average 2.09 and 1.94 calls carrying 1.72 and 1.69 [1].

| System | Calls per task | Helpers per call | Plan transfer |
|---|---|---|---|
| Opus, Claude Code | 0.86 | 5.55 | +6.41 static, +6.27 dynamic |
| Sonnet, Claude Code | 0.76 | 6.14 | not tested as author |
| Astra, Codex | 2.09 | 1.72 | −2.53 static, +1.34 dynamic |
| Sol, Codex | 1.94 | 1.69 | not tested as author |

One call does most of the job for Opus, at 70% of the runs that call out at all, against about a third for Astra. Almost every Astra call holds four helpers or fewer, where a quarter of Opus calls carry nine or more [1]. That split is a design choice, and it does not follow from raw skill.

The second test holds the model doing the work steady and changes only who wrote the plan. On 32 of the tasks, plans from Opus raised Kimi from 35.75 to 46.61 and DeepSeek from 18.37 to 25.24, while plans from Astra lowered both [1]. Astra finishes 27.34% of tasks on its own at max effort, against at most 16.48% for those four models, so the weaker planner is the stronger solo performer [1]. The authors say it directly: strong solo performance does not by itself produce plans that help other models [1]. I read that sentence three times, because it inverts the hiring logic most teams still use.

## By the numbers

- **6.4 points:** The average gain to four models when Opus wrote the plan and never touched their files [1].
- **$29.26 a task:** Astra at extra-high effort, 3.31 points behind Opus at high effort at 4.4 times the cost [1].
- **0.86 workflow calls:** Opus per task at high effort, in groups of 5.55 helpers against Astra's 2.09 calls of 1.72 [1].

<!-- tactical-insight -->

## Where change control breaks

The vendor market prices a different unit. At TechEd 2026, the business-software maker (SAP) described one governed entry point through which agents from outside suppliers join the same company workflow [2]. Every change to one of its agents passes a governed pipeline before production [3]. Builders there pick from more than 70 AI models, and a new enterprise gateway is planned for early 2027 to bring sign-in checks, policy enforcement, routing, monitoring, usage tracking and auditing into one place [4]. Each of those controls attaches to the agent, or to the traffic it gives off.

The measurement puts the variable object upstream of both. A team that approves an agent and later swaps the model behind it, or nudges its effort setting, has changed the planner, and the planner writes the plan. Effort alone moves the numbers: from low to max, Astra's calls per task rise 67% while its group size moves 5% [1]. The field shapes the split as well, and legal work pulls every system toward larger groups than operational work does [1]. I'd want to know which model and effort setting a fabric's approval record actually names, because the plan it signed off on may not be the plan that runs.

The desk has argued half of this before. Once a procedure is known, compiling it into a fixed workflow beats asking a model to work it out again every time, which is the point behind [275 planning rules a router breaks](/your-router-breaks-275-constraints/). The transfer test supplies the other half: a compiled plan is portable, and the evidence is that a good author's plan kept its value when four different models carried it out.

<!-- nuanced-takeaway -->

## The catch

The 6.4 points are not structure on its own. Source models also wrote the instructions each helper received, so the paper says plainly that the gain may blend better organisation with task knowledge passed down in those words [1]. The transfer test covers 32 of the 145 tasks and two authoring models. Every setup ran once per task with no estimate of variance, each model ran in a single harness, and written and three-dimensional work was graded by a language-model judge whose agreement with people was never measured [1]. The four models doing the work were weaker ones, picked so a good plan could lift them, so this is not a contest between two frontier planners.

Where I've landed is narrower than the headline version. The claim is not that a workflow file ports cleanly between stacks. Nor is it that coordination beats one agent on cost: a controlled study of 13 company procedures, published on 7 November, found every coordinated design spending 1.4 to 4.7 times the single agent's tokens for gains that mostly could not be told apart from noise [5]. The claim is that planning quality can be measured apart from model quality, which makes the plan an artifact a fabric can version, review and test on its own tasks. Models stay interchangeable at the bottom of the stack. The plan is what a fabric keeps.

## Sources

- [1] Zheng Jiang, Fang Niu, Bo Peng et al., "WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems", arXiv:2611.12856, submitted 9 November 2026 — https://arxiv.org/html/2611.12856v1
- [2] SAP News, "SAP Empowers AI Developers to Build What Matters and Turn Intent into Autonomous Execution", 27 October 2026 — https://news.sap.com/?p=248010
- [3] SAP, "SAP TechEd 2026 Innovation News Guide" — https://www.sap.com/topics/events/teched/innovation-news-guide-2026
- [4] SAP, "Top 5 things to know from SAP TechEd 2026" — https://www.sap.com/blogs/top-sap-teched-2026-announcements
- [5] Subhrangshu Nandi et al., "Agent Architecture Cost–Success Trade-offs: A Controlled Evaluation across Enterprise-Style SOPs", arXiv:2611.12953, submitted 7 November 2026 — https://arxiv.org/abs/2611.12953
