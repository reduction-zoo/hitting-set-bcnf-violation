# Verification of round 001 candidate

Candidate: `work/algorithm.py` and its [general argument](proof.md), initially committed with round 001 and repaired after the [independent review](../reviews/initial/review.md). The prepared checker used Z3 only for source feasibility and enumerated target closures directly. After the explicit-label repair, the complete injected loop passed on 125 fixed cases, covering 202 actual target outputs, including witness and no-solution outputs. The target instance and every recovered source answer were validated against their definitions.

`verify.py` supplies an independent target oracle without importing `check.py` or `algorithm.py`: Z3 encodes closure at each of at most `|A|` stages and searches for a partial closure in `R`. Each returned determinant is checked again by a direct closure computation. On 50 fresh seeded sources (seeds 3021–3070; universe size 0–5, family size 0–6, `k` up to `n+2`) and two explicitly labeled sources, it solved the actual constructed target instances and tested 77 target outputs, with up to three distinct determinants per instance. Independent exhaustive source enumeration checked every recovered set and every no-solution answer. Both target output kinds occurred.

Commands from repository root:

```sh
uv sync --locked
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --self-test
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --candidate campaigns/hitting-set-bcnf-violation/work/algorithm.py
uv run python campaigns/hitting-set-bcnf-violation/work/verify.py --candidate campaigns/hitting-set-bcnf-violation/work/algorithm.py
```

Results on 2026-09-23: self-test 125 cases (47 solvable, 78 unsolvable); candidate loop 125 instances and 202 target outputs; additional verification 52 instances and 77 target outputs. The [reviewer's legal-target check](../reviews/initial/check_domain.py) first failed on `[2,4]` at revision `7c97eac` and now passes, with no unknown FD attributes. The target-closure Z3 formula has one Boolean per attribute and stage and is practical here only at small finite sizes. The proof, not these finite counts, bears the all-input/all-output claim. Larger attribute sets and unusual large element labels were not executed; binary `k>n`, noncanonical labels and degenerate empty cases were exercised. No runtime, memory, or solver-performance claim was measured.
