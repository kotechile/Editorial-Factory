# SKILL: Executive Editor (the plain-language / gloss pass)

## 1. Objective

Make every article readable by a smart reader who does not work in the article's field. The target
reader is a supply-chain manager reading about model evaluation, or a CTO reading about customs
duty: they understand the argument but not the vocabulary. This pass is the step that turns
specialist vocabulary into something that reader can follow **without leaving the sentence**.

This file is the standard and the term table. `skills/story_draft.md` §3 requires the gloss at
drafting time; `scripts/humanize_loop3.py` requires it on the Loop 3 rewrite; and
`scripts/check_accessibility.py` **hard-fails** a draft or final that uses one of the gated terms
without an explanation at first use. Nothing downstream will rescue a term that ships undefined.

## 2. The rule, in order

1. **Use the plain word if one exists.** "Objection" beats "protective action". "Slows down" beats
   "degrades throughput". "The company named on the import" beats "importer of record". If the plain
   phrase carries the same meaning, the gloss is not needed at all.
2. **If the term must stay, gloss it at first use, in that same sentence.** An em-dash clause or a
   parenthetical, describing what the thing **measures or does** — never a dictionary definition and
   never a restatement of its name.
3. **Never invent.** If the source does not explain the term, say what it does using the plain words
   the source used. A fabricated definition or a made-up acronym expansion is a hallucination and a
   hard failure (see the acronym rule in `skills/claude_humanizer.md`).
4. **Once.** The gloss happens at the first body use. Later bare uses are correct and expected — a
   rule that glosses every mention makes the prose unreadable.
5. **Never in a glossary.** A definitions block at the end of the article, a "key terms" list, or a
   footnote does not satisfy this: the reader hit the term in the second paragraph and read on.

## 3. Shapes that pass the gate

```text
F1 — a single score that balances catching real cases against raising false alarms — climbed to 0.763.
p95 (the slowest 5% of requests) doubled overnight.
a dedupe pass, which removes near-copies before the model ever trains on them
the classifier, the part of the system that puts each case into a bucket
```

All four carry a clause a reader can act on. Note there is no "which means", no "also known as", and
no definition verb — `check_accessibility.py` reads the **shape** (parenthesis, em-dash clause, or
comma appositive), not a vocabulary.

## 4. Shapes that fail — and the fix

| Failing sentence | Why | Fix |
|---|---|---|
| `…blended F1 climb from 0.325 to 0.763` | A reader cannot picture it | `blended F1 — a single score that balances catching real cases against raising false alarms — climb from 0.325 to 0.763` |
| `Then it stripped the most alike fifth, a dedupe pass: every diversity score rose` | The colon explains the *result*, not the term | `a dedupe pass, which removes near-copies before the model trains` |
| `F1 is the harmonic mean of precision and recall` | Two more undefined terms | `F1 — a single score that balances catching real cases against raising false alarms` |
| `our KV cache saturated` | Mechanism named, never explained | `our KV cache (the saved attention state that makes repeat prompts cheap) saturated` |
| `## The dedupe trap` … term never glossed in the prose | A heading is not a gloss | Gloss it in the first sentence under the heading |

## 5. The gated terms

Hard-failed by `scripts/check_accessibility.py::SPECIALIST` when unglossed at first use:

| Term | What the gloss has to convey |
|---|---|
| `F1` (also `F-1`, "F1 score") | one number mixing two kinds of error; say which two |
| `dedupe` / `dedup` / `deduplication` | that it removes near-identical copies before training/testing |
| `classifier` | the component that puts each case into a bucket |
| `test set` / `eval set` | the held-out cases used to judge the system |
| `synthetic data` | machine-written examples standing in for real ones |
| `cosine similarity` | how close two vectors point, i.e. how alike two things are |
| `embedding` | text turned into a list of numbers so closeness can be measured |
| `KV cache` | saved attention state that makes repeat prompts cheap |
| `fine-tuning` | further training of an existing model on your own examples |
| `precision` + `recall` (as a pair) | of the flags raised, how many were right; of the real cases, how many were caught |
| `p50` / `p95` / `p99` | the share of requests slower than this number |

Advisory (reported, never fatal) — replace where possible: `latency`, `throughput`, `token`,
`recall` on its own, `benchmark`, `baseline`, `pipeline`, `orchestration`.

**Membership rule for adding a term.** It earns a place in `SPECIALIST` only when both hold:
(a) a general reader cannot follow the sentence without it, and (b) the word has no ordinary-English
reading that would turn a gloss into noise. "Recall" fails (b) — product recalls exist — which is why
only the `precision`+`recall` *pair* is gated. Add a test in `scripts/test_check_accessibility.py`
with the new term in both shapes, and run `python3 scripts/test_check_accessibility.py`.

## 6. Why this is a gate and not a style note

Measured 2026-11-03 on `/your-dedupe-cut-f1-by-74/`: the headline and the whole argument ride on "F1",
and the body also uses "dedupe pass", "classifier", "test set" and "synthetic" sets. Every existing
gate passed it — Flesch 61, no undefined acronyms (the ALL-CAPS rule cannot see a token like `F1`),
and the jargon list is finance/trade only. A style note in the drafting skill had been ignored for
exactly the reason style notes are ignored: nothing failed.

Calibration on the existing corpus when the gate landed: 19 of 21 readable published artifacts
passed unchanged, so it is not a wall of noise — it catches prose that genuinely never explains its
own vocabulary.

## 7. Command

```bash
python3 scripts/check_accessibility.py context/drafts/YYYY-MM-DD_<slug>_draft.md
# "unglossed terms: F1, dedupe" in the output = the publish holds until both are explained
```
