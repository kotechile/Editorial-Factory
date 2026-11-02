---
title: "Your 90-Day Key: Still Live"
vertical: enterprise_ai_governance
kind: evergreen
archetype: evergreen
evergreen: true
persona: enterprise_cai
one_big_thing: "A machine key's exposure is its validity window, not its rotation schedule: the platforms that issue one already default to about an hour, so the number to put in policy is a maximum lifetime in hours, and a rotation that does not delete the replaced key leaves two live keys instead of one."
date: 2026-11-02
slug: your-90-day-key-is-two-live-keys
meta_title: "Your 90-Day Key: Still Live"
meta_title_source: "derived_from_title"
meta_description: "Google's guide for swapping service keys says replace them at least every 90 days, then names the step most teams skip: remove the old one."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-90-day-key-is-two-live-keys/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Two metal service-key cartridges at a server rack, one seated in a live slot and another set down beside a brass hourglass."
image_caption: "Your 90-DAY Key Is Still Live: A 90-day rotation that skips deletion leaves two live keys."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

Google's guide for swapping service keys says replace them at least every 90 days, then names the step most teams skip: remove the old one [3]. Skip that step and the swap makes a second live copy instead of retiring the first, because a new key does not kill the old one: the original is still live [3]. That is why the calendar number in your policy is not the number an incident lead asks about. At 3 a.m., the question is how long a stolen copy keeps working, and an agent holding two keys has an answer measured in months.

<!-- tension -->

## The big picture:

The systems that issue machine keys have already voted, and they voted for hours. A Kubernetes bound token, a short-lived token tied to a running pod, lives one hour unless you change it, and the node's background worker (kubelet) renews it before it lapses [1]. An assumed Amazon Web Services (AWS) role, a temporary identity a caller steps into, runs from a 15-minute floor to a one-hour standard, and can reach 12 hours [2]. Google caps short-lived tokens at an hour out of the box, and raising that cap to 12 hours takes a company-level policy [4].

The old-style static key, one you paste and keep, is the odd one out. It sits outside the short-lived credential system, so nothing renews it, and the vendor's fallback advice is a 90-day swap [3]. Against a one-hour token, 90 days is 2,160 hours, which is 2,160 times the window (90 × 24 = 2,160). That gap is not a rounding difference between vendors. It is the gap between a key that dies with the job and one that outlives the quarter it was issued in.

A reviewer reading a person's login uses a third ladder. The federal sign-in standard caps a user session at no more than 24 hours at its second security level, with an hour of idle time ending it, and cuts that to 12 hours with 15 minutes idle at the third [6]. That standard covers people, not agents, and nothing in it sets a rule for machines. My read is that it still shows where a reviewer's instinct sits: a day is the outside of a session, and a quarter is not.

## By the numbers

- **90 days — Rotation by calendar:** the vendor's standing advice for service keys, and the period most control docs copy into policy [3]. The same page ends its swap steps by removing the replaced key, which is the step that starts the clock [3].
- **1 hour — Bound-token standard:** a Kubernetes TokenRequest token (a short-lived pod credential) expires with its pod or after a set life that is an hour unless changed. The node worker renews it before it lapses, and the docs' own example asks for 3,607 seconds [1].
- **12 hours — Role ceiling:** the top of an assumed role's login, against a 15-minute floor [2], and the most a short-lived Google token can reach, through a company policy rather than a request setting [4].
- **24 hours — Human login ladder:** the outside of a login window at the standard's middle level, cut to 12 hours with a 15-minute idle limit at the third [6].

<!-- tactical-insight -->

## What I'd watch:

- **Cancelling a key works differently on each system.** A bound token cannot be cancelled on its own: the docs say to expire one by removing the pod it is tied to [1]. A response plan that says "revoke the token" names a control that system does not offer.
- **The legacy pool is where old keys still live.** Tokens created automatically before the switch to bound tokens are cut off only after a year of disuse, not a year of age [1]. One in daily use never ages out, so the count of old tokens stored as Kubernetes Secrets (the cluster objects that hold credentials) still mounted across clusters is the number worth reporting.
- **The exception list is the policy.** Short-lived tokens are the default, so a longer window becomes a decision someone signs. Google makes 12 hours a company-level setting rather than a request value [4], and the role ceiling is a role setting, not something a caller asks for [2]. My sense is that a register of those exceptions will age better than the policy text above it.
- **The direction of travel removes the key rather than shortens it.** The same vendor advises avoiding service keys wherever a stronger method exists [5], which matters when you buy: a platform that takes only a pasted key will hold that exception for years.

<!-- nuanced-takeaway -->

## The catch

None of this is free. A job that cannot create its own key, or a vendor that takes only a pasted one, turns a short-lifetime rule into an outage the first time a swap fails. The vendor warns against expiring keys for exactly that reason [3]. Where [Agent Identity: The Wrong Layer](/agent-identity-missed-the-real-breach/) argues which layer deserves the spend, this is the narrower question of the window.

What I find hard to square is that the long key usually survives because nobody built the thing that renews it, not because anyone judged the risk acceptable. So the control is honestly reported as two numbers: the ceiling for the agents you can automate, and the count of exceptions you cannot. A policy with one number and no exception count describes a rule, not a state.

<!-- tldr -->

## At a glance

**The shift:** machine keys now default to roughly an hour, leaving the static key as the last long-lived item in the stack.
**The number:** one hour — a bound token's default life.
**The risk:** a swap that spares the old key doubles your risk.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
## Related reading

- [An Agent's Logs Aren't Evidence](/agent-audit-trail-not-evidence/) — what an action record has to hold, and how long to keep it
- [Kill Switch Misses Half Your Agents](/kill-switch-misses-half-your-agents/) — what containment can do when a key cannot be revoked
<!-- internal-links:end -->

## Sources

[1] Kubernetes documentation — Managing Service Accounts (bound service account tokens, revocation, legacy token clean-up), https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/
[2] Amazon Web Services — IAM user guide, credential lifetimes when assuming a role, https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html
[3] Google Cloud — Service account key rotation, https://cloud.google.com/iam/docs/key-rotation
[4] Google Cloud — Create short-lived credentials for a service account, https://cloud.google.com/iam/docs/create-short-lived-credentials-direct
[5] Google Cloud — Best practices for managing service accounts, https://cloud.google.com/iam/docs/best-practices-service-accounts
[6] National Institute of Standards and Technology — SP 800-63-4, Digital Identity Guidelines: Authentication, https://pages.nist.gov/800-63-4/sp800-63b.html
