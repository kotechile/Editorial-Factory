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
Anthropic's own retrieval test missed the right passage 5.7% of the time when it fetched the 20 best-matching chunks. Add document context to every chunk, then rank the results a second time with a separate model, and the miss rate fell to 1.9% — a 67% cut [1].

The corpus did not change. The question set did not change. What changed was the shape of the lookup.

<!-- tension -->

## The big picture:

Most teams treat the memory tier as a purchase, when the numbers that decide it sit in the query.

I keep coming back to how lopsided the levers are. The step that cut the miss rate hardest was not a new embedding model. It was a rerank pass: fetch 150 candidates, score them again, keep 20 [1].

The reason is structural. A short chunk carries its own words but not the document around them, so an embedding built from that chunk cannot tell a quarterly total from an annual one [1]. Rewriting each chunk to name its source document fixes that before any search runs.

Independent work from Chroma puts a number on the boundary itself. Recall moved by up to 9% across chunking strategies, and the 800-token sizing that Chroma reports as OpenAI's documented default scored near the bottom of the table [2].

So there are three rungs, and they are not interchangeable: how the text was cut, how many candidates you ask for, and whether a second model reorders them.

## By the numbers

- **5.7% to 1.9% — Miss rate after reranking:** The top-20 failure rate on Anthropic's corpus, after contextual chunks and a reranker. Contextual chunks alone reached 3.7% [1].
- **150 to 20 — Candidates kept:** The documented pipeline pulls 150 candidates, reranks them, and passes only 20 chunks into the prompt [1].
- **85.4% against 89.5% — Recall by chunk size:** Recall for 800-token chunks with 400-token overlap, against 400-token chunks with no overlap, on the same embedding model [2].
- **7.44% against 1.06% — Embedding model gain:** Average score gain from a larger embedding model, against 1.06% for a smaller swap. The model out-swung every chunking choice tested [3].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are spending their budget in a fixed order, and it is not the order the tooling suggests.

- **The vendor default is the wrong start.** The 800-token chunk with 400 tokens of overlap that Chroma reports as OpenAI's documented default scored 85.4% recall — below average in the report — and the lowest scores on its other metrics [2]. The 400-token split with no overlap scored 89.5% [2].
- **Reranking carries the last leg.** Reranked contextual chunks reached 1.9%, against 2.9% for contextual chunks without a rerank [1]. That gap is one extra model call per query, paid in latency.
- **Small corpora skip the funnel entirely.** Below 200,000 tokens — about 500 pages — the post's own advice is to put the whole corpus in the prompt and skip retrieval [1]. That threshold is the first thing I would want answered before any index gets built.
- **Semantic chunking has to earn its compute.** A three-task study found its gains context-dependent, and fixed-size splitting often won on realistic documents [3].

<!-- nuanced-takeaway -->

## The catch

My read is that the funnel is real but narrower than the framing suggests.

The headline ladder is vendor-reported. Anthropic ran its own benchmark on its own corpus, so 5.7% to 1.9% describes one knowledge base and one question set [1]. Chroma's 85.4% against 89.5% comes from a token-level test with one embedding model and five retrieved chunks [2].

The studies also measure retrieval, not finished tasks. A passage that is found still has to be used well, and none of these numbers says how much a lower miss rate is worth at the end of the chain.

There is a counter-signal worth keeping in view. In the three-task study, embedding quality often outweighed the chunking decision [3], which is why the model swap sits first in the order above and the chunk boundary second.

The funnel also has a floor. Contextualising every chunk costs one model call per chunk at build time, and reranking costs one per query at run time [1].

<!-- tldr -->

## At a glance

- **The Big Shift:** An agent's semantic memory is queried through a funnel — chunk boundary, candidate count, rerank pass — and the funnel moves the miss rate more than a like-for-like model upgrade [1][2][3].
- **Why It Matters:** A missed passage is an answer the model never gets to give, and the fix is a query shape inside the runtime, not a new database.
- **What I'd Watch:** Where the funnel gets configured as teams build memory tiers.
  - **A 400-token split:** Smaller chunks with no overlap beat the 800-token default on recall in Chroma's table [2].
  - **A rerank step:** A second model that reorders the top candidates, which carried the last leg from 2.9% to 1.9% [1].
  - **A 200,000-token floor:** The corpus size under which retrieval is not worth running at all [1].
- **The Catch:** The headline ladder is vendor-reported on one corpus, the studies score retrieval rather than finished tasks, and contextual chunks and reranking both add cost at build time and at query time [1][2][3].

## Sources

[1] Anthropic (Engineering). "Introducing Contextual Retrieval." Published 19 September 2024, read 22 October 2026. https://www.anthropic.com/news/contextual-retrieval

[2] Smith, B. and Troynikov, A. "Evaluating Chunking Strategies for Retrieval." Chroma Technical Report, 3 July 2024, read 22 October 2026. https://research.trychroma.com/evaluating-chunking

[3] Qu, R., Bao, F. and Tu, R. "Is Semantic Chunking Worth the Computational Cost?" arXiv:2410.13070v1, 2024, read 22 October 2026. https://arxiv.org/html/2410.13070v1
