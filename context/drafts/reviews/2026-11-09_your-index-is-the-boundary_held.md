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
A chunk is one passage cut from a document before indexing. Its embedding — the list of numbers a vector store searches — can be read back. An inversion model rebuilt 92% of a 32-token chunk exactly from the embedding alone [1]. That makes the index a second copy of the corpus, held in a store most access reviews never visit. The governance question is not which query filter to apply. It is how many indexes the enterprise runs, and who may read each one.

<!-- tldr -->
## At a glance

- **The shift:** The index is the access boundary, not the query filter.
- **The number:** 92% of a 32-token chunk, rebuilt exactly from its embedding alone [1].
- **The risk:** A filter after retrieval has already released the chunk from the store.

<!-- tension -->
## The big picture:

A retrieval system does four things in order, and the order is the problem. It chunks each document, embeds those chunks, writes the text and vectors into the store, and at query time asks for the nearest vectors. The nearest chunks come back before any access rule has run. The application then filters them and keeps the passages the caller may read. By then the wrong chunk has left the store, been re-scored, cached, and written into a trace.

I checked the inversion paper twice because the number looked too clean: the 92% figure is scoped to 32-token chunks, not whole documents [1]. The same paper recovered full names from clinical notes, so the leak is not a synthetic-text quirk [1]. A chunk that leaves the store before access control has already crossed the boundary the query filter was meant to protect.

The same index is also a write target. A published attack assumed an attacker who could write five malicious documents per target question into a knowledge base of millions [2]. The attack steered 90% of answers to the response it chose [2]. Its authors tested several defences, and none held [2]. A poisoned document's reach is the set of queries that share its index. Isolation turns one bad document into one bad answer instead of one bad company.

## By the numbers

- **18,000 tenants a node:** active-tenant density Weaviate reports for a nine-node test cluster [4].
- **1,000 collections:** default cap Qdrant Cloud sets per cluster [3].

<!-- tactical-insight -->
## What I'd watch:

The vendors have priced the trade-off, so the choice shows up as a cost per tenant that a finance lead can compare. Qdrant's docs set out three rungs: split by a field where tenants are many and small; give a tenant its own shard, a slice of the index, where tenants are fewer and larger; promote at roughly 20,000 points [3]. Weaviate is blunter because a tenant is a shard. Its docs report a nine-node cluster holding around 170,000 active tenants, and it moves idle tenants to object storage so the open-file-per-process limit stops applying [4].

What I watch is where teams put the classification attribute. A team that copies it from the source system at ingest gets a boundary it can audit, because the chunk and its parent document share one permission record. A team that rebuilds permissions at query time runs a second, weaker copy of the access model. The two drift apart at the first reorganisation, when a folder moves and the index never hears about it.

<!-- nuanced-takeaway -->
## The catch

Isolation is not free, and the vendor docs say the trade-off out loud. Qdrant warns that many collections "can quickly become expensive", and it recommends them only for a limited set of tenants that need strict isolation [3]. The same page advises against too many dedicated shards [3]. A platform serving many tenants will not run one collection per tenant, which is why the tiered ladder exists.

The harder limit is identity, because a partition can only exclude a caller the store can tell apart. An agent with one credential that reaches every partition keeps the reach it had before the split. I would not buy the split without settling the credential alongside it. The version that survives an audit is the pair: a narrow identity asking a partitioned store for what it may see, with the check done before retrieval rather than after. The check that runs afterwards is too late.

## Sources

- [1] Jack Morris and Alexander M. Kuleshov, "Text Embeddings Reveal (Almost) As Much As Text" (arXiv:2310.06816v1, October 2023) — https://arxiv.org/html/2310.06816v1
- [2] Wei Zou, Runpeng Geng, Binghui Wang and Jinyuan Jia, "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models" (arXiv:2402.07867v3, August 2024) — https://arxiv.org/html/2402.07867v3
- [3] Qdrant documentation, "Multiple vectors, multitenancy" — https://qdrant.tech/documentation/guides/multiple-partitions/
- [4] Weaviate documentation, "Data" concepts, multi-tenancy — https://weaviate.io/developers/weaviate/concepts/data
