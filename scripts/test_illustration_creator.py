#!/usr/bin/env python3
"""Tests for scripts/illustration_creator.py — run: python3 scripts/test_illustration_creator.py

Hermetic: no network, no LLM, no credits. The art director is a stub returning canned JSON and the
kie.ai transport is a stub returning canned task states, so the whole commission — direction,
refusal-repair, generation, provenance, idempotency, frontmatter surgery — is exercised offline.

The regression cases are the ways a generated header actually fails: a treatment repeating
back-to-back, a prompt that asks for legible text, a "macro" brief that is really a wide shot, an
alt text a screen reader cannot use, a cue the article does not contain, a "successful" task with no
image, a result URL that is not an image, and a second run that silently re-spends credits.
"""

from __future__ import annotations

import json
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import illustration_creator as ic  # noqa: E402

PASS, FAIL = [], []


def check(name: str, condition: bool, detail: str = ""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


def raises(name: str, fn, contains: str = ""):
    try:
        fn()
    except BaseException as exc:                    # noqa: BLE001 - the fail-closed path is the assertion
        ok = contains.lower() in str(exc).lower()
        check(name, ok, f"raised {exc!r}" if ok else f"message missing {contains!r}: {exc}")
        return str(exc)
    check(name, False, "did not raise")
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# fixtures
# ─────────────────────────────────────────────────────────────────────────────

ARTICLE = """---
title: "Reshoring Didn't Kill Tariff Risk — It Moved Upstream Into Packaging"
vertical: supplier_risk_reshoring_decision
persona: ops_leader
one_big_thing: "The tariff did not die with reshoring, it moved upstream into packaging."
date: 2026-09-26
slug: reshoring-moved-the-tariff-upstream
synthesis: true
sources:
  - https://fortune.com/2026/09/15/coca-cola-invest-10-billion
  - https://media.rabobank.com/asset/unwrapped.pdf
---

<!-- lead -->
Coca-Cola pledged $10 billion for U.S. plants, yet roughly $3.1 billion of plastics trade landed under a 53% duty [1].

<!-- tension -->
## Tariffs Move Upstream

**The big picture:** Section 338 stacks on the base rate, so packaging crosses a taxed border [2].

**By the numbers:**
- **$3.1 billion:** the exposed slice of the plastics trade [2].
- **53–55%:** the all-in duty on covered items [2].

<!-- nuanced-takeaway -->
## The Catch

The rate is an all-in figure, not a headline tariff.

## Sources
[1] Fortune — "Coca-Cola to invest $10 billion" — https://fortune.com/example
[2] Rabobank — "Unwrapped" — https://media.rabobank.com/example.pdf

<!-- linkedin -->
Internal variant that must never change the image.
"""


PROMPTS = {
    "editorial_macro": "Extreme close-up macro photograph of translucent plastic resin pellets on a "
                       "rough surfaced steel plate, 100mm macro lens, one razor-sharp focal plane, "
                       "shallow depth of field, soft directional daylight, hero object off-centre.",
    "clay_render": "Matte clay 3D render of a small modular assembly: three machined component "
                   "housings with one bay cover unlatched and a connector half-inserted, studio "
                   "render on a neutral seamless backdrop, single soft key light with gentle "
                   "contact shadows, matte muted palette.",
    "component_assembly": "Minimalist studio composition of a modular component assembly: one rack "
                          "rail carrying two module bays, an inspection latch left open on the "
                          "lower bay, hard clean edges, generous negative space, matte muted "
                          "palette of slate grey and ochre.",
}


def brief_json(**over) -> str:
    """A commissionable brief for ARTICLE, with override hooks (the prompt follows the treatment)."""
    base = {
        "style_id": "editorial_macro",
        "rationale": "The story turns on a physical material — plastic resin — and the duty that now "
                     "lands on it before it becomes packaging.",
        "cue": "Moved Upstream Into Packaging",
        "subject": "translucent plastic resin pellets on a rough surface",
        "model": "flux",
        "prompt": PROMPTS["editorial_macro"],
        "negative_prompt": ic.DEFAULT_NEGATIVE,
        "aspect_ratio": "16:9",
        "resolution": "1K",
        "alt_text": "Translucent plastic resin pellets resting on a steel plate.",
        "caption": "The duty now lands on the material before it becomes packaging.",
        "title": "Plastic resin pellets",
        "credit": "Illustration: Editorial-Factory Intelligence Unit",
        "depicts_real_brand": False,
    }
    base.update(over)
    if "prompt" not in over and base["style_id"] in PROMPTS:
        base["prompt"] = PROMPTS[base["style_id"]]
    return json.dumps(base)


def stub_llm(payload: str, *, calls: list | None = None, model: str = ic.GEMINI_MODEL):
    def call(prompt: str, **kwargs):
        if calls is not None:
            calls.append(prompt)
        return payload
    return call


def sequence_llm(*payloads: str, calls: list | None = None):
    """A director that answers differently each time — how a refusal gets repaired."""
    queue = list(payloads)

    def call(prompt: str, **kwargs):
        if calls is not None:
            calls.append(prompt)
        return queue.pop(0) if len(queue) > 1 else queue[0]
    return call


PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 64
JPEG = b"\xff\xd8\xff" + b"0" * 64


class StubTransport:
    """A kie.ai that answers createTask / recordInfo / the result download from a script."""

    def __init__(self, *, states=None, body=PNG, download_status=200, create_ok=True,
                 result_urls=("https://temp.example/img",)):
        self.states = list(states or ["success"])
        self.body = body
        self.download_status = download_status
        self.create_ok = create_ok
        self.result_urls = list(result_urls)
        self.calls: list[tuple] = []
        self.tasks = 0

    def __call__(self, method, url, *, body=None, headers=None, timeout=120):
        self.calls.append((method, url))
        if method == "POST" and url.endswith("/jobs/createTask"):
            if not self.create_ok:
                return 200, json.dumps({"code": 500, "msg": "model not found"}).encode()
            self.tasks += 1
            return 200, json.dumps({"code": 200, "data": {"taskId": f"task{self.tasks}"}}).encode()
        if method == "GET" and "recordInfo" in url:
            state = self.states.pop(0) if len(self.states) > 1 else self.states[0]
            payload = {"code": 200, "data": {
                "taskId": "task1", "state": state, "failMsg": "" if state != "fail" else "Internal Error",
                "creditsConsumed": 7.0 if state == "success" else 0, "costTime": 26000,
                "resultJson": json.dumps({"resultUrls": self.result_urls})
                if state == "success" else "{}"}}
            return 200, json.dumps(payload).encode()
        if method == "GET":
            return self.download_status, self.body
        raise AssertionError(f"unexpected call {method} {url}")


def client(**kwargs) -> ic.KieClient:
    """A client whose sleeps and polls are instant — the stub API answers immediately."""
    kwargs.setdefault("poll_timeout", 0.5)
    return ic.KieClient("test-key", transport=kwargs.pop("transport", StubTransport()),
                        poll_interval=0, sleeper=lambda _s: None, **kwargs)


# ─────────────────────────────────────────────────────────────────────────────
print("treatment catalogue")
# ─────────────────────────────────────────────────────────────────────────────

check("the catalogue has more than one treatment (the desk is not a filter)",
      len(ic.STYLES) >= 6, str(len(ic.STYLES)))
check("every treatment states when to reach for it",
      all(s.when and len(s.when) > 40 for s in ic.STYLES.values()))
check("every treatment carries prompt vocabulary and a valid model",
      all(s.keywords and s.model in ic.MODELS for s in ic.STYLES.values()))
check("every treatment's vocabulary is lowercase (the match is case-folded)",
      all(k == k.lower() for s in ic.STYLES.values() for k in s.keywords))
check("no treatment's own vocabulary invites bare geometry",
      not any(ic._PRIMITIVE_RE.search(k) for s in ic.STYLES.values() for k in s.keywords),
      str([k for s in ic.STYLES.values() for k in s.keywords if ic._PRIMITIVE_RE.search(k)]))
check("the constructed treatments' vocabulary is mechanism vocabulary",
      all(ic._MECHANISM_RE.search(k) for k in ic.STYLES["component_assembly"].keywords),
      str(ic.STYLES["component_assembly"].keywords))
check("a retired treatment id names its replacement",
      bool(ic.RETIRED_STYLES) and all(v in ic.STYLES for v in ic.RETIRED_STYLES.values()),
      str(ic.RETIRED_STYLES))
MECHANISM_WORDS = ("module", "modules", "assembly", "assemblies", "latch", "latches", "switch",
                   "switches", "gearbox", "gearboxes", "truss", "trusses", "rack", "brackets",
                   "inspection gate", "relay", "connector")
check("the mechanism vocabulary matches the singular and the plural of a real part",
      all(ic._MECHANISM_RE.search(w) for w in MECHANISM_WORDS),
      str([w for w in MECHANISM_WORDS if not ic._MECHANISM_RE.search(w)]))

print("\nwhat the image is a reading of")
check("the core text carries the thesis and the lead",
      "moved upstream into packaging" in ic.article_core_text(ARTICLE).lower())
check("...but not the Sources URLs or the LinkedIn variant",
      "media.rabobank.com" not in ic.article_core_text(ARTICLE)
      and "Internal variant" not in ic.article_core_text(ARTICLE))
before = ic.source_hash(ARTICLE)
check("reformatting ## Sources does not change the digest",
      ic.source_hash(ARTICLE.replace("https://fortune.com/example", "https://example.org/x")) == before)
check("rewriting the lead does change it",
      ic.source_hash(ARTICLE.replace("$10 billion", "$12 billion")) != before)
check("source names are read for the 'never depict these' list",
      "Fortune" in ic.source_names(ARTICLE) and "Rabobank" in ic.source_names(ARTICLE),
      str(ic.source_names(ARTICLE)))
check("the numbers section is offered to the director",
      any("53" in n for n in ic._numbers(ARTICLE)), str(ic._numbers(ARTICLE)))

print("\nthe brief — accepted")
brief = ic.validate_brief(json.loads(brief_json()), ARTICLE, allowed=ic.allowed_styles([]))
check("a valid brief parses into a Brief", brief.style_id == "editorial_macro")
check("...with the model id resolved for the API", brief.model_id == "flux-2/pro-text-to-image")
check("...and the cue kept verbatim", brief.cue == "Moved Upstream Into Packaging")

print("\nthe brief — every refusal is explicit")
def refuse(over: dict, contains: str, allowed=None):
    raw = json.loads(brief_json(**over))
    return raises(f"refused: {contains.split('—')[0].strip()[:58]}",
                  lambda: ic.validate_brief(raw, ARTICLE, allowed=allowed or ic.allowed_styles([])),
                  contains)

refuse({"style_id": "interpretive_dance"}, "unknown treatment", allowed=ic.allowed_styles([]))
raises("refused: a treatment used in the last illustrations",
       lambda: ic.validate_brief(json.loads(brief_json()), ARTICLE,
                                 allowed=ic.allowed_styles(["editorial_macro"])),
       "does not repeat a treatment")
refuse({"model": "dall-e"}, "unknown model")
refuse({"style_id": "clay_render", "model": "flux"}, "model_override_reason")
check("...and a stated reason lets the deviation through",
      ic.validate_brief(json.loads(brief_json(style_id="clay_render", model="flux",
                                              model_override_reason="the desk wants soft-body forms "
                                                                    "in a photographic grade")),
                        ARTICLE, allowed=ic.allowed_styles([])).model == "flux")
refuse({"prompt": "A macro close-up of a desk with a sign reading TARIFF RELIEF, 100mm macro lens, "
                  "shallow depth of field."}, "legible text")
refuse({"prompt": "A wide landscape photograph of a factory floor at dawn, seen from the doorway, "
                  "with soft light."}, "vocabulary")
refuse({"prompt": "Extreme close-up macro photograph of 塑料 pellets on a steel plate, 100mm macro "
                  "lens, shallow depth of field."}, "non-Latin")
refuse({"negative_prompt": "blurry, low quality"}, "forbid text")
refuse({"aspect_ratio": "1:1"}, "featured-header shape")
refuse({"resolution": "4K"}, "is not one of 1K, 2K")
refuse({"alt_text": "Pellets."}, "alt_text is")
refuse({"alt_text": "Photo of translucent plastic resin pellets on a steel plate and a thumb."},
       "opens on the medium")
refuse({"alt_text": "A matte clay 3D render showing plastic pellets on a steel plate."},
       "opens on the medium")
refuse({"caption": "no full stop here"}, "caption must be")
refuse({"title": "x"}, "media title must be")
refuse({"rationale": "it fits"}, "rationale must be")
refuse({"cue": "the tariff story"}, "not a verbatim phrase")
refuse({"depicts_real_brand": True}, "depicts a real company")
refuse({"prompt": "Macro close-up photograph of a light bulb glowing above a handshake, 100mm macro "
                  "lens, shallow depth of field, soft daylight."}, "stock-photo cliché")

print("\ndomain grounding — a shape is not a subject")
# The two headers this rule was written from, taken from the desk's own sidecars: two agentic-AI
# articles illustrated as "a rectangle with a colour band" and "a block resting on a wedge".
geometry_message = raises(
    "refused: a prompt whose subject is bare geometry (a rectangle with colour bands)",
    lambda: ic.validate_brief(json.loads(brief_json(
        style_id="clay_render", model="nanobanana",
        prompt="Matte clay 3D render of one large geometric rectangle divided horizontally into "
               "distinct bands of colour, hard edges, generous negative space, matte muted flat "
               "palette.")),
        ARTICLE, allowed=ic.allowed_styles([])), "bare geometry")
check("...and grounding is the only complaint (the treatment vocabulary is satisfied)",
      "vocabulary" not in geometry_message, geometry_message[:200])
raises("refused: a clay render of 'simplified forms' with no mechanism in the frame",
       lambda: ic.validate_brief(json.loads(brief_json(
           style_id="clay_render", model="nanobanana",
           prompt="Matte clay 3D render of three or four simplified geometric forms stacked in a "
                  "clear physical arrangement, studio render on a neutral seamless backdrop, matte "
                  "muted palette, single soft key light.")),
           ARTICLE, allowed=ic.allowed_styles([])), "bare geometry")
raises("refused: cut-paper collage of torn paper scraps with no symbolic mechanism",
       lambda: ic.validate_brief(json.loads(brief_json(
           style_id="paper_collage", model="nanobanana",
           prompt="Cut-paper editorial collage, layered torn paper scraps and strips in muted ink colours, "
                  "clean silhouette edges against a plain background, no legible print.")),
           ARTICLE, allowed=ic.allowed_styles([])), "bare geometry")
check("...but a paper collage depicting a symbolic certificate silhouette is commissionable",
      ic.validate_brief(json.loads(brief_json(
          style_id="paper_collage", model="nanobanana",
          prompt="Minimalist editorial cut-paper collage featuring the silhouette of a stock certificate "
                 "and an hourglass, halftone newsprint texture, clean edges, generous negative space, "
                 "no legible print.")),
          ARTICLE, allowed=ic.allowed_styles([])).style_id == "paper_collage")
check("...but a primitive shape carried by a named mechanism is commissionable",
      ic.validate_brief(json.loads(brief_json(
          style_id="component_assembly", model="nanobanana",
          prompt="Minimalist studio composition of a modular rack holding two rectangular module "
                 "bays, an inspection latch left open, generous negative space, hard clean edges, "
                 "matte muted palette.")),
      ARTICLE, allowed=ic.allowed_styles([])).style_id == "component_assembly")
# A compositional phrase is not shape-talk: "clean geometry" in a photograph describes how the shot
# is framed, and refusing it would send a legitimate architectural brief back for no reason.
check("...and a photographic prompt's compositional 'clean geometry' is not mistaken for the subject",
      ic.validate_brief(json.loads(brief_json(
          style_id="architectural_night", model="flux",
          prompt="Architectural photograph of a modern industrial control building at blue hour, lit "
                 "windows as the only warm light, long exposure with no moving figures, deep blue "
                 "ambient light, clean geometry, small human scale implied by a doorway.")),
      ARTICLE, allowed=ic.allowed_styles([])).style_id == "architectural_night")
raises("refused: a retired treatment, naming the one that replaced it",
       lambda: ic.validate_brief(json.loads(brief_json(style_id="minimal_geometry", model="nanobanana")),
                                 ARTICLE, allowed=ic.allowed_styles([])), "was retired")
refuse({"subject": ""}, "what is in the frame")

print("\nthe art director — refusals are fed back, then exhausted")
calls: list = []
bad_cue = json.dumps({**json.loads(brief_json()), "cue": "a phrase not in the text"})
repaired = ic.direct(ARTICLE, history=[], llm=sequence_llm(bad_cue, brief_json(), calls=calls))
check("a refused brief is retried, not repaired in place", len(calls) >= 2, str(len(calls)))
check("...and the second answer is used", repaired.style_id == "editorial_macro")
check("...with the attempt count recorded", repaired.attempts == 2, str(repaired.attempts))
check("...and the refusal text is carried into the retry prompt",
      "REFUSED" in calls[1], calls[1][-200:])
exhausted = raises("three refusals in a row raise instead of choosing for the director",
                   lambda: ic.direct(ARTICLE, history=[],
                                     llm=stub_llm(json.dumps({**json.loads(brief_json()),
                                                              "style_id": "nope"}))),
                   "did not produce a commissionable brief")
check("...naming the last refusal", "unknown treatment" in exhausted, exhausted[-120:])

seen: list = []
ic.direct(ARTICLE, history=["editorial_macro", "clay_render"],
          llm=stub_llm(brief_json(style_id="component_assembly", model="nanobanana"), calls=seen))
check("the director is told which treatments are already used",
      "editorial_macro, clay_render" in seen[0] and "MUST choose one of" in seen[0])
check("...and a repeat inside the window is not in the allowed set",
      "editorial_macro" not in seen[0].split("MUST choose one of: ")[1].split("\n")[0])
check("...and the commission carries the domain-grounding mandate",
      "DOMAIN GROUNDING" in seen[0] and "bare geometry" in seen[0])
check("...and the commission anchors on Headline and Excerpt",
      "VISUAL ANCHOR" in seen[0] and "Headline:" in seen[0] and "Excerpt:" in seen[0])
# Every vertical the desk publishes to must have a domain bullet: a list that stopped at finance left
# the whole residential set (wellroost.com) ungrounded, which is how a home story came back as an
# abstract house-with-hourglass collage. And rule 5 must not *recommend* editorial_macro for the
# operational topics rule 6 forbids it on, or the two rules cancel out.
_DOMAINS = ["enterprise AI", "supply chain", "energy / utilities", "heavy industry", "finance / tax",
            "residential / home", "career / compensation", "personal tech / tinkering",
            "cross-border living"]
check("...and the vertical -> domain list names a domain for every family on the desk",
      all(d in seen[0] for d in _DOMAINS), str([d for d in _DOMAINS if d not in seen[0]]))
_photo_rule = next((ln for ln in seen[0].splitlines()
                    if ln.startswith("- For stories involving physical operations")), "")
_recommended = _photo_rule.split("Do NOT")[0]
check("...and the photographic-preference rule no longer recommends editorial_macro for operational work",
      bool(_photo_rule) and "editorial_macro" not in _recommended, _photo_rule)

print("\nrotation")
history = ["editorial_macro", "cinematic_still", "clay_render", "document_flatlay", "paper_collage"]
allowed = ic.allowed_styles(history)
check("the last four treatments are withheld", "editorial_macro" not in allowed
      and "document_flatlay" not in allowed, str(allowed))
check("...but the fifth-from-last is available again", "paper_collage" in allowed)
check("a catalogue smaller than the window still yields a choice",
      len(ic.allowed_styles(list(ic.STYLES))) >= 3)
check("four withheld treatments never empty the desk (the window is a style rule, not a corner)",
      all(len(ic.allowed_styles(list(s))) >= 6 for s in
          __import__("itertools").permutations(ic.STYLES, ic.HISTORY_WINDOW)),
      str([len(ic.allowed_styles(list(s))) for s in
           __import__("itertools").permutations(ic.STYLES, ic.HISTORY_WINDOW)]))
constructed = [s for s, v in ic.STYLES.items() if v.model == "nanobanana"]
check("the catalogue's constructed family is the small one (this is what can be emptied)",
      len(constructed) <= ic.HISTORY_WINDOW, str(constructed))
emptied = list(constructed) + ["editorial_macro"] * 2
check("...and a window that would leave no constructed treatment re-admits one",
      any(ic.STYLES[s].model == "nanobanana" for s in ic.allowed_styles(emptied)),
      str(ic.allowed_styles(emptied)))
readmitted = [s for s in ic.allowed_styles(constructed)
              if s in set(constructed[:ic.HISTORY_WINDOW])]
check("...re-admitting the one closest to leaving the window, never the newest",
      readmitted == [constructed[-1]], str(readmitted))
readmit_prompt = ic.director_prompt(ARTICLE, history=list(constructed), allowed=ic.allowed_styles(list(constructed)))
check("...and the director is told that re-admission is not an invitation to repeat",
      "re-admitted" in readmit_prompt, readmit_prompt[:200])
check("...while an ordinary window says nothing about re-admission",
      "re-admitted" not in ic.director_prompt(ARTICLE, history=["editorial_macro"],
                                              allowed=ic.allowed_styles(["editorial_macro"])))

with tempfile.TemporaryDirectory() as tmp:
    ledger = pathlib.Path(tmp) / "illustration_log.md"
    ledger.write_text("| Date | Slug | Vertical | Style | Model | Aspect | Resolution | Credits | File |\n"
                      "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
                      "| 2026-09-29 | `a` | v | `clay_render` | flux | 16:9 | 1K | 5 | `x` |\n"
                      "| 2026-09-30 | `b` | v | `minimal_geometry` | nanobanana | 16:9 | 1K | 18 | `y` |\n",
                      encoding="utf-8")
    check("the ledger is read newest-first",
          ic.style_history(ledger) == ["component_assembly", "clay_render"], str(ic.style_history(ledger)))
    check("...and a row written under a retired id counts as the treatment that replaced it",
          ic.canonical_style_id("minimal_geometry") == "component_assembly"
          and "minimal_geometry" not in ic.style_history(ledger),
          str(ic.style_history(ledger)))
    check("a ledger that does not exist yet is simply empty, not an error",
          ic.style_history(pathlib.Path(tmp) / "nope.md") == [])

print("\nmodel request shapes (the two models do not take the same fields)")
macro = ic.validate_brief(json.loads(brief_json()), ARTICLE, allowed=ic.allowed_styles([]))
flux_payload = ic.KieClient.payload(macro)
check("flux-2 takes prompt/aspect_ratio/resolution", set(flux_payload) ==
      {"prompt", "aspect_ratio", "resolution"}, str(sorted(flux_payload)))
check("...with the negative folded into the prompt", "Do not include:" in flux_payload["prompt"])
clay = ic.validate_brief(json.loads(brief_json(style_id="clay_render", model="nanobanana")),
                         ARTICLE, allowed=ic.allowed_styles([]))
nano_payload = ic.KieClient.payload(clay)
check("nano-banana-pro additionally takes image_input and an explicit output_format",
      nano_payload["image_input"] == [] and nano_payload["output_format"] == "png",
      str(sorted(nano_payload)))
check("...and its model id is the one kie.ai knows", clay.model_id == "nano-banana-pro")

print("\ngeneration")
gen = client().generate(macro)
check("an image is downloaded and typed from its magic bytes",
      gen.image == PNG and gen.ext == "png" and gen.content_type == "image/png", gen.content_type)
check("...with the task id and credits recorded", gen.task_id == "task1" and gen.credits == 7.0)
check("...and the exact request kept for the sidecar", gen.request["model"] == "flux-2/pro-text-to-image")
check("a JPEG answer is typed jpeg and named .jpg",
      client(transport=StubTransport(body=JPEG)).generate(macro).ext == "jpg")
check("a webp answer is typed webp",
      client(transport=StubTransport(body=b"RIFF" + b"\x00" * 4 + b"WEBP" + b"0" * 8))
      .generate(macro).ext == "webp")

interrupted = StubTransport(states=["waiting", "queuing", "generating", "success"])
check("polling rides through the intermediate states",
      client(transport=interrupted).generate(macro).task_id == "task1")
check("...having asked more than once", len(interrupted.calls) >= 4, str(len(interrupted.calls)))

retrying = StubTransport(states=["fail", "success"])
check("a failed task is retried (kie.ai's upstream fails intermittently)",
      client(transport=retrying).generate(macro).task_id == "task2")
check("...and the retry created a second task", retrying.tasks == 2, str(retrying.tasks))
raises("a task that fails every attempt surfaces the provider's reason",
       lambda: client(transport=StubTransport(states=["fail"])).generate(macro), "Internal Error")
raises("a task that never finishes is a timeout, not an empty image",
       lambda: ic.KieClient("k", transport=StubTransport(states=["generating"]), poll_interval=0,
                            poll_timeout=0.01, sleeper=lambda _s: None).generate(macro),
       "did not finish within")
raises("a 'successful' task with no resultUrls is an error",
       lambda: client(transport=StubTransport(result_urls=[])).generate(macro), "no resultUrls")
raises("a result URL that is not an image is refused",
       lambda: client(transport=StubTransport(body=b"<html>expired</html>")).generate(macro),
       "not a JPEG/PNG/WEBP")
raises("a refused createTask names the model",
       lambda: client(transport=StubTransport(create_ok=False)).generate(macro), "model not found")

print("\nstorage, sidecar and ledger")
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    record = ic.store("my-slug", gen, macro, ARTICLE, root=root, now="2026-10-01T12:00:00+00:00")
    image_path = root / record["local_path"]
    sidecar = ic.read_sidecar("my-slug", root)
    check("the image lands beside its sidecar", image_path.exists() and image_path.name == "featured.png")
    check("the sidecar carries the brief, the task and the spend",
          sidecar["style"] == "editorial_macro" and sidecar["task_id"] == "task1"
          and sidecar["credits"] == 7.0 and sidecar["prompt"] == macro.prompt)
    check("...the sha256 of the bytes and of the article text it read",
          sidecar["sha256"].startswith("sha256:") and sidecar["source_hash"] == ic.source_hash(ARTICLE)
          and sidecar["bytes"] == len(PNG))
    check("...and the pinned/attempt provenance the operator may need",
          "director_attempts" in sidecar and sidecar["pinned"] == {})
    ic.append_ledger(record, md=ARTICLE, root=root)
    ic.append_ledger(record, md=ARTICLE, root=root)          # revision 1: not a second row
    ledger_text = (root / "context" / "illustration_log.md").read_text()
    check("one ledger row per generation", ledger_text.count("`my-slug`") == 1,
          str(ledger_text.count("`my-slug`")))
    check("...stating the treatment and the model", "`editorial_macro` | flux" in ledger_text)

    second = ic.store("my-slug", gen, macro, ARTICLE, root=root, now="2026-10-02T09:00:00+00:00")
    check("regenerating bumps the revision and keeps the previous reading in history",
          second["revision"] == 2 and len(second["history"]) == 1
          and second["history"][0]["sha256"] == record["sha256"], json.dumps(second["history"])[:120])
    jpg_record = ic.store("my-slug", ic.KieClient("k", transport=StubTransport(body=JPEG),
                                                  poll_interval=0, sleeper=lambda _s: None)
                          .generate(macro), macro, ARTICLE, root=root)
    leftovers = sorted(p.name for p in image_path.parent.iterdir())
    check("a re-generation in another format does not leave two featured files",
          leftovers == ["featured.jpg", "featured.json"], str(leftovers))
    ic.append_ledger(jpg_record, md=ARTICLE, root=root)
    check("...and the ledger gains a row for the new revision",
          (root / "context" / "illustration_log.md").read_text().count("`my-slug`") == 2)

print("\nthe asset key (a slug that still carries its date)")
DATED = ARTICLE.replace("slug: reshoring-moved-the-tariff-upstream",
                        "slug: 2026-10-01_reshoring-moved-the-tariff-upstream")
check("a dated frontmatter slug is normalized to the bare post slug",
      ic.slug_from_frontmatter(DATED) == "reshoring-moved-the-tariff-upstream",
      ic.slug_from_frontmatter(DATED))
check("...and a bare slug is left alone",
      ic.slug_from_frontmatter(ARTICLE) == "reshoring-moved-the-tariff-upstream")
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    dated_md, _, dated_meta = ic.ensure_illustration(DATED, root=root, client=client(),
                                                    llm=stub_llm(brief_json()))
    check("...so the image is filed under the slug the CMS push looks for",
          dated_meta["local_path"] ==
          "context/assets/illustrations/reshoring-moved-the-tariff-upstream/featured.png"
          and (root / dated_meta["local_path"]).is_file(), dated_meta["local_path"])
    check("...and the artifact records that same path",
          ic.split_frontmatter(dated_md)[0]["image_path"] == dated_meta["local_path"],
          ic.split_frontmatter(dated_md)[0].get("image_path", ""))

print("\nthe pipeline pass — idempotent by content, not by presence")
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    transport = StubTransport()
    md, notes, meta = ic.ensure_illustration(ARTICLE, root=root, client=client(transport=transport),
                                             llm=stub_llm(brief_json()))
    fm, body = ic.split_frontmatter(md)
    check("the artifact now carries the image fields",
          fm["image_style"] == "editorial_macro" and fm["image_alt"] and fm["image_path"],
          str({k: fm.get(k) for k in ic.IMAGE_KEYS}))
    check("...and the Supabase metadata the CMS push needs",
          meta["alt_text"] == fm["image_alt"] and meta["local_path"] == fm["image_path"]
          and meta["task_id"] == "task1")
    check("...and the note reports the direction and the spend",
          any("direction: editorial_macro" in n for n in notes) and any("credits" in n for n in notes),
          str(notes))
    check("the body is untouched by the frontmatter edit", "Tariffs Move Upstream" in body)
    check("the YAML list survives the frontmatter edit",
          "- https://fortune.com/2026/09/15/coca-cola-invest-10-billion" in md
          and "synthesis: true" in md)
    tasks_after_first = transport.tasks

    md2, notes2, meta2 = ic.ensure_illustration(md, root=root, client=client(transport=transport),
                                                llm=stub_llm(brief_json()))
    check("a second run spends nothing and generates nothing", transport.tasks == tasks_after_first)
    check("...and says so", any("already present" in n for n in notes2), str(notes2))
    check("...returning the same metadata (so the CMS push is unchanged)",
          meta2["sha256"] == meta["sha256"])

    rewritten = md.replace("$10 billion", "$12 billion")
    _, notes3, meta3 = ic.ensure_illustration(rewritten, root=root,
                                              client=client(transport=transport),
                                              llm=stub_llm(brief_json()))
    check("a rewritten article is recommissioned", transport.tasks == tasks_after_first + 1)
    check("...and the operator is told the text changed",
          any("text changed" in n for n in notes3), str(notes3))
    check("...as revision 2", meta3["revision"] == 2, str(meta3.get("revision")))

    _, notes4, _ = ic.ensure_illustration(md, root=root, client=client(transport=transport),
                                          llm=stub_llm(brief_json()), force=True)
    check("--force recommissions an unchanged article", transport.tasks == tasks_after_first + 2)

with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    transport = StubTransport()
    ic.ensure_illustration(ARTICLE, root=root, client=client(transport=transport),
                           llm=stub_llm(brief_json()))
    tasks = transport.tasks
    # An article illustrated AFTER it was published: the image and its brief exist, the artifact
    # carries no image fields. Re-running must fill them in, not buy a second reading of the same
    # words — which is what a corpus backfill does to every pre-feature article.
    filled, notes5, meta5 = ic.ensure_illustration(ARTICLE, root=root,
                                                  client=client(transport=transport),
                                                  llm=stub_llm(brief_json()))
    check("an artifact whose image exists but whose frontmatter lacks the fields is filled in",
          "image_style:" in filled and ic.has_illustration(filled), "no fields written")
    check("...without generating anything", transport.tasks == tasks, f"tasks={transport.tasks}")
    check("...and says so", any("generating nothing" in n for n in notes5), str(notes5))
    check("...keeping the same image (the sidecar is not rewritten)",
          meta5["sha256"] == ic.read_sidecar("reshoring-moved-the-tariff-upstream", root)["sha256"]
          and ic.read_sidecar("reshoring-moved-the-tariff-upstream", root)["revision"] == 1)

raises("a pinned treatment the director will not follow fails loudly",
       lambda: ic.validate_brief(json.loads(brief_json(style_id="clay_render", model="nanobanana")),
                                 ARTICLE, allowed=ic.allowed_styles([]),
                                 pinned_style="component_assembly"),
       "pinned treatment")

with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    _, _, pinned_meta = ic.ensure_illustration(
        ARTICLE, root=root, client=client(), pinned_style="component_assembly",
        llm=stub_llm(brief_json(style_id="component_assembly", model="nanobanana")))
    pinned_sidecar = ic.read_sidecar("reshoring-moved-the-tariff-upstream", root)
    check("...and a followed pin is recorded as a pin, not as the director's own choice",
          pinned_sidecar["pinned"] == {"style": "component_assembly"}
          and pinned_meta["style"] == "component_assembly", json.dumps(pinned_sidecar["pinned"]))

print("\nconsistency check (metadata only — the binary may live only on the host)")
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    md, _, _ = ic.ensure_illustration(ARTICLE, root=root, client=client(), llm=stub_llm(brief_json()))
    check("a complete artifact reports no drift", ic.check_artifact(md, root=root) == [],
          str(ic.check_artifact(md, root=root)))
    check("an artifact with no illustration says so (and is not drift)",
          ic.check_artifact(ARTICLE, root=root)[0].startswith("no illustration"))
    sidecar_file = ic.sidecar_path("reshoring-moved-the-tariff-upstream", root)
    sidecar_file.write_text(json.dumps({**json.loads(sidecar_file.read_text()), "alt_text": "different"}),
                            encoding="utf-8")
    check("frontmatter that disagrees with the sidecar is drift",
          any("image_alt != sidecar alt_text" in p for p in ic.check_artifact(md, root=root)),
          str(ic.check_artifact(md, root=root)))
    sidecar_file.unlink()
    check("an illustration whose sidecar is gone is drift",
          any("no sidecar" in p for p in ic.check_artifact(md, root=root)))

print("\nthe report never spends (this is what the gate and a human run)")
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    path = root / "published" / "2026-09-26_x.md"
    path.parent.mkdir(parents=True)
    path.write_text(ARTICLE, encoding="utf-8")
    lines = ic._report(path, root)
    check("an artifact with no illustration is reported as such",
          "no illustration" in lines[0], str(lines))
    md, _, _ = ic.ensure_illustration(ARTICLE, root=root, client=client(), llm=stub_llm(brief_json()))
    path.write_text(md, encoding="utf-8")
    lines = ic._report(path, root)
    check("...and once illustrated, the report names the treatment and the task",
          "editorial_macro" in lines[0] and "task1" in lines[1], str(lines))
    check("...and says whether the article text still matches the image's reading",
          "text unchanged" in lines[1], str(lines[1]))
    path.write_text(md.replace("$10 billion", "$12 billion"), encoding="utf-8")
    check("...flagging a text change as a due re-read",
          "TEXT CHANGED" in ic._report(path, root)[1], str(ic._report(path, root)[1]))

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for name in FAIL:
        print(f"  FAILED: {name}")
sys.exit(1 if FAIL else 0)
