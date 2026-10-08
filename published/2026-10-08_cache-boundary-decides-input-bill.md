---
title: "Where the Prompt Breaks Decides the AI Bill"
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "The cache boundary — where the static prefix ends — sets most of an agent's input bill: pin the reusable head, push dynamic content to the tail, and the cached read rate is earnable; a single changing token ahead of the boundary forfeits it entirely."
date: 2026-10-08
slug: cache-boundary-decides-input-bill
archetype: evergreen
evergreen: true
meta_title: "Where the Prompt Breaks Decides the AI Bill"
meta_title_source: "derived_from_title"
meta_description: "A research team ran the same agent workload through OpenAI, Anthropic, and Google and found that prompt caching cut application programming interface (API)…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/cache-boundary-decides-input-bill/featured.png"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "A matte modular mechanical assembly with a fixed block and an interchangeable cartridge slot on a neutral backdrop."
image_caption: "The cache boundary forces developers to strictly separate static instructions from dynamic inputs."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A research team ran the same agent workload through OpenAI, Anthropic, and Google and found that prompt caching cut application programming interface (API) costs by 41% to 80% [1]. The savings did not come from shopping for the cheapest model. It came from where the static part of the prompt ended — and most teams never make that choice on purpose.

<!-- tension -->

## The big picture:

A large language model (LLM) does not read a prompt from scratch every time, as long as the start of the prompt never changes.

Providers store the computed state behind a repeated prefix, then bill a fraction of the input price whenever that prefix is reused [2][3][4]. That is what prompt caching means, and it is not free. 

Writing the prefix to the cache carries a premium, and only the reuse earns it back. The economics turn on one design choice. 

The static head — system instructions, tool definitions, reference documents — is the only part a cache can hold. Anything dynamic, such as a timestamp, a session code, or a fresh question, has to sit after that boundary. 

Put a live value at the front, and the cache misses on every call at full price.

I have been watching how quietly this moves the bill. My read: Providers have turned prompt layout from a style preference into a line item, and most budgets never model it.

## By the numbers

- **41% to 80% — Cached cost cut:** Prompt caching slashed API costs by 41% to 80% across 500-plus agent sessions with 10,000-token system prompts [1].
- **13% to 31% — Faster first token:** The same benchmark measured a shorter wait before the answer starts, because reused input skips fresh processing [1].
- **1.25× write, 0.1× read — The cache spread:** Anthropic and OpenAI charge 1.25 times the base input price to write a five-minute cache, but only 0.1 times the base price to read it [2][3].
- **1.35× vs. 2× — Break-even:** Writing a prefix once and reusing it once costs 1.35 times the ordinary input price, compared to 2 times for processing it twice with no cache [3].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that the fix is mostly free. It costs a code update, not a new contract, so the open question is which habit a team adopts first.

- **A frozen head:** The measured recipe pins system instructions and tool schemas at the front and pushes dynamic content — timestamps, session codes, retrieved results — to the very end [1].
- **Time-to-live matching:** A five-minute write costs 1.25 times the base rate, but a one-hour write costs twice the base rate [2]. A prefix reused only now and then is not worth the longer window.
- **Hit-rate tracking:** OpenAI tells builders to divide cached tokens by total input tokens and watch the ratio [3]. A prefix that never hits the cache shows up as wasted spend.

What I'd watch next is whether cache layout earns its own review step, the way a database change already does.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is the gap between the ceiling and the floor. The headline numbers are each vendor's absolute best case. 

OpenAI advertises cached input "discounted up to 95%" [3]. Google's automatic caching gives a 90% discount on cached tokens, but only 75% on its older Gemini 2.0 models [4].

Caching is also brittle by design. A prefix that is only mostly stable is close to useless. One changing token ahead of the boundary forces a fresh write every time. 

OpenAI's own example is blunt: A prefix reused just once beats no caching, but a prefix that rarely repeats keeps paying the write premium for nothing [3].

The discount is also never the whole bill. Cached input is cheaper, but the output tokens are not cached at all. My read: Caching lowers the floor on the part of the bill teams were already watching, but does nothing for the part that grows with every agent step.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Token Prices Just Halved. The CFO Still Can’t Read the Bill." -> https://giniloh.com/token-prices-just-halved-the-cfo-still-cant-read-the-bill/ [same site (giniloh.com); same category; topical overlap: anthropic, bill, openai] Link "Token Prices Just Halved. The CFO Still Can’t Read the Bill." in the section where the article touches anthropic, bill, openai. -->
<!-- internal-link hint: "Multi Agent Orchestration" -> https://giniloh.com/multi-agent-orchestration-building-the-one-person-enterprise/ [same site (giniloh.com); same category; topical overlap: agent, team] Link "Multi Agent Orchestration" in the section where the article touches agent, team. -->
<!-- internal-link hint: "OpenAI just made the agent loop a commodity" -> https://giniloh.com/openai-just-made-the-agent-loop-a-commodity/ [same site (giniloh.com); same category; topical overlap: agent, openai] Link "OpenAI just made the agent loop a commodity" in the section where the article touches agent, openai. -->
## Related reading

- [Token Prices Just Halved. The CFO Still Can’t Read the Bill.](https://giniloh.com/token-prices-just-halved-the-cfo-still-cant-read-the-bill/)
- [Multi Agent Orchestration](https://giniloh.com/multi-agent-orchestration-building-the-one-person-enterprise/)
- [OpenAI just made the agent loop a commodity](https://giniloh.com/openai-just-made-the-agent-loop-a-commodity/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Prompt caching can cut an agent's input cost by 41% to 80%, but only if the static part of the prompt stays fixed and dynamic content sits after the boundary.
- **Why It Matters:** The cache boundary, not the model choice, now sets most of the input bill. A single changing token at the front can erase the entire discount.
- **What I'd Watch:** How teams manage the cache boundary before they negotiate on price.
  - **A frozen head:** Pinning system instructions and tool schemas at the front so the reusable prefix never changes.
  - **Time-to-live matching:** Choosing the cache window that fits how often a prefix repeats, since longer windows cost more to write.
  - **Hit-rate tracking:** Measuring cached tokens against total input tokens to see which prefixes actually earn their keep.
- **The Catch:** Discounts are vendor ceilings, not floors, and only input is cached. The output tokens that actually drive agent costs receive no discount.

## Sources
[1] Lumer et al., "Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks" (arXiv:2601.06007, Jan 2026) — prompt caching reduced API costs by 41% to 80% and time to first token by 13% to 31% across OpenAI, Anthropic and Google over 500-plus agent sessions with 10,000-token system prompts; placing dynamic content at the end of the system prompt gave more consistent benefits (https://arxiv.org/abs/2601.06007)
[2] Anthropic, "Prompt caching" (Claude documentation) — a five-minute cache write costs 1.25 times the base input token price, a one-hour write 2 times, and a cache read 0.1 times (https://docs.claude.com/en/docs/build-with-claude/prompt-caching)
[3] OpenAI, "Prompt caching" (platform documentation) — cache writes cost 1.25× the uncached input rate and reads 0.1× (0.05× on GPT-6.1 Sol); cached input discounted up to 95%; one write plus one reuse costs 1.35× ordinary input against 2× uncached (https://platform.openai.com/docs/guides/prompt-caching)
[4] Google Cloud, "Context caching overview" (Vertex AI / Gemini Enterprise) — implicit caching is on by default and gives a 90% discount on cached tokens, 75% on Gemini 2.0 models (https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview)

## Gate report
lead: PASS — Directly states the outcome and the core mechanism (static prompt boundary) without throat-clearing.
tension: PASS — Explains LLM caching simply, maintains short paragraphs, and includes a clear first-person observer cue.
tactical-insight: PASS — Uses actionable observations, avoids imperative commands, and includes a clear first-person cue.
nuanced-takeaway: PASS — Realistically frames vendor ceilings and output token costs with strong first-person framing.
tldr: PASS — Follows the exact 4-part Smart Brevity structure with distinct bullet definitions.
