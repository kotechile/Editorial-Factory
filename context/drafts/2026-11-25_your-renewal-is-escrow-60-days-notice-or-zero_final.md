---
title: Your Renewal Is Escrow: 60 Days' Notice, or Zero
vertical: enterprise_build_vs_buy
kind: news
persona: eng_leader
one_big_thing: "On November 2 a docs vendor invalidated every customer's API token at once. A line-by-line read of 14 SaaS renewal clauses shows your own exit is fenced slower: 60 days' written notice, or half of what remains."
date: 2026-11-25
slug: your-renewal-is-escrow-60-days-notice-or-zero
synthesis: true
sources:
  - https://news.ycombinator.com/item?id=50354336
  - https://licenseware.io/saas-renewal-terms-notice-periods-price-increases
meta_title: "Your Renewal Is Escrow: 60 Days' Notice, or Zero"
meta_description: "One vendor invalidated every customer's API token in a night. The renewal clauses of 14 SaaS vendors show your own exit is fenced far slower. What the two documents price."
image_path: "context/assets/illustrations/your-renewal-is-escrow-60-days-notice-or-zero/featured.jpg"
image_style: "paper_collage"
image_model: "nanobanana"
image_alt: "Your Renewal Is Escrow. A severed paper key on the left, a blank contract certificate fenced behind a barred gate with an hourglass on the"
image_caption: "Your Renewal Is Escrow: One vendor killed every API token in a night — 14 SaaS renewal clauses price your exit."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
At 19:00 Central European Time on November 2, someone stole a docs vendor's credentials, so GitBook replaced every credential it owns and "invalidated every customer's application programming interface (API) tokens on our platform" — the keys one system uses to call another [1]. One step in a security notice; thousands of integrations went dark at once. Four days later, a clause-by-clause read of 14 SaaS vendors — Microsoft, Google, Salesforce, Atlassian, Adobe and nine more — showed what the same exit costs when you choose it [2]. One vendor wants 60 days' written notice before you may cut seats. Another takes half of everything left if you leave early. Several state no notice window at all.

<!-- tldr -->

## At a glance

A breach at the documentation vendor GitBook wiped every customer's API token in one night. A line-by-line read of 14 SaaS renewal terms shows the exit buyers choose is fenced by notice windows and early-exit fees. This article prices that asymmetry.

<!-- tension -->

## What the documents say

The incident first, in order. At 19:00 in Paris on November 2, the attacker took control of some of GitBook's infrastructure credentials [1]. GitBook calls it a sophisticated, highly targeted attack using AI agents [1]. The company took the app and its logged-in docs sites offline, but kept published content live on cached data [1]. Its investigation found the attacker may have accessed four kinds of holdings: Git Sync secrets, GitBook's own API tokens, third-party API tokens that customers used to connect external tools, and questions that site visitors had asked GitBook Assistant [1]. The word "may" is the vendor's own hedge, and it stays. I read that third item three times before its weight landed. A documentation site looks like a small purchase, yet its customers had handed it working credentials against their own repos and their own connected tools. When GitBook hit its reset button, the button fired against holdings that belong to the buyers. The customer who reported the incident on the thread had seen no official notice at that time — GitBook may have told others out of band [1].

Now the contract. A line-by-line read of 14 vendors' own public terms, checked November 13, found that all 14 renew automatically by default: doing nothing means another term [2]. Notice to stop a renewal runs from none stated up to 30 days [2]. Notion asks for 60 days' written notice just to reduce seats for the next term [2]. Microsoft permits seat cuts only within seven days of adding the licences [2]. Leaving early costs money, and the rules differ by vendor: Adobe charges 50% of the remaining obligation on an annual plan paid monthly, Google requires the full commitment, and Atlassian makes the rest of the term due at once [2]. Most renewals also reset to the list price in force at renewal, and promotional discounts tend to expire there [2]. Price-change notice runs from 30 days at Google Workspace to nothing stated at Microsoft 365, Atlassian and Adobe [2].

Neither document mentions the other. That collision is our reading, not theirs — no source here says renewal is credential escrow. But put the two side by side and the shape shows. The vendor's exit from your workflow was instant and unilateral. Your exit from the vendor is slow, written, and priced, in months of notice or a share of what remains. The breach did not create this power. The incident response simply ran it at full speed, on a timeline no buyer set. The renewal clause is the same power, scheduled and listed. Buyers deposit live credentials; sellers hold them; the way out appears in two documents that never meet inside one negotiation.

## By the numbers

- **60 days' written notice:** what Notion demands before you may cut seats at renewal [2].
- **50% of the remaining obligation:** Adobe's early-exit charge on an annual plan billed monthly [2].
- **Every customer's API tokens:** what GitBook invalidated in one response step [1].

<!-- tactical-insight -->

## What the field is doing

The people closest to this are reading the contracts before the renewal, not after the incident. The compiled read exists because someone went vendor by vendor through the standing terms and wrote down what each exit costs [2]. Its own caveat matters: a negotiated Order Form can override any cell, so the public clause is a floor, not your floor [2]. What I am watching is whether buyers start asking for that override in writing before the renewal date, not at it.

The incident also gave buyers a free drill. When GitBook's tokens died at once, each customer saw in real time which of their systems stood on that vendor's credentials. Our earlier piece on [the incident clock: 4 hours, not 15 days](/ai-incident-clock-4-hours-not-15-days/) made the same point about response timing: the clock that matters runs during the event, and the vendor's timetable is not the buyer's. Some teams now map their tokens before each renewal — the same habit aimed at a calendar instead of a clock.

The exit path also hides where nobody looks, and November put a price on finding it. A teardown of a Wi-Fi air purifier, published November 11, began with the owner banned by the vendor for running an old community integration [3]. He went weeks unable to control his own fan while support reversed the ban. His way out was a detail in the device's own setup data: two URLs aim the hardware at the vendor's servers, and whoever runs the setup sets them — so he aimed them at his own [3]. Rebuilding that flow took a language model about 20 minutes, where the author put the manual work at hours to days [3]. The exit was in the buyer's hands the whole time. What changed is the labour price of finding it.

<!-- nuanced-takeaway -->

## The catch

Nothing here says GitBook acted badly. Its update reads like the response you would want: block the attacker, replace every credential, take the service down rather than guess, and publish what happened [1]. Invalidating customer tokens was the correct move inside its own walls. That is the problem. A well-run vendor's duty to itself is the same act that strands its customers. And no clause in the read obliges a vendor to make your exit cheap. It must only let you leave — slowly, at a price it lists [2].

So the number to negotiate is not the seat price. It is the shape of the exit: how much notice, which credentials, and who re-issues them. My reading, held loosely: teams that price the exit first will find the seat price moves toward them, because a buyer who can leave is a buyer who can say no. The breach did not change any contract. It showed what the contracts were worth all along. The next renewal is the moment to run that math.

## Sources
- [1] GitBook security incident update, quoted in the Hacker News thread "Gitbook Breached", event 2026-11-02, posted 2026-11-03 — https://news.ycombinator.com/item?id=50354336
- [2] Alex Cojocaru, "SaaS Renewal Terms: What 14 Vendors' Contracts Say About Auto-Renewal, Notice and Price Rises" (compiled read of the vendors' own public terms, checked 2026-11-13) — https://licenseware.io/saas-renewal-terms-notice-periods-price-increases
- [3] Scott J. Goldman, "Reverse Engineering My Coway Air Purifier to Ditch the Cloud", 2026-11-11 — https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/
