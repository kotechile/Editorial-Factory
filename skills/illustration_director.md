# SKILL: Illustration Director (Featured Image)

## 1. Objective
Give every article one header image that reads as a **decision about that story**, not a filter applied
to the desk. The image is commissioned from the article's own text by a frontier art director
(`scripts/illustration_creator.py`), generated on kie.ai, and delivered with the metadata the CMS needs
(alt text, caption, credit, library title) and the provenance the desk needs (prompt, model, task id,
credits, the text digest it read).

Three failures it exists to prevent: **sameness** (forty posts in one visual language read as one
machine), an image **wrong** in a way that costs — legible gibberish baked into the pixels, a brand mark,
a stock-photo cliché, unusable alt text — and **sterile images**: generic server blades, blank cubes, an
unlatched gate on a flat background. Editorial imagery must carry **instantly readable domain
semiotics** anchored in the article's own vertical.

### The 4-step creative process — talk like an art director, not a search engine
Asking for "work" yields a laptop on a coffee table and asking for "AI" a server rack: that is stock
filler, and the header is the first promise to a reader.

1. **Anchor on the core thesis (`one_big_thing`) and extract the governing conflict.** The hero subject
   must embody the single non-negotiable assertion of the piece and the collision of two forces
   (`core_thesis`, `core_conflict`, `main_idea`). **The peripheral-anecdote trap:** a delivery van, a
   screw, a resin sack, packaging tape, a pallet of scrap or a coffee cup cited to illustrate an
   abstract point is never the hero — the hero is the governing mechanism or systemic tension.
2. **Choose an evocative hero object or scene** and embody the dilemma through physical tension: an
   object between opposing forces, compressed by a constraint, balanced on a knife edge. **No
   foggy/overcast bias** for freight or industry: crystal-clear air, high-contrast directional light,
   deep contact shadows, saturated materials (`object_or_scene`).
3. **Choose the treatment and its model** from the catalogue below, weaving that treatment's own
   vocabulary into the prompt.
4. **Craft a cinematic prompt**: camera angle, lens, directional light (chiaroscuro, a single spotlight,
   low raking sun, rim highlights), physical texture (weathered metal, frosted copper, polished basalt)
   and generous negative space. **No in-frame text, no faces.**

Conceptual and symbolic beats literal — a GPU blade inside a datacenter can enhance a story about power
costs; a datacenter standing in for the idea cannot. Landscape `16:9`, asymmetrical balance, premium
editorial register (*The Atlantic*, *Wired*, *Bloomberg Businessweek*), never stock photography.

## 2. The treatment catalogue (`STYLES` in `scripts/illustration_creator.py`)
The art director may only choose from the catalogue; it is stated to the director verbatim, and a brief
that names a treatment without that treatment's vocabulary is refused. Ten treatments exist in code —
these are the only valid ids (`--style` rejects anything else). Full `when`/`medium`/`craft` text and the
prompt formula for each: casebook.

| id | model | reach for it when |
|---|---|---|
| `editorial_macro` | flux-2 Pro | one physical thing carries the news — a part, a material, a document — and what it costs or crosses a border is the story |
| `cinematic_still` | flux-2 Pro | one decisive moment or place a film still could carry: a yard at dawn, a control room, a shutdown line |
| `document_flatlay` | flux-2 Pro | regulatory or contractual — a filing, a mandate, a rate notice, a purchase order that changed the economics |
| `clay_render` | Nano Banana Pro | structural, abstract news (a stack reordered, a layer added) with no literal object: a small assembly of recognisable parts |
| `technical_isometric` | Nano Banana Pro | how a system, process or stack actually works: money flows, supply chains, an agent assembly line |
| `component_assembly` | Nano Banana Pro | a single number, rule or gate with no scene to photograph: a modular bay, an unlatched inspection gate |
| `paper_collage` | Nano Banana Pro | a purely conceptual synthesis or policy dilemma with no physical facility; **never** for freight, energy or hardware |
| `long_lens_industry` | flux-2 Pro | scale is the narrative driver: a port, a refinery, a data-centre hall, a skyline of cranes |
| `studio_object` | flux-2 Pro | a product, device or price for a thing the reader could buy: an appliance, a panel, a robot arm |
| `architectural_night` | flux-2 Pro | change after hours — automation displacing shifts, capacity running while people sleep |

`minimal_geometry` (bare shapes) was **retired**; `RETIRED_STYLES` maps it to `component_assembly`, so
the ledger's old rows still count in the anti-repeat window. Five ids that older versions of this file
listed — `split_screen_contrast`, `terminal_audit`, `historical_artifact`, `cross_section_cutaway`,
`schematic_blueprint` — **do not exist in `STYLES`** and must not be commissioned.

**Model routing is a fact about the models, not a preference.** flux-2 Pro is photographic and physical
(macro, cinematic still, flat-lay, telephoto industry, studio object, night architecture); Nano Banana
Pro is better at constructed scenes (clay render, isometric cutaway, component assembly, paper collage).
A brief that deviates from its treatment's catalogue model must state a `model_override_reason`
(≥20 chars) — a silent substitution is how a "photograph" brief lands on an illustration model and comes
back looking like neither.

**The treatment's own `craft`/`medium` text is read literally.** No treatment may prescribe a seamless
sweep or a background gradient: each names a real material surface (weathered concrete, brushed steel, a
workbench, torn rag paper) and one directional light, which is what stops the director commissioning a
parts-on-a-sweep render the model then draws.

## 3. Selection rules

- **The treatment must not repeat.** The last four illustrations' treatments are withheld from the
  allowed set. Rows from the *same* article are excluded from that window — a rewritten article reusing
  its own treatment is not a repetition — and the window is never narrowed below four: at this catalogue
  size four withheld treatments cannot empty the desk, while a shorter window re-uses one sooner.
- **Families are guarded separately.** The two catalogue models are the families (six flux treatments,
  four Nano Banana ones). When the window would leave a family with no treatment at all, its oldest
  blocked member is re-admitted and the director is told it is a re-admission, not an invitation to
  repeat.
- **A shape is not a subject.** A prompt whose subject is bare geometry — a cube, a sphere, a wedge, a
  slab, "simplified forms" — is refused in code (`_PRIMITIVE_RE` + `_MECHANISM_RE`) and answered again.
  For an abstract story reach for a recognisable engineering analogy (modular server components, an
  unlatched inspection gate, a relay switch, a linkage, a connector) and name it in the prompt.
- **A pinned treatment is an override, not a default.** `--style <id>` / `--model` exists to break a
  refusal loop or recover a headerless post, never to pre-choose the picture: legitimate for an article
  the director keeps mis-reading, wrong when the failure was a token budget, not a prompt shape.
- **In practice**, anchor on a real place or object where you can (`cinematic_still`,
  `editorial_macro`, `studio_object`, `long_lens_industry` → flux); use `clay_render`,
  `technical_isometric`, `component_assembly`, `paper_collage` (→ Nano Banana) for process diagrams and
  conceptual models — with a mechanism in the frame, never a bare shape.

## 4. Non-negotiable direction rules (enforced in code, not just in the prompt)

1. **The cue is quoted, not written.** The brief carries a `cue`: **a phrase of ≤10 words copied
   verbatim from the article** that drove the treatment, plus one concrete noun from the story. The
   image must belong unmistakably to the story's domain (compute → server halls, wafers, optical routing;
   energy → substations, busbars; logistics → freight hubs, staging bays; property → an unbranded EV on a
   home charger, a roofline array), because the director's vertical→domain list must name a domain for
   **every** vertical the desk publishes to (`public.vertical_sites`, mirrored in
   `context/verticals.json`). Never cross-contaminate domains or invent micro-metaphors (variance as a
   lone screw, agent topologies as plumbing), and never use `editorial_macro` for systemic or
   architectural topics. If the lead names an EV, an aircraft or a robotic arm, that machine is the hero
   subject — never a background utility box.
2. **No legible text.** Random lettering, pseudo-words, numbers and UI clutter render as rubble: the
   negative prompt must forbid them explicitly and the positive prompt may not ask for text ("a sign
   reading…" is refused). Cover typography is composited afterwards (§5), never written by the model.
3. **No brand marks or logos, and no numerals on dials.** `IMAGE_GUARD` is appended to every prompt and
   forbids people, faces, hands, garbled text, random lettering, **numbers**, signage, watermarks, UI
   and **logos**, so brand identity may be carried only by authentic industrial design, silhouette and
   livery — never by an emblem, wordmark, nameplate or a number printed on a dial, gauge or meter. No
   recognisable real person, no human face or hands in frame.
4. **No stock-photo clichés** — light bulb, handshake, chess pieces, glowing brain, gavel, scales,
   thumbs-up, rockets, dartboards, puzzle pieces (`_CLICHE_RE`).
5. **The treatment must be real in the prompt**: at least one word of the chosen treatment's vocabulary
   (macro → "macro / close-up / depth of field") must appear, or the brief is refused.
6. **A shape is not a subject**: a primitive shape may appear only beside a named mechanism ("a modular
   rack with two module bays", "an unlatched inspection gate"); bare geometry is refused. A
   compositional phrase ("clean geometry" in an architectural shot) is not shape-talk.
7. **The image must describe the topic and must not be sterile.** A reader seeing only the header must
   be able to name the subject area, and the frame must sit in one of the story's own classes: physical
   components or a supply-chain bottleneck; a policy collision or market move; infrastructure,
   automation or scale-driven change; or a systems/engineering process. The commission forbids the
   sterile output — a floating cube, a plain rack on a gradient, a lone object on a seamless sweep.
8. **The negative prompt is a liability, not a safety net.** kie takes the prompt as ONE text field, so
   every prohibition is read back as a token to draw. Only the legibility/brand set is worth that risk
   and it is appended from `IMAGE_GUARD`, never from the director's `negative_prompt`; the director's
   own negative stays on the brief as provenance and must never enumerate subject matter.
9. **A brief must be potent enough to earn an image credit.** `validate_brief` requires a named optic, a
   light, a material and a framing rule (flux), or a structural arrangement, a light, a material and a
   framing rule (Nano Banana) — all classes, because an `any()` passes on the word "shadow".
10. **The layout is mandated.** The brief carries a `composition` field naming the framing rule (extreme
    asymmetry, split-screen diptych, low angle with scale contrast, symmetrical top-down); a composition
    that anchors nothing is how two articles end up with the same centred object. An article contrasting
    two scenarios or migration paths (*cloud to on-premise*, *gas versus electric*) takes a split-screen
    diptych: A left, B right, one clean dividing axis, unified lighting.
11. **Header shape and delivery**: `16:9` only (the site crops a 7:4 card and a 16:9 masthead from it),
    1K render at 1344x768 (the owner's call, so cost and look stay put), upscaled 1.79× to a 2400x1350
    sRGB master, progressive JPEG under 400KB, uploaded as `<slug>-featured.jpg`
    (`scripts/image_delivery.py`). Keep the frame simple and the type large: an upscaled busy frame shows it.

Three refused briefs in a row raise `BriefError` (with the last refusal quoted) rather than being
repaired here: the treatment choice is the product, so a refusal is fed back to the director and
answered again — the module never picks for it.

## 5. Alt text, caption and the overlay
- **Alt text is a deliverable**: **40–140 characters** by the delivery check (keep it ≤ ~120), English,
  **one complete sentence describing the pixels** — the subject first, never opening "image of" /
  "photo of" / "render of", never a fragment, and **never the headline glued onto a sentence**. It is
  the only text a screen reader or an image search can read: "AutoStore warehouse grid receding to a
  roll-up door with an oxidised red padlock." is right; "71% Margin Is Your Exit Bill. AutoStore
  warehouse grid…" is a defect twice over — a duplicated title, and a vendor named over a generic
  render. The caption is one quotable sentence; both are checked by length and shape.
- **The cover typography** (`scripts/illustration_overlay.py`) is the last step before the push: kicker,
  headline and hook composited at a fixed recipe into the emptiest corner, with ink and scrim measured
  from the pixels the block covers until the pair clears a WCAG contrast target. The clean render is kept
  as `featured.base.<ext>`, so the step is idempotent, and a header is only finished when the type reads.

## 6. Where things live
- Image: `context/assets/illustrations/<slug>/featured.<jpg|png|webp>` — **not committed**; the CMS
  media library is its canonical home.
- Brief: `context/assets/illustrations/<slug>/featured.json` — **committed**: the full direction
  (treatment, cue, rationale, prompt, negative), the generation (model, task id, credits, sha256 of the
  bytes), the reader metadata (alt, caption, title, credit), `pinned` when a treatment was forced, and
  `source_hash` — the digest of `article_core_text`, the article text it read. A regeneration bumps
  `revision` and keeps the previous reading in `history`.
- Ledger: `context/illustration_log.md` — one row per generation; the next article's anti-repeat window.
- Supabase: `metadata.illustration` on the article row (the CMS push reads the staged path, alt text and
  caption from it); the attachment is captioned and set as the post's `featured_media`, with
  `metadata.wordpress` recording `media_id`, `media_url` and `media_alt` so the next push reuses it.

**Idempotency is by content, not by presence.** An unchanged article is never re-generated — the
sidecar's `source_hash` matches the digest of `article_core_text` (the body minus sources and the
LinkedIn variant) and a `pinned` treatment is reused; a rewritten article is. `--force` overrides,
`--check` compares frontmatter and sidecar with no network call, and a regeneration keeps the previous
reading in `history`.

## 7. Commands
```bash
python3 scripts/illustration_creator.py context/drafts/X_final.md              # report — no spend
python3 scripts/illustration_creator.py context/drafts/X_final.md --dry-run    # brief only (LLM tokens, no credits)
python3 scripts/illustration_creator.py context/drafts/X_final.md --apply      # direct + generate + write the artifact
python3 scripts/illustration_overlay.py --slug X                               # composite the cover type
python3 scripts/illustration_creator.py --backfill --limit 3                   # every artifact missing one
python3 scripts/illustration_creator.py X.md --apply --style technical_isometric   # pin the treatment
python3 scripts/illustration_creator.py X.md --apply --model nanobanana            # pin the model
python3 scripts/illustration_creator.py --check published/*.md                 # exit 1 on sidecar drift (no network)
python3 scripts/wp_draft.py --slug <slug> --reimage                            # re-commissioned header on an existing post
```

`--dry-run` and `--apply` each call the director afresh, so a passing `--dry-run` brief cannot be
reused by `--apply`; budget a refusal as its own director calls (three LLM calls each, **no image
credits**). Publishing without a header is not a fallback — the post goes live with
`featured_media: 0` until `wp_draft --reimage` follows a successful `--apply`.

In the pipeline it runs inside the persistence pass (`scripts/publish.py`, `[image]` notes), is
skippable (`--no-illustration`, or `ILLUSTRATION_ENABLED=false`), and is re-run by the host sweep
(`scripts/cron-wp-drafts.sh`) before pushing drafts — an article whose generation failed gets its image
on the next sweep instead of never.

**Never move or delete `featured.jpg` to force a new overlay copy — it destroys the clean base.** The
overlay reuses the copy in the sidecar's `overlay` key; to change the wording, re-copy
(`cp featured.base.jpg featured.jpg`), drop `overlay`, and run the overlay.

## 8. Cost and failure handling
- **Measured cost per render:** flux-2 Pro ≈5–7 credits (~30–60 s); **Nano Banana Pro ≈18 credits**
  (~30 s, PNG). **A failed task is not billed** — `KieClient` retries a failed task 3× and reports every
  attempt (`creditsConsumed=0`). Balance: `GET https://api.kie.ai/api/v1/chat/credit`.
- A **director refusal** is a headerless publish, not a failed publish: after three refusals
  `publish.py` logs `[image] featured image FAILED` and carries on, and the artifact, the row and the
  CMS post all go live with `featured_media: 0`. Read that line before calling the publish clean and
  recover with a pinned treatment (`--apply --style <treatment> --model <model>`), which supplies the
  missing framing rule, then `wp_draft.py --slug <slug> --reimage`. Retrying unpinned repeats the same
  refusal and spends director calls, not credits.
- A **truncated director call** looks the same and must **not** be pinned: `frontier output truncated
  (finish_reason=length)` is a token budget, not a prompt shape, so a plain `--apply` commissions on the
  first attempt. A kie.ai `Internal Error` is retried on the task with each attempt reported.
- A **hang is not a fast fail**: when kie.ai stalls on an accepted task the retry loop can block for
  minutes and `publish.py` can time out *before* it writes `published/`, the log, Supabase or the
  sitemap (the illustration pass runs first). Re-run publish with `--no-illustration` to persist, then
  recover the header later with `--apply` or the host sweep.
- Missing `KIE_API_KEY` → an error naming it (an `sk-ant-…` key authenticates the Claude API but not
  `api.kie.ai`); missing `DEEPSEEK_API_KEY` → an error naming the director model. Neither ever yields a
  placeholder image.
- **A rejected render must not outlive its rejection.** Delete the rejected staging directory before
  retrying (it short-circuits every retry, and `review.ok: true` with `skipped: true` means *unchecked*,
  not passed), and read the pixels with vision before trusting a sidecar.

## 9. Self-healing
When a generated header fails a rule not yet pinned by `scripts/test_illustration_creator.py`, add the
rule to `validate_brief` and the regression case to the suite in the same change — the gate
(`verify.sh` §8.56) runs the suite hermetically on every deploy. A rule that lives only in the commission
(domain grounding, treatment-vs-topic judgement) is not mechanically checkable from the brief, so pin its
*contract*: the suite asserts the commission still carries the domain mandate and a domain for every desk
vertical. When a vertical is added to `public.vertical_sites`, add its domain bullet to `director_prompt`
STEP 2 and the assertion in the same change.
