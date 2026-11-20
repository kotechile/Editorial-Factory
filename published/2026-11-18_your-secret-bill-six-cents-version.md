---
title: "Your Secret Bill: 6 Cents a Version"
vertical: enterprise_build_vs_buy
kind: evergreen
archetype: evergreen
evergreen: true
persona: eng_leader
one_big_thing: "A secrets manager bills the object you keep — AWS the secret, Google the live version — so rotation and rollback policy set the bill, and the self-hosted floor is a five-node cluster no small bill can justify."
date: 2026-11-18
slug: your-secret-bill-six-cents-version
meta_title: "Your Secret Bill: 6 Cents a Version"
meta_title_source: "derived_from_title"
meta_description: "Amazon Web Services (AWS) bills 40 cents a month for every secret it stores. Google bills six cents a month for every live version of a secret, which is a…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-secret-bill-six-cents-version/featured.jpg"
image_style: "paper_collage"
image_model: "nanobanana"
image_alt: "Per-Secret Vs Per-Version Billing. One large paper-cut key with a price tag faces six duplicate keys, each with its own tag."
image_caption: "Per-Secret Vs Per-Version Billing: The difference is not a discount — it decides which rotation habit a team can afford."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Amazon Web Services (AWS) bills 40 cents a month for every secret it stores [1]. Google bills six cents a month for every live version of a secret, which is a different object on the invoice [6]. That difference is not a discount, and it decides which rotation habit a team can afford. On the per-secret meter a rotation is free, because the vendor does not charge for the new version [2]. On the per-version meter each rotation is a new line, and the rollback copy you keep is the thing you pay for. Teams compare the sticker instead, then build the service themselves to dodge a fee that starts at $6.02 a month [4].

<!-- tldr -->

## At a glance

This piece covers how cloud secrets managers bill: AWS charges per stored secret while Google charges per live version, so at seven versions the two meters flip and a rotation job that keeps old copies pays for each one.

<!-- tension -->

## The object on the meter

Both rate cards cover the same job, and they count different things. One counts what you store; the other counts what you keep. AWS prices the secret at 40 cents a month, prorated by the hour [1]. It adds 5 cents for every 10,000 calls to the application programming interface (API) that hands back the value [3]. Google prices each active version at six cents a month, with six free per account, and charges 3 cents per 10,000 read operations [6].

Both vendors print worked examples, which is where the gap stops being theory. The AWS page totals a ten-thousand-secret estate at $4,060 a month [5]. Only $60 of that is the calls, because the other $4,000 is the storing of the secrets [5]. The same estate on the Google meter, one live version each, is 9,994 billable versions plus 12 million read operations [6]. That lands near $636 a month, for the same objects [7].

I read the two examples side by side and expected the version meter to win, but not by this much. A key rotated each quarter and kept with one rollback copy runs two live versions most of the year. Seven such versions bill at $0.42 a month, which is two cents above the flat per-secret price [1]. The crossover sits at seven live versions, and almost nobody has priced it.

<!-- by-the-numbers -->

## By the numbers

- **$60:** the read-call line in the vendor's ten-thousand-secret example [5].
- **144 versions:** what Google's worked example bills, after six free ones [6].
- **3 nodes:** the quorum a five-member Vault set needs before it commits a write [8].

<!-- tactical-insight -->

## What the meter rewards

The habit that pays depends on the cloud, not on security doctrine. A team that rotates often and keeps a rollback copy pays the same on the per-secret meter as one that never touches the key [2]. On the per-version meter the retired copy is the cheap action, since a destroyed version costs nothing [7]. What I am watching is whether the rotation job also removes the copy it replaces. A job that forgets leaves one behind on every cycle, and the bill keeps both.

Scheduled rotation is metered too. Google charges five cents for each rotation notification past the third [7]. That line is small, and it tells you whether the rotation is automated or somebody's calendar reminder.

The read path is the other lever. A service that asks for its credential on every request pays by volume, then pays again in wait time [3]. The teams that avoid this keep the value in memory until a short lifetime expires. The version count also sets [how long a self-hosted cluster stays supported](/your-cluster-hidden-clock/), which is a second cost in the same unit.

<!-- nuanced-takeaway -->

## The catch

The self-hosted option is not priced by this arithmetic, and that is the part I find hard to square. HashiCorp documents the floor: storage runs on Raft, a consensus protocol, and a five-member set needs three live nodes before it accepts a write [8]. Every node is also unsealed by hand from a set of key shares, so a restart needs those shares in the room [9]. The software is free, and the cluster is the cost.

At the small end, the bill that cluster replaces is $72.24 a year [4]. That is about an hour of a developer's time at the 2025 median wage [10]. Self-hosting still wins where a call cannot leave the building, and there the meter does not matter. Everywhere else the decision is which object you want counted, and the answer depends on how long you keep a copy.

At ten thousand secrets the spread is $48,720 a year against $7,627, so the version count deserves a look before the contract does [5]. The line on the invoice a team still controls is the removal step, and it costs nothing to add.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Cloud Support Costs" -> /your-support-bill-an-engineer-at-190k/ [same site (aichieve.net); same category; topical overlap: bill, version] Link "Cloud Support Costs" in the section where the article touches bill, version. -->
<!-- internal-link hint: "Every Check Bills Your 5-Hour Window" -> /duet-bills-your-five-hour-window/ [same site (aichieve.net); same category; topical overlap: bills, every] Link "Every Check Bills Your 5-Hour Window" in the section where the article touches bills, every. -->
<!-- internal-link hint: "Cloud Uptime SLAs Are Not Insurance" -> /sla-credit-is-not-insurance/ [same site (aichieve.net); same category; topical overlap: amazon, bill] Link "Cloud Uptime SLAs Are Not Insurance" in the section where the article touches amazon, bill. -->
## Related reading

- [Cloud Support Costs](/your-support-bill-an-engineer-at-190k/)
- [Every Check Bills Your 5-Hour Window](/duet-bills-your-five-hour-window/)
- [Cloud Uptime SLAs Are Not Insurance](/sla-credit-is-not-insurance/)
<!-- internal-links:end -->

## Sources

- [1] Amazon Web Services, "AWS Secrets Manager Pricing" (per-secret price) — https://aws.amazon.com/secrets-manager/pricing/
- [2] Amazon Web Services, "AWS Secrets Manager Pricing" (rotation note, Example 1) — https://aws.amazon.com/secrets-manager/pricing/
- [3] Amazon Web Services, "AWS Secrets Manager Pricing" (API call pricing) — https://aws.amazon.com/secrets-manager/pricing/
- [4] Amazon Web Services, "AWS Secrets Manager Pricing" (Example 1 total) — https://aws.amazon.com/secrets-manager/pricing/
- [5] Amazon Web Services, "AWS Secrets Manager Pricing" (Example 4) — https://aws.amazon.com/secrets-manager/pricing/
- [6] Google Cloud, "Secret Manager pricing" (active versions, worked example) — https://cloud.google.com/secret-manager/pricing
- [7] Google Cloud, "Secret Manager pricing" (access operations, destroyed versions, rotation notifications) — https://cloud.google.com/secret-manager/pricing
- [8] HashiCorp, "Vault — Integrated Storage" — https://developer.hashicorp.com/vault/docs/internals/integrated-storage
- [9] HashiCorp, "Vault — Seal and Unseal" — https://developer.hashicorp.com/vault/docs/concepts/seal
- [10] U.S. Department of Labor, O*NET OnLine, "Software Developers (15-1252.00)" — https://www.onetonline.org/link/summary/15-1252.00
