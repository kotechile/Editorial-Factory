---
title: AWS Cannot Restore Bahrain: 144 Services Lost
vertical: enterprise_tech_leadership
persona: eng_leader
one_big_thing: "A cloud region can be declared permanently unrecoverable, so the only durable copy of your data is the one that sits outside the region and outside the provider's control."
date: 2026-10-13
slug: aws-cannot-restore-bahrain
---

<!-- lead -->
Amazon Web Services (AWS) cannot give customers their data back from its Middle East (Bahrain) region. The company's status page says the damage there "spanned multiple Availability Zones and exceeded what our regional and multi-AZ services are designed to withstand" [1]. AWS adds that it is "unable to restore access to the resources and data hosted exclusively in this Region".

The same 15 September 2026 statement declared one zone in its United Arab Emirates (UAE) region unrecoverable too [1]. The service list runs to 144 disrupted items for Bahrain, and 135 for the UAE. What is lost is narrow and worth stating twice: only data with no copy outside the region [1].

<!-- tension -->

## The big picture:

This is not an outage that ran long. AWS has not run out of time. It has run out of options. The status page says the company checked every damaged facility and "exhausted every option for restoring data and resources that had not been migrated before the Region became unavailable" [1]. A further statement is promised in early 2027.

I keep coming back to what this redundancy was built to survive. AWS's own fault-isolation paper spaces zones "up to 60 miles (~100 km)" apart [2]. It lists the dangers they are made to outlast: "utility power, water disruption, fiber isolation, earthquakes, fires, tornadoes, or floods". Every one of those is an accident of equipment. What came in March 2026 was physical damage to several buildings in one night, which AWS attributes to the conflict in the Middle East [1].

The company had also said, in writing, what the design could take. Amazon S3 is "designed to withstand the total loss of a single Availability Zone (AZ) while maintaining S3's durability and availability" [1]. That held once. When a second zone in the UAE went dark, S3 error rates rose.

So the buyer of multi-zone and multi-region cover inside one provider was sold a short, numbered list of disasters. The failure that arrived was not on the list.

## By the numbers

- **144 — services disrupted, Bahrain:** AWS lists 144 services as Disrupted for the Bahrain event and 135 for the UAE event, and states that the region's data cannot be recovered [1].
- **~100 km — the design distance:** zones sit up to 60 miles apart, close enough for live copying and far enough to beat the dangers AWS names in its fault-isolation paper [2].
- **12 hours 30 minutes — a second ceiling, the same week:** Google's us-central1 Cloud Storage writes fell over for 12 hours 30 minutes on 8 October 2026. Its write-up says staff tried to add emergency capacity and were "blocked by systemic regional capacity limits" [3].
- **Early 2027 — the next answer:** AWS paused billing for the region, expects repairs to take months, and says more detail on Bahrain follows in early 2027 [1].

<!-- tactical-insight -->

## What I'd watch:

The reflex after a story like this is to buy a second zone, or a second vendor. Both are real moves. Neither is the one that gets tested. I am watching the copy, and where that copy is allowed to sit.

AWS points customers to other regions and tells them to rebuild from "remote backups", picking regions "as appropriate for your latency and data residency requirements" [1]. That last clause is the whole problem. It is a legal question wearing an engineering costume.

- **The residency limit:** for regulated data, the backup that saves you may sit in a country you cannot store it in. Where that is true, the gap is a limit on the design, not a flaw in it, and it belongs in a risk list rather than a recovery plan [4].
- **The restore, not the copy:** live copying keeps a second version warm. A backup nobody has ever rebuilt from is a hope with a calendar entry.
- **The way back:** a rebuild that needs the dead region's own console or keys is not a way back at all. AWS spent days restoring the tools that let customers move data out [1].
- **Who owns what:** the provider runs the building, the customer owns the data inside it. The Bahrain ruling is that line, drawn in public [1].

<!-- nuanced-takeaway -->

## The catch

My read is that this will be over-read in one direction and under-read in the other. It is not proof that the cloud is a bad buy. Cost is why most of this work sits there, and the fair counter-argument is that moving back often does not pay. One consultant's line in a recent survey of exits has stuck with me: "a lot of cloud repatriation projects are actually FinOps projects in disguise" [6].

The part I keep circling is what the event does not prove. Zones were never sold as cover against a strike on several buildings in one night, and the design paper is plain that it covers a fixed list of accidents [2]. No provider can promise to beat an attacker. What a provider can promise is honesty about the scope of cover, and this ruling is unusually clear on that point.

Where I have landed: the useful question is not whether a region can fail. It is whether anything you own lives in exactly one place, and whether the rules let you put a second copy somewhere else. Multi-zone answers the first question well. It cannot answer the second one at all.

<!-- tldr -->

## At a glance

- **The Big Shift:** AWS has told customers that data kept only in its Middle East (Bahrain) region cannot be recovered, and declared one zone in its UAE region unrecoverable at the same time, after damage that beat what its regional and multi-zone services were built to survive [1].
- **Why It Matters:** the durability promise behind multi-zone and multi-region cover is written against a fixed list of dangers, and the event that broke it was not on that list. A region's data, not just its uptime, can be a single point of failure.
- **What I'd Watch:** whether teams test the way back rather than the live copy, and whether the second copy is allowed to sit where it is needed.
  - **Rebuild drill:** moving a backup into another region and starting it, on a clock, on a schedule. That is the only proof a backup works.
  - **Residency check:** getting a legal answer, not an engineering guess, on which countries a copy may sit in.
  - **Region independence:** making sure the way back does not lean on the console, keys or network of the region being recovered from.
- **The Catch:** moving everything back is not automatically the fix. The cost case for staying is often strong, and the copies that save you may be exactly the copies your data rules forbid.

## Sources
[1] AWS Health Dashboard, service health — continued-disruption entries for Middle East (Bahrain) me-south-1 and Middle East (UAE) me-central-1, including the 2026-09-15 determinations, the 2026-04-30 billing suspension and the 2026-03-02 physical-cause statement — https://health.aws.amazon.com/health/status
[2] AWS, *Fault Isolation Boundaries* whitepaper, "Availability Zones" — https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html
[3] Google Cloud Service Health, incident report, Cloud Storage, us-central1, 2026-10-08 — https://status.cloud.google.com/incidents/mSFVt6PiP557bjRyYsut
[4] InfoQ, "AWS Cannot Restore Data Held Only in Damaged Middle East Availability Zones", 2026-09-21 — https://www.infoq.com/news/2026/09/aws-middle-east-data-loss
[5] Reuters, "Amazon's AWS is unable to restore access to Bahrain, one UAE cloud data zone after war", 2026-09-15 — https://www.reuters.com/world/middle-east/amazons-aws-is-unable-restore-access-bahrain-one-uae-cloud-data-zone-after-war-2026-09-15
[6] ZDNET, "Companies are ditching the cloud to save millions – should you?", 2026-10-05 — https://www.zdnet.com/tech/cloud-repatriation-enterprise-cost-optimization
