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
A chunk is one passage cut from a document before indexing. Its embedding — the list of numbers a vector store searches — can be read back as text. An inversion model rebuilt 92% of a 32-token chunk exactly from the embedding alone [1]. So the index is a second copy of the corpus, held in a store most access reviews never visit. The governance question is not which query filter to apply. It is how many indexes the enterprise runs, and who may read each one.

<!-- tldr -->
## At a glance

- **The shift:** The index is the access boundary, not the query filter.
- **The number:** 92% of a 32-token chunk, rebuilt exactly from its embedding alone [1].
- **The risk:** A filter after retrieval has already released the chunk from the store.

<!-- tension -->
## Where the copy gets made

A search system does four things in order, and the order is the problem. It cuts each document into chunks, turns them into vectors, and writes the text and the vectors into a store. At query time it embeds the question and asks for the nearest vectors, which come back as chunks before any access rule has run. The application then filters those results and keeps the passages its caller may read. By then the wrong chunk has left the store, been re-scored by a second model, cached, and written into a trace.

The scope of the inversion result is what I keep coming back to: 92% holds for a 32-token chunk, not for a whole document [1]. That is still enough to recover a name, and the same authors pulled full names out of clinical notes [1]. The rule that decides whether a passage may be read sits on the chunk itself: its source document, what that document is labelled, and who the source system says may read it. A store that carries none of those three fields cannot enforce anything at query time. It can only hand back candidates and trust the application to drop the right ones.

Most attribute-based access control (ABAC) work goes into the query, which is the wrong end of the path. The same index is also a write target, which turns the boundary into a spending decision. A published attack assumed an attacker who could write five malicious documents per target question into a knowledge base of millions [2]. It steered 90% of answers to the response the attacker chose, and the defences its authors tested did not hold [2]. A poisoned document's reach is the set of queries that share its index. Isolation turns one bad document into one bad answer instead of one bad company.

## By the numbers

- **90% of answers:** The share an attacker steered after writing five documents per target question into a large store [2].
- **18,000 tenants a node:** The active-tenant density Weaviate reports for a nine-node test cluster [4].
- **1,000 collections:** The default cap Qdrant Cloud sets per cluster [3].

<!-- tactical-insight -->
## How the vendors tier isolation

The vendors have priced the trade-off, so the choice shows up as a cost per tenant that a finance lead can compare. Qdrant's docs set out three rungs. Split by a field where tenants are many and small, give a tenant its own shard where tenants are fewer and larger, and promote a tenant at roughly 20,000 points [3]. Weaviate is blunter, because a tenant is a shard: its docs report a nine-node cluster holding around 170,000 active tenants, and idle tenants move to object storage so the open-file-per-process limit stops applying [4].

The tiered design carries a limit of its own. Tenants on the first rung are separated by a filter rather than by a physical boundary, so the classification field has to be right for every small tenant even when the large ones are walled off. Where I watch is how teams populate that field. A team that copies it from the source system at ingest gets a boundary it can audit, because the chunk and its parent document share one permission record. A team that rebuilds permissions at query time runs a second, weaker copy of the access model. The two drift apart at the first reorg, when a folder moves and the index never hears about it.

<!-- nuanced-takeaway -->
## The catch

Isolation is not free, and the vendor docs say it plainly. Qdrant warns that many collections "can quickly become expensive", and recommends them only for a limited set of tenants that need strict isolation [3]. The same page also caps how many dedicated shards a cluster may carry [3]. Few platforms run one collection per customer. That is why the tiered ladder exists at all.

The harder limit is identity, because a split can only exclude a caller the store can tell apart. An agent holding one key that reaches every split keeps the reach it had before the change. I would not buy the split without settling the credential beside it. The version that survives an audit is the pair: a narrow identity asking a partitioned store for what it may see, with the check done before retrieval rather than after. The check that runs afterwards is too late, and [a security metric scored on the wrong channel](/silent-leak-bypasses-your-filter/) has already shown how much it misses.

## Sources

- [1] Jack Morris and Alexander M. Kuleshov, "Text Embeddings Reveal (Almost) As Much As Text" (arXiv:2310.06816v1, October 2023) — https://arxiv.org/html/2310.06816v1
- [2] Wei Zou, Runpeng Geng, Binghui Wang and Jinyuan Jia, "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models" (arXiv:2402.07867v3, August 2024) — https://arxiv.org/html/2402.07867v3
- [3] Qdrant documentation, "Multiple vectors, multitenancy" — https://qdrant.tech/documentation/guides/multiple-partitions/
- [4] Weaviate documentation, "Data" concepts, multi-tenancy — https://weaviate.io/developers/weaviate/concepts/data
