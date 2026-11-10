---
title: Your 47-Day Certificate Trap
vertical: nhil_infrastructure_ops
kind: evergreen
archetype: evergreen
evergreen: true
persona: it_ops_leader
one_big_thing: "A sealed enclave's certificate renewal rate is set by an outside calendar, so unattended issuance inside the fence is a capacity decision, not a housekeeping one."
date: 2026-11-10
slug: your-47-day-certificate-trap
image_path: "context/assets/illustrations/your-47-day-certificate-trap/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Your 47-DAY Certificate Trap. Sealed enclave certificate bay with an outside public clock casting a long shadow across an empty slot"
image_caption: "Your 47-DAY Certificate Trap: The trap is the renewal rate a 47-day certificate demands of an enclave nobody can visit."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

The trap in a 47-day certificate is not the shorter life. It is the renewal rate that life demands of an enclave nobody can visit. By March 2029 a public certificate will live 47 days, and every renewal after that has to happen with no one in the path [1]. That rule is already written, by the CA/Browser Forum, the body that sets the baseline requirements every public certificate authority (CA) follows. Outside the fence a ticket queue is a nuisance. Inside, the enclave cannot reach a public CA for a new certificate, or a revocation list to check one, so the queue becomes the outage and the fix is an issuer the estate runs itself.

<!-- tldr -->

## At a glance

- **The shift:** Public certificate lifetimes run on a fixed calendar, and each rung is shorter than the last.
- **The number:** 200 days is the ceiling in force today.
- **The risk:** An enclave that renews by ticket fails whenever the person holding it is away.

<!-- tension -->

## A public clock, a sealed estate

The schedule has four rungs, set once. A certificate issued before 15 March 2026 could live 398 days. The limit is 200 days now, 100 from 2027, and 47 from 2029 [1]. The same rules cut the validation data an issuer may reuse, from 398 days to 200, then 100, then 10 [1]. The proof behind a certificate now ages faster than the certificate.

Issuers move ahead of the floor. Let's Encrypt, which signs much of the public web, issues 90-day certificates and plans to halve that to 45 days by 2028 [3]. Its reuse window for a checked domain falls from 30 days to 7 hours [3]. The reason is revocation. The industry summary of the ballot calls revocation lists and online status checks unreliable, and says browsers often ignore them [2].

That argument is the one that reaches an enclave, because a revocation list is an outside service, and an air gap removes both directions at once. No outbound call to a public issuer. No inbound status check to prove a certificate is still good. What is left is what the estate runs itself. An issuer inside the fence, a way to hand out the trust bundle every client reads, and a clock that says when the next certificate is due.

What I notice is that the estate which feels this first is not the biggest one. A cloud tenant renews at the provider's edge and never sees a certificate at all. The estate that feels it is the one running its own issuer, because that is where a published schedule turns into somebody's Tuesday.

At 500 certificates, a 398-day limit meant about 1.3 renewals a day. The last rung means 7.8 per certificate a year, or 3,883 renewals [1]. That is roughly ten a day, every working day, on a schedule the estate does not control. What I keep circling is that isolation is not what makes an enclave slow here. The calendar is.

## By the numbers

- **10.6 renewals a day:** what 500 certificates cost at the last rung. [1]
- **1,825 renewals a year:** the same 500 certificates at the 100-day rung. [1]

<!-- tactical-insight -->

## What to build before 2027

Teams closest to this have stopped treating renewal as monitoring and started treating it as a build item. The shape that recurs is an issuer inside the fence that speaks a machine protocol, the Automated Certificate Management Environment (ACME). A service then asks for its own certificate and gets one with no hand on it. Three pieces sit around that. A trust bundle delivered by config tooling rather than by hand, an alarm at half of the remaining life, and a fail-closed rule for anything that cannot renew itself.

The shape is familiar from credential rotation. Teams that swap a service key on a 90-day cycle learned the hard part is [removing the old credential](/your-90-day-key-is-two-live-keys/), not issuing the new one. A certificate has the same tail. The retired one has to leave every client's trust store, or the estate keeps trusting what it meant to retire.

What I'd watch is the first rung that lands on a workload nobody owns. An agent runtime is the clear case. It holds a certificate for a tool endpoint, no operator watches it, and nothing inside it opens a ticket when a handshake starts failing. A renewal path that needs a person stays invisible until the certificate is the thing that broke.

<!-- nuanced-takeaway -->

## The catch

None of this binds a private authority. The baseline requirements cover public certificates, and an enclave may keep issuing 398-day internal certificates for as long as it likes [1]. Several do, and their auditors accept it. The honest reading is narrower than a warning about 2029. What has already moved is the ceiling on the certificates an estate shows to partners, vendors and outward endpoints, and the last rung is the direction every automation standard is going.

My read, held loosely: the issuer is the cheap part, a week of work for a small one. The expensive half is handing out trust, because every service, box and client must take the new roots and drop the old ones. A box with a vendor-fixed lifetime will fail on the vendor's schedule whatever the estate builds. The budget line that decides this is config tooling, not crypto.

## Sources

- [1] CA/Browser Forum, "Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates", servercert repository § 6.3.2 — https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md
- [2] DigiCert, "TLS certificate lifetimes will officially reduce to 47 days" — https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days
- [3] Let's Encrypt, "Decreasing Certificate Lifetimes to 45 Days", 2 December 2025 — https://letsencrypt.org/2025/12/02/from-90-to-45
