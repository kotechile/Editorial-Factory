# SKILL: Illustration Director (Featured Image)

## 1. Objective
Give every article one header image that reads as a **decision about that story**, not a filter
applied to the desk. The image is commissioned from the article's own text by a frontier art
director (`scripts/illustration_creator.py`), generated on kie.ai, and delivered with the metadata
the CMS needs (alt text, caption, credit, library title) and the provenance the desk needs (prompt,
model, task id, credits, the text digest it read).

The failure this skill exists to prevent is sameness: forty posts sharing one visual language read
as one machine, and a header that has nothing to do with the article reads as filler. The second
failure it prevents is an image that is *wrong* in a waay that costs — legible gibberish text baked
into the pixels, a real company's mark, a stock-photo cliché, alt text a screen reader cannot use.
The third failure is **boring, sterile images**: generic server blades, blank modular cubes, or unlatched
gates on flat backgrounds that lack soul, drama, and narrative weight.

Editorial imagery must have **instantly readable domain semiotics** anchored directly in the article's own vertical.

### The 4-Step Creative Process (The Art Director Standard: Conceptual, Arresting, Non-Literal)
**Talk to the AI like an Art Director, NOT a search engine.** We are so trained to be literal: asking for "work" yields a laptop on a coffee table; asking for "AI" yields a server rack in a datacenter. That is generic, soulless stock filler. The header image is the first promise to a reader — the front door to the house. It must make someone pause, think, and click.

Core principles:
- **Capture Core Theme, Mood, and Tension Without Literal Illustrations**: Avoid pedestrian 1-to-1 depictions. For AI, software, or models, NEVER default to literal datacenters, server racks, or blue circuit traces.
- **Conceptual & Symbolic Visual Storytelling**: Use evocative metaphors, atmospheric elements, striking color palettes, and minimalistic yet impactful compositions. Embody tensions through visual symbolism (e.g. an optical glass prism splitting directional light across dark obsidian, monolithic stone slabs in delicate equilibrium, architectural corridors divided by razor-thin blades of light).
- **Visually Arresting Sense of Curiosity**: Create clarity, balance, and intrigue. The image should feel modern, premium, and editorial (like Medium.com feature spreads, The Atlantic, Wired, Bloomberg Businessweek).
- **Refined Aesthetics & Lighting**: Ultra-high quality, crisp directional lighting (chiaroscuro, golden hour, blue hour), soft gradients, tactile textures, and generous negative space. Zero in-image text, logos, or human faces.
- **Landscape Composition**: Keep the landscape header format (`16:9` or `3:2`) for CMS featured headers, composed with asymmetrical balance and deliberate breathing room.

1. **Anchor on the Core Thesis ('One Big Thing') & Extract the Governing Conflict**:
   - The hero subject MUST visually embody `one_big_thing` — the single non-negotiable revelation and central assertion of the article.
   - **The Peripheral Anecdote Trap**: Articles frequently cite supporting anecdotes, minor case studies, or incidental props (e.g., a delivery van, a screw, a random resin sack, packaging tape, a pallet of scrap, a coffee cup) to illustrate an abstract concept. NEVER elevate an incidental anecdote into the hero subject. The hero subject must represent the **governing mechanism or systemic tension** that drives the entire piece (e.g. formula error inflating safety stock vs actual demand variance, memory write-path persistence bypassing prompt guardrails, rising capital cost vs automation ROI).
   - Identify the core dramatic conflict: where two economic, technical, or operational forces collide or compress an outcome, identify both. Recorded in `core_thesis`, `core_conflict`, and `main_idea`.
2. **Select an Evocative Hero Object or Scene (Conceptual & Symbolic Storytelling)**:
   - Choose a tangible hero object or authentic narrative scene that powerfully represents the core thesis without being pedestrian or literal.
   - Embody the governing dilemma through physical tension: an object caught between opposing forces, compressed by constraints, balancing on a knife edge, or placed in an evocative environment capturing the inflection point.
   - **Eliminate Foggy/Overcast Bias**: For supply chain, freight, logistics, and industrial operations, do NOT default to dreary grey fog, murky mist, or overcast washouts. Use crystal-clear air, high-contrast directional lighting (golden-hour rake, hard geometric sunlight, crisp high-bay industrial illumination), deep black contact shadows, and rich saturated materials (safety yellow, cobalt, weathered orange). Recorded in `object_or_scene`.
3. **Choose the Best Treatment & Model**: Select the treatment from the catalogue that provides maximum visual impact, weaving that treatment's core vocabulary naturally into the prompt.
4. **Craft a Cinematic, High-Texture Prompt**: Specify camera angle, lens/optics (e.g. 35mm anamorphic wide, 100mm macro), dramatic directional lighting (chiaroscuro, deep shadows, single directional spotlight, low-raking sunlight, rim highlights), rich physical textures (weathered metals, frosted copper, polished basalt, optical glass), and generous negative space. Zero in-image text or typography.

## 2. The treatment catalogue (`STYLES` in `scripts/illustration_creator.py`)
The art director may only choose from the catalogue; it is stated to the director verbatim, and
every brief that names a treatment without the vocabulary of that treatment is refused.

## Visual Treatment Catalogue & Selection Rules

When selecting an image treatment for an article or story, choose from the following catalogue based on the narrative trigger. Always route generation to the specified catalogue model (`flux-2 Pro` or `Nano Banana Pro`) and apply the corresponding prompt style formula.

### 1. Editorial Macro (`flux-2 Pro`)
- **Reach for it when:** The story turns on one physical thing (a rare mineral, a microchip, a forged seal) where detail, texture, and scale convey economic or geopolitical stakes.
- **Prompt Formula:** [Subject] captured in extreme macro, hyper-detailed surface texture, dramatic chiaroscuro side-lighting casting deep shadows, shallow depth of field, tactile realism, moody editorial magazine style.

### 2. Cinematic Still (`flux-2 Pro`)
- **Reach for it when:** The article holds one decisive, tense moment or place (a yard at dawn, a control room console, a shutdown line) charged with human presence or imminent transition.
- **Prompt Formula:** [Location/Scene] at twilight, anamorphic lens flare, moody desaturated palette with a single vivid neon accent, volumetric fog, wide cinematic 2.39:1 framing, photographic realism.

### 3. Document Flatlay (`flux-2 Pro`)
- **Reach for it when:** The story is regulatory or contractual (a classified filing, a signed mandate, an emergency rate notice) requiring clean intellectual authority.
- **Prompt Formula:** [Documents/Artifacts] arranged in precise geometric flat-lay on dark brushed slate, crisp overhead studio lighting, sharp typographic contrast, minimal modernist editorial layout.

### 4. Clay Render (`Nano Banana Pro`)
- **Reach for it when:** The news is structural and abstract (a market reordered, a supply layer added, a data flow rerouted) and needs to be visualized as a tangible physical model.
- **Prompt Formula:** Minimalist matte-clay architectural model of [System/Process], soft pastel gradients, tactile rounded edges, clean studio cyclorama lighting, playful modern isometric design.

### 5. Technical Isometric (`Nano Banana Pro`)
- **Reach for it when:** The article explains how a complex system actually works (money flows, multi-agent pipelines, global distribution loops).
- **Prompt Formula:** High-precision axonometric cross-section of [System], glowing neon vector pathways, cutaway layers revealing internal mechanics, dark matte tech background, crisp blueprint clarity.

### 6. Component Assembly (`Nano Banana Pro`)
- **Reach for it when:** The story centers on a single hard constraint, gate, or physical boundary with no human scene to photograph.
- **Prompt Formula:** Industrial macro shot of [Hardware/Bay/Gate], heavy unlatched steel hinges, grease-slicked bolt threads, industrial amber work-light glare, gritty raw hardware aesthetic.

### 7. Paper Collage (`Nano Banana Pro`)
- **Reach for it when:** The piece is a synthesis of two colliding developments, where the friction of the collision is the story.
- **Prompt Formula:** Mixed-media handmade paper cut-out collage depicting [Concept A colliding with Concept B], textured newsprint, torn kraft edges, bold primary ink splashes, tactile layered depth.

### 8. Long Lens Industry (`flux-2 Pro`)
- **Reach for it when:** Scale is the primary narrative driver (a sprawling port, a midnight refinery, a data-centre hall packed with cooling towers).
- **Prompt Formula:** Extreme telephoto compressor shot of [Industrial Site], heat haze distortion waves, rows of rhythmic steel framing, flat geometric layering, monumental scale.

### 9. Studio Object (`flux-2 Pro`)
- **Reach for it when:** The story covers a specific consumer or enterprise product, device, or hardware breakthrough hitting the market.
- **Prompt Formula:** Sleek minimalist product shot of [Device] floating on a reflective obsidian plinth, soft ambient rim lighting, premium matte finish, commercial advertising perfection.

### 10. Architectural Night (`flux-2 Pro`)
- **Reach for it when:** The change happens after hours (automation displacing shifts, algorithmic capacity running while a city sleeps).
- **Prompt Formula:** Brutalist concrete facility at midnight, glowing warm windows cutting through pitch-black surroundings, solitary glowing server racks, long exposure mood, architectural digest style.

### 11. Split Screen Contrast (`Nano Banana Pro`)
- **Reach for it when:** The article contrasts two competing realities (before/after reform, legacy vs. automated stack, urban vs. rural adoption).
- **Prompt Formula:** Diptych split-screen composition contrasting [State A] on the left with warm golden tones against [State B] on the right in stark cool cyan, clean architectural dividing line, graphic editorial contrast.

### 12. Terminal Audit (`flux-2 Pro`)
- **Reach for it when:** The story centers on a software bug, security breach, algorithmic anomaly, or deep-dive code/data investigation.
- **Prompt Formula:** Macro shot of an illuminated vintage amber CRT terminal screen displaying lines of [Code/Data logs] in a dark server room, glowing reflection on a brushed steel desk surface, cinematic hacker aesthetic.

### 13. Historical Artifact (`flux-2 Pro`)
- **Reach for it when:** The piece covers legal precedents, foundational agreements, archival investigations, or multi-decade structural shifts.
- **Prompt Formula:** Aged parchment manuscript of [Document Name] with wax seals and handwritten margin notes, resting on a worn oak table, illuminated by a single warm desk lamp, museum archive lighting, shallow depth of field.

### 14. Cross Section Cutaway (`Nano Banana Pro`)
- **Reach for it when:** The article explains hidden physical infrastructure buried beneath ground or water (subsea cables, metro transit tunnels, subterranean storage).
- **Prompt Formula:** 3D technical cutaway render of [Infrastructure] revealing subterranean layers, bedrock strata, embedded conduit pathways, clean vector callouts, architectural presentation style.

### 15. Schematic Blueprint (`Nano Banana Pro`)
- **Reach for it when:** The story introduces an entirely new system architecture, protocol standard, or conceptual framework before public rollout.
- **Prompt Formula:** White-on-blue architectural blueprint schematic of [System Architecture] with fine drafting lines, crisp grid coordinates, subtle paper grain texture, engineering precision style.

`minimal_geometry` (bare shapes, "no objects") was **retired**: it was the only entry whose `when`
fitted an abstract software story *and* the only one that forbade objects, so it collected exactly the
headers a reader cannot connect to the article. `component_assembly` replaces it and `RETIRED_STYLES`
maps the old id, so the ledger's old rows still count in the anti-repeat window.

**Model routing is a fact about the models, not a preference.** flux-2 Pro is photographic and
physical (macro, cinematic still, flat-lay, telephoto industry, studio object, night architecture);
Nano Banana Pro is better at constructed scenes (clay render, isometric cutaway, component assembly,
paper collage). A brief that deviates from its treatment's catalogue model must state a
`model_override_reason` (≥20 chars) — a silent substitution is how a "photograph" brief lands on an
illustration model and comes back looking like neither.

**The treatment's own `craft`/`medium` text is a direction, and it is read literally.** It is what
made the desk sterile: `clay_render`'s medium read "studio render on a neutral seamless backdrop" and
`component_assembly`'s craft "gallery-print calm", so the director commissioned a parts-on-a-sweep
render and the model drew one. No treatment may prescribe a seamless sweep or a background gradient —
each constructed treatment now names a real material surface (weathered concrete, brushed steel, a
workbench, a drafting table, a table of torn rag paper) and one directional light. The suite pins
this, so a future catalogue entry cannot reintroduce the sweep.

**A shape is not a subject.** For an abstract story the director must reach for a recognisable
physical engineering analogy (modular server components, an unlatched inspection gate, a relay switch,
a linkage, an interlocking connector, a workstation terminal) and name it in the prompt. A prompt whose
subject is bare geometry — a cube, a sphere, a wedge, a slab, "simplified forms" — is refused in code
(`_PRIMITIVE_RE` + `_MECHANISM_RE`) and answered again. The evidence is in the ledger: two agentic-AI
articles were illustrated as "a rectangle with a colour band" and "a block resting on a wedge".

**When to use which model, in practice**: anchor the article by a real place or object where you can
(`cinematic_still`, `editorial_macro`, `studio_object`, `long_lens_industry` → Flux-2 Pro); use
`clay_render`, `technical_isometric`, `component_assembly` and `paper_collage` (→ Nano Banana Pro) for
process diagrams and conceptual models — with a mechanism in the frame, never a bare shape.

## 3. Non-negotiable direction rules (enforced in code, not just in the prompt)
1. **One concrete noun from the story, anchored by the Title + Excerpt with readable domain semiotics.** The art director
   reads the substantive article body to extract the `main_idea` and choose an evocative `object_or_scene`.
   The brief must carry a `cue`: a phrase of ≤10 words copied verbatim from the article that drove
   the treatment. The image must visually symbolize the concept in the Headline + Excerpt across all
   treatments — never generic office workers at desks, and never unformed paper scraps or bare geometry.
   Crucially, the hero subject must directly embody the story's core protagonist, machine, or systemic phenomenon.
   If the headline or lead names an electric vehicle (EV), car, aircraft, cargo vessel, intermodal gantry, industrial turbine, or robotic arm: **that machine must be the hero subject in the frame!**
   Never invert the protagonist by replacing the central machine with an empty background utility box or meter panel.
   Crucially, the image must belong unmistakably to the domain of the story (e.g. AI/compute -> server
   halls/wafers/optical routing; energy -> substations/busbars; logistics -> freight hubs/staging bays;
   residential/property -> an unbranded EV plugged into the home during a blackout, a house envelope, a garage utility wall, a roofline array).
   The director's own vertical→domain list must name a domain for **every** vertical the desk publishes
   to (public.vertical_sites, mirrored in `context/verticals.json`), including the whole residential
   set that feeds wellroost.com — a list that stops at finance leaves half the desk with no grounding
   and is how a home story comes back as an abstract house-with-hourglass collage.
   Never cross-contaminate unrelated domains or invent obscure micro-metaphors
   (like depicting mathematical variance as a lone screw, or software agent topologies as pneumatic valves or plumbing manifolds).
   For software, algorithms, and multi-agent coordination, depict optical beam-splitters, parallel light pathways,
   axonometric technical cutaways, or synchronized instruments — never industrial plumbing. Never use
   `editorial_macro` for systemic, architectural, or operational topics where extreme close-ups strip away
   environmental meaning — and never *recommend* it for those topics elsewhere in the commission (rule 5's
   photographic-preference list must not name it, or the two rules cancel out).
2. **No legible text from the image model, ever.** No text, letters, numbers, wordmarks, signage or UI
   in the frame (they render as rubble) — the negative prompt must forbid them explicitly and the positive
   prompt may not *ask* for them ("a sign reading…" is refused). This is about text the model draws.
   The desk's own cover typography — a topic kicker, the headline and a hook — is composited
   afterwards as a separate, measured step (`scripts/illustration_overlay.py`), because a deliberately
   conceptual image is often not descriptive enough on its own and the type has to carry the topic.
   It is never written by the image model, and it never carries the desk's own name.
3. **No real brand logos, no recognisable people.** The source list is passed to the director as a
   "never depict these companies" list; the brief must assert `depicts_real_brand: false`.
   However, this applies to trademarks, emblems, and logos — it does **NOT** mean omitting the underlying vehicle or machine.
   When the story is about Tesla, Ford, or BYD, depict a sleek, modern, unbranded generic electric vehicle without proprietary badges.
4. **No stock-photo clichés** — light bulb, handshake, chess pieces, glowing brain, gavel, scales,
   thumbs-up, rockets, dartboards, puzzle pieces (`_CLICHE_RE`).
5. **The treatment must be real in the prompt**: at least one word of the chosen treatment's
   vocabulary (e.g. macro → "macro / close-up / depth of field") must appear, or the brief is
   refused. A "macro" brief that is really a wide shot is a different image wearing the label.
6. **A shape is not a subject.** A prompt may mention a primitive shape only when it also names a
   recognisable mechanism ("a modular rack with two module bays", "an unlatched inspection gate"); a
   prompt whose subject is bare geometry — a cube, sphere, wedge, slab, "simplified forms" — is
   refused with that reason and answered again (`_PRIMITIVE_RE` vs `_MECHANISM_RE`). A compositional
   phrase ("clean geometry" in an architectural shot) is not shape-talk and must keep passing.
7. **The treatment must not repeat.** The last four illustrations' treatments are withheld from the
   allowed set, and the director may not answer with one of them. Rows belonging to the *same*
   article are excluded from that window: a rewritten article reusing its own treatment is not a
   repetition. The window is not narrowed below four — at this catalogue size it can never empty the
   desk, and a shorter window would re-use a treatment sooner. What *can* be emptied is a **family**
   (the two catalogue models: 6 flux treatments, 4 nano-banana ones — three of the four constructed
   treatments were used back to back in the first ten illustrations). When the window would leave a
   family with no treatment at all, its oldest blocked member is re-admitted and the director is told
   it is a re-admission, not an invitation to repeat.
8. **Alt text is a deliverable**: ≤125 chars, in English, describing the subject, never starting
   "image of"/"photo of". The caption is one quotable sentence. Both are checked by length and shape.
9. **Featured-header shape**: `16:9` or `3:2`, 1K by default, 2K only where fine physical detail is
   the point.
10. **The image must describe the topic, and must not be sterile.** A reader who sees only the header,
    before the headline, has to be able to name the article's subject area, and the frame has to sit
    in one of the story's own subject-matter classes: physical components/materials or a supply-chain
    bottleneck; a policy collision, regulatory shift or multi-faceted market move; infrastructure,
    automation or scale-driven industrial change; or a systemic process/technical engineering
    operation. The commission forbids the sterile output — a floating abstract cube, a plain rack on a
    neutral gradient, an empty floating widget, a lone object on a seamless sweep — requires each
    prompt to name a real optic (with its falloff) and sculpted light (chiaroscuro, a single
    directional window light, low-raking golden hour, rim highlights), and forbids human faces and
    hands. `sectioned mechanical hardware, precise physical fasteners, industrial brushed metal
    framing` is the vocabulary for a story that is *about* hardware — it is never the default for an
    abstract topic, which the micro-metaphor rule 1 already refuses.
11. **The negative prompt is a liability, not a safety net.** kie takes the prompt as ONE text field,
    so every prohibition is read back as a token to draw: a brief forbidding "abstract cubes, spheres,
    wedges" is a brief that asked for them. Only the legibility/brand set is worth that risk and it is
    appended from `IMAGE_GUARD`, never from the director's `negative_prompt` — a systemic story came
    back as a cube-and-block assembly precisely because the shape negatives travelled with the prompt.
    The director's own negative stays on the brief as provenance and must never enumerate subject
    matter.
12. **A brief must be potent enough to earn an image credit.** `validate_brief` refuses a prompt that
    names no optic, no light, no material and no framing rule (flux), or no structural arrangement, no
    light, no material and no framing rule (Nano Banana). All classes are required — an `any()` over
    the list passes on the single word "shadow". The anchors differ because the models do: flux stages
    a photograph, Nano Banana builds a structure.
13. **The layout is mandated.** The brief carries a `composition` field naming the framing rule
    (extreme asymmetry, low-angle with scale contrast, symmetrical top-down); a composition that
    anchors nothing is how two different articles end up with the same centred object on the same
    sweep.

Three refused briefs in a row raise `BriefError` (with the last refusal quoted) rather than being
repaired here: the treatment choice is the product, so a refusal is fed back to the director and
answered again — the module never picks for it.

## 4. Where things live
- Image: `context/assets/illustrations/<slug>/featured.<jpg|png|webp>` — **not committed**; the CMS
  media library is its canonical home and this file is the upload's source.
- Brief: `context/assets/illustrations/<slug>/featured.json` — **committed**: the full direction
  (treatment, cue, rationale, prompt, negative), the generation (model, task id, credits, sha256 of
  the bytes), the reader metadata (alt, caption, title, credit), and `source_hash`, the digest of
  the article text it read. A regeneration bumps `revision` and keeps the previous reading in
  `history`.
- Ledger: `context/illustration_log.md` — one row per generation. This is what the next article's
  director reads for the anti-repeat window.
- Supabase: `metadata.illustration` on the article row (the CMS push reads the staged path, the alt
  text and the caption from it).
- CMS: the attachment is uploaded and captioned, then set as the post's `featured_media`;
  `metadata.wordpress` records `media_id`, `media_url` and `media_alt` so the next push reuses it.

## 5. Commands
```bash
python3 scripts/illustration_creator.py context/drafts/X_final.md              # report — no spend
python3 scripts/illustration_creator.py context/drafts/X_final.md --dry-run    # brief only (LLM tokens, no image credits)
python3 scripts/illustration_creator.py context/drafts/X_final.md --apply      # direct + generate + write the artifact
python3 scripts/illustration_overlay.py --slug X                               # composite the cover type
python3 scripts/illustration_creator.py --backfill --limit 3                   # every artifact missing one
python3 scripts/illustration_creator.py X.md --apply --style technical_isometric   # pin the treatment
python3 scripts/illustration_creator.py X.md --apply --model nanobanana            # pin the model
python3 scripts/illustration_creator.py --check published/*.md                # exit 1 on frontmatter/sidecar drift (no network)
python3 scripts/wp_draft.py --slug <slug> --reimage                            # put a re-commissioned header on a post that already exists
```

**The cover typography** (`scripts/illustration_overlay.py`) is the last step before the push, for any
article, new or re-commissioned. It writes three lines for the article — a topic kicker, the headline
and a hook — and composites them with the fixed recipe (kicker 2.9% of height in gold, headline 8.6%
bold, hook 3.6%, upper-left or the emptiest corner). Two things are measured rather than assumed: the
corner comes from the edge energy of the image, and the ink and scrim come from the brightest (for
light ink) or darkest (for dark ink) pixel the text block actually covers, raised until the pair
clears a WCAG contrast target. The clean render is kept beside the composited one as
`featured.base.<ext>`, so the step is idempotent and the copy is reused on a re-run. A header is only
finished when the type reads: this is what makes a deliberately conceptual image describable.
A *regenerated* image needs the last command: the CMS push is idempotent by the media slug
(`<slug>-featured`), so an ordinary push reuses the attachment it recorded and only refreshes its
alt/caption — the new reading would sit on this host while the reader kept seeing the old one. The
sweep cannot cover it either (it only pushes rows with no `post_id` yet). `--reimage` uploads the
staged image, points the post at it, deletes the attachment it replaced, writes
`metadata.illustration` + `metadata.wordpress` on the row, and sends no title, excerpt, body or
status — so a live post keeps what an editor tuned in it.

In the pipeline it runs inside the persistence pass (`scripts/publish.py`, `[image]` notes), is
skippable (`--no-illustration`, or `ILLUSTRATION_ENABLED=false`), and is re-run by the host sweep
(`scripts/cron-wp-drafts.sh`) before pushing drafts — so an article whose generation failed gets its
image on the next sweep instead of never.

## 6. Cost and failure handling
- Measured: flux-2 Pro ≈5-7 credits per image (~30-60 s), Nano Banana Pro ≈18 credits (~30 s, PNG).
  A failed task is not billed, which is why `KieClient` retries a failed task 3× and reports every
  attempt. The unused balance is one call: `GET https://api.kie.ai/api/v1/chat/credit`.
- Idempotency is by content, not by presence: an unchanged article is never re-generated (the
  sidecar's `source_hash` matches), a rewritten article is (its text changed). `--force` overrides.
- Missing key → explicit error naming `KIE_API_KEY` (the kie.ai gateway key; an `sk-ant-…` Anthropic
  key authenticates the Claude API but not `api.kie.ai`). Missing `GOOGLE_API_KEY` → explicit error
  naming the director model. Neither ever yields a placeholder image.
- kie.ai upstreams fail intermittently with `Internal Error` on an accepted task: the client retries
  the *task* (new task id) and reports each attempt; a persistent failure surfaces, and the article
  still publishes without a header image.
- A **hang is not a fast fail**: when kie.ai stalls on an accepted task instead of returning
  `Internal Error`, the retry loop can block for many minutes and `scripts/publish.py` times out
  *before* it writes `published/`, the log, Supabase or the sitemap — the persistence steps run
  after the illustration pass. On a hang, re-run publish with `--no-illustration` to persist, then
  recover the header later with `scripts/illustration_creator.py <artifact> --apply` or the host
  sweep.
- The sweep reports an article whose Supabase metadata carries an illustration but whose staged file
  is missing from this host — it pushes the draft without the image and says so, rather than
  silently shipping a headerless post.

## 7. Self-healing
When a generated header fails a rule that is not yet pinned by `scripts/test_illustration_creator.py`
(a new class of unusable prompt, a new metadata defect), add the rule to `validate_brief` and the
regression case to the suite in the same change — the gate (`verify.sh` §8.56) runs the suite
hermetically on every deploy.

A rule that lives only in the commission (domain grounding, treatment-vs-topic judgement) is not
mechanically checkable in the brief alone, so pin its *contract* instead: the suite asserts the
commission still carries the domain mandate and that its vertical→domain list names a domain for
every desk vertical. When a vertical is added to `public.vertical_sites`, add its domain bullet to
`director_prompt` STEP 2 and the matching assertion to the suite in the same change.
