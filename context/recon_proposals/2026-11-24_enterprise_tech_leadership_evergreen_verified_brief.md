# Verified Brief: enterprise_tech_leadership — 2026-11-24 (evergreen: backup storage-tier economics)

Every claim below was fetched from its primary URL on 2026-11-24 (gate fetch, `EditorialFactorySourceVerifier/1.0`) and the figure matched in the fetched text. Verified status per the gate's own evidence windows in `2026-11-24_enterprise_tech_leadership_evergreen_brief.md`.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | AWS S3 FAQ | S3 Standard durability is 99.999999999% (11 nines), a design objective for the authoritative dataset | VERIFIED | https://aws.amazon.com/s3/faqs/ | "S3 Files is designed to provide 99.999999999% durability (11 nines) for your authoritative dataset" — the FAQ states design objective language; the draft must not present it as an SLA. |
| 2 | AWS Glacier FAQ | S3 Glacier Deep Archive list price is $0.00099 per GB-month, "about $1 per TB-month" | VERIFIED | https://aws.amazon.com/glacier/faqs/ | "From just $0.00099 per GB-month (less than one-tenth of one cent, or about $1 per TB-month)" |
| 3 | Google Cloud Storage pricing | Archive storage class lists at $0.0013 per GiB-month (region pricing) | VERIFIED | https://cloud.google.com/storage/pricing | price table row: "Archive storage $0.05 $0.065 $0.05 $0.065" access charges with storage band "$0.01 $0.013 $0.001 $0.0013" per GiB-month columns (multi-region/dual-region/region values) |
| 4 | Google Cloud storage-classes doc | Archive class minimum storage duration is 365 days (Nearline 30, Coldline 90) | VERIFIED | https://cloud.google.com/storage/docs/storage-classes | "Archive storage ARCHIVE 365 days Yes 99.95% in multi-regions and dual-regions" |
| 5 | Azure access tiers overview | An Azure archive blob takes up to 15 hours to rehydrate depending on priority | VERIFIED | https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview | "Data in the archive tier can take up to 15 hours to rehydrate, depending on the priority you specify" |

Notes for the drafter:
- The AWS S3 pricing page (`aws.amazon.com/s3/pricing/`) renders its storage-class rate table client-side; the verifier's text extraction contains no storage rates. Do not cite storage rates from that page.
- $1/TB-month is AWS's own gloss on $0.00099/GB-month — one figure, never presented as two.
- "11 nines" is a durability design objective, not an availability SLA; the draft must keep the distinction.
