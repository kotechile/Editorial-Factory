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
Your doorbell no longer needs a vendor's cloud to hold a conversation. Home Assistant, the open smart-home hub, shipped its November release on 2026-11-04, and the reason is a change in the standard itself: Matter, the shared smart-home rulebook, added cameras to its spec. Cameras that follow it now show up as live video on your dashboard, and a test feature adds a button that lets you speak back through them [1]. Talking to the door is what a camera plan has been selling all along. That job now runs between your browser and the camera, on your own network [1].

<!-- tldr -->
## At a glance
Home Assistant's November release made cameras that follow the Matter standard appear as live feeds, with a talk button added as a preview. This piece covers what that pulls out from under camera subscriptions, and which limits still apply at home.

<!-- tension -->
## The plan's last paid feature
The pieces arrived in stages. Matter 1.5, the spec release that moved cameras into the open standard, came first [1]. Then the camera support sat in the hub's server code for a while, doing work no one could see, and Home Assistant 2026.11 brought it to the surface on 2026-11-04 [3]. A camera subscription sold three things in a stack. It kept your clips on someone else's server, it relayed the video so your phone could reach home, and it carried your voice back to the door. The camera part of Matter turned the hardware into a plain, open definition, and this release pulls the interface onto the hub you already run [1]. The video no longer detours through a vendor's server on its way to you. The stream runs over WebRTC (the browser-to-browser video protocol) straight between your browser and the camera, and the feed mirrors the camera's own state, including whether its privacy mode is on [1]. I read the release notes twice before I saw which piece the standard had swallowed last. Storage was already easy to replace in a house that keeps its data local — one earlier piece here [counted what an always-recording camera can quietly fill](/your-camera-eats-66-gb-daily/) [2] — but speaking through the door was the feature even skeptics paid for. The release notes put it plainly: a Labs preview called Two-way audio "adds a talk button to the live stream, so you can talk to whoever is near your camera or doorbell" [1].

## By the numbers
- The talk button works with Matter cameras and Reolink cameras set to direct streaming, and nothing else yet [1].
- Matter 1.5 is the spec release that moved cameras into the open standard [1].

<!-- tactical-insight -->
## What to watch
The open question is which cameras will get the button, and the answer sits with the hardware makers, not the hub. The preview reaches only two kinds of camera today. Matter cameras work out of the box, and Reolink cameras work when set to their direct RTSP (the raw camera-streaming format) mode, because the older streaming formats cannot carry sound back to the camera [1]. A Matter camera also needs a Matter server new enough for the job, since Home Assistant finds cameras only when the server it talks to can see them [1]. The microphone carries its own limit. Browsers allow microphone access only over a secure connection, so the talk button currently requires opening Home Assistant at its HTTPS address, and the developers say support inside the mobile apps is still in development [1]. The people closest to this are already testing the edges. Matter Alpha's coverage notes the talk button appears only where the camera's integration has added support [3]. Reolink has told Matter Alpha that its mains-powered cameras with a speaker should support the new abilities through Home Assistant [3]. What I am watching now is each maker's firmware changelog, because that is where the camera profile of the standard either ships or doesn't — the store page will not tell you.

<!-- nuanced-takeaway -->
## The catch
This sets a floor, not a funeral. It is a preview, not a finished feature, and the release notes never pretend otherwise [1]. The same path that makes the stream direct also narrows who gets it: a camera that speaks the camera profile of the standard, a current Matter server, and a secure connection for the microphone. The subscription is not dead either. Cloud archiving still holds footage off-site, which matters when a thief takes the very camera that filmed them. What changed is the floor under the price. Talk-back, the feature that paid for itself at the door, is now something the standard hands you, and every renewal notice this winter gets measured against that [1].

## Sources
- [1] Home Assistant, "2026.11: A lot in store!", 2026-11-04 — https://www.home-assistant.io/blog/2026/11/04/release-202611/
- [2] Editorial desk, "Your Camera Eats 66 GB: The Hidden Cost", 2026-10 — https://wellroost.com/your-camera-eats-66-gb-daily/
- [3] Matter Alpha, "Matter cameras and two-way talk officially arrive in Home Assistant 2026.11", 2026-11 — https://www.matteralpha.com/industry-news/matter-cameras-and-two-way-talk-officially-arrive-in-home-assistant-2026-11
