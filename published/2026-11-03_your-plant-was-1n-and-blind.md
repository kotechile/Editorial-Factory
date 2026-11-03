---
title: Your Plant Was 1N and Blind
vertical: nhil_infrastructure_ops
kind: news
persona: it_ops_leader
one_big_thing: "A backup power system is only as independent as the evidence feeding it: when the generator start signal and the grid's post-event record are both read upstream of the device that isolates them, neither the site nor the utility can prove what happened."
date: 2026-11-03
slug: your-plant-was-1n-and-blind
synthesis: true
sources:
  - https://status.cloud.google.com/incidents/Xs2XTHzAVC9YnafnPyzj
  - https://arxiv.org/abs/2610.38216
meta_title: "Your Plant Was 1N and Blind"
meta_title_source: "derived_from_title"
meta_description: "At 06:53 London time on 20 October, a Google Cloud data centre lost one of its two power feeds and did nothing about it."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-plant-was-1n-and-blind/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Your Plant Was 1N And Blind. Open breaker module with two control boxes wired to a live busbar, one contact block open."
image_caption: "Your Plant Was 1N And Blind: the site cannot prove what happened when its backup is blind."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

At 06:53 London time on 20 October, a Google Cloud data centre lost one of its two power feeds and did nothing about it [1]. The site was already down to a single feed, 1N in industry shorthand, because a breaker had been opened and locked out six days earlier for repairs. The generator-start controller was checking voltage on the wrong side of that open breaker, so it saw live power and never sent the start signal. The plant was blind to the only fact that mattered: one of its two paths was gone [1]. The battery bank gave five minutes, then emptied. The zone stayed dark for six hours and eight minutes [1].

Eight days later, a paper on data centre load reductions described the same fault from the other end of the wire. The recorders that grid operators are now putting in at these sites see only current and voltage at the point of connection. A load that falls because a training job stopped looks the same there as one that falls because the site dropped onto its own backup [2].

<!-- tension -->

## The plant could not see itself

I've been reading Google's report as a controls failure, not a generator failure. The site was built with 2N power: two full paths for every critical load, plus one high-voltage generator bank run by two programmable logic controllers. That is two computers watching the same inputs [1].

On 14 October, a quarterly generator load test turned up something that needed fixing. Feeder B was opened by hand and locked out, leaving the site on one path while the work was done. That is a normal and careful way to work [1].

What made it fatal was that the control system had no input telling it the work was happening. The voltage check for both controllers was wired upstream, on the source side of the breaker that had been pulled. Feed B was still live on the utility's side of that gap. So both controllers read a healthy supply on a path that no longer reached the building, and neither called for a start [1].

The team tried a remote transfer through the same controller, and the system blocked it. The battery bank emptied and the halls went dark. Only then did a person move the load to the standby feed by hand. Power was back before eight that morning [1].

Redundancy did not fail the way operators expect it to, with a generator that will not crank or a switch that sticks. Both controllers did exactly what they were told. They were told to watch the wrong node. Two controllers reading one point give one opinion, and the second copy protects you from a dead part, not from a shared mistake.

## By the numbers

- **23:54 Pacific — standby feed back:** a person closed that transfer by hand, sixty-one minutes after the fault [1].
- **03:13 — redundancy verified:** both controllers were reset and tested against voltage and breaker position before the plant was trusted again [1].
- **Hundreds of gigawatts — connection requests:** the load now asking for a place on the grid, measured at a fence that sees current and voltage only [2].

<!-- tactical-insight -->

## Where the second opinion comes from

My read on the grid side is that it runs on the same single reading. The paper notes that the North American Electric Reliability Corporation, which writes the grid's reliability rules, asks transmission owners to install disturbance recorders at these facilities. Those recorders usually observe only voltage and current at the point of connection [2]. Telling a shed load from a backup switch in the moment depends on how big the drop was against noise in the reading. It also depends on how fast the fault cleared, how the workload reaches the fence, and how much bandwidth the recorder has [2].

Google's fix is a settings change, and it is right for that site. Engineers reconfigured the controllers and then checked them against both voltage and breaker position [1]. The authors propose something different, an estimator that reads workload data next to the fence measurement to work out how much of a facility stayed connected [2]. Both answers move the evidence instead of doubling it. That is the pattern the people closest to the problem keep reaching for.

The incident also shows how an automatic response loads its neighbours. When the zone dropped, traffic moved to the other zones and the rerouted work filled their spare room, so requests queued and failed across the region [1]. The failover was correct and it was still an incident. Bank apps, parcel tracking and property listings went with it [3]. A regional failure travels down a supply chain nobody drew.

<!-- nuanced-takeaway -->

## The catch

The root cause is Google's own account of its own equipment, published on 27 October, five days after a first report. No outside audit has confirmed it. It is detailed, and still a company describing its own failure.

The paper is a model result, not a field measurement. Its finding that the two causes look identical holds only in a steady-state model. The authors list the conditions under which the dip itself can tell them apart [2]. The fair claim is narrow. What the grid can see at the fence is not enough, on its own, to say why a data centre's load moved. That is a statement about the evidence now being installed, not a claim that no recorder can ever tell.

What I keep circling is the timing. The maintenance came from a finding in a load test, which is the system working as it should, and it lasted from 14 October until the fault. Nothing in the plant's controls knew, and nothing in the grid's records would have shown it either. The [ride-through duty the site agreed to](/rack-ride-through-two-second-duty/) is a promise about holding on, not about what happens when it lets go.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Jira Bill Rose 10%" -> /flat-price-was-the-hedge/ [same site (aichieve.net); same category; topical overlap: cloud, october] Link "Your Jira Bill Rose 10%" in the section where the article touches cloud, october. -->
<!-- internal-link hint: "$915M Illusion: Your AI Judge Moves" -> /buying-ai-quality-when-the-score-belongs-to-the-judge/ [same site (aichieve.net); same category; topical overlap: time] Link "$915M Illusion: Your AI Judge Moves" in the section where the article touches time. -->
<!-- internal-link hint: "Every Check Bills Your 5-Hour Window" -> /duet-bills-your-five-hour-window/ [same site (aichieve.net); same category; topical overlap: october] Link "Every Check Bills Your 5-Hour Window" in the section where the article touches october. -->
## Related reading

- [Your Jira Bill Rose 10%](/flat-price-was-the-hedge/)
- [$915M Illusion: Your AI Judge Moves](/buying-ai-quality-when-the-score-belongs-to-the-judge/)
- [Every Check Bills Your 5-Hour Window](/duet-bills-your-five-hour-window/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The shift:** spare paths are standard, but both signals are read upstream of the switch that isolates them.
- **The number:** five minutes of battery, then six hours and eight minutes dark.
- **The risk:** under maintenance, the plant looks healthy to both its controller and the grid recorder.

## Sources
[1] Google Cloud Service Health, incident report for the europe-west2 outage (final report posted 2026-10-27): https://status.cloud.google.com/incidents/Xs2XTHzAVC9YnafnPyzj
[2] Data Center Load Reductions: Attribution, Measurement Limits, and Estimation, arXiv:2610.38216 (2026-10-28): https://arxiv.org/abs/2610.38216
[3] The Register, "Google Cloud says a 'power event' caused today's outage" (2026-10-20): https://www.theregister.com/paas-and-iaas/2026/10/20/google-cloud-says-a-power-event-caused-todays-outage/5304160
