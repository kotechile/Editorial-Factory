---
title: Your 200K Prompt's Hidden Rate Cliff
vertical: enterprise_ai_finops
kind: evergreen
archetype: evergreen
persona: enterprise_cai
evergreen: true
one_big_thing: "Context length is a price column, not a capability: crossing a schedule's line reprices every token in the request — twice on Gemini 3.1 Pro's 200K line, five times above Claude Haiku 5.5's 100,000-token step — so the 95th-percentile prompt, not the average, sets what a workflow costs."
date: 2026-11-12
slug: your-200k-prompts-hidden-rate-cliff
meta_title: "Your 200K Prompt's Hidden Rate Cliff"
meta_title_source: "derived_from_title"
meta_description: "One token past a schedule's context line reprices the whole request. On Gemini 3.1 Pro Preview that line sits at 200,000 input tokens, and the input rate…"
meta_description_source: "derived_from_lead"
---

<!-- lead -->

One token past a schedule's context line reprices the whole request [1]. On Gemini 3.1 Pro Preview that line sits at 200,000 input tokens, and the input rate doubles there because the schedule moves the request into a second, dearer column [1]. A context budget is therefore a rate decision, not a quality setting. The number that settles it is the 95th-percentile (p95) prompt length, which most teams have never measured.

<!-- tldr -->

## At a glance

- **The shift:** Context length is its own price column, and crossing it reprices the whole request [1].
- **The number:** $7.20 a million input tokens above Gemini's 200K line, $3.60 below [1].
- **The risk:** Average-prompt budgets leave the tail in the dearer column.

<!-- tension -->

## Where the Split Falls

Google's table for Gemini 3.1 Pro Preview is split into two columns, one for prompts up to 200,000 input tokens and one above [1]. A footnote spells out the result: "If a query input context is longer than 200K tokens, all tokens (input and output) are charged at long context rates" [1]. The row prices input at $3.60 a million below the line and $7.20 above it [1]. Cached input doubles in that same row, from $0.36 to $0.72 [1]. A cached read is the part of a prompt the vendor stores and re-reads at a discount, so even the cheap tokens stop being cheap above the split.

Text output moves less. It goes from $21.60 to $32.40, a step of about one and a half [1]. Anthropic answers the same question in a different way. Claude Haiku 5.5 is priced by prompt length: $0.10 a million input tokens up to 100,000, then $0.50 [2]. Claude 4.6 and later models carry the full one-million-token window at the standard rate, so a 900k-token request bills at the same per-token rate as a 9k-token request [2].

I read the two pages side by side twice before the shape of it settled. A vendor's window size is a capability claim; its line is a price [1]. One schedule puts the line at 200,000 tokens, another puts a steeper one at 100,000 on a single model, and a third sells the long window flat. None of the three explains why its line sits where it does. What they publish is the arithmetic, and that arithmetic does not grow in step with the text a request adds.

The arithmetic is worth doing once. At the Gemini rates, a 200,000-token prompt answered with 5,000 tokens costs $0.828 [1]. The same request at 200,001 tokens costs $1.602, so one more token adds $0.774 [1]. Trimming a 250,000-token prompt to 190,000 removes 24% of the text and 62% of the input bill. That is why the long tail of prompt lengths decides more than the middle does. The saving comes from sending less, not from sending the same amount at a lower rate.

## By the numbers

- **$0.72 a million cached tokens:** Gemini 3.1 Pro's cached-input rate once a prompt passes the 200K line [1].
- **100,000 tokens:** The length where Claude Haiku 5.5's input rate steps up fivefold [2].
- **32K tokens:** The length at which only half of the 17 models in the Ruler benchmark still performed adequately [3].

<!-- tactical-insight -->

## What the Cap Measures

None of the three schedules says where a buyer's own prompt lengths sit, so the useful number has to be built internally [1]. It is the 95th-percentile prompt, not the average, because the tail is what crosses the line. I keep coming back to how cheap that measurement is next to the invoice it explains. One query over the prompt log and a histogram per workflow produce it.

The cache boundary still decides most of an input bill: on a standard schedule, [where the prompt breaks decides the AI bill](/cache-boundary-decides-input-bill/). Above the line that boundary buys a smaller discount, because the cached rate moves with everything else [1].

The schedules also show that a shorter window is not the same purchase as a cheap one [1]. The same workload sent as two calls under the line bills at the standard column. Sent as one long call, it bills at the long-context column, and the two invoices differ by more than the extra text.

A vendor's own documentation points the same way. Anthropic's page notes that the batch discount does not apply to its managed agent sessions, because those sessions are stateful and interactive [2]. A team running long agent histories therefore has fewer levers below the line than a team running documents. What I would watch next is whether the splits move at all [1]. A step at 100,000 tokens costs a vendor less to revisit than a flat million-token window [1]. The promotional windows already printed on the Gemini page show how fast a listed rate can change [1].

<!-- nuanced-takeaway -->

## The Catch

The limits are real, and the first is the one I would test hardest against my own traffic. The measured leg is dated. The Ruler benchmark tested 17 models for a 2024 paper, and half of them fell short of adequate results at 32K tokens [3]. That is an argument for testing a model on your own documents before paying for a long window [3]. It is not evidence that any model shipping now is weak.

Two smaller caveats belong beside it. The answer line is repriced less steeply than input, so a workload with long outputs gets less relief from trimming than its prompt suggests [1]. Most production prompts also sit far below these lines, and a short prompt never meets the split. The cliff is a problem for long documents and long agent histories, not for every call a company makes.

What survives the caveats is narrower and still expensive. The window is a capability, the line is a price, and the default setup — every request carrying everything — is the one that pays the higher column.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "40 kW Line: Why the AI Rack Is a Building Project" -> /rack-power-density-ceiling-build-before-you-buy/ [same site (aichieve.net); same category; topical overlap: line, past] Link "40 kW Line: Why the AI Rack Is a Building Project" in the section where the article touches line, past. -->
<!-- internal-link hint: "Token Prices Hit Record Lows. Enterprise AI Bills Didn't." -> /token-price-record-low-budget-overrun/ [same site (aichieve.net); same category; topical overlap: rate, token] Link "Token Prices Hit Record Lows. Enterprise AI Bills Didn't." in the section where the article touches rate, token. -->
<!-- internal-link hint: "Your Rate Limit's Hidden 100x" -> /your-rate-limit-1-39-a-second/ [same site (aichieve.net); same category; topical overlap: hidden, rate] Link "Your Rate Limit's Hidden 100x" in the section where the article touches hidden, rate. -->
## Related reading

- [40 kW Line: Why the AI Rack Is a Building Project](/rack-power-density-ceiling-build-before-you-buy/)
- [Token Prices Hit Record Lows. Enterprise AI Bills Didn't.](/token-price-record-low-budget-overrun/)
- [Your Rate Limit's Hidden 100x](/your-rate-limit-1-39-a-second/)
<!-- internal-links:end -->

## Sources

- [1] Google Cloud, "Vertex AI generative AI pricing" — long-context footnotes and the Gemini 3.1 Pro Preview row, list prices as of 2026-11-12 — https://cloud.google.com/vertex-ai/generative-ai/pricing
- [2] Anthropic, "Claude API pricing" — long context pricing, prompt caching and batch notes, as of 2026-11-12 — https://docs.claude.com/en/docs/about-claude/pricing
- [3] Hsieh et al., "RULER: What's the Real Context Size of Your Long-Context Language Models?", 2024 — https://arxiv.org/abs/2404.06654
