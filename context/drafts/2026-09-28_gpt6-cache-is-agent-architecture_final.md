---
title: "The Cache Just Became Your Agent's Contract"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "OpenAI's GPT-6 prompt caching (Sept 22) turns persistent agent context into a managed cost asset — up to 90% off reused input tokens — and makes cache reuse an interface-design rule."
date: 2026-09-28
slug: gpt6-cache-is-agent-architecture
---

<!-- lead -->
On Sept. 22, OpenAI changed how prompt caching works for its Generative Pre-trained Transformer (GPT-6) models. It gives builders up to 90% off reused input tokens for AI agents that run for hours [1]. That huge discount is the headline. The part I keep circling is the fine print: the savings only survive if tool setups stay stable.

<!-- tension -->
## Context Is Now Cash

I've been watching how builders price these agent systems all month, and this update marks a huge shift. OpenAI no longer treats a prompt as a throwaway request. Instead, it treats the prompt as a managed asset where stability saves real money.

**The big picture:** A long-running agent sends the same rules and tool shapes on every turn, and you pay full price each time. GPT-6 changes the math because the discount only applies to matching early text reused within a 30-minute window [1]. OpenAI tells builders to keep tool shapes and order exactly the same so older text stays useful [1]. This rewards fixed, stable setups. That is exactly what the Remote Procedure Call (RPC) crowd has wanted for a long time to keep systems reliable.

**By the numbers:**
- **Up to 90%:** The discount OpenAI applies to cached input tokens reused within a 30-minute window [1].
- **Hours:** How long GPT-6 agents are built to run on single tasks, like fixing code [1].
- **More than 50%:** The drop in prompt tokens needing fresh processing that GitHub reports for Copilot across billions of requests [2].

<!-- tactical-insight -->
## The New Rules of Design

What strikes me here is how fast this turns into a design problem rather than a pricing issue. Teams are already changing their habits to protect their cache hit rates.

Instead of pulling a tool out in the middle of a task—which breaks the cache—builders now use the `allowed_tools` setting or set `tool_choice` to none [1]. They add new rules to the very end of the prompt as developer messages so the early text stays useful [1].

**What I'd watch:** How teams manage tool shapes just like Application Programming Interface (API) contracts.
- **Clear cache breaks:** Builders now pick exactly which parts of a prompt to reuse, rather than saving everything blindly [1].
- **Thinking changes:** Systems can now adjust how hard an agent thinks via a settings change (`configuration_update`) without breaking the saved cache [1].
- **Cache prewarming:** Teams load shared rules before the first user request so nobody has to wait [1].

<!-- nuanced-takeaway -->
**The catch:** The discount only works if your text is truly reusable. If your tools or thinking steps change every turn, you miss the cache and pay full price [1].

My read: this may not change things as fast as it looks. An idle agent loses the discount completely after 30 minutes [1], and the "more than 50%" Copilot stat comes from a news piece quoting GitHub's chief product officer rather than a direct GitHub report [2]. Caching saves real money, but it has to be architected for. The headline number is a ceiling, not a floor.

**Go deeper:**
<!-- internal-links -->

<!-- tldr -->
- **The Big Shift:** OpenAI rebuilt GPT-6's prompt caching so agents that run for hours can reuse shared text at up to 90% off, but only if tool shapes stay stable.
- **Why It Matters:** Agents send the same rules every turn, making that repeat action the biggest cost factor. Turning prompt text into a saved, stable asset changes where the design choices and the money actually live.
- **What I'd Watch:** whether cache stability becomes a strict rule for agent builders.
  - **Clear cache breaks:** Markers that let a builder choose which prompt parts get reused instead of saving everything.
  - **Thinking changes:** A way to dial a task's thinking up or down mid-chat without breaking the saved text.
  - **Cache prewarming:** Loading shared rules and tools before the first request so the user never waits.
- **The Catch:** The discount only pays off when text is truly reusable, and the 30-minute window means idle agents lose the savings completely.

## Sources
[1] OpenAI — "Better prompt caching for GPT-6" (Sept 22, 2026) — https://openai.com/index/better-prompt-caching-for-gpt-6
[2] TECHx Media — "OpenAI Improves Prompt Caching for GPT-6 Agents" (Sept 22, 2026) — https://techxmedia.com/en/openai-improves-prompt-caching-for-gpt-6-agents

<!-- linkedin -->
I've been reading the AI agent news all month, and one update from Sept. 22 stopped me. OpenAI rebuilt prompt caching for its Generative Pre-trained Transformer (GPT-6) models to give builders up to 90% off reused input tokens for agents that work for hours.

But they slipped in a fine print that turns the feature into a strict design rule: keep your tool shapes and order stable, or the cache misses and you pay full price.

My read: the prompt stopped being a throwaway request and became a managed asset where stability has a dollar value. Cache reuse now rewards the same fixed, stable setups the reliability crowd has wanted all along — just for money instead of correctness.

The part I keep circling: three new tools — cache breaks, thinking changes that don't break the cache, and prewarming — only make sense if you treat context as a core asset, not just a bag of words.

The catch: the 90% discount is a ceiling, not a floor. Change your tools every turn and you miss.

I'm curious how others are handling it: are tool shapes about to get the same strict review rules as Application Programming Interface (API) contracts?

## Gate report
lead: PASS — Delivers the core news and 90% discount immediately in the first sentence with clear, simple language.
tension: PASS — Frames the shift with "The big picture:" and includes a mandatory "By the numbers:" section with three bolded stats.
tactical-insight: PASS — Uses "What I'd watch:" to introduce three bolded observations of what operators are doing, replacing complex jargon with plain terms.
nuanced-takeaway: PASS — Opens with "The catch:" and provides honest limitations regarding the 30-minute window and vendor-reported stats using everyday vocabulary.
tldr: PASS — Strictly follows the 4-part Smart Brevity At a Glance schema with plain-English summaries and indented sub-bullets, ensuring broad readability.
