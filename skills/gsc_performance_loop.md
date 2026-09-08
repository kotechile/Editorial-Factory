# SKILL: GSC Performance Loop & Continuous Learning

## 1. Objective
Track post-publishing ranking trajectory, CTR, and search impression velocity in Google Search Console, feeding insights back into Growth OS memory (`performance_learnings.md`) to refine future topic selection and headline styling.

## 2. Tracking Cadence
- **Day 7 Check**: Initial indexation, early impressions, and schema validation.
- **Day 14 Check**: Strike-distance position movement (tracking if moving into top 10).
- **Day 30 Review**: CTR benchmark review, conversion metrics, and content refresh evaluation.

## 3. Execution Protocol
Run the performance loop evaluator:
```bash
python3 scripts/gsc_feedback.py --export
```

## 4. Learning Extraction
Update `context/growth_os/performance_learnings.md` when:
1. An article achieves a CTR > 5% on striking-distance queries (log the headline formula).
2. An article stalls at position 12–20 (trigger internal linking boost or section expansion).
3. A rich FAQ snippet is captured in Google SERP (log the Q&A formatting pattern).
