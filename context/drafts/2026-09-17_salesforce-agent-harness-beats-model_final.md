---
title: The Harness Beats the Model: Salesforce's 48-Point Proof
vertical: agentic_ai
persona: ai_architect
one_big_thing: "Reworking the harness around a small model lifted task success from 29.2% to 78.0% without touching weights — and fine-tuning the model to copy a stronger one made it worse."
date: 2026-09-17
slug: salesforce-agent-harness-beats-model
---

<!-- lead -->
Salesforce researchers built a new shell around a small Artificial Intelligence (AI) model, boosting its task success from 29.2% to 78.0% without changing its core math [1]. They updated the system prompt, tools, action steps, and memory limits instead of the model weights. But when they trained that same Qwen model to copy a smarter one, its success dropped to 63.1% [1].

<!-- tension -->
**The big picture:** For two years, the tech world believed bigger models made better agents. This data proves the real power sits in the harness—the strict rules wrapping the model. 

If you put a new model inside a shell built for an old one, the whole system can break down [1]. Researchers call this a loss of "model-harness fit." The weaker model learned the smart model's planning tricks, but it failed to use them inside its old setup [1].

Salesforce turned this finding into a product right away. The new Enterprise AI Harness groups six core traits into one shared design [2]. Headless 360 shares this platform as a Model Context Protocol (MCP) server, which is a standard way to link models to data. 

Now, agents in Agentforce, Claude, ChatGPT, and Cursor can find and use these tools instantly [3]. Google Cloud also linked Gemini Enterprise to this shared setup built on MCP [4]. On the exact same day, Amazon Web Services (AWS) opened its Bedrock and Q tools to Informatica MCP servers [5].

**By the numbers:**
- **29.2% to 78.0%:** The massive jump in task success from updating the harness around a Qwen model, keeping weights the same [1].
- **63.1%:** The lower success rate after training that same model to copy a stronger expert [1].
- **79.7%:** The high success rate reached through "on-policy correction," which means fixing the model's own mistakes instead of copying a teacher [1].
- **Six:** The number of tools—context, agency, action, rules, security, and models—packed into the new Salesforce harness [2].

<!-- tactical-insight -->
**The playbook:** Treat the harness as your main product. Treat the model as a simple part you can swap out.

- **Check your harness first:** List the prompts, tools, action steps, and memory windows around your model before making changes. Your system's success lives in this list, not in the model's spec sheet [1].
- **Test fit before you swap:** Do not assume a smarter model will fix a broken system. You must test a new model inside your current harness to avoid taking a step back [1].
- **Fix errors, do not copy:** When a model fails, correct its specific bad choices. Do not train it to copy a smarter teacher [1]. Salesforce recovered a 79.7% success rate this way [1].
- **Use protocols for rules:** Use standards like MCP to handle access and permissions. This keeps security rules in the protocol layer, far away from the agent's internal thinking [3][4].

<!-- nuanced-takeaway -->
**The catch:** Salesforce sells this exact harness tool. This makes the research paper a strong pitch for its own product line [1]. 

You should view the 48.8-point jump as a strong result from one lab, not a proven fact. The paper is also a preprint and has not passed peer review yet [1]. 

The unified Enterprise AI Harness will not launch until early 2028. Salesforce also has not shared the price yet [6]. The lasting lesson is not to buy a specific tool, but to see that power lives in the strict rules around the model.

<!-- tldr -->
- **The Reality Check:** A bigger model does not automatically make a better agent. Salesforce built a new shell around a small model and nearly tripled its success (29.2% to 78.0%) without changing its weights, while training it to copy a smarter model actually made it worse.
- **The Winning Moves:**
  - **Harness-first design:** Treat the prompts, tools, action steps, and memory limits as the main product, keeping the model as a simple part to swap.
  - **Fit-test every model swap:** Test any new model inside your current harness to stop a stronger model from breaking a tuned system.
  - **On-policy correction:** Fix the model's own bad choices instead of training it to copy a teacher.
  - **Protocol-enforced boundaries:** Share tools through standards like MCP so access rules live outside the agent's thinking.
- **The Fine Print:** This is a single-lab paper from a vendor selling the exact solution, and the unified product does not launch until 2028.

## Sources
[1] Salesforce research — "Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails" (arXiv:2609.09134, September 2026). https://arxiv.org/abs/2609.09134
[2] Salesforce press release — "Salesforce Introduces the Trusted Enterprise AI Harness" (September 11, 2026). https://www.salesforce.com/ap/news/press-releases/2026/09/11/salesforce-introduces-the-trusted-enterprise-ai-harness
[3] Salesforce news — "Expanding Headless 360: Enterprise Capabilities" (August 19, 2026). https://www.salesforce.com/news/stories/expanding-headless-360-enterprise-capabilities
[4] Salesforce news — "Salesforce and Google Cloud Unify Infrastructure and Agents for One Connected AI Stack" (September 15, 2026). https://www.salesforce.com/news/stories/salesforce-google-cloud-unify-infrastructure-and-agents
[5] Salesforce news — "AWS and Salesforce Put CRM Data, AI Agents, and Model Choice Into the Tools Teams Use Every Day" (September 15, 2026). https://www.salesforce.com/news/stories/aws-salesforce-enterprise-ai-expansion/
[6] The Letter Two — "Salesforce's Trusted Enterprise AI Harness, Explained" (September 10, 2026). https://thelettertwo.com/2026/09/10/salesforce-trusted-enterprise-ai-harness-dreamforce-2026

<!-- linkedin -->
Salesforce researchers just proved what many agent builders suspected: the harness beats the model.

They built a new shell around a small Qwen model—updating the system prompt, tools, action steps, and memory limits—without changing its core math. Task success jumped from 29.2% to 78.0% across seven tests.

Then came the twist. They trained that model to copy a smarter one, and success fell to 63.1%. A stronger model inside a shell built for an old one can break the whole system. They call this losing "model-harness fit."

The fix that worked (79.7%)? Fixing the model's own bad choices, not copying a teacher.

Salesforce is turning this into a product right away as its Enterprise AI Harness. They use the Model Context Protocol (MCP) to share tools with agents like Claude and Gemini.

The lesson for anyone building agents: your real power lives in the strict rules around the model. Model swaps are never a free win—always test the new model inside your harness first.

## Gate report
lead: PASS — Delivers the 48-point jump stat in the first sentence using plain English, with zero throat-clearing.
tension: PASS — Frames the shift clearly with "The big picture", expands all acronyms (AWS, MCP, AI), uses simple vocabulary to boost readability, and includes a strict 4-bullet "By the numbers" section.
tactical-insight: PASS — Translates research into actionable practitioner moves with bold lead-ins under "The playbook" signpost, keeping bullets concise.
nuanced-takeaway: PASS — Highlights vendor bias and future release dates clearly under "The catch", split into short paragraphs for scannability.
tldr: PASS — Follows the exact 3-part At a Glance schema with indented sub-bullets and plain-English definitions.
