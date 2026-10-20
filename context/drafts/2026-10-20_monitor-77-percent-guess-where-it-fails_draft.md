---
title: "Your Monitor's 77% Guess: Where It Fails"
vertical: smart_home_telemetry
persona: pro_homeowner
one_big_thing: "A panel monitor measures the circuits it clamps and guesses at everything else, and the published precision of that guess collapses as more appliances are separated (77% across four, 0.10 for the dish washer), so only a clamped circuit is a number you can spend money on."
date: 2026-10-20
slug: monitor-77-percent-guess-where-it-fails
archetype: evergreen
evergreen: true
---

<!-- lead -->
A 2026 paper on a small energy monitor reports 77% precision when it pulls four appliances out of one main meter [1]. That is the average. In the same table the fridge scores 0.84 precision and the dish washer scores 0.10 [1]. So a box that says "dish washer" is right about one time in ten. Your monitor's 77% guess fails unevenly, and the paper shows where.

<!-- tension -->

## The big picture:

A home energy monitor holds two instruments in one case. The clamp around a cable measures the current in that cable. That is a reading. Everything above it in the app is a model.

The model watches the total at the mains. Then it works out which device inside the house caused each bump. Researchers call this load disaggregation. An owner just sees a pie chart.

That job is hard, and the research says so plainly. In the 2026 study the same model hit 90% precision and 96% recall with two appliances [1]. With four it fell to 77% precision and 80% recall [1]. Two extra loads cost thirteen points of precision.

Precision here means the share of its labels that are correct. Recall means the share of real events it finds. Both numbers come from the paper's own table, not from a vendor.

The average hides the worst case. The four-load table reports fridge at 0.84 precision and 0.94 recall, microwave at 0.75 and 0.95, electric furnace at 0.50 and 0.15, and the dish washer at 0.10 and 0.08 [1]. Nine of every ten "dish washer" labels are something else.

The paper explains why the fridge and the microwave separate so well. The fridge makes low-power transitions over long runs, and the microwave makes high-power transitions over short ones [1]. It prints the four-load table without explaining the dish washer.

This is not a toy experiment. It ran on a public dataset from six homes, with five training the model and the sixth held out for testing [1]. The whole model fit in 17 kilobytes and answered in 0.43 milliseconds on a microcontroller [1]. That is the class of method behind an appliance line on a device that costs less than a clamp kit.

A second team measured the naming problem and found a similar shape. Their network classified which of four appliances was running and reached 88.9% accuracy with 88% F1 [2]. Their AlexNet variant reached 80.67% [2]. Per-appliance accuracy inside one home ran from 86.58% for the refrigerator to 94.6% for the dish washer, but only "for carefully chosen values of thresholds", which is their qualifier, not mine [2].

An open reproduction of the same family of models, trained one appliance at a time, lands between 0.5671 F1 for the microwave and 0.8478 for the washing machine [3]. Different data, same spread.

I keep coming back to what this means for a house. Space heating and air conditioning were 52% of annual household energy use in 2020 [4]. The loads an owner most wants to watch are the two biggest. They are also two of the hardest to pull out of a single mains reading. A clamp on the air handler circuit settles it. A guess does not.

## By the numbers

- **77% — Four-appliance precision:** Pulling four appliances from one meter dropped the 2026 model from 90% precision on two loads to 77% on four, with recall falling from 96% to 80% [1].
- **0.10 — Dish washer precision:** Inside that same four-load model the dish washer scored 0.10 precision and 0.08 recall, while the fridge scored 0.84 and 0.94 [1].
- **88.9% and 80.67% — Four-class naming:** A ResNet18 reached 88.9% accuracy and 88% F1 naming which of four appliances was running; the same team's AlexNet reached 80.67% [2].
- **52% — Heating and cooling share:** Space heating and air conditioning were 52% of annual household energy use in 2020, the two loads a monitor is bought to watch [4].

<!-- tactical-insight -->

## What I'd watch:

The argument is settled by arithmetic, not by brand. A clamp measures one conductor and reports what it measured. A disaggregation line reports what a model decided. In an app the two numbers look identical.

- **The clamp count:** A monitor with eight or sixteen branch clamps covers the circuits an owner would act on. Those are the air handler, the water heater, the car charger, the dryer, the pool pump. Each is a measurement rather than an estimate.
- **The inferred lines:** A whole-home monitor without branch clamps still gives an honest total. The breakdown above that total is where the 77% lives. It is a ranking aid, not a reading.
- **The threshold caveat:** Several published accuracies improve a lot with tuned detection thresholds [2]. A threshold tuned on one house is not evidence about another house.
- **The separable shapes:** The research keeps finding that big, sharp, high-power steps separate well and slow, low-power cycling does not [1]. That is the physical reason a fridge is easy and a furnace is not.

What I expect next is disclosure. No consumer monitor publishes its own precision and recall on homes it did not train on. Until one does, an appliance-level line is an unmeasured claim. A clamp is the only part of the system a buyer can check in a week.

<!-- nuanced-takeaway -->

## The catch

A clamp is honest about the wire, not about the device. Two loads on one circuit become one number again. That is what a shared bedroom circuit or a kitchen small-appliance run gives you.

The furnace line in the 2026 table scored 0.50 precision and 0.15 recall [1]. A furnace is exactly the kind of load that shares a circuit in many houses.

The benchmark is also small. Six homes in one dataset, with one held out, is enough to show the direction of the error [1]. It is not enough to predict any particular house.

An owner who buys a monitor for the appliance breakdown alone is paying for the feature with the weakest published record. The total and the circuit lines are the parts that hold up.

I would still install one. The counter-argument is not that the guess is useless. It is that the guess and the measurement arrive in the same app, in the same typeface, with the same confidence. Only one of them can be checked against a nameplate.

<!-- tldr -->

## At a glance

- **The Big Shift:** A panel monitor's appliance-level breakdown is a model's classification, not a meter reading. In a 2026 peer-reviewed result, separating four loads dropped precision to 77%, and the dish washer landed at 0.10.
- **Why It Matters:** Heating and cooling are 52% of household energy use, and those are the loads an owner most wants to see. Acting on an inferred number means acting on something the published record already shows to be unreliable.
- **What I'd Watch:**
  - **Clamp coverage:** The number of branch clamps decides how much of the app is measured rather than inferred.
  - **Held-out accuracy:** Whether a vendor publishes precision and recall on homes it did not train on.
  - **Threshold tuning:** Accuracies that depend on hand-tuned thresholds do not travel between houses.
- **The Catch:** A clamp measures a circuit, and a shared circuit is still one number. The published benchmarks cover a handful of homes, not yours.

## Sources

[1] Wu, Tan, Duan, Yakovlev, Rahman and Shafik, "A Real-Time Tsetlin Machine-based Non-intrusive Load Monitoring System on MCUs", arXiv 2608.18780v2, accepted at the International Symposium on the Tsetlin Machine 2026 — https://arxiv.org/html/2608.18780v2
[2] Shahab et al., "Energy Disaggregation & Appliance Identification in a Smart Home: Transfer Learning enables Edge Computing", arXiv 2301.03018v2 — https://arxiv.org/html/2301.03018v2
[3] St. Angel, "Energy Management Using Real-Time Non-Intrusive Load Monitoring" (goruck/nilm), replication results on the REFIT household dataset — https://github.com/goruck/nilm
[4] US Energy Information Administration, "Use of energy explained: Energy use in homes" — https://www.eia.gov/energyexplained/use-of-energy/homes.php
