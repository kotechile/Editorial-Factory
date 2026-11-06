import re
from pathlib import Path

src = Path("context/drafts/reviews/2026-11-06_your-iso-ceiling-fixed-at-vesting_held.md")
dst = Path("context/drafts/2026-11-06_your-iso-ceiling-fixed-at-vesting_final.md")
t = src.read_text()

subs = [
# title: precise hook, 100 STRONG, lead_ok
('title: "Your ISO Cap Is Fixed at Vesting, Not at Exercise"',
 'title: "Your ISO Ceiling: $100,000, Dead Before Exercise"'),
# lead: gloss the nonstatutory term at first use, keep the lead short-strong
("That is why a buyout is the moment the label can go dead: the deal usually makes every remaining slice buyable at once, and a slice exercised after that acceleration is a nonstatutory option in full.",
 "That is why a buyout is the moment the label can go dead: the deal usually makes every remaining slice buyable at once, and a slice exercised after that acceleration is a plain, nonstatutory option in full."),
# at-a-glance risk: say exactly what acceleration does
("- **The risk:** A buyout's acceleration pushes most of the grant out of the qualified bucket.",
 "- **The risk:** A buyout's acceleration pushes everything past the cap out of the qualified bucket."),
# tension opener: a genuinely short sentence for rhythm variance
("The tax code measures the cap once a year. Options that become buyable",
 "The tax code measures the cap once a year. That is all a calendar year means here. Options that become buyable"),
# tension: define nonstatutory at first body use
("The first stays qualified, the second is split into a qualified part and a plain part, and the third, exercised after the deal, fails in full [4].",
 "The first stays qualified, the second splits into a qualified part and a nonstatutory part, and the third, exercised after the deal, fails in full [4]. A nonstatutory option is simply a plain option, taxed as wages when you exercise it."),
# tactical opener: short sentence
("The rules draw one usable line: an acceleration does not count until the clause fires, so an option exercised before that point keeps its label [4].",
 "The order matters more than the paperwork. An acceleration does not count until the clause fires, so an option exercised before that point keeps its label [4]."),
# catch opener: short sentence
("What I keep tripping on is how uneven the label's value turns out to be.",
 "The label's value is uneven. What I keep tripping on is how much the timing moves it."),
# catch close: restore the inline internal link (article_shape requires one)
("The open question is what the plain share does to an offer once the ceiling has split it. The answer depends on base pay, cash, and vesting stock, not on the ISO label alone.",
 "The open question is what the plain share does to an offer once the ceiling has split it. [The total-compensation model](/calculators/total-comp/) prices base, cash and vesting stock against a growth guess, which is where the split shows up in the number."),
]
for a, b in subs:
    if a not in t:
        print("MISS:", a[:70])
    t = t.replace(a, b, 1)

dst.write_text(t)
print("written", dst, len(t))
