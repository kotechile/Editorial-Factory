---
title: "Your 8 GiB Node Sells 6.1: The Hidden Reserve"
vertical: enterprise_tech_leadership
kind: evergreen
archetype: evergreen
evergreen: true
persona: eng_leader
one_big_thing: "A node pool's spec sheet is not the capacity a team can promise, because the scheduler advertises memory minus a provider-set reserve and an eviction buffer — a reserve worth 24% of an 8 GiB node on GKE against 8% on the same node under AKS — so node shape, request budgets and the SLO on top of them have to be sized from allocatable and the kernel's throttle point, not from the advertised GiB."
date: 2026-11-17
slug: your-8-gib-node-sells-6-1
meta_title: "Your 8 GiB Node Sells 6.1: The Hidden Reserve"
meta_description: "A node's spec sheet overstates what a team can schedule: GKE reserves a quarter of a small node's memory, AKS an eighth, and the kernel throttles the rest."
---

<!-- lead -->
An 8 GiB node sells you 6.1 GiB of memory you can really use, because the cloud vendor keeps a hidden reserve before your pods ever start [2]. That 1.9 GiB never shows on the order form, and it is where capacity plans break. A team signs up to the figure on the spec sheet, then watches pods get refused at three quarters of it. The same eight-gigabyte node under Azure's rule keeps 650 megabytes, leaving 7.25 gigabytes for pods [3]. Same spec sheet, less than half the loss.

<!-- tldr -->
## At a glance

- **The shift:** Vendors take a share of every node before pods run [2].
- **The numbers:** An 8 GiB node gives you 6.1 GiB to schedule [2].
- **The risk:** Capacity plans built from spec sheets overpromise by a quarter on small nodes [2].

<!-- tension -->
## Where the memory goes first

The kubelet runs pods on each node, and it has carried the same memory floor for years [1]. It starts taking memory back when free memory drops below 100Mi on Linux nodes, and it also watches the disk. The main filesystem is watched at 10%, the image filesystem at 15%, and free inodes at 5% [1]. These are not warnings. A hard floor means an instant kill, with no grace period at all [1].

Each managed vendor then takes its own cut. On Google's service the ladder runs in steps: 25% of the first 4 GiB, 20% of the next 4, 10% of the next 8, 6% of the next 112, and 2% above 128 GiB [2]. A further 100 MiB is kept back for pod eviction [2]. Azure's rule is the lesser of 20 megabytes per pod plus 50, or 25% of total memory. Its own example is an eight-gigabyte node with 30 pods keeping 650 megabytes [3].

Run Google's ladder across sizes and the shape of the problem shows. A 4 GiB node gives up 1.10 GiB and hands out 2.90 GiB. An 8 GiB node hands out 6.10. A 128 GiB node hands out 118.58 GiB [2]. The cut hits small nodes hardest, so the smaller the machine, the bigger the share you never see. Those are sums from a published ladder, not a vendor's promise about a product.

A leader feels this first, because a node pool is usually bought on price per listed gigabyte. That listed figure is the one number in the purchase no customer can use. Spreading work across many small nodes therefore buys overhead instead of room, and the same money on fewer large nodes yields more usable memory. The cloud is an agility loan, as this desk has argued, and the fine print is not the rate. It is the share of each node the scheduler will never lend out.

Teams that get this right treat the two vendors' rules as part of the price. On an eight-gigabyte node Google keeps 1.80 GiB before its buffer, and Azure keeps 650 megabytes. A capacity plan built from spec sheets is comparing two different products. What I find hard to square is how often that sum happens in a spreadsheet built from a price list. [The upgrade clock that runs under every cluster](/your-cluster-hidden-clock/) hides the same kind of cost on the upkeep side.

## By the numbers

- **100 MiB of memory:** The kubelet's default hard floor, below which it kills pods with no grace period [1].
- **650 megabytes held back:** What Azure keeps from an eight-gigabyte node that runs 30 pods [3].
- **1.10 GiB gone:** What a 4 GiB node loses to reserve and buffer before a pod starts [2].

<!-- tactical-insight -->
## What the kernel does with it

Usable memory is what the scheduler may promise. It is not what the kernel enforces, and the gap decides which pod dies first. A Burstable pod, one that asks for less memory than it allows, gets a throttle point called memory.high, set at its request plus 0.9 times the space between request and limit [4]. A container asking for 256 MiB with a 1 GiB limit is slowed at about 947 MiB, well below its own ceiling [4].

The pod with no limit is the worse case. A Burstable pod with no limit has the node's usable memory used in place of its limit, so it is slowed against the whole node rather than its own request [4]. Guaranteed pods, where request and limit are equal, get no throttle point at all [4]. The same split shows in the kill order. BestEffort pods go first, then Burstable, then Guaranteed, and only pods over their requests are ever chosen [4].

The disk half surprises teams after a quiet release. A 10% floor on a 100 GiB disk means 10 GiB is never free for images, logs or scratch space, and the failure arrives as a wave of evictions rather than a disk alert [1]. My read is that most of these reserves get found during an incident, which is the worst time to learn the gap between the memory you bought and the memory you got.

The reserve is also turning into a setting rather than a fact. Google's versions from 1.37.2-gke.1325000 let an operator set the system reserve [2]. That turns a hidden default into a choice someone names in a design review.

<!-- nuanced-takeaway -->
## The catch

Every figure here comes from a vendor's own docs, and vendors change formulas. Google's ladder describes versions before 1.37.2-gke.1325000 [2]. Azure's rule applies to Azure Kubernetes Service (AKS) 1.29 and later [3]. The 100 MiB floor is a default an admin can move [1]. The sums also ignore processor reservations, the system pods every node runs, and the gap between a node's size and what its pods ask for. None of it tells a team whether its work deserves the node it bought.

None of those vendor caveats changes the sums a team has to do. The usable figure the node reports, less the eviction floor, is the real promise, and it is the number worth taking into the room. Reading each vendor's formula before comparing two shapes is what stops one spec sheet from hiding a quarter of a machine at one vendor and an eighth at another. I have stopped treating the size on the box as capacity at all.

## Sources

- [1] Kubernetes Documentation, "Node-pressure Eviction" — https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
- [2] Google Cloud, "Plan node sizes" (GKE node allocatable resources) — https://cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes
- [3] Microsoft Learn, "Node resource reservations in Azure Kubernetes Service (AKS)" — https://learn.microsoft.com/en-us/azure/aks/node-resource-reservations
- [4] Kubernetes Documentation, "Pod Quality of Service Classes" — https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/
