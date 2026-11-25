---
title: "Your Egress Bill: Six Times the Storage Line"
vertical: enterprise_build_vs_buy
kind: evergreen
archetype: evergreen
evergreen: true
persona: eng_leader
primary_keyword: "egress pricing"
secondary_keywords: ["object storage cost", "data transfer out", "S3 egress", "free egress storage"]
one_big_thing: "Object storage's real meter is the data leaving: one gigabyte out costs six times a month of storing it on Google Cloud, and the vendors that dropped the egress fee priced it back into storage — so rank storage offers by the egress ratio, never by the storage list price."
date: 2026-11-25
slug: your-egress-bill-six-times-storage
---

<!-- lead -->

The monthly bill arrived with two lines that did not belong in the same sentence: $41 to store the data, $492 to move it. That arithmetic is not a mis-billing. Google Cloud prices Standard storage at $0.000027397 per GiB-hour, which lands near $0.020 per GiB-month [2], and data transfer out to worldwide destinations at $0.12 per gigabyte for the first 10 TiB [2]. One gigabyte leaving costs six months of keeping it. Every object-storage rate card works this way: storage is metered by the object's life, and movement is metered by the gigabyte out, and the second meter is the one nobody forecasts.

<!-- tldr -->

## At a glance

- **The shift:** Cloud object storage sells a cheap storage line and an expensive exit line.
- **The number:** $0.12 per GB out against $0.020 per GB-month in, on the same Google Cloud page [2].
- **The risk:** A serving workload — exports, download links, cross-cloud sync — pays the exit meter many times over, and the cheapest-at-rest offer becomes the dearest-at-serving.

<!-- tension -->

## Two meters, one rate card

AWS states the exit price in its own worked example: data transfer out from Amazon S3 in Europe (Ireland) to the internet is $0.09 per gigabyte, and 20 GB out in the example costs $1.80 [1]. Inside the cloud the exit is cheaper — the same page's S3 Tables replication example prices inter-region transfer from Oregon to Northern Virginia at $0.02 per GB [1]. The free allowance is a rounding error: 100 GB of transfer out per month, aggregated across every AWS service and region [1]. Past that, the meter runs at the full rate.

The page hides this in plain sight. The S3 rate tables themselves render behind client-side templates — the storage cells read as placeholders in the page's own source — while the worked examples print the transfer rates as text. My read is that this is not a conspiracy, it is a layout: the number AWS leads with is storage, because storage is the line that wins the comparison on a price screen.

Google's storage ladder makes the ratio legible. Standard storage is the hourly figure above; Nearline, Coldline and Archive drop the at-rest price and add retrieval fees — $0.01, $0.02 and $0.05 per GiB — plus minimum storage durations of 30, 90 and 365 days [2]. Delete an Archive object in week two and you are charged as if it had stayed a year [2]. Every discount tier is a trade of storage price for movement and duration penalties, which is the same two-meter design wearing a sale tag.

## The zero-egress counter-offer

Two vendors abolished the second meter. Cloudflare R2 prices Standard storage at $0.015 per GB-month, Class A write operations at $4.50 per million and Class B reads at $0.36 per million, and states the policy in one line: "There are no charges for egress bandwidth for any storage class" [3]. Backblaze B2 starts at $6.95 per TB-month — about $0.007 per gigabyte — with no minimum storage duration fee, egress free up to three times the average stored data and $0.01 per GB beyond that [4].

Free egress is not a discount; it is a repricing. R2 charges 75% more per GB-month than Google's Standard class [2][3]. B2's 3x allowance is a claim about workload shape — a backup emits little, an app serving files emits everything, monthly. The vendors who look expensive on the storage line are the ones who stopped charging you to leave.

## By the numbers

- **$0.09 per GB:** AWS's own worked example for transfer out to the internet from S3 in Europe (Ireland) [1].
- **$0.12 per GB:** Google Cloud egress to worldwide destinations, first 10 TiB, against $0.020 per GB-month of Standard storage [2].
- **$0.015 vs $0.007:** R2's storage price against B2's — the two free-egress vendors are 2.2x apart on the line they do charge [3][4].

<!-- tactical-insight -->

## The crossover test

Do the division before the contract. Store 2 TB and move 4 TB out each month — a common serving shape, one copy in, two copies out. On Google Cloud the storage line is about $41 (2,048 GB at $0.020) and the transfer line is about $492 (4,096 GB at $0.12): twelve times the storage [2]. On AWS the transfer line alone is about $369 (4,096 GB at $0.09) [1]. On R2 the same workload is $31 storage, $0 transfer, and the request meter — two million Class B reads — adds $0.72 [3]. On B2 the 4 TB sits inside the 3x allowance of 6 TB, so the month costs about $14 total [4].

The ranking that matters is the exit multiple, and it does not follow the storage price. B2 has the cheapest storage and the cheapest serving. Google sits mid-table at rest and last at the exit. A workload that emits little — backups, cold archives, replicated copies nobody reads — should ignore all of this and pick on storage price and duration penalties, because the exit meter never spins. A workload that serves, exports or syncs should rank offers by what a gigabyte out costs, and only then compare storage.

Check the shape first, not the rates: pull last month's transfer-out from the bill, divide it by stored GB, and that single number — the egress-to-storage ratio — decides the shortlist. A ratio under one favors whatever storage is cheapest. A ratio over four makes the egress line the whole decision.

## The catch

The free-egress offer is also a statement about where your data lives. Exit fees are small per gigabyte and enormous as lock-in: moving 50 TB between clouds at $0.09 per GB costs $4,600 before anyone plans the migration [1]. The vendors charging it are pricing the difficulty of leaving; the vendors not charging it are competing for the migration. Neither is charity.

R2's zero applies to bandwidth only — Infrequent Access storage carries a $0.01 per GB retrieval processing fee [3], and B2's allowance is a ceiling, so a sync job that bursts past 3x stored pays $0.01 per GB for the overflow [4]. And no rate card removes the other trap this desk has priced before: the [cloud bill break-even](/the-cloud-bill-break-even-when-renting-servers-stops-paying/) still turns on utilization, and an exit meter on top of it can flip a settled answer. Price the movement first, then re-check the storage.

<!-- internal-links -->

## Sources

- [1] AWS, "Amazon S3 Pricing" — https://aws.amazon.com/s3/pricing/
- [2] Google Cloud, "Cloud Storage pricing" — https://cloud.google.com/storage/pricing
- [3] Cloudflare, "R2 Pricing" — https://developers.cloudflare.com/r2/pricing/
- [4] Backblaze, "B2 Cloud Storage Pricing" — https://www.backblaze.com/cloud-storage/pricing
