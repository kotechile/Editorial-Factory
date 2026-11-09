# Verified Brief: enterprise_ai_governance — 2026-11-09 (evergreen)

Archetype: evergreen. Source of record: `context/recon_proposals/2026-11-09_enterprise_ai_governance_evergreen_brief.md`
(evergreen gate PASS, rows=5 verified=5 hosts=arxiv.org, qdrant.tech, weaviate.io).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | retrieval store | An embedding can be inverted back to its text: a multi-step method recovers 92% of 32-token inputs exactly | VERIFIED | https://arxiv.org/html/2310.06816v1 | "a multi-step method that iteratively corrects and re-embeds text is able to recover 92 % … of 32-token text inputs exactly" |
| 2 | retrieval store | The same work recovers personal information (full names) from clinical notes, so the inversion is not limited to synthetic text | VERIFIED | https://arxiv.org/html/2310.06816v1 | "our model can recover important personal information (full names) from a dataset of clinical notes" |
| 3 | write path | Poisoned documents steer answers: 90% attack success with five malicious texts per target question in a database of millions | VERIFIED | https://arxiv.org/html/2402.07867v3 | "Our results show PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts" |
| 4 | write path | The paper's tested defences did not hold | VERIFIED | https://arxiv.org/html/2402.07867v3 | "We also evaluate several defenses and our results show they are insufficient to defend against PoisonedRAG" |
| 5 | isolation cost | Qdrant Cloud caps a cluster at 1,000 collections by default, and collections are expensive to create | VERIFIED | https://qdrant.tech/documentation/guides/multiple-partitions/ | "creating many collections can quickly become expensive. Only create multiple collections when you have a limited number of tenants that need strict isolation. Qdrant Cloud limits each cluster to a maximum of 1000 collections by default" |
| 6 | isolation cost | The vendor's ladder is tiered: payload filter → dedicated shard → promotion at roughly 20,000 points | VERIFIED | https://qdrant.tech/documentation/guides/multiple-partitions/ | "The recommended threshold for promoting a tenant is the same as the indexing threshold for a single collection, which is approximately 20,000 points" |
| 7 | isolation cost | Weaviate reports the tenant density a node supports | VERIFIED | https://weaviate.io/developers/weaviate/concepts/data | "a 9-node test cluster built on n1-standard-8 machines holds around 170k active tenants. There are 18,000 to 19,000 tenants per node" |
| 8 | isolation cost | Inactive tenants are offloaded, so the per-process file limit stops applying | VERIFIED | https://weaviate.io/developers/weaviate/concepts/data | "If you set unused tenants as inactive, the open file per process limit does not apply" |

## Flags the drafter must carry

- **Row 1 is scoped to 32 tokens.** The 92% figure is for 32-token inputs and falls as the input lengthens; the article states the scope in the same sentence and never writes "92% of a document".
- **Row 3 is a laboratory result.** It assumes an attacker who can write into the knowledge base, against specific retrievers and models; the article says "a published attack" and "an attacker who can write", never "90% of RAG systems are exploitable".
- **Rows 5–8 are the vendors' own documentation of their own products**, retrieved 2026-11-09; they are cited as what those platforms document, not as measurements of a customer deployment.
- **No figure for "how many enterprises run one index" exists in the evidence set**, so the article makes no prevalence claim.

## Claims removed before drafting

- A secondary blog's "the revocation took 26 hours" anecdote — no primary source, and the blog is a vendor asset; removed.
- A "permission leakage rate" from a survey with no retrievable methodology page; removed rather than paraphrased.
