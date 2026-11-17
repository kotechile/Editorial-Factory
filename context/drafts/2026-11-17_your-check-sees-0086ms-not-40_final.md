---
title: "Your Check Sees 0.086ms, Not 40"
vertical: nhil_infrastructure_ops
kind: news
persona: it_ops_leader
one_big_thing: "Microsoft signed off its Exchange Online recovery by validating stability at each stage while restored servers failed once live traffic returned, and a paper out twelve days earlier shows why such a gate lies: a probe kept reading 0.086ms for a service running at 40.139ms, so the control an infrastructure team needs is a fixed-rule check that every probe and rollback still sits on the serving path."
date: 2026-11-17
slug: your-check-sees-0086ms-not-40
synthesis: true
sources:
  - https://www.irishexaminer.com/world/arid-41937567.html
  - https://arxiv.org/abs/2611.00838
image_path: "context/assets/illustrations/your-check-sees-0086ms-not-40/featured.jpg"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "Your Check Sees 0.086Ms, Not 40. Network tap probe still lit on an old route port while a fresh patch cord carries the serving path on a"
image_caption: "Your Check Sees 0.086Ms, Not 40: Microsoft spent Thursday and Friday bringing Exchange Online back, telling customers."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Microsoft spent Thursday and Friday bringing Exchange Online back, telling customers it was restoring service in stages while it "validated stability at each stage" [1]. At least 74 countries lost mail, calendars and Teams before that gate was satisfied [2]. Twelve days before the outage, a team of network researchers had published the reason such a gate can pass when it should not: a probe keeps reporting after the service it stands for has moved [3]. Their testbed read 0.086ms on a path the traffic had left while the service ran at 40.139ms, so your check sees a healthy route that no longer carries the work [3].

<!-- tldr -->
## At a glance
- **The shift:** Gates now sign off recovery, and a gate can outlive the path it reads.
- **The number:** A rerouted service ran at 40.139ms; its probe said 0.086ms.
- **The risk:** A check passes on a node while the service behind it fails.

<!-- tension -->
## The instrument failed first

The disruption was detected after midday US Eastern on 12 November, and reports spread across continents within about an hour [2]. Microsoft's first account blamed servers that went unavailable and heavier load on the rest, and by Friday evening it still had no timeline for full recovery [2]. The company then narrowed the cause to "an issue during an earlier network capacity upgrade that surfaced following a recent network change," and it ruled out cyber activity and AI [1].

Then came the part to read twice. Microsoft's health postings said a process that sets up secure connections on the affected servers was overloaded [4]. That is the gate deciding whether a request may enter, not the mailbox behind it. Those postings also described servers that came back and then stopped answering once normal traffic resumed [4]. A node can pass a check while it sits idle and fail once the service it belongs to arrives.

The paper shows how a change can do this on purpose with nothing broken. A service runs through one router and is moved to a second. Reachability holds and the config is valid, so the change meets its goal [3]. But the probe that vouches for the service was tied to the old route, and it keeps reading a path the traffic has left [3].

Engineers then added 40ms of delay to the new branch and moved the traffic onto it [3]. Round-trip time, the time a request takes to cross the network and return, hit 40.139ms against a 25ms target [3]. The probe still said 0.086ms [3]. A separate probe on the new branch confirmed the delay, which is how the gap was measured [3].

I read the two events as one failure class. Microsoft's team ran a per-stage check, which is the right instinct, and it checked a node where it needed to check the service that node carries. The statement keeps cause apart from proof: the cause was the network upgrade, and the proof is what made the recovery look staged and safe [1]. A credit would not have closed that gap either, since [an uptime credit is a capped refund, not insurance](/sla-credit-is-not-insurance/) against what an outage costs.

## By the numbers
- **74 countries:** The reach of the Exchange disruption within about an hour [2].
- **0.086ms:** The reading a stale probe kept returning after the service moved off its route [3].
- **107 plans blocked:** Goal-matched agent plans the dependency check stopped before they ran [3].

<!-- tactical-insight -->
## Where the check belongs

The paper's answer is unfashionable, because it is not a model. Its assurance layer keeps a map that ties each service goal to the tools that watch it, the paths it uses, the parts that fail together and the rollback it would need [3]. Before an action runs, and again after each step of a plan, the layer asks whether those ties still hold [3]. Where a watching gap is short and fixable, it adds a temporary probe and removes it once cover returns [3]. Where a rollback would stop working, it refuses the step instead of writing a new one [3].

What I find hard to square is how cheap that is next to what teams are buying instead. The fixed-rule check added a mean 12.21 microseconds per decision across 13 cases, rising to 1.08ms where it tests that a rollback can still run [3]. The model doing the planning took 130.47 seconds per trial on average, and a second round of planning did not rescue a single blocked case [3]. The rejected plans got feedback and 270 fresh attempts between them, and none passed the same checks [3]. A model that cannot see the tie cannot be talked into respecting it.

Two details from this window say where attention goes instead. Germany's federal cyber agency told Reuters its own authorities were unaffected because they did not lean on Microsoft 365 services, which is a fact about the map, not about spare capacity [2]. In the paper's 15-plan test, a broad ban on every route and interface change across the relevant routers blocked all five unsafe plans and nine of the ten benign ones [3]. Safety bought with bans is billed to the speed of the team that has to live under them.

<!-- nuanced-takeaway -->
## The catch

The evidence has edges, and they matter. The paper's 15-plan set was built to exercise the requirements it models, and its authors say plainly that it shows intended behavior under controlled conditions, not detection in a live network [3]. Their testbed is eight nodes in containers, and the campaign varies intents rather than topologies [3]. The outage side is thinner still. The overloaded connection process and the failing restored servers come from reporting on Microsoft's health postings, not from a post-incident report, and the company has promised one [4]. Until it lands, the link between the two is my reading of the sequence.

What survives that caveat is narrow and useful. A tie check will not tell an operator whether a change was the right call, and it will not stop a bad change from meeting its goal. It tells them whether the thing they are about to trust still reads the service they are serving, which is the only question a recovery gate can answer before the traffic arrives.

## Sources

- [1] Reuters, "Microsoft Outlook, Teams outage eases after over a day but recovery timeline uncertain" — https://www.irishexaminer.com/world/arid-41937567.html
- [2] BBC News, "Courts, spies and MPs: How the Microsoft outage has been felt around the world" — https://www.bbc.com/news/articles/cqp9d58eldlro
- [3] Hussain, Kalogiannis, Salahuddin, Li and Voigt, "Can Agentic AI Undermine Its Own Assurance Loop? Closed-Loop Dependency Assurance for Cognitive Network Digital Twins", arXiv 2611.00838, 31 October 2026 — https://arxiv.org/abs/2611.00838
- [4] ProtoThema English, "Microsoft outage enters second day as recovery efforts falter" — https://en.protothema.gr/2026/11/13/microsoft-outage-enters-second-day-as-recovery-efforts-falter-disrupting-outlook-teams-and-government-services-worldwide
