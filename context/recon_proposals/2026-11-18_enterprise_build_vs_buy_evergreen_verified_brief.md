# Verified Brief: enterprise_build_vs_buy — 2026-11-18 (evergreen)

Archetype: evergreen. Topic: a secrets manager is billed on the object you keep — AWS on the secret, Google on the active version — so rotation and rollback practice set the bill, while the self-hosted floor is a five-member Raft peer set. Every row below was read on the page itself (not from a search excerpt). Rows 1–7 are the vendors' own published rate cards and are labelled vendor claims; row 8 is the project's own operational documentation; row 9 is the BLS wage vintage published through O*NET.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | AWS — the secret is the unit | A secret is billed at 0.40 USD per secret per month, prorated by the hour | VERIFIED | https://aws.amazon.com/secrets-manager/pricing/ | "$0.40 / secret / month"; "the price per secret is calculated as $0.40 * 1 hour / (30 days * 24 hours) = $0.00056 / secret/ hour" |
| 2 | AWS — rotation is not metered | Creating a new version of an existing secret is not charged | VERIFIED | https://aws.amazon.com/secrets-manager/pricing/ | "Note: rotating a secret creates a new version of the secret. You are not charged for creating new versions." |
| 3 | AWS — the access meter | API calls are billed separately at 0.05 USD per 10,000 | VERIFIED | https://aws.amazon.com/secrets-manager/pricing/ | "@ $0.05/10,000 call"; "@ $0.05/10,000 calls" |
| 4 | AWS — the vendor's own small example | 15 secrets plus 4,040 API calls totals 6.02 USD a month | VERIFIED | https://aws.amazon.com/secrets-manager/pricing/ | "$6.02 Total (per month)" |
| 5 | AWS — the vendor's own large example | 10,000 secrets plus 12M API calls totals 4,060.00 USD a month, of which the calls are 60.00 | VERIFIED | https://aws.amazon.com/secrets-manager/pricing/ | "$4,000.00 10,000 secrets @ $0.40 / secret $60.00 12M API calls (10,000 secrets * 40 API calls/day * 30 days) @ $0.05/10,000 calls $4,060.00 Total (per month)" |
| 6 | Google — the version is the unit | An active secret version is billed at 0.06 USD a month after six free per account | VERIFIED | https://cloud.google.com/secret-manager/pricing | "150 active secret versions, 6 secret versions are free. Billing total: 144 active secret versions at $0.06: $8.64" |
| 7 | Google — destroyed versions and the other meters | Destroyed versions are free; access operations run 0.03 USD per 10,000 after 10,000 free; rotation notifications cost 0.05 USD each after three | VERIFIED | https://cloud.google.com/secret-manager/pricing | "Destroyed secret versions Free"; "Access operations 0 count to 10,000 count $0.00 (Free) / 10,000 count, per 1 month / account 10,000 count and above $0.03 / 10,000 count, per 1 month / account"; "Rotation Notifications 0 count to 3 count $0.00 (Free) / 1 count, per 1 month / account 3 count and above $0.05 / 1 count, per 1 month / account" |
| 8 | HashiCorp Vault — the build floor | Raft quorum is a majority of the peer set, so a five-member set needs three nodes, and without quorum the cluster cannot commit new logs | VERIFIED | https://developer.hashicorp.com/vault/docs/internals/integrated-storage | "For a peer set of size N , quorum requires at least ceil( (N + 1) / 2 ) members. For example, quorum in a peer set of 5 members requires 3 nodes. If a cluster cannot achieve quorum, the cluster becomes unavailable and cannot commit new logs." |
| 9 | HashiCorp Vault — unsealing | With the default Shamir seal, every node is unsealed separately with the threshold of shares | VERIFIED (prose only — no gate row) | https://developer.hashicorp.com/vault/docs/concepts/seal | "When you use the Shamir seal with multiple nodes, you must unseal each node with the required threshold of shares." |
| 10 | O*NET — the labour conversion | The 2025 median software-developer wage is 65.38 USD an hour, 135,980 USD a year | VERIFIED | https://www.onetonline.org/link/summary/15-1252.00 | "Median wages (2025) $65.38 hourly, $135,980 annual" |

## Derived arithmetic (desk, recomputed 2026-11-18 — no gate reads these)

- Same inventory, two clouds: 10,000 secrets at 0.40 = 4,000 USD a month, plus 12M calls at 0.05 per 10,000 = 60 USD, gives the vendor's own 4,060 USD. The Google equivalent: 9,994 billable versions at 0.06 = 599.64 USD, plus 12M access operations at 0.03 per 10,000 = 36 USD, gives 635.64 USD — 6.4× lower for an identical inventory.
- Crossover: 0.40 ÷ 0.06 = 6.67, so a secret that keeps seven live versions costs more on Google than on AWS.
- Annual: 4,060 × 12 = 48,720 USD, or 745 engineer-hours at 65.38; 635.64 × 12 = 7,627.68 USD, or 117 engineer-hours; the gap is 41,092 USD, about 629 engineer-hours.
- The avoided bill at small scale: 6.02 × 12 = 72.24 USD a year, about 1.1 engineer-hours.

## Binding rulings for the drafter

- AWS's own page says new versions are free; that sentence is the whole contrast and must be quoted, not paraphrased into "AWS does not charge for rotation" alone.
- Never call 4,060 USD the price of "a secrets manager": it is 10,000 secrets fetched 40 times a day each. The small example is 6.02 USD.
- Google's free allowance is six active versions and 10,000 access operations per account per month; do not restate it as "six secrets".
- The build side's floor is five Raft members and three of them quorate; unsealing is a separate per-node step and is prose only (row 9).
- O*NET is a conversion, never a benchmark of what any given firm pays.
- Do not claim AWS is more expensive in every case: below seven live versions per secret, Google's meter is the cheaper one.

## Gate result

The pass marker lives on `context/recon_proposals/2026-11-18_enterprise_build_vs_buy_evergreen_brief.md`
(the artifact `scripts/verify.sh` reads); this file is the claim ledger behind it, not a gate artifact.
