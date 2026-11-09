---
title: "92% Trap: Your Index Is a Copy"
vertical: enterprise_ai_governance
kind: evergreen
archetype: evergreen
evergreen: true
persona: enterprise_cai
one_big_thing: "A retrieval index is a second copy of the corpus, not a filtered view of it — a chunk's embedding inverts back to 92% of a 32-token input, five injected documents steer 90% of answers, and the vector stores themselves tier isolation from a field filter to a dedicated shard — so how many indexes an enterprise runs is the access boundary, and a check that runs after retrieval is decoration."
date: 2026-11-09
slug: your-index-is-the-boundary
meta_title: "92% Trap: Your Index Is a Copy"
meta_description: "An embedding is not a fingerprint: 92% of a 32-token chunk comes back from its vector alone, so the index, not the query filter, is the access boundary."
---

<!-- lead -->
A chunk is one passage cut from a document before indexing. Its embedding — a list of numbers that stands for the passage — is what the store searches, and it is also what an attacker can read back. Give that list to an inversion model, and 92% of a 32-token chunk comes back exactly as it was written [1]. So the index is a second copy of your corpus, held in a store that most access reviews never visit. The governance question is not which filter to put on the query. It is how many indexes the enterprise will run, and who may read each one.

<!-- tldr -->

## At a glance

- **The shift:** Retrieval access is moving from a query filter to an index boundary.
- **The number:** 92% of a 32-token chunk, rebuilt from its embedding alone [1].
- **The risk:** A filter after retrieval has already passed the chunk to the re-scoring service and the log.

<!-- tension -->

## Where the copy gets made

A retrieval system does four things in order, and the order is the problem. At ingest it cuts each document into chunks, turns them into vectors and writes the text, the vector and some fields into the store. At query time it embeds the question and asks for the closest vectors, which come back as chunks before any access rule has run. The application then filters the results and keeps the passages its caller may read. By then the wrong chunk has left the store, been re-scored by a second model, cached, and written into a trace.

My read is that most attribute-based access control (ABAC) programmes spend their effort on the query. But the attribute that decides the answer sits on the chunk: its source document, that document's classification, and who the source system says may read it. A store that carries none of those three fields cannot enforce anything at query time. It can only return candidates, and trust the application to drop the right ones.

The same index is also a write target, and that turns the boundary into a spending decision. A published attack wrote five malicious documents per target question into a knowledge base of millions, and steered 90% of answers to the response it chose [2]. Its authors tested paraphrasing, duplicate filtering and other defences, and none held [2]. A poisoned document's reach is the set of queries that share its index, not a property of the document. Isolation is what turns one bad document into one bad answer instead of one bad company.

## By the numbers

- **90% of answers:** The share an attacker steered after writing five documents per target question into a large store [2].
- **18,000 tenants a node:** The active-tenant density Weaviate reports for a nine-node test cluster [4].
- **1,000 collections:** The default ceiling Qdrant Cloud sets on one collection per tenant [3].

<!-- tactical-insight -->

## How the stores themselves tier it

The vendors have already priced the trade-off, so the choice shows up as a cost per tenant that a CFO can compare. Qdrant's docs set out three rungs. The first splits by a field where tenants are many and small. The second gives a tenant its own shard where tenants are fewer and larger. A tenant moves to its own shard at roughly 20,000 points [3]. Weaviate is blunter, because a tenant is a shard: its docs report a nine-node cluster holding around 170,000 active tenants, and it moves idle tenants to object storage so the per-node file limit stops applying [4].

What I watch is where teams put the classification attribute. A team that copies it from the source system at ingest gets a boundary it can audit, because the chunk and its parent document then share one permission record. A team that rebuilds permissions at query time runs a second, weaker copy of the access model. The two drift apart at the first reorg, when a folder moves and the index never hears about it.

<!-- nuanced-takeaway -->

## The catch

Isolation is not free, and the vendors say so more plainly than most buyers expect. Qdrant warns that many collections "can quickly become expensive", and recommends them only for a limited set of tenants that need strict isolation [3]. The same page sets a default cap on collections and advises against too many dedicated shards [3]. A platform serving tens of thousands of customers will never run one index per customer, which is why the tiered ladder exists at all.

The harder limit is identity. A partition only excludes a caller the store can tell apart, so an agent with one credential that reaches every partition has the reach it had before the split. My sense is that the boundary and the credential have to be settled together. The version that survives an audit is the pair: a narrow identity asking a partitioned store for what it may see, with the check done before retrieval rather than after. The check that runs afterwards is the one [a safety measure scored on the wrong channel](/silent-leak-bypasses-your-filter/) has already been shown to miss what matters most.

## Sources

- [1] Jack Morris and Alexander M. Kuleshov, "Text Embeddings Reveal (Almost) As Much As Text" (arXiv:2310.06816v1, October 2023) — https://arxiv.org/html/2310.06816v1
- [2] Wei Zou, Runpeng Geng, Binghui Wang and Jinyuan Jia, "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models" (arXiv:2402.07867v3, August 2024) — https://arxiv.org/html/2402.07867v3
- [3] Qdrant documentation, "Multiple vectors, multitenancy" — https://qdrant.tech/documentation/guides/multiple-partitions/
- [4] Weaviate documentation, "Data" concepts, multi-tenancy — https://weaviate.io/developers/weaviate/concepts/data
