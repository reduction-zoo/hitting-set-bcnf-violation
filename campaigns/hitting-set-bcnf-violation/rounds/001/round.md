# Round 001: threshold gated projected dependency

## Plan

Gap: the fixed target needs a partial closure in R exactly when a small hitting set exists. Prior evidence: Prepare has 120 labeled source instances and an independent target closure oracle. Experience search on 2026-09-23 for `BCNF`, `hitting set`, `functional dependency`, and `closure` in local and board collections found no applicable entry. A secondary survey reproduces a Beeri–Bernstein hardness argument but its displayed construction does not visibly encode the hitting-set size bound; it is context, not a premise of this attempt.

Hypothesis: put the elements and two markers C,D in R. Element-to-set FDs and an all-sets-to-C FD detect a hit. A polynomial Horn threshold circuit detects more than k selected elements outside R. Only C together with threshold derives D; CD derives all element attributes. Thus a hit with at most k elements derives C but leaves D out, while a larger hit becomes a superkey. A nonhit derives neither marker. Proposed recovery projects any violation determinant X to the element attributes.

First discriminating check: execute the prepared injected-instance candidate loop on the full fixed corpus, independently enumerate actual target outputs, and validate every recovered source answer. A mismatch refutes this construction or decoder; passing supports only finite behavior and triggers a general proof and additional verification.

## Evidence and diagnosis

The first loop passed on 120 cases and 195 target outputs. During the general proof audit, the prepared contract was found to impose `k≤n`, contrary to the fixed question. This was a preparation defect, not a candidate counterexample. The repair added one legal `k>n` case and kept the original evidence in commit `6b73fcf`; the repaired foundation is commit `885c585`. The corrected loop passed on 121 cases and 196 target outputs. Independent Z3 target-closure verification then passed on 50 fresh seeded cases and 75 target outputs. Both valid output kinds occurred. Exact commands and domains are in [verification](../../work/verification.md). The [proof](../../work/proof.md) classifies all determinants `X⊆R` and covers arbitrary valid target witnesses and no-solution.

Observation: the threshold-gated partial closure behaves as predicted on all checked cases. Supported cause: the threshold derivation is outside `R` and can affect `R` only after `C` is derived. Consequence: this candidate is ready for an independent correctness, novelty and significance review. Finite runs alone do not prove the theorem. No counterexample was found.

Outcome: supported, pending independent review. Round 001 is one mechanism: threshold-gated projected dependency.

Experience extraction: [threshold-gated partial closure](../../../../research/experience/threshold-gated-partial-closure.md) created on 2026-09-23 as an unreviewed reusable lemma; no board file was edited.

## Next action

Commit round 001, ask the registered reviewer in a fresh context to audit the unchanged candidate and primary literature, then resolve specific findings or advance to writing.
