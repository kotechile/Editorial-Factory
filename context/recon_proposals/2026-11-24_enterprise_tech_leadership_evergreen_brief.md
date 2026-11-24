# Evergreen Brief: enterprise_tech_leadership — 2026-11-24
**Archetype:** evergreen
**Vertical:** enterprise_tech_leadership
**Persona:** eng_leader
**Decision the reader is facing:** Which storage class to commit each backup tier to — and whether the restore itself survives a disaster — when the cheapest tier also carries a 365-day minimum-storage clock and up to 15 hours of rehydration before the first byte comes back. The decision bites at the next backup-policy review, DR renewal or ransomware tabletop, not at the bill.
**Durability:** Storage-class prices, minimum-storage durations and rehydration ceilings are contractual and change on a year scale, not a month scale — the list prices here are as of 2026-11-24 (S3 Glacier Deep Archive $0.00099/GB-month per AWS's Glacier FAQ as of that fetch, GCS Archive $0.0013/GiB-month per Google's pricing page as of that fetch, GCS Archive minimum duration 365 days as of the 2026 storage-classes doc, Azure archive rehydration up to 15 hours as of the current access-tiers overview). The mechanism — tier by restore-time requirement, not by storage price — is correct in 12 months even if a rate moves a tenth of a cent.
**De-dup:** `2026-11-17_your-8-gib-node-sells-6-1` is this vertical's nearest prior evergreen artifact (published 2026-11-17): it prices the gap between a node's advertised memory and the scheduler's allocatable — compute capacity, no storage class, no restore clock. `2026-11-10_your-pager-caps-at-2-incidents` prices on-call attention; `2026-11-03_your-pool-becomes-2000-connections` prices connection memory; `2026-10-06_cloud-repatriation-break-even` decides rent-vs-own from utilisation and egress, not from where backup copies sleep. Today's news artifact `2026-11-24_23-of-26-builds-saved-nothing` argues build-vs-buy for AI features — no storage tiering. Cross-vertical check run by hand because `check_dedup` reads this vertical only: `grep -ril "glacier\|storage class\|backup tier\|rehydrat" published/ context/drafts/` names no artifact in any vertical, so no published article argues that a backup's storage price is the wrong axis for the tier decision.
**Thesis:** A backup's restore-time requirement, not its storage price, is the axis the storage class must be picked on — because the cheapest tier's real cost is paid on the restore side: a 365-day minimum-storage clock you can't shorten when a backup is wrong, a rehydration ceiling of up to 15 hours before the first byte returns, and a retrieval bill that lands exactly when the business is on fire.

**Lead:** §2's founder-voice pillar for this vertical ("the cloud is an operational agility loan") plus `customer-truth.md` Anecdote 1 (the $68,000/month AWS transfer shock — the pattern where a pricing line nobody priced at design time dominates the bill). The persona's `wants` field asks for "concrete numbers, decision frameworks, what to do Monday morning", and the 30-day intel feeds' `market_metrics` show continued cost-optimization coverage. GSC striking-distance was checked and is thin on this query set (bonus signal only; not load-bearing).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | AWS — Amazon S3 FAQs (durability) | https://aws.amazon.com/s3/faqs/ | 2026-11-24 | 99.999999999% durability (11 nines) is S3 Standard's design objective for the authoritative dataset | vendor claim |
| 2 | AWS — Amazon S3 Glacier FAQs | https://aws.amazon.com/glacier/faqs/ | 2026-11-24 | $0.00099 per GB-month is the S3 Glacier Deep Archive list price — about $1 per TB-month | vendor claim |
| 3 | Google Cloud — Cloud Storage pricing | https://cloud.google.com/storage/pricing | 2026-11-24 | $0.0013 per GiB-month is the Archive storage class list price (region pricing, Iowa/US) | vendor claim |
| 4 | Google Cloud — Storage classes (docs) | https://cloud.google.com/storage/docs/storage-classes | 2026-11-24 | 365 days is the minimum storage duration for Archive storage (30 days Nearline, 90 days Coldline) | measured |
| 5 | Microsoft Learn — Azure Blob Storage access tiers overview | https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview | 2026-11-24 | 15 hours is the worst-case rehydration time to read a blob out of the Azure archive tier, depending on rehydration priority | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Backup tiering by restore-time requirement (storage class clocks and rehydration ceilings) | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| Inter-region egress gravity forcing region consolidation | 8 | 7 | 5 | 7 | 6.9 | dropped — the only anchor in the AWS pricing page's rate table is a worked example, and the table itself is client-rendered (probe 2026-11-24) |
| PITR windows: snapshot retention vs continuous recovery point | 7 | 8 | 5 | 6 | 6.6 | dropped — no second host carries a verifiable window figure; would rest on one vendor's docs |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=5 hosts=3 decision="sha1:6faff3c583" dedup="matched a prior artifact: 2026-11-17_your-8-gib-node-sells-6" window_days=180 checked_at=2026-11-24T18:32:50+00:00 -->
<!-- evergreen-gate:end -->
