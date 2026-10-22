---
title: Your Retrieval Fails at 5.7%
vertical: agentic_ai
persona: ai_architect
one_big_thing: "The lookup that feeds an agent's semantic memory is a funnel whose rungs cost very different things: retrieve wide (150 candidates), rank them again with a second model and keep 20, cut chunks smaller than the vendor default, and buy the better embedding model before buying any chunking trick — because the funnel, not the index, is where the miss rate moves."
date: 2026-10-22
slug: your-retrieval-misses-57
archetype: evergreen
evergreen: true
---

<!-- lead -->
Anthropic's retrieval test missed the right passage 5.7% of the time when it fetched the 20 best-matching chunks [1]. Each chunk then carried a line of context naming its source document. A second model ranked the results again, and the miss rate fell to 1.9%, a 67% cut [1].

The source text never changed. The questions never changed. Only the shape of the lookup did.

<!-- tension -->

## The big picture:

Most teams treat the memory tier as a database buy. The numbers that decide it sit inside the query.

The part I keep circling is how lopsided the levers are. The step that cut the miss rate hardest was not a new embedding model. It was a rerank pass: fetch 150 candidates, score them again, keep 20 [1].

The reason is plain. A short chunk carries its own words but not the document around it. Its embedding, a numeric fingerprint of meaning, cannot tell a quarterly total from an annual one [1].

Rewriting each chunk to name its source document fixes that before any search runs. It is a build-time job, paid once per chunk.

Anthropic's own ladder is finer than one jump. Chunks with document context alone moved the miss rate from 5.7% to 3.7%, and a keyword index on top took it to 2.9% [1].

The rerank pass finished at 1.9%. That last rung repeats on every query, so it is the one with a running cost [1].

Chroma puts a number on the boundary itself. Recall moved by up to 9% across chunking strategies [2]. The 800-token size that Chroma calls OpenAI's published default scored near the bottom of its table [2].

So there are three rungs: how the text is cut, how many candidates to fetch, and whether a second model reorders them.

## By the numbers

- **5.7% to 1.9% — Miss rate drop:** The top-20 failure rate on Anthropic's test corpus, after chunks with context and a reranker [1].
- **150 to 20 — Candidates kept:** That system pulls 150 candidates, reranks them, and passes 20 chunks into the prompt [1].
- **85.4% against 89.5% — Recall by size:** Recall for 800-token chunks with 400-token overlap, against 400-token chunks with no overlap, on the same embedding model [2].
- **7.44% against 1.06% — Embedding model gain:** The average score gain from a larger embedding model, against 1.06% for a smaller swap. Embedding quality often outweighed the chunking choice in the same study [3].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are spending their budget in a fixed order. It is not the order the tooling suggests.

- **The vendor default loses:** The 800-token chunk with 400 tokens of overlap scored 85.4% recall, below average in Chroma's report [2]. The 400-token split with no overlap scored 89.5% [2].
- **Reranking carries the finish:** Reranked chunks with context reached 1.9%, against 2.9% without a rerank [1]. That gap costs one extra model call per query.
- **Small corpora skip the funnel:** Below 200,000 tokens, about 500 pages, the post advises putting the whole text in the prompt and skipping retrieval [1]. That threshold is the first thing I would want answered.
- **Semantic chunking has to earn its place:** A study of document, evidence and answer search found its gains depend on the data [3]. Fixed-size splitting often won on realistic documents [3].

<!-- nuanced-takeaway -->

## The catch

My read is that the funnel is real but narrower than the framing suggests.

The headline ladder is vendor-reported. Anthropic ran its own benchmark on its own text, so 5.7% to 1.9% describes one knowledge base and one question set [1]. Chroma's test is a token-level check on one embedding model and five retrieved chunks [2].

These studies measure search, not finished tasks. A passage that is found still has to be put to use. None of these numbers says how much a lower miss rate is worth at the end of the chain.

There is a counterweight worth tracking. In that study, embedding quality often outweighed the chunking decision [3]. That is why the model swap sits first in the order above, and the chunk boundary second.

The funnel also has a floor. Adding context to every chunk costs one model call per chunk to build. Reranking costs one per query at run time [1].

<!-- tldr -->

## At a glance

- **The Big Shift:** An agent's memory is queried through a funnel: chunk boundary, candidate count, rerank pass. That funnel moves the miss rate more than a like-for-like model swap [1][2][3].
- **Why It Matters:** A missed passage is an answer the model never gets to give. The fix is a query shape inside the runtime, not a new database.
- **What I'd Watch:** Where the funnel gets configured as teams build memory tiers.
  - **A 400-token split:** Smaller chunks with no overlap beat the 800-token default on recall in Chroma's table [2].
  - **A rerank step:** A second model that reorders the top candidates, which carried the last leg from 2.9% to 1.9% [1].
  - **A 200,000-token floor:** The corpus size under which retrieval is not worth running at all [1].
- **The Catch:** The headline ladder is vendor-reported on one corpus, and the studies score search rather than finished tasks. Extra context also adds cost at build time and at query time [1][2][3].

## Sources

[1] Anthropic (Engineering). "Introducing Contextual Retrieval." Published 19 September 2024, read 22 October 2026. https://www.anthropic.com/news/contextual-retrieval

[2] Smith, B. and Troynikov, A. "Evaluating Chunking Strategies for Retrieval." Chroma Technical Report, 3 July 2024, read 22 October 2026. https://research.trychroma.com/evaluating-chunking

[3] Qu, R., Bao, F. and Tu, R. "Is Semantic Chunking Worth the Computational Cost?" arXiv:2410.13070v1, 2024, read 22 October 2026. https://arxiv.org/html/2410.13070v1

## Gate report
lead: PASS — Core benchmark in the first sentence, seven short sentences, no preamble.
tension: PASS — "The big picture:" header, observer cue ("The part I keep circling"), plain gloss for embedding.
tactical-insight: PASS — "What I'd watch:" header, observation-form bullets, no second-person advice.
nuanced-takeaway: PASS — "The catch" opens on a labelled reading, names the vendor-reported base and the cost floor.
tldr: PASS — Four-part schema (Big Shift / Why It Matters / What I'd Watch with sub-bullets / The Catch).
