# SKILL: Illustration Director (Featured Image)

## 1. Objective
Give every article one header image that reads as a **decision about that story**, not a filter
applied to the desk. The image is commissioned from the article's own text by a frontier art
director (`scripts/illustration_creator.py`), generated on kie.ai, and delivered with the metadata
the CMS needs (alt text, caption, credit, library title) and the provenance the desk needs (prompt,
model, task id, credits, the text digest it read).

The failure this skill exists to prevent is sameness: forty posts sharing one visual language read
as one machine, and a header that has nothing to do with the article reads as filler. The second
failure it prevents is an image that is *wrong* in a way that costs — legible gibberish text baked
into the pixels, a real company's mark, a stock-photo cliché, alt text a screen reader cannot use.
The third failure is **boring, sterile images**: generic server blades, blank modular cubes, or unlatched
gates on flat backgrounds that lack soul, drama, and narrative weight.

### The 4-Step Creative Process
To ensure editorial imagery matches the standard of top publications (Wired, The Atlantic, Bloomberg Businessweek):
1. **Read Substantive Content & Extract Main Idea**: The LLM reads the core body of the article (not just the headline/excerpt) to identify the central tension, turning point, or real-world stake. Recorded in `main_idea`.
2. **Select an Evocative Hero Object or Scene**: Choose a tangible, storytelling hero object or authentic narrative scene with character, texture, and drama (e.g., an aborted 3D print bird's nest on a glass bed, container cranes at blue hour in coastal fog, high-voltage copper busbars, or a physical relay bypass wired around a dark logic board). Never sterile cubes or plain server racks. Recorded in `object_or_scene`.
3. **Choose the Best Treatment & Model**: Select the treatment from the catalogue that provides maximum visual impact, weaving that treatment's core vocabulary naturally into the prompt.
4. **Craft a Cinematic, High-Texture Prompt**: Specify camera angle, lens/optics (e.g. 35mm anamorphic wide, 100mm macro), dramatic atmospheric lighting (golden hour, volumetric blue-hour haze, rim lighting), rich physical textures (weathered metals, frosted copper, polymers), and elegant composition with negative space.

## 2. The treatment catalogue (`STYLES` in `scripts/illustration_creator.py`)
The art director may only choose from the catalogue; it is stated to the director verbatim, and
every brief that names a treatment without the vocabulary of that treatment is refused.

| Treatment | Reach for it when | Catalogue model |
| --- | --- | --- |
| `editorial_macro` | the story turns on one physical thing — a part, a material, a component, a document — and what it costs, contains or crosses a border is the news | flux-2 Pro |
| `cinematic_still` | the article holds one decisive moment or place (a yard at dawn, a control room, a shutdown line) | flux-2 Pro |
| `document_flatlay` | the story is regulatory or contractual — a filing, a mandate, a rate notice, a purchase order | flux-2 Pro |
| `clay_render` | the news is structural and abstract — a stack reordered, a layer added, a flow rerouted — and the idea is stated as a small assembly of recognisable parts | Nano Banana Pro |
| `technical_isometric` | the article explains how a system or process actually works (money flows, supply chains, an agent assembly line) | Nano Banana Pro |
| `component_assembly` | the story is a single number, rule, gate or shift and there is no scene to photograph — the frame is a real assembly (a modular bay, an unlatched inspection gate, a rack of blades) | Nano Banana Pro |
| `paper_collage` | the piece is a synthesis of two colliding developments and the collision is the story | Nano Banana Pro |
| `long_lens_industry` | scale is the story — a port, a refinery, a data-centre hall, a yard full of cranes | flux-2 Pro |
| `studio_object` | the story is a product, device, price or market for a thing the reader could buy | flux-2 Pro |
| `architectural_night` | the change happens after hours — automation displacing shifts, capacity running while people sleep | flux-2 Pro |

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
1. **One concrete noun from the story, anchored by the Title + Excerpt.** The art director
   reads the substantive article body to extract the `main_idea` and choose an evocative `object_or_scene`.
   The brief must carry a `cue`: a phrase of ≤10 words copied verbatim from the article that drove
   the treatment. The image must visually symbolize the concept in the Headline + Excerpt across all
   treatments — never generic office workers at desks, and never unformed paper scraps or bare geometry.
2. **No legible text, ever.** No text, letters, numbers, wordmarks, signage or UI in the frame
   (they render as rubble) — the negative prompt must forbid them explicitly and the positive
   prompt may not *ask* for them ("a sign reading…" is refused).
3. **No real brands, no recognisable people.** The source list is passed to the director as a
   "never depict these companies" list; the brief must assert `depicts_real_brand: false`.
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
python3 scripts/illustration_creator.py --backfill --limit 3                   # every artifact missing one
python3 scripts/illustration_creator.py X.md --apply --style technical_isometric   # pin the treatment
python3 scripts/illustration_creator.py X.md --apply --model nanobanana            # pin the model
python3 scripts/illustration_creator.py --check published/*.md                # exit 1 on frontmatter/sidecar drift (no network)
python3 scripts/wp_draft.py --slug <slug> --reimage                            # put a re-commissioned header on a post that already exists
```
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
