---
title: "Your Agent's Fix Fails: 39.5% of the Time"
vertical: agentic_resilience_failure
kind: evergreen
archetype: evergreen
evergreen: true
persona: infra_engineer
one_big_thing: "An incident agent's useful number is verified recovery, not root-cause accuracy: across two independent Kubernetes benchmarks, detection runs 72.7% to 99.7% while a fix that was valid and then executed lands at 14.5% to 60.3%, the invalid plans miss on the operation (67.9%) rather than the service (1.3%), and live replay recovered none of 48 domain-name faults against all 36 pod failures — so autonomy has to be bounded per fault class by a check that reproduces the fault, never by the agent's own recovery declaration."
date: 2026-11-11
slug: your-agent-fix-fails-39-of-right-calls
meta_title: "Your Agent's Fix Fails: 39.5% of the Time"
meta_title_source: "derived_from_title"
meta_description: "An incident agent's fix fails the incident's own rules more often than its diagnosis does. Models now name the right service almost every time, then hand…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-agent-fix-fails-39-of-right-calls/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "A steel gate with a padlock divides a lit server aisle from a dark data hall."
image_caption: "Your Agent's Fix Fails: autonomy needs a fault-reproducing check, not the agent's own report."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

An incident agent's fix fails the incident's own rules more often than its diagnosis does. Models now name the right service almost every time, then hand back a plan the rules reject. One benchmark, published on 6 July 2026, scored both halves: its strongest models named the right service in 91.4% to 99.7% of cases, and gave a fix the rules accept in only 36.8% to 60.3% [1]. Even when the call was right, the fix was rejected 39.5% of the time [1]. A second benchmark, out on 4 November, shows the same shape on real operator defects: 72.7% to 90.9% fault detection against 14.5% to 52.7% end-to-end closure [2]. A gate that reads finding accuracy passes an agent that cannot repair what it finds.

<!-- tldr -->

## At a glance

- **The shift:** The measured unit moved from naming a cause to accepting a plan of action.
- **The number:** 146 of 302 plans that passed an offline check also recovered live.
- **The risk:** A cleared alert can hide a fault the agent never fixed.

<!-- tension -->

## The gap opens at the operation

Root cause analysis (RCA) tools have spent years getting good at a question that turns out to be half the work. The R2Act team, from Beihang University and Microsoft Research Asia, took checked incidents from a demo shop app and wrote down which fixes were valid for each one [1]. Then they scored the plan, not the sentence. Five model setups that diagnose best scored 36.8% to 60.3% on that plan. The same models missed a step even when they got the cause right.

I read the error table three times before I believed the ordering. Of 755 rejected plans, 513 chose an operation the incident did not call for, and 224 wrapped a fair operation in a plan that broke the rules for a valid fix [1]. Ten missed the target or its dependency, and eight did nothing at all [1]. The models had found the service already. What they could not do was say which action belongs to that fault, on which object, in what order.

SWEOps-Bench, from Sun Yat-sen University and the Chinese University of Hong Kong, reached the same place from the other side. Its 55 tasks are real defects from 16 Kubernetes operator projects, each replayed in a live cluster from the project's own code [2]. Agents there spotted the fault 72.7% to 90.9% of the time and closed it end to end 14.5% to 52.7% of the time [2]. The paper records both awkward cases: some runs recovered while naming the wrong cause, and others cleared the alarm while failing the check tied to the fault [2].

## By the numbers

- **67.9% of rejected plans:** Wrong operation, the largest single class of repair error [1].
- **16 operator projects:** Real defects replayed in live clusters, judged by each project's own tests [2].
- **96 domain-name faults:** None recovered in live replay, against 36 of 36 pod failures [1].

<!-- tactical-insight -->

## Where the gate has to sit

What I find most useful in both setups is that neither lets the agent grade its own work. SWEOps-Bench asks for a stated recovery inside the time budget, plus a pass on every check that applies [2]. A check the agent never ran counts as a failure [2]. R2Act sends the same plans through a live replay, where the offline scorer decides validity and the cluster decides recovery [1].

The fault split is the part to carry into a rollout review. On the R2Act set, replay recovered every pod failure and every fault that pegs the processor [1]. It recovered 23 of 39 request aborts and 11 of 34 memory-pressure faults, and none of the 96 domain name system (DNS) cases [1]. The authors say why: a DNS fix leans on dependency and configuration facts that sit outside the service the model named [1]. That is a different kind of work from restarting a pod. A pilot weighted toward pod kills will certify an agent that cannot touch a DNS record, so the mix of faults, not the number of tasks, sets what the certificate is worth.

Vendors have noticed. One product page reports 94% accuracy in automated cause identification [3]. That is a real number about the first half of the job, quoted in the units of the first half.

<!-- nuanced-takeaway -->

## The catch

Both benchmarks are small and narrow. R2Act leans on one demo app with injected faults [1]. SWEOps-Bench leans on 55 defects in 16 operators, and most of those codebases are small [2]. Neither is a fleet of real incidents, and the figures are as of their release dates, not a running average.

The two headline numbers also sit on different scales. 91.4% to 99.7% is service-level diagnosis, while 36.8% to 60.3% is plan-level validity. Dividing one by the other gives a ratio with no meaning. So does quoting the low end of one against the high end of the other.

What I keep circling is the checker itself, because a check tied to a fault only exists where that fault can be reproduced. A test suite can confirm that a DNS lookup works again. It cannot confirm that a partial rollback left the ledger correct. That is the lesson [the safety gate moves to verified state](/agent-safety-gate-moves-to-verified-state/) draws from another dataset. The evidence that counts is made outside the system being judged. Someone has to build it before autonomy is worth granting.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Agent's Contract Gap" -> /your-agent-contract-gap-63-unmet/ [same site (aichieve.net); same category; topical overlap: agent's, rules] Link "Your Agent's Contract Gap" in the section where the article touches agent's, rules. -->
## Related reading

- [Your Agent's Contract Gap](/your-agent-contract-gap-63-unmet/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

- [1] Qi, Luan, Zhang, Huang, Fung, Tong, Yang and Qian, "Can LLMs Really Recover Microservice Failures? A Recovery-Aware Evaluation of Diagnosis-to-Action Reasoning," arXiv:2607.04623, 6 July 2026 — https://arxiv.org/html/2607.04623v1
- [2] Chen, Yu and Chen, "SWEOps-Bench: Evaluating Agents for End-to-End Resolution of Software-Induced Cloud Incidents," arXiv:2611.06099, 4 November 2026 — https://arxiv.org/html/2611.06099v1
- [3] NeuBird, "Best Root Cause Analysis Tools in 2026" — https://neubird.ai/blog/root-cause-analysis-tools
