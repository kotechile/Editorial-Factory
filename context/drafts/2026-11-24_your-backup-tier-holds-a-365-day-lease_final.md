---
title: "Your Backup Tier: A 365-Day Trap"
vertical: enterprise_tech_leadership
kind: evergreen
archetype: evergreen
evergreen: true
persona: eng_leader
one_big_thing: "The cheapest backup storage tier is cheap to store and expensive to open: a 365-day minimum and a 15-hour restore clock decide your disaster plan, not the list price."
date: 2026-11-24
slug: your-backup-tier-holds-a-365-day-lease
image_path: "context/assets/illustrations/your-backup-tier-holds-a-365-day-lease/featured.jpg"
image_style: "long_lens_industry"
image_model: "flux"
image_alt: "The 365-DAY Backup Tier Trap. Rows of sealed tape-archive cabinets in a dark data hall, one cabinet open with an amber worklight inside its"
image_caption: "The 365-DAY Backup Tier Trap: A 365-day lock and a 15-hour restore, not the list price, decide your disaster plan."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your backup tier should be picked by how fast a restore must work, because the real cost is paid when you open the copy, not when you store it. The bottom class holds every object for at least 365 days once it lands, and a worst-case archive restore can take up to 15 hours before the first byte returns. The 365-day lock is Google's Archive rule [4]. The 15-hour restore is Azure's stated worst case [5]. Either clock turns a storage choice into a disaster-recovery (DR) choice.

<!-- tldr -->
## At a glance
This article is for engineering leaders choosing where each backup tier sleeps. It prices the cheapest storage classes at AWS, Google Cloud and Azure, and argues the restore-time requirement — not the storage price — should pick the class.

<!-- tension -->
## The clock behind the cheap price
Amazon Web Services (AWS) prices its bottom storage class, S3 Glacier Deep Archive, at $0.00099 per gigabyte-month [2]. Google Cloud's Archive class lists at $0.0013 per GiB-month, in the same band [3]. On a price screen the classes look interchangeable: park old backups in the cheap one, keep today's data in the fast one, and the dashboard stays green.

What the price screen leaves out is the clock. Google's Archive class carries a 365-day minimum storage duration, so a wrong backup removed early still bills the full year [4]. Azure states the ceiling on the other side: an archived blob takes up to 15 hours to rehydrate — to be pulled out of cold storage and made readable again — depending on the priority you pay for [5]. I read the low price as deferral: the vendor can batch your restore work behind paying jobs, so you save on storage and borrow against the hour you need the bytes back.

## By the numbers
- **$1 per terabyte-month:** The Deep Archive storage price, before any retrieval work begins [2].
- **365 days:** The minimum you pay for one object in Google's Archive class, even if you remove it on day one [4].
- **15 hours:** The worst-case wait before an archived Azure blob is readable again [5].

<!-- tactical-insight -->
## Where the decision actually lands
The teams running cold storage for a living watch three clocks, not one price. Storage is the first. Retrieval is the second, and it bills by volume when you pull data back. The restore clock is the third, and Azure's 15-hour rehydration ceiling is what that clock looks like at the bottom tier [5].

The pattern I keep seeing in teams that have run a real restore is two-hop staging. A hot or cool class answers in minutes and holds the copies a DR event would actually need first. The deep archive holds only the copies compliance rules say to keep. Google's own 30-, 90- and 365-day minimums make this a real ladder, because each rung bills differently when a backup is wrong [4]. The trap catches the teams whose backups look healthiest on the price dashboard: a cheap tier with a long clock looks identical to a cheap tier with a short one right up until the restore. It is the same shape as pricing compute off a spec sheet — [the gap between a node's advertised memory and the capacity the scheduler can actually promise](/your-8-gib-node-sells-6-1/).

Where the two clocks bite next is the ransomware tabletop or the DR renewal. Someone asks how long until the data is back, and the tier answers: tomorrow, if we file the request today.

<!-- nuanced-takeaway -->
## The catch
None of this makes the cheap tier wrong; it makes it a lease with a term. AWS's 11-nines durability claim is a design objective, not a service level, so the tier promises the bytes survive rather than the restore behaving [1]. The missing divisor in any flat price comparison is how often you restore. A terabyte opened once a year is a rounding error. The same terabyte opened during an outage becomes a fifteen-hour outage of its own [5]. What I would do at the next backup-policy review is write down the restore-time requirement for each copy first, then let it pick the class — and the price table stops being the decision.

## Sources
- [1] AWS, "Amazon S3 FAQs" — https://aws.amazon.com/s3/faqs/
- [2] AWS, "Amazon S3 Glacier FAQs" — https://aws.amazon.com/glacier/faqs/
- [3] Google Cloud, "Cloud Storage pricing" — https://cloud.google.com/storage/pricing
- [4] Google Cloud, "Storage classes" — https://cloud.google.com/storage/docs/storage-classes
- [5] Microsoft, "Azure Blob Storage access tiers overview" — https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview
