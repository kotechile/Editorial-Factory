---
title: "Where the Prompt Breaks Decides the AI Bill"
vertical: enterprise_ai_finops
persona: enterprise_cai
one_big_thing: "The cache boundary — where the static prefix ends — sets most of an agent's input bill: pin the reusable head, push dynamic content to the tail, and the cached read rate is earnable; a single changing token ahead of the boundary forfeits it entirely."
date: 2026-10-08
slug: cache-boundary-decides-input-bill
archetype: evergreen
evergreen: true
---

<!-- lead -->
A research team ran the same agent workload through OpenAI, Anthropic and Google and found that prompt caching cut its application programming interface (API) costs by 41% to 80% [1]. The saving did not come from shopping for the cheapest model. It came from where the static part of the prompt ended — and most teams never decide that on purpose.

<!-- tension -->

## The big picture:

A large language model (LLM) does not re-read a prompt from scratch every time, as long as the start of the prompt never changes. Providers store the computed state behind a repeated prefix, then bill a fraction of the input price whenever that prefix is reused [2][3][4]. That is what prompt caching means, and it is not free: writing the prefix to the cache carries a premium, and only the reuse earns it back.

The economics turn on one design choice. The static head — system instructions, tool definitions, reference documents — is the only part a cache can hold.

Anything dynamic, such as a timestamp, a session code or a fresh question, has to sit after that boundary. Put a live value at the front and the cache misses on every call, at full price.

I have been watching how quietly this moves the bill. My read: providers have turned prompt layout from a style preference into a line item, and most budgets never model it.

## By the numbers

- **41% to 80% — Cached cost cut:** Across OpenAI, Anthropic and Google, prompt caching cut API cost by 41% to 80% over 500-plus agent sessions with 10,000-token system prompts [1].
- **13% to 31% — Faster first token:** The same benchmark measured a shorter wait before the answer starts, because reused input skips fresh processing [1].
- **1.25× write, 0.1× read — The cache spread:** Anthropic bills a five-minute cache write at 1.25 times the base input price and a read at 0.1 times; OpenAI uses the same 1.25× write and 0.1× read [2][3].
- **1.35× vs 2× — Break-even:** OpenAI's own math: writing a prefix once and reusing it once costs 1.35× ordinary input, against 2× for processing it twice with no cache [3].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that the fix is mostly free — it costs a refactor, not a new contract — so the open question is which habit a team adopts first.

- **A frozen head:** The measured recipe is to pin system instructions and tool schemas at the front and push dynamic content — timestamps, session codes, retrieved results — to the very end [1].
- **Time-to-live matching:** A five-minute write costs 1.25× but a one-hour write costs 2×, so a prefix reused only now and then is not worth the longer window [2].
- **Hit-rate tracking:** OpenAI tells builders to divide cached tokens by total input tokens and watch the ratio; a prefix that never hits the cache shows up as wasted spend [3].

What I'd watch next is whether cache layout earns its own review step, the way a schema change already does.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is the gap between the ceiling and the floor. The headline numbers are each vendor's best case. OpenAI advertises cached input "discounted up to 95%," and Google's implicit caching gives a 90% discount on cached tokens — but only 75% on its older Gemini 2.0 models [3][4].

Caching is also brittle by design. A prefix that is only mostly stable is not half as good; it is close to useless, because one changing token ahead of the boundary forces a fresh write every time. OpenAI's own example is blunt: a prefix reused just once already beats no caching (1.35× against 2×), but a prefix that rarely repeats keeps paying the write premium for nothing [3].

The discount is also never the whole bill. Cached input is cheaper; the output tokens, which are the expensive ones, are not cached at all. My read: caching lowers the floor on the part of the bill teams were already watching, and does nothing for the part that grows with every agent step.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Prompt caching can cut an agent's input cost by 41% to 80%, but only if the static part of the prompt stays static and dynamic content sits after the boundary.
- **Why It Matters:** The cache boundary, not the model choice, now sets most of the input bill — and one changing token at the front can erase the entire discount.
- **What I'd Watch:** How teams manage the cache boundary before they negotiate on price.
  - **A frozen head:** Pinning system instructions and tool schemas at the front so the reusable prefix never changes.
  - **Time-to-live matching:** Choosing the cache window that fits how often a prefix repeats, since longer windows cost more to write.
  - **Hit-rate tracking:** Measuring cached tokens against total input tokens to see which prefixes actually earn their keep.
- **The Catch:** Discounts are vendor ceilings, not floors, and only input is cached — the output tokens that drive agent cost are not.

## Sources
[1] Lumer et al., "Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks" (arXiv:2601.06007, Jan 2026) — prompt caching reduced API costs by 41% to 80% and time to first token by 13% to 31% across OpenAI, Anthropic and Google over 500-plus agent sessions with 10,000-token system prompts; placing dynamic content at the end of the system prompt gave more consistent benefits (https://arxiv.org/abs/2601.06007)
[2] Anthropic, "Prompt caching" (Claude documentation) — a five-minute cache write costs 1.25 times the base input token price, a one-hour write 2 times, and a cache read 0.1 times (https://docs.claude.com/en/docs/build-with-claude/prompt-caching)
[3] OpenAI, "Prompt caching" (platform documentation) — cache writes cost 1.25× the uncached input rate and reads 0.1× (0.05× on GPT-6.1 Sol); cached input discounted up to 95%; one write plus one reuse costs 1.35× ordinary input against 2× uncached (https://platform.openai.com/docs/guides/prompt-caching)
[4] Google Cloud, "Context caching overview" (Vertex AI / Gemini Enterprise) — implicit caching is on by default and gives a 90% discount on cached tokens, 75% on Gemini 2.0 models (https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview)

## Gate report
lead: pending
tension: pending
tactical-insight: pending
nuanced-takeaway: pending
tldr: pending
