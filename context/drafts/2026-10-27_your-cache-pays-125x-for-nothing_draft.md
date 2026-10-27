---
title: "Your Cache Pays 1.25x for Nothing"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A prompt-cache mistake is a silent fault at a call site, decidable against the provider's offered feature on a date, and invisible to both the trace and the bill."
date: 2026-10-27
slug: your-cache-pays-125x-for-nothing
---

<!-- lead -->
Your agent's cache pays 1.25 times the input price to write a prefix for five minutes, and a tenth of that price to read it back [2][3]. Nothing in your stack complains when the read never comes. Zhang and colleagues read 120 prompt-caching pull requests across 10 open-source agent systems and found that most of the mistakes fail silently, with no error and no slowdown to spot [1]. The fault sits at the call site, which is the one place a normal trace never looks, and two of the field fixes that followed landed in Anthropic's own software development kit (SDK) [1].

<!-- tension -->

## The big picture:

Prompt caching stores the work behind a repeated prefix, then bills a small share of the input price when that prefix comes back unchanged. The write costs extra and only the reuse pays it back. So the whole plan rests on a call site doing two things right: sending the same stable head in the same order, and reading back what it wrote [2][3].

That is a deal with one vendor's interface on one day, and those interfaces move. Anthropic's own page states a silent path: a request smaller than the shortest prompt it will cache is handled without caching, and no error comes back [2]. OpenAI answers with tools instead, a dashboard for cache hit rates and a checker for misses [3]. Neither sentence says your set-up is right. They say a wrong one will not call attention to itself.

The 120 pull requests fall into two families: a request-side mistake, where the marked prefix is not the prefix that ships, and a read-side counting mistake, where the report names the wrong tokens [1]. The second family hides a trap in the vendor's own docs. Anthropic's input_tokens field covers only the tokens after the last marked point, so a team that adds up that field alone is not measuring what it sent; the true total is read tokens plus written tokens plus that tail [2].

I keep coming back to how ordinary this looks from the outside. The sums for where a prefix breaks are already laid out in [Where the Prompt Breaks Decides the AI Bill](/cache-boundary-decides-input-bill/). What is new this week is proof that the set-up around that boundary is often wrong, and that a green run, a flat latency chart and a believable bill all sit beside it.

## By the numbers

- **120 pull requests — Study sample:** 120 caching pull requests from 10 widely used open-source agent systems, the first study of cache mistakes in real applications [1].
- **0.71 and 0.78 — Checker rate:** Precision and recall on the 120 labelled mistakes, before the checker was pointed at unseen code [1].
- **32 in 571 — Field finds:** 32 mistakes across 571 agent projects at 0.86 precision, which drew 21 developer confirmations and 18 fixes upstream, one of them in Anthropic's official kit [1].
- **1.25× write, 0.1× read — The gap:** Anthropic's rates for a five-minute write and for a cache read, read from its price table on 2026-10-27; OpenAI quotes the same read rate against a 1.25× write for thirty minutes [2][3].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is that the people closest to this stopped trying to catch it downstream. They moved the check to the site and gave it a date, because what a caching call depends on is what the vendor offered on a given day, not what the code says today.

- **Conditions per site:** The checker treats each mistake as a call site plus the conditions correct caching needs there; it finds the sites with CodeQL, then settles each condition against a dated record of what the vendor supported, or a model check [1].
- **Three counters:** Read tokens, written tokens and the tail after the last marked point together describe the request; the last one alone understates it [2].
- **Cost per case:** promptfoo's 0.124.1 release lets an assertion record cost without a threshold, so a suite can carry spend per case instead of one total at the end [5].
- **Quality at the same grain:** A study of a deployed system across five call sites found that routing each site to its best local model reached 91.8% against 95.4% at no per-call cost [4]. Hosting only the two text-generating sites matched hosting everything, 39 of 43 cases, for 28% of the spend, and the pooled accuracy hid one small model acting on 87.2% of requests for devices the site did not own [4].

I would want to see whether cache checks end up in the same review step as the prompt layout, or stay a speed ticket nobody reopens.

<!-- nuanced-takeaway -->

## The catch

The vendor surface is better than "nothing tells you" implies. OpenAI ships a hit-rate dashboard and a miss checker, so a team on one vendor with steady traffic can see a cache that never hits [3]. What those tools cannot say is whether the conditions at one site still hold after an interface changes.

The checker's own numbers keep it honest. At 0.71 precision, about three flags in ten are not faults, and the 0.86 field figure comes from 32 finds in 571 projects rather than a full count [1]. The sample is 10 popular systems, picked because they had caching pull requests to read, so the rate describes the projects that tried, not the wider field [1].

My read is that the 25% premium is the smaller number here. A write that is never read costs 1.25 times the uncached price for those tokens, which is a sum on the published rates, not a measured result. The bigger number is one nobody can put on a slide: the fixes that landed upstream were found by reading code, not by watching a graph.

One more caveat travels with every figure above. Vendor rates sit on pages with no date, so they carry a 2026-10-27 stamp here and should never be read as a contract [2][3].

<!-- tldr -->

## At a glance

- **The Big Shift:** A study of 120 caching pull requests across 10 open-source agent systems found that most cache mistakes fail silently, and a site-level check found 32 more across 571 projects [1].
- **Why It Matters:** Caching bills extra for the write and a tenth for the read, so a site that writes and never reads pays more than if it had never cached, while its traces, latency and alerts all look normal [1][2][3].
- **What I'd Watch:** Whether the cache check joins the same review as the prompt layout, and whether it runs at the site rather than on the invoice.
  - **Conditions per site:** The needs of one caching call at one spot, checked against what the provider supported on a date, which is what the authors' CodeQL checker does [1].
  - **Three counters:** Read tokens, written tokens and the tail after the last marked point, which together describe the request and which one field alone cannot [2].
  - **Cost per case:** Recording spend on each eval case rather than at the end of the run, now possible in promptfoo's assertions [5].
- **The Catch:** The checker's 0.71 precision means three flags in ten miss, the field proof is 32 finds rather than a full count, and the provider dashboards already show a hit rate, just not whether a site's conditions still hold [1][3].

## Sources
[1] Zhang et al., "Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents" (arXiv:2610.34817, 2026-10-26) — 120 prompt-caching pull requests from 10 open-source agent systems; request-side misconfiguration and read-side usage miscount; most mis-integrations fail silently; checker at 0.71 precision and 0.78 recall on the labelled set; 32 mis-integrations across 571 projects at 0.86 precision; 21 developer confirmations and 18 upstream fixes including one in Anthropic's official SDK (https://arxiv.org/abs/2610.34817)
[2] Anthropic, "Prompt caching" (Claude documentation, read 2026-10-27) — five-minute cache writes at 1.25 times and one-hour writes at 2 times the base input price, cache reads at 0.1 times (0.05 times on Opus 5.5 and Sonnet 5.5); input_tokens covers only tokens after the last breakpoint, so total input is cache_read plus cache_creation plus input; requests under the minimum cacheable length are processed without caching and no error is returned (https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
[3] OpenAI, "Prompt caching" (platform documentation, read 2026-10-27) — cached input discounted up to 95%; cache read charge 0.1 times uncached input (0.05 times on GPT-6.1 Sol and Terra); cache write charge 1.25 times for a 30-minute lifetime and 2.5 times for 12 hours; one write plus one full reuse costs 1.35 times ordinary input against 2 times for processing twice; Prompt Caching Dashboard for cache read hit rates and Prompt Cache Diagnostics for misses (https://platform.openai.com/docs/guides/prompt-caching)
[4] Kasnesis et al., "Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Language Models in a Deployed Agentic Home-Automation System" (arXiv:2610.09021, 2026-10-06) — 9 models from 0.8B to a frontier hosted model across 5 call sites, 280 cases and 2,520 scored calls; routing each site to its best local model reaches 91.8% against 95.4% at no per-call cost; hosting only the two generative sites matches hosting everything (39/43 against 39/43) for 28% of the spend; aggregate accuracy hides an actuation safety failure, with one model actuating on 87.2% of requests for devices the site does not own (https://arxiv.org/abs/2610.09021)
[5] promptfoo, release 0.124.1 (2026-10-08) — assertions record cost without a threshold; the provider catalog exposes text-token pricing (https://github.com/promptfoo/promptfoo/releases/tag/0.124.1)
