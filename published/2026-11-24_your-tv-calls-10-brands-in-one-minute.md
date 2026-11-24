---
title: Your TV Calls 10 Brands: The Hidden Guest List
vertical: smart_home_telemetry
kind: evergreen
archetype: evergreen
evergreen: true
persona: pro_homeowner
one_big_thing: "A smart TV phones ten outside services in its first power-on minute, and the FBI's standing advice is to stop sharing a Wi-Fi with them. A guest network is the floor; a firewalled IoT VLAN is the fix."
date: 2026-11-24
slug: your-tv-calls-10-brands-in-one-minute
meta_title: "Your TV Calls 10 Brands: The Hidden Guest List"
meta_title_source: "derived_from_title"
meta_description: "Within one minute of powering on, a Samsung smart TV calls 10 outside brands, and nobody has signed in to any of them."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-tv-calls-10-brands-in-one-minute/featured.jpg"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "Your TV Calls 10 Brands Before You Sign. Router on a utility-closet shelf with a firewall gate separating a smart TV and doorbell from a"
image_caption: "Your TV Calls 10 Brands Before You Sign: Untrusted gadgets share your main Wi-Fi — moving them out is the cheapest trust upgrade."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Within one minute of powering on, a Samsung smart TV calls 10 outside brands, and nobody has signed in to any of them [2]. The list runs from Google Play to Netflix, Spotify and Facebook. That hidden guest list matters because a device trusted with nothing still sits inside a network trusted with everything. Every smart gadget you plug in joins the same Wi-Fi that holds your laptop and your files. Moving them out is not a device upgrade. It is a network change, and it is the cheapest trust upgrade in the house.

<!-- tldr -->
## At a glance
This guide is for homeowners who run a mixed smart-home network. Measured device traffic shows gear you bought calling third parties you never chose, and FBI advisories document home devices being hijacked for crime. The finding: a separated, firewalled device network is the cheapest trust upgrade in the house.

<!-- tension -->
## The Flat Network Was a Decision

The record has stacked up over eight years, and each layer shows the same gap. In 2018, a team at Princeton began studying more than 50 home smart devices through their tool, IoT Inspector. They found a smart TV calling 10 outside brands the moment it powered on, and a home camera quietly checking in with its maker's Dynamic Domain Name System (DNS) relay — the service that maps a camera name to its changing internet address [2].

Two years later, the Electronic Frontier Foundation (EFF) tested one Ring doorbell app for Android. It shipped personal data to four tracking firms: names, private internet protocol (IP) addresses and lasting device IDs reached Facebook, Mixpanel, AppsFlyer and Branch.io [1].

The abuse has since turned criminal at scale. The FBI traced a device botnet the Bureau calls Badbox back to 2023 and broke that campaign in 2024. A botnet is a fleet of hijacked devices run by one operator. A newer strain still infects TV sticks and picture frames with hidden control software, the Bureau warned in a June 2025 public notice [3]. By March 2026, a fresh FBI warning flagged a new abuse: criminals rent hijacked home devices as residential proxies, so their traffic looks like it came from your house [4].

I read those four findings twice before the common thread stopped hiding: trust. On a flat network, each device can reach every other device. So a streaming stick with a factory password sits one step from your laptop. Whoever harvests that stick inherits your household's reach. They may collect device IDs, or they may rent your connection out.

## By the numbers

- **10 outside brands:** the services a Samsung TV called in its first power-on minute, with no accounts [2].
- **Four analytics firms:** the companies that received personal data from one Android doorbell app [1].
- **2024:** the year the FBI disrupted the original Badbox botnet campaign [3].

<!-- tactical-insight -->
## How Owners Draw the Line

The FBI's guidance is blunt. If your router offers more than one network, keep your computers off the network your smart gear uses [4]. It also tells owners to turn off Universal Plug and Play (UPnP — the protocol that lets a device open router ports by itself) and to firewall each segment.

The ladder most home networks follow has three rungs. The guest network name your router already ships is the floor: the devices share an internet pipe, but a boundary exists. A dedicated IoT virtual local area network (VLAN) goes further. It carves the devices into their own subnet, and firewall rules can block every path back to your main segment. The full treatment pins each device to the few cloud endpoints it needs and nothing else. That is how owners of locally-run systems do it — the same people who choose [a doorbell that keeps its video on their own network](/your-doorbell-wont-need-the-cloud/) rather than a vendor's cloud.

What I keep noticing is how rarely the floor gets used. Guest networks have shipped with routers for a decade, and the FBI's advice appears in both of its recent advisories. The gap is not knowledge. It is that isolation stays invisible until the evening it matters.

<!-- nuanced-takeaway -->
## The catch

Walling devices off has a price, and saying it out loud keeps the fix honest. A wall breaks the features that assume one network. Phone apps that find devices by multicast DNS (mDNS — local name-broadcasting) stop finding them, and casting to speakers stumbles. First-time setup often needs the cloud, so a walled device may need a short bridge. The EFF test covered one 2020 Android app, and vendors have changed since; today's gear is not yesterday's. A VLAN also takes care: firewall rules need a note of which device needs what, or the segment hardens into "everything blocked, everything broken."

Where I land is that the trade still favors the wall. A broken casting session costs minutes. A hijacked camera inside your trusted segment costs the story of your whole network. The flat network is only cheaper until the night it isn't.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Smart Home & Security" -> /categories/smart-home-security/ [same site (wellroost.com); same category; the article's own category hub (Smart Home & Security); topical overlap: hidden, smart] Link "Smart Home & Security" in the section where the article touches hidden, smart. -->
<!-- internal-link hint: "Your Camera Eats 66 GB" -> /your-camera-eats-66-gb-daily/ [same site (wellroost.com); same category; topical overlap: hidden, smart] Link "Your Camera Eats 66 GB" in the section where the article touches hidden, smart. -->
<!-- internal-link hint: "Your 80 PSI Trap: A Valve and a Tank" -> /your-80-psi-trap/ [same site (wellroost.com); same category; topical overlap: smart] Link "Your 80 PSI Trap: A Valve and a Tank" in the section where the article touches smart. -->
## Related reading

- [Smart Home & Security](/categories/smart-home-security/) — more on Smart Home & Security
- [Your Camera Eats 66 GB](/your-camera-eats-66-gb-daily/) — more on Smart Home & Security
- [Your 80 PSI Trap: A Valve and a Tank](/your-80-psi-trap/) — more on Smart Home & Security
<!-- internal-links:end -->

## Sources
- [1] Electronic Frontier Foundation, "Ring Doorbell App Packed with Third-Party Trackers", January 2020 — https://www.eff.org/deeplinks/2020/01/ring-doorbell-app-packed-third-party-trackers
- [2] Princeton CITP, "Announcing IoT Inspector: Studying Smart Home IoT Device Behavior", April 2018 — https://blog.citp.princeton.edu/2018/04/23/announcing-iot-inspector-a-tool-to-study-smart-home-iot-device-behavior
- [3] FBI, PSA I-060525-PSA, "Home Internet Connected Devices Facilitate Criminal Activity", June 2025 — https://www.fbi.gov/investigate/cyber/alerts/2025/home-internet-connected-devices-facilitate-criminal-activity
- [4] FBI, PSA I-031226-PSA, "Evading Residential Proxy Networks: Protecting Your Devices from Becoming a Tool for Criminals", March 2026 — https://www.fbi.gov/investigate/cyber/alerts/2026/evading-residential-proxy-networks-protecting-your-devices-from-becoming-a-tool-for-criminals
