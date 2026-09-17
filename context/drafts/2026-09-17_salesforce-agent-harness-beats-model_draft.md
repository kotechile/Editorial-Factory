---
title: The harness beats the model: Salesforce's 48-point proof
vertical: agentic_ai
persona: ai_architect
one_big_thing: "Reworking the harness around a small model lifted task success from 29.2% to 78.0% without touching weights — and fine-tuning the model to copy a stronger one made it worse."
date: 2026-09-17
slug: salesforce-agent-harness-beats-model
---

<!-- lead -->
Salesforce researchers took a small Qwen model and rebuilt the scaffolding around it — the system prompt, tool set, execution hooks, and context handling — without touching a single weight. Mean task success jumped from 29.2% to 78.0% across seven enterprise-agent benchmarks [1]. Then they fine-tuned that same model to copy a stronger one, and success *fell* to 63.1% [1].

<!-- tension -->
**The big picture:** For two years the agentic story has been "a bigger model is a better agent." This data inverts it. The leverage is in the harness — the deterministic boundary around the model — not the weights. The counterintuitive kicker is the second result: upgrade the model inside a harness tuned for the old one, and the whole system can regress. The researchers call this a loss of "model–harness fit": the weaker model adopted the stronger one's planning strategy but couldn't execute it inside a harness built for its old behavior [1].

Salesforce productized the finding the same week. Its Enterprise AI Harness bundles six capabilities — context, agency, action, governance, security, and models — "delivered through a common, composable architecture" [2]. Headless 360 exposes the whole platform as a Model Context Protocol (MCP) server that agents in Agentforce, Claude, ChatGPT, and Cursor can discover and invoke in real time [3]. On the same day, Google Cloud wired Gemini Enterprise to Salesforce's headless architecture "built on MCP" [4], and AWS opened its Bedrock and Quick surfaces to Informatica MCP servers [5].

**By the numbers:**
- **29.2% → 78.0%:** the jump in mean task success from evolving the harness around a Qwen model, weights untouched — a gain of 48.8 points [1].
- **78.0% → 63.1%:** the drop when that model was fine-tuned to imitate a stronger expert's trajectories [1].
- **79.7%:** the recovery from "on-policy correction" — fixing the model's own failing turns instead of copying a teacher [1].
- **Six:** the capabilities in Salesforce's Enterprise AI Harness — context, agency, action, governance, security, models [2].

<!-- tactical-insight -->
**The playbook:** Treat the harness as the product and the model as a swappable part.

- **Inventory the harness first.** Before any model swap, list the prompt, tools, hooks, and context windows that sit around it. That list — not the model card — is where your reliability lives [1].
- **Test model–harness fit, don't assume it.** Salesforce's regression (78.0% → 63.1%) shows a stronger model can make a tuned system worse. Benchmark the *new model inside your existing harness* before you commit [1].
- **Prefer on-policy fixes over imitation.** When a model lags, correct its own failing turns rather than fine-tuning it to copy a stronger teacher. Salesforce recovered 79.7% that way [1].
- **Enforce the boundary with a protocol, not a prompt.** Headless 360 and the Gemini interop both use MCP so capability access and permissions ride in the protocol layer, not inside the agent's reasoning [3][4].

<!-- nuanced-takeaway -->
**The catch:** Salesforce is selling the harness, so its preprint is an argument for its own product line — treat the 48.8-point gap as a strong, single-lab result, not a settled law. It's a preprint, not peer-reviewed [1]. And the unified Enterprise AI Harness isn't generally available yet; Salesforce says the "new capabilities and the unified experience" land in Q1 FY 2028, with pricing undisclosed [6]. The durable claim isn't "Salesforce's harness is the answer" — it's "the deterministic boundary around the model is where the leverage moved, and model swaps are not free."

<!-- tldr -->
- **The Reality Check:** A frontier model is not automatically a better agent. Salesforce rebuilt the scaffolding around a small model and success nearly tripled (29.2% → 78.0%) with zero weight changes — then the model got *worse* when it was trained to copy a stronger one.
- **The Winning Moves:**
  - **Harness-first design:** treat the prompt, tools, hooks, and context windows as the product; the model is a replaceable part.
  - **Fit-test every model swap:** benchmark a new model inside your existing harness — a stronger model can regress a tuned system.
  - **On-policy correction:** fix the model's own failing turns instead of fine-tuning it to imitate a teacher.
  - **Protocol-enforced boundaries:** expose capabilities through MCP so permissions and access live in the protocol, not in the agent's reasoning.
- **The Fine Print:** The result is a single-lab preprint, and Salesforce sells the harness, so read the 48-point gap with skepticism. The unified harness product isn't generally available until Q1 FY 2028 — the durable lesson is about where leverage lives, not which vendor's harness to buy.

## Sources
[1] Salesforce research — "Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails" (arXiv:2609.09134, September 2026). https://arxiv.org/abs/2609.09134
[2] Salesforce press release — "Salesforce Introduces the Trusted Enterprise AI Harness" (September 11, 2026). https://www.salesforce.com/ap/news/press-releases/2026/09/11/salesforce-introduces-the-trusted-enterprise-ai-harness
[3] Salesforce news — "Expanding Headless 360: Enterprise Capabilities" (August 19, 2026). https://www.salesforce.com/news/stories/expanding-headless-360-enterprise-capabilities
[4] Salesforce news — "Salesforce and Google Cloud Unify Infrastructure and Agents for One Connected AI Stack" (September 15, 2026). https://www.salesforce.com/news/stories/salesforce-google-cloud-unify-infrastructure-and-agents
[5] Salesforce news — "AWS and Salesforce Put CRM Data, AI Agents, and Model Choice Into the Tools Teams Use Every Day" (September 15, 2026). https://www.salesforce.com/news/stories/aws-salesforce-enterprise-ai-expansion/
[6] The Letter Two — "Salesforce's Trusted Enterprise AI Harness, Explained" (September 10, 2026). https://thelettertwo.com/2026/09/10/salesforce-trusted-enterprise-ai-harness-dreamforce-2026

<!-- linkedin -->
Salesforce's own researchers just measured what agent teams have suspected: the harness beats the model.

They rebuilt the scaffolding around a small Qwen model — system prompt, tools, execution hooks, context handling — without touching a single weight. Task success jumped from 29.2% to 78.0% across seven enterprise benchmarks.

Then the twist: they fine-tuned that model to copy a stronger one, and it got *worse* — down to 63.1%. A stronger model inside a harness tuned for the old one can regress the whole system. They call it losing "model–harness fit."

The fix that worked (79.7%): on-policy correction — fixing the model's own failing turns — not imitation.

Salesforce is productizing the finding as its Enterprise AI Harness (context, agency, action, governance, security, models), with Headless 360 exposing the platform as MCP tools and Gemini Enterprise wired in over MCP.

The lesson for anyone shipping agents: the deterministic boundary around the model is where your leverage lives. And model swaps are never free — benchmark the new model inside your harness before you commit.
