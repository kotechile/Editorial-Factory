from pathlib import Path

DRAFT = Path("context/drafts/2026-11-06_your-iso-ceiling-fixed-at-vesting_draft.md")
FINAL = Path("context/drafts/2026-11-06_your-iso-ceiling-fixed-at-vesting_final.md")

SRC6 = ('6. Internal Revenue Service, "Publication 525 (2025), Taxable and Nontaxable Income — '
        'statutory and nonstatutory stock options" — https://www.irs.gov/publications/p525')

def add_source(text):
    if "publications/p525" in text:
        return text
    lines = text.rstrip().splitlines()
    # insert after the last numbered source line
    idx = max(i for i, l in enumerate(lines) if l[:2].strip().rstrip(".").isdigit() and l[1] == ".")
    lines.insert(idx + 1, SRC6)
    return "\n".join(lines) + "\n"

# ---- final: precise wording, correct citations
f = FINAL.read_text()
f = f.replace(
    "The tax code measures the cap once a year. That is all a year means here.",
    "The tax code measures the cap once a year.")
f = f.replace(
    "The same rule counts grants in the order they were made, so an older award fills the year before a newer one gets a look [1].",
    "The same rule counts grants in the order they were made, so an older award fills the year before a newer one gets a look [1]. Nothing about your exercise date enters it.")
f = f.replace("Acceleration is where the trap sits. A deal does the damage. The rules count",
              "Acceleration is where the trap sits, and this is the part advisers skip. The rules count")
f = f.replace(
    "Inside an ISO that gap goes into the alternative minimum tax (AMT), a second tax calculation, while a plain option books it as wages [3].",
    "Inside an ISO the gap is not wages while you hold: it goes into the alternative minimum tax (AMT), a second tax calculation, and the whole gain stays a capital gain only if you hold past the statutory period. A plain option reports the gap as wages the day you exercise [6].")
f = f.replace(
    '4. Code of Federal Regulations, "26 CFR § 1.422-4 — $100,000 limitation, Examples 3 and 4"',
    '4. Code of Federal Regulations, "26 CFR § 1.422-4 — $100,000 limitation: rules (b)(4), (b)(6) and (c), with Examples 3 to 6"')
f = add_source(f)
FINAL.write_text(f)

# ---- draft: same source list, same citation number for the tax-treatment claim
d = DRAFT.read_text()
d = d.replace(
    "inside an ISO that gap goes into the alternative minimum tax (AMT), a second tax sum, while a plain option books it as wages [3].",
    "inside an ISO the gap goes into the alternative minimum tax (AMT), a second tax sum, while a plain option books it as wages [6].")
d = add_source(d)
DRAFT.write_text(d)

print("patched")
