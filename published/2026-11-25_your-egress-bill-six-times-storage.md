---
title: "Egress Pricing: Six Times the Storage Line"
vertical: enterprise_build_vs_buy
kind: evergreen
archetype: evergreen
evergreen: true
persona: eng_leader
primary_keyword: "egress pricing"
secondary_keywords: ["object storage cost", "data transfer out", "S3 egress", "free egress storage"]
one_big_thing: "Object storage's real meter is the data leaving: one gigabyte out costs six times a month of keeping it on Google Cloud, and the vendors that dropped the egress fee priced it back into storage — so rank storage offers by the egress ratio, never by the storage list price."
date: 2026-11-25
slug: your-egress-bill-six-times-storage
meta_title: "Egress Pricing: Six Times the Storage Line"
meta_title_source: "derived_from_title"
meta_description: "The monthly bill arrived with two lines that did not belong in the same sentence: $41 to keep the data, $492 to move it. That is not a mis-billing."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-egress-bill-six-times-storage/featured.jpg"
image_style: "paper_collage"
image_model: "nanobanana"
image_alt: "Egress Pricing Six Times The Storage Line. A paper receipt coil with a long tape spooling across a steel bench, the exiting tape far larger"
image_caption: "Egress Pricing Six Times The Storage Line: The meter that decides the bill is data leaving — buy on the egress ratio, not the list."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

The monthly bill arrived with two lines that did not belong in the same sentence: $41 to keep the data, $492 to move it. That is not a mis-billing. Google Cloud prices Standard storage at $0.000027397 per GiB-hour, which lands near $0.020 per GiB-month [2]. It prices data transfer out to worldwide destinations at $0.12 per gigabyte for the first 10 TiB [2]. One gigabyte leaving costs six months of keeping it. Every cloud rate card works this way. Storage is metered by the object's life. Movement is metered by the byte out. The second meter is the one nobody forecasts.

<!-- tldr -->

## At a glance

This article compares the published rate cards of Amazon Web Services (AWS), Google Cloud, Cloudflare R2 and Backblaze B2 for engineering leaders choosing object storage. It argues that the egress meter, not the storage price, decides the bill for any workload that serves data out.

<!-- tension -->

## Storage, and the meter on the way out

AWS states the exit price in its own worked example: data transfer out from Amazon S3 in Europe (Ireland) to the internet is $0.09 per gigabyte, and 20 gigabytes out in the example cost $1.80 [1]. Inside the cloud the exit is cheaper. The same page's S3 Tables example prices inter-region transfer from Oregon to Northern Virginia at $0.02 per gigabyte [1]. The free allowance is small: 100 gigabytes of transfer out per month, shared across all of AWS and all regions [1]. Past that, the meter runs at the full rate.

The page hides this in plain sight. The S3 price tables render behind client-side templates — the rate cells read as placeholders in the page's own source — while the worked examples print the transfer rates as text. I read the source twice before accepting that. AWS leads with the storage price because that is the line that wins a price-screen comparison. The exit rate sits in a footnote-shaped example.

Google's storage ladder makes the ratio legible. Standard storage is the hourly figure above. Nearline, Coldline and Archive cut the at-rest price and add retrieval fees of $0.01, $0.02 and $0.05 per GiB. They also add minimum stays of 30, 90 and 365 days [2]. Delete an Archive object in week two and you are charged as if it had stayed a year [2]. Each discount tier is the same two-meter design wearing a sale tag: a cheaper storage price traded for movement fees and duration penalties.

Two vendors dropped the second meter. Cloudflare R2 prices Standard storage at $0.015 per gigabyte-month. Its write operations cost $4.50 per million; its reads cost $0.36 per million. And it states the policy in one line: "There are no charges for egress bandwidth for any storage class" [3]. Backblaze B2 starts at $6.95 per terabyte-month, about $0.007 per gigabyte. It has no minimum storage duration fee. Egress is free up to three times the stored data, then $0.01 per gigabyte [4].

Free egress is not a discount. It is a repricing. Google's Standard class runs near $0.020 per GiB-month [2]. R2's $0.015 is 75% more than that [3]. B2's 3x allowance is a claim about workload shape: a backup emits little, an app serving files emits everything, monthly. The vendors who look costly on the storage line are the ones who stopped charging you to leave.

## By the numbers

- AWS's own worked example prices internet egress from S3 in Europe (Ireland) at $0.09 per gigabyte [1].
- R2 asks $0.015 per gigabyte-month and B2 asks $0.007 [4], a 2.2x gap between the free-egress vendors.
- Google Cloud's free egress allowance is zero; AWS's is 100 gigabytes a month, shared across every service and region [1].

<!-- tactical-insight -->

## The crossover test

Do the division before the contract. Say a team keeps 2 terabytes and moves 4 terabytes out each month — one copy in, two copies out. That shape is illustrative, not measured. On Google Cloud the storage line is about $41 (2,048 gigabytes at $0.020) and the transfer line is about $492 (4,096 gigabytes at $0.12): twelve times the storage [2]. On AWS the transfer line alone is about $369 [1]. On R2 the same workload is $31 of storage and $0 of transfer; two million reads add $0.72 [3]. On B2 the 4 terabytes sit inside the 3x allowance of 6 terabytes, so the month costs about $14 total [4].

The ranking that matters is the exit multiple, and it does not follow the storage price. B2 has the cheapest storage and the cheapest serving. Google sits mid-table at rest and last at the exit. A workload that emits little — backups, cold archives, copies nobody reads — should ignore all of this. It should pick on storage price and duration penalties, because the exit meter never spins. A workload that serves, exports or syncs should rank offers by what a unit out costs, and only then compare storage.

What I would do Monday is check the shape before the rates. Pull last month's transfer-out from the bill. Divide it by the stored data. Let that one number — the egress-to-storage ratio — pick the shortlist. A ratio under one favors whatever storage is cheapest. A ratio over four makes the egress line the whole decision.

<!-- nuanced-takeaway -->

## The catch

The free-egress offer also says where your data lives. Exit fees are small per gigabyte and huge as lock-in: moving 50 terabytes between clouds at $0.09 per gigabyte costs $4,600 before anyone plans the migration [1]. Where I land after staring at these four cards: the exit fee is priced at exactly how badly you want out, and the vendors who waive it are bidding for your next migration. Neither is charity.

R2's zero applies to bandwidth only. Its Infrequent Access class adds a $0.01 per gigabyte retrieval fee [3]. B2's allowance is a ceiling: a sync job that bursts past 3x stored pays $0.01 per gigabyte for the overflow [4]. No rate card removes the other trap priced on this desk before. The [cloud bill break-even](/the-cloud-bill-break-even-when-renting-servers-stops-paying/) still turns on utilization, and an exit meter on top of it can flip a settled answer. Price the movement first. Then re-check the storage.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "$250k AI Upkeep Tax" -> /enterprisebuildvsbuy-the-250k-ai-upkeep-tax/ [same site (aichieve.net); same category; topical overlap: bill, pricing] Link "$250k AI Upkeep Tax" in the section where the article touches bill, pricing. -->
<!-- internal-link hint: "Cloud Uptime SLAs Are Not Insurance" -> /sla-credit-is-not-insurance/ [same site (aichieve.net); same category; topical overlap: bill, monthly] Link "Cloud Uptime SLAs Are Not Insurance" in the section where the article touches bill, monthly. -->
<!-- internal-link hint: "Your CI Bill: 232 Hours Before You Build" -> /your-ci-bill-232-hours/ [same site (aichieve.net); same category; topical overlap: bill, line] Link "Your CI Bill: 232 Hours Before You Build" in the section where the article touches bill, line. -->
## Related reading

- [$250k AI Upkeep Tax](/enterprisebuildvsbuy-the-250k-ai-upkeep-tax/)
- [Cloud Uptime SLAs Are Not Insurance](/sla-credit-is-not-insurance/)
- [Your CI Bill: 232 Hours Before You Build](/your-ci-bill-232-hours/)
<!-- internal-links:end -->

## Sources

- [1] AWS, "Amazon S3 Pricing" — https://aws.amazon.com/s3/pricing/
- [2] Google Cloud, "Cloud Storage pricing" — https://cloud.google.com/storage/pricing
- [3] Cloudflare, "R2 Pricing" — https://developers.cloudflare.com/r2/pricing/
- [4] Backblaze, "B2 Cloud Storage Pricing" — https://www.backblaze.com/cloud-storage/pricing
