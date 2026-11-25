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
---

<!-- lead -->
At 19:00 Central European Time on November 2, someone took a docs vendor's infrastructure credentials [1]. GitBook's own incident update lists the response: replace every credential it owns, and "invalidated every customer's application programming interface (API) tokens on our platform" — the keys one system uses to call another [1]. One step in a security notice; thousands of integrations went dark at once. Four days later, a clause-by-clause read of 14 SaaS vendors — Microsoft, Google, Salesforce, Atlassian, Adobe and nine more — showed what the same exit costs when you choose it [2]. One vendor wants 60 days' written notice before you may cut seats. Another takes half of everything left if you leave early. Several state no notice window at all.

<!-- tldr -->
## At a glance
One breach response wiped a vendor's customers' tokens overnight — an exit nobody chose, at the vendor's speed. A read of 14 renewal terms shows the exit you choose is fenced: notice of zero to 30 days and a cost to leave early. The price sits in the contract.

<!-- tension -->
## What the documents say

First, the holdings. GitBook's investigation says the attacker "may have accessed" four kinds of secrets: Git Sync secrets, GitBook's own API (interface) tokens, "third-party API tokens used to connect external tools to GitBook", and questions asked by site visitors [1]. That third item deserves a second read. A documentation site looks like a small purchase. Its customers had still handed it working credentials against their own repositories and their own connected tools. The vendor's reset button fired against holdings that belong to the buyers.

Next, the contract. All 14 vendors in the read auto-renew by default [2]. Notice to stop a renewal runs from none stated up to 30 days [2]. Notion asks 60 days' written notice just to reduce seats for the next term [2]. Microsoft allows seat cuts only within 7 days of adding the licences [2]. Leaving early costs real money [2]. Adobe takes 50% of what remains on an annual plan paid monthly. Google wants the full commitment. Atlassian makes the rest of the term due at once. Most renewals also reset to the list price in force at renewal, and discounts expire [2].

The two documents have never met on one page. That is the finding. The vendor's exit from your workflow is instant and theirs. Yours is slow and written down. It is priced in months of notice, or a share of what remains. The breach did not create this power. The incident response simply ran it at full speed, on a timeline you did not set. The renewal clause is the same power, priced and scheduled. So I call the arrangement escrow. The buyer deposits live credentials. The seller holds them. The way out appears in two places that never join a negotiation.

## By the numbers
- **60 days' written notice** — what Notion demands before you may cut seats at renewal. [2]
- **50% of the remaining obligation** — Adobe's early-exit charge on an annual plan billed monthly. [2]
- **Every customer's API tokens** — what GitBook invalidated in one response step. [1]

<!-- tactical-insight -->
## What the field is doing

My read of the field: the people closest to this read the contracts before the renewal, not after the incident. The read exists because an asset-management firm traced the price changes of 2025–2026 back to their clauses [2]. The clauses set the notice windows, the price resets, and the discounts that expire at renewal. Their own caveat holds: a negotiated Order Form overrides the standard terms, so the public clause is a floor, not your floor [2].

The incident also gives buyers a free drill, if they take it. When one vendor's tokens died at once, each customer saw which of their systems stood on that vendor's credentials. Our earlier piece on [the incident clock: 4 hours, not 15 days](/ai-incident-clock-4-hours-not-15-days/) made the same point about response timing. The clock that matters runs during the event, and the vendor's timetable is not yours. Mapping your tokens before a renewal is the same habit aimed at a calendar instead of a clock.

The escrow also hides where nobody looks. A November teardown of a Wi-Fi air purifier found the owner banned by the vendor for running an old community integration [3]. He went weeks unable to control his own fan while support reversed the ban. His exit came from a detail in the device's own setup data. Two URLs aim the hardware at the vendor's servers, and whoever runs the setup sets them — so he aimed them at his own [3]. Rebuilding that flow took a language model about 20 minutes. By hand, the author put it at hours to days [3]. The exit path was in the buyer's hands the whole time. What changed in 2026 is the labour price of finding it.

<!-- nuanced-takeaway -->
## The catch

Nothing here says GitBook acted badly. Its update reads like the response you would want: block the attacker, replace every credential, take the service down rather than guess, and publish what happened [1]. Invalidating customer tokens was the correct move inside its own walls. That is the problem. A well-run vendor's duty to itself is the same act that strands its customers. And no clause in the read obliges the vendor to make your exit cheap. It must only let you leave, slowly, at a price it lists [2].

So the number to negotiate is not the seat price. It is the shape of the exit: how much notice, which credentials, and who re-issues them. My reading, held loosely: teams that price the exit first will find the seat price moves toward them. A buyer who can leave is a buyer who can say no. The breach did not change the contract. It showed what the contract was worth all along.

## Sources
- [1] GitBook security incident update, quoted in the Hacker News thread "Gitbook Breached", event 2026-11-02, posted 2026-11-03 — https://news.ycombinator.com/item?id=50354336
- [2] Alex Cojocaru, "SaaS Renewal Terms: What 14 Vendors' Contracts Say About Auto-Renewal, Notice and Price Rises" (compiled read of the vendors' own public terms, checked 2026-11-13) — https://licenseware.io/saas-renewal-terms-notice-periods-price-increases
- [3] Scott J. Goldman, "Reverse Engineering My Coway Air Purifier to Ditch the Cloud", 2026-11-11 — https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/
