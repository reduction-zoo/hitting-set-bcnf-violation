# Round 001: threshold gated projected dependency

## Plan

Gap: the fixed target needs a partial closure in R exactly when a small hitting set exists. Prior evidence: Prepare has 120 labeled source instances and an independent target closure oracle. Experience search on 2026-09-23 for `BCNF`, `hitting set`, `functional dependency`, and `closure` in local and board collections found no applicable entry. A secondary survey reproduces a Beeri–Bernstein hardness argument but its displayed construction does not visibly encode the hitting-set size bound; it is context, not a premise of this attempt.

Hypothesis: put the elements and two markers C,D in R. Element-to-set FDs and an all-sets-to-C FD detect a hit. A polynomial Horn threshold circuit detects more than k selected elements outside R. Only C together with threshold derives D; CD derives all element attributes. Thus a hit with at most k elements derives C but leaves D out, while a larger hit becomes a superkey. A nonhit derives neither marker. Proposed recovery projects any violation determinant X to the element attributes.

First discriminating check: execute the prepared injected-instance candidate loop on the full fixed corpus, independently enumerate actual target outputs, and validate every recovered source answer. A mismatch refutes this construction or decoder; passing supports only finite behavior and triggers a general proof and additional verification.

## Evidence and diagnosis

The first loop passed on 120 cases and 195 target outputs. During the general proof audit, the prepared contract was found to impose `k≤n`, contrary to the fixed question. This was a preparation defect, not a candidate counterexample. The repair added one legal `k>n` case and kept the original evidence in commit `6b73fcf`; the repaired foundation is commit `885c585`. The corrected loop passed on 121 cases and 196 target outputs. Independent Z3 target-closure verification then passed on 50 fresh seeded cases and 75 target outputs. Both valid output kinds occurred. Exact commands and domains are in [verification](../../work/verification.md). The [proof](../../work/proof.md) classifies all determinants `X⊆R` and covers arbitrary valid target witnesses and no-solution.

Observation: the threshold-gated partial closure behaves as predicted on all checked cases. Supported cause: the threshold derivation is outside `R` and can affect `R` only after `C` is derived. Consequence: this candidate is ready for an independent correctness, novelty and significance review. Finite runs alone do not prove the theorem. No counterexample was found.

Independent review [initial](../../reviews/initial/review.md) returned **revise**. Its legal input `U=[2,4]`, `E=[[4]]`, `k=1` exposed an implementation and prepared-contract defect: forward FDs mentioned absent `a0,a1`. The review counterexample failed before repair and remains in commit `6a04629`. The repair indexes arbitrary explicit element names in F, decodes original names in G, and expands the independently labeled corpus. The [review check](../../reviews/initial/check_domain.py) now passes; so do 125 prepared instances/202 outputs and 52 additional instances/77 outputs. The proof and bounds now state the indexing map. This is a repair of the same threshold-gated mechanism, not a new round.

Outcome: supported on the repaired implementation, with an [independent advance review](../../reviews/label_repair/review.md) and a compiled, inspected [paper](../../work/manuscript.pdf). Round 001 is one mechanism: threshold-gated projected dependency. At closeout, the prepared loop exercised 125 source instances and 202 target outputs, the additional Z3 target loop exercised 52 instances and 77 outputs, and the reviewer checked all outputs on three labeled cases. These counts measure finite evidence; the proof handles arbitrary legal instances and target outputs.

Experience extraction: [threshold-gated partial closure](../../../../research/experience/threshold-gated-partial-closure.md) created and updated on 2026-09-23, with independent review context; no board file was edited.

## Next action

Hand off the completed rule and paper for expert review. Historical comparison with the inaccessible full 1979 journal text remains open; no further construction work is indicated by the current evidence.
