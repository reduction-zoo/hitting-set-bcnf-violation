# Verification of round 001 candidate

Candidate: `work/algorithm.py` and its [general argument](proof.md), committed with round 001. The prepared checker used Z3 only for source feasibility and enumerated target closures directly. After the binary-`k` contract repair, the complete injected loop passed on 121 fixed cases, covering 196 actual target outputs, including witness and no-solution outputs. The target instance and every recovered source answer were validated against their definitions.

`verify.py` supplies an independent target oracle without importing `check.py` or `algorithm.py`: Z3 encodes closure at each of at most `|A|` stages and searches for a partial closure in `R`. Each returned determinant is checked again by a direct closure computation. On 50 fresh seeded sources (seeds 3021–3070; universe size 0–5, family size 0–6, `k` up to `n+2`), it solved the actual constructed target instances and tested 75 target outputs, with up to three distinct determinants per instance. Independent exhaustive source enumeration checked every recovered set and every no-solution answer. Both target output kinds occurred.

Commands from repository root:

```sh
uv sync --locked
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --self-test
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --candidate campaigns/hitting-set-bcnf-violation/work/algorithm.py
uv run python campaigns/hitting-set-bcnf-violation/work/verify.py --candidate campaigns/hitting-set-bcnf-violation/work/algorithm.py
```

Results on 2026-09-23: self-test 121 cases (44 solvable, 77 unsolvable); candidate loop 121 instances and 196 target outputs; additional verification 50 instances and 75 target outputs. The target-closure Z3 formula has one Boolean per attribute and stage and is practical here only at small finite sizes. The proof, not these finite counts, bears the all-input/all-output claim. Larger attribute sets and arbitrary noncanonical input labels were not executed; binary `k>n` and degenerate empty cases were exercised. No runtime, memory, or solver-performance claim was measured.
