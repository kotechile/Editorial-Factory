---
title: Your Doorbell Won't Need the Cloud
vertical: smart_home_telemetry
kind: news
persona: pro_homeowner
one_big_thing: "Home Assistant 2026.11 made Matter 1.5 cameras a first-class feature with two-way talk. The doorbell feature vendors fold into subscriptions now runs on your own network."
date: 2026-11-24
slug: your-doorbell-wont-need-the-cloud
---

<!-- lead -->
Your doorbell no longer needs a vendor's cloud to hold a conversation. Home Assistant, the open smart-home hub, shipped its November release, and the reason is a change in the standard itself: Matter, the shared home standard, added cameras to its spec. Cameras that follow it now show up as live video feeds, and a button lets you speak back through them [1]. Talking to the door is what a camera plan has been selling all along. That job now runs between your browser and the camera, on your own network [1].

<!-- tldr -->
## At a glance
The new Home Assistant release made cameras that follow the Matter standard appear as live video feeds, with a talk button added as a test feature. This piece looks at what that pulls out from under camera plans, and which limits still apply at home [1].

<!-- tension -->
## The plan's last paid feature
The groundwork sat in the hub's server code for a while, doing work no one could see. This release brings it to the surface [3]. A camera plan sold three things at once. It kept your clips on someone else's server, it relayed the video so your phone could reach home, and it carried your voice back to the door. The camera part of Matter turned the hardware into a plain, open definition, and this release pulls the interface onto the hub you already run [1]. That is why the shift lands now: the parts finally agree on a common rule. The video no longer detours through a vendor's server. The stream runs between your browser and the camera, and the feed mirrors the camera's own state [1]. That includes whether its privacy mode is on. What I find striking is which piece the standard chose to swallow last. Storage was already easy to replace in a house that keeps its data local — an earlier piece here [counted what an always-recording camera can quietly fill](/your-camera-eats-66-gb-daily/) [2] — but speaking through the door was the feature even skeptics paid for. The release notes put it plainly: a test feature called Two-way audio "adds a talk button to the live stream, so you can talk to whoever is near your camera or doorbell" [1].

## By the numbers
- **2 camera paths:** the talk button works with Matter cameras and with Reolink cameras, and nothing else yet [1].
- **1.5:** the Matter spec release that moved cameras into the open standard [1].

<!-- tactical-insight -->
## What to watch
The part I keep circling is which cameras will actually get the button. Only two kinds of camera reach the button today. Matter cameras work out of the box, and Reolink cameras work when set to their direct streaming mode, because the older streaming formats cannot carry sound back to the camera [1]. A Matter camera also needs a Matter server new enough for the job. Home Assistant finds cameras only when the server it talks to can see them [1]. The microphone carries its own limit. Browsers allow mic access only over a secure connection, so the talk button currently requires opening Home Assistant at its secure web address. The team says support inside the mobile apps is still being built [1]. The people closest to this are already testing the edges. Matter Alpha's coverage notes the talk button appears only where the camera's own link-up has added support [3]. Reolink has told Matter Alpha that its plug-in cameras with a speaker should get the new abilities through Home Assistant [3]. That is the pattern to expect from every maker: the gear decides, not the hub. So read your camera maker's release notes rather than the store page. The question that settles whether your gear benefits is whether its firmware ships the camera profile of the standard. That answer lands in the maker's own change notes.

<!-- nuanced-takeaway -->
## The catch
My read is that this sets a floor under the price, not a funeral for the plan. This is a test feature, not a finished product, and the release notes never pretend otherwise [1]. The path that makes the stream direct also narrows who gets it. You need a camera that speaks the camera profile of the standard, a current server, and a secure connection for the mic. The plan is not dead either. Cloud archiving still holds footage off-site. That matters when a thief takes the very camera that filmed them. What changed is the floor under the price. Talk-back, the feature that paid for itself at the door, is now something the standard hands you. Every renewal notice this winter gets measured against that [1].

## Sources
- [1] Home Assistant, "2026.11: A lot in store!", 2026-11-04 — https://www.home-assistant.io/blog/2026/11/04/release-202611/
- [2] Editorial desk, "Your Camera Eats 66 GB: The Hidden Cost", 2026-10 — https://wellroost.com/your-camera-eats-66-gb-daily/
- [3] Matter Alpha, "Matter cameras and two-way talk officially arrive in Home Assistant 2026.11", 2026-11 — https://www.matteralpha.com/industry-news/matter-cameras-and-two-way-talk-officially-arrive-in-home-assistant-2026-11
