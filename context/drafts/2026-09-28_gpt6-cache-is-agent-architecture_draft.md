---
title: "The Cache Just Became Your Agent's Contract"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "OpenAI's GPT-6 prompt caching (Sept 22) turns persistent agent context into a managed cost asset — up to 90% off reused input tokens — and makes cache reuse an interface-design rule."
date: 2026-09-28
slug: gpt6-cache-is-agent-architecture
---

<!-- lead -->
On September 22, OpenAI shipped an unglamorous but load-bearing change to its GPT-6 models (the Generative Pre-trained Transformer family): a rebuilt prompt-caching layer that hands builders "discounts of up to 90% on cached input tokens" for agents that "work for hours" on a single task [1]. The discount is the headline. The fine print — a quiet instruction to keep your tool schemas stable or forfeit the savings — is the actual story.

<!-- tension -->
I've been watching how agentic systems are priced all month, and this release marks a shift I keep coming back to: OpenAI is no longer treating the prompt as a disposable request. It's treating it as a managed, versioned asset whose stability now carries a dollar value.

The cost pathology here is well known. A long-running agent re-sends the same instructions, tool definitions, and context on every turn, and every re-send is billed at full price. Prompt caching was always the answer, but GPT-6 changes the contract: the discount only applies to "eligible shared prefixes reused within a 30-minute window," and OpenAI's own guidance tells builders to "keep tool definitions, schemas, and ordering stable so earlier context stays reusable" [1]. In other words, cache economics now reward deterministic interfaces — the exact property the "deterministic RPC boundaries" crowd has been arguing for on reliability grounds alone.

**By the numbers:**
- **Up to 90%:** the discount OpenAI now applies to cached input tokens reused within a 30-minute window [1]
- **Hours:** how long GPT-6 persistent agents are designed to run on a single task — refactoring a codebase or producing a researched document [1]
- **More than 50%:** the cut in prompt tokens needing fresh processing that GitHub reports for Copilot, across billions of requests [2]

<!-- tactical-insight -->
What strikes me here is how quickly this becomes an interface-discipline problem, not a pricing problem. OpenAI shipped three primitives that only make sense if you treat context as a first-class artifact: explicit cache breakpoints (choose which prefixes to reuse), the ability to change reasoning effort without invalidating the cache via a `configuration_update`, and cache prewarming that loads shared context before the first user request [1].

The operators closest to this are already being pushed into specific habits. OpenAI's guidance is to use `allowed_tools` to keep only the relevant tools callable, or set `tool_choice` to none, instead of removing tool definitions — because removing a definition from the middle of the context shatters the prefix and kills the cache [1]. New instructions get appended to the end as developer messages so earlier context stays reusable [1].

What I'd watch next: whether tool schemas start being versioned like API contracts, with cache-aware change management around them. If a schema change silently blows up your cache-hit rate, teams will want the same linting and review discipline for tool definitions that they already apply to wire protocols.

<!-- nuanced-takeaway -->
I could be wrong that this matters as much as I'm implying. The discount only lands if your context is genuinely reusable: if your tool definitions or reasoning effort churn every turn, you miss and pay full freight, and the 30-minute window means an idle agent forfeits the discount entirely [1]. The "more than 50%" Copilot figure is also vendor-reported — it surfaces in a trade write-up attributed to GitHub's chief product officer, not in a retrievable primary GitHub statement [2]. Caching is real savings, but it's savings that have to be architected for, and the headline number is a ceiling, not a floor.

<!-- tldr -->
- **The Big Shift:** OpenAI rebuilt GPT-6's prompt caching so agents that run for hours can reuse shared context at up to 90% off — and made cache reuse depend on keeping tool schemas and instruction ordering stable.
- **Why It Matters:** Persistent agents re-send the same instructions and tool definitions every turn, and that repetition is now the dominant cost lever. Turning context into a cached, versioned asset changes where the architecture decisions — and the money — actually live.
- **What I'd Watch:** whether cache-stability becomes a first-class interface contract for agent builders.
  - **Cache breakpoints:** explicit markers that let a builder choose which prompt prefixes get reused instead of caching everything blindly.
  - **Reasoning-effort changes without cache invalidation:** a way to dial a task's reasoning up or down mid-conversation without destroying the reusable prefix.
  - **Cache prewarming:** loading shared instructions and tool definitions ahead of the first request so the user never waits on them.
- **The Catch:** the discount only pays off when context is genuinely reusable — churn your tools or reasoning each turn and you miss. The 30-minute reuse window and the vendor-reported Copilot figure are both softer than the headline suggests.

## Sources
[1] OpenAI — "Better prompt caching for GPT-6" (Sept 22, 2026) — https://openai.com/index/better-prompt-caching-for-gpt-6
[2] TECHx Media — "OpenAI Improves Prompt Caching for GPT-6 Agents" (Sept 22, 2026) — https://techxmedia.com/en/openai-improves-prompt-caching-for-gpt-6-agents

<!-- linkedin -->
I've been reading the agent-infrastructure announcements all month, and one from September 22 stopped me. OpenAI rebuilt GPT-6's prompt caching to hand builders "discounts of up to 90% on cached input tokens" for agents that "work for hours" — and then slipped in the fine print that turns the feature into a design rule: keep your tool schemas and instruction ordering stable, or the cache misses and you pay full freight.

My read: the prompt stopped being a disposable request and became a managed asset whose stability has a dollar value. Cache reuse now rewards the same deterministic, stable interfaces the reliability crowd has wanted all along — just for money instead of for correctness.

The part I keep circling: three new primitives — cache breakpoints, reasoning-effort changes that don't invalidate the cache, and prewarming — only make sense if you treat context as a first-class artifact, not a bag of tokens.

The catch: the 90% is a ceiling, not a floor. Churn your tools every turn and you miss. And the "more than 50% fewer tokens needing fresh processing" figure GitHub reports for Copilot is vendor-reported via a trade write-up, not a primary statement.

I'm curious how others are handling it: are tool schemas about to get the same versioning and review discipline as API contracts?
