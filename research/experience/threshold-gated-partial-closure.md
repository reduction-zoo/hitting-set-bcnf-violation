# Threshold-gated partial closure

Tags: functional dependencies, Horn threshold circuit, projected BCNF violation, hitting set.

## Claim and applicability

For a relation subset containing element attributes plus markers C,D, keep family-detection and a polynomial cardinality-threshold Horn circuit outside the subset. If all-family detection derives C, C plus an exceeded threshold derives D, and CD derives all elements, then a partial closure inside the subset corresponds to a family-hitting selection within the threshold. The threshold circuit is needed because enumerating all `k+1`-element subsets may be exponential when `k` is binary encoded.

## Evidence and status

Newly derived in [round 001](../../campaigns/hitting-set-bcnf-violation/rounds/001/round.md), with [proof](../../campaigns/hitting-set-bcnf-violation/work/proof.md) and finite [verification](../../campaigns/hitting-set-bcnf-violation/work/verification.md). The [initial review](../../campaigns/hitting-set-bcnf-violation/reviews/initial/review.md) supported the closure lemma on canonical labels but found an explicit-label implementation defect, repaired on 2026-09-23. The [focused review](../../campaigns/hitting-set-bcnf-violation/reviews/label_repair/review.md) advanced the repair. Status: independently reviewed for this application; historical priority remains qualified by incomplete literature coverage. This is not a claim about unrelated FD gadgets.

## Consequence for search

A threshold can guard a projected dependency while keeping auxiliary state outside the target relation. When reusing, check that no other FD derives an element or marker early and that every partial closure decodes to a legal source witness.

## Use history

- 2026-09-23: derived and used in round 001; passed finite checks, independent review pending.
- 2026-09-23: initial review found a label-domain defect; the same mechanism was repaired and rechecked, with focused re-review pending.
- 2026-09-23: focused review advanced the repaired rule; the reusable claim is supported for the stated FD pattern.
