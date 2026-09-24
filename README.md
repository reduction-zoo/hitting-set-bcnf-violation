# Hitting Set → Boyce-Codd normal form violation

**Status:** `ready_for_expert_review` · **Research model:** `GPT-6 family; exact variant unavailable` · **Submitted:** 2026-09-23

The public campaign supplies deterministic polynomial-time construction and recovery for the fixed Hitting Set to Boyce-Codd normal form violation contract. Every valid target output recovers a valid source output, including NO-SOLUTION.

## Construction

Create an attribute for each universe element and an auxiliary attribute for each family set. Incidence dependencies derive a marker when the selected elements hit every set. A polynomial Horn threshold circuit derives a second marker when more than `k` elements are selected; both markers then determine the whole tested relation. Thus a partial closure exists exactly for a hitting set of size at most `k`. Recovery maps the selected attributes back to their original element labels.

## Evidence

- **Mathematical correctness and recovery: Written proof; independent agent review advanced.** The [general proof](campaigns/hitting-set-bcnf-violation/work/proof.md) covers every legal input and target output. The registered [focused review](campaigns/hitting-set-bcnf-violation/reviews/label_repair/review.md) advanced the repaired construction. Human expert acceptance remains pending.
- **Construction and recovery complexity: Written polynomial bounds.** The proof bounds the target encoding by `O(L² log(L+2))` bits for source length `L` and proves polynomial time for both maps. The bounds are not formally certified or claimed optimal.
- **Executable verification: Finite checks passed.** Independent source oracles agreed on 125 cases. The candidate loop checked 202 actual target outputs; a separate Z3 target oracle checked 77 outputs on 52 instances. The reviewer checked every target output on three labeled cases. These checks support the implementation; the general claim rests on the proof. See the [verification record](campaigns/hitting-set-bcnf-violation/work/verification.md).
- **Formal certification and maintainer acceptance: Pending / not performed.** No Lean proof, human expert acceptance, or upstream integration is recorded. The full 1979 Beeri–Bernstein journal construction was unavailable for historical comparison; see the [campaign state](campaigns/hitting-set-bcnf-violation/state.md).

## Reproduce

Run from the repository root:

```sh
uv sync --locked
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --self-test
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --candidate campaigns/hitting-set-bcnf-violation/work/algorithm.py
uv run python campaigns/hitting-set-bcnf-violation/work/verify.py --candidate campaigns/hitting-set-bcnf-violation/work/algorithm.py
```

The finite checks execute the construction and recovery maps. They do not replace the general proof.

## Artifacts

- [Fixed question](campaigns/hitting-set-bcnf-violation/question.md)
- [Campaign state](campaigns/hitting-set-bcnf-violation/state.md)
- [Manuscript](campaigns/hitting-set-bcnf-violation/work/manuscript.pdf)
- [Construction and recovery](campaigns/hitting-set-bcnf-violation/work/algorithm.py)
- [General proof](campaigns/hitting-set-bcnf-violation/work/proof.md)
- [Independent review](campaigns/hitting-set-bcnf-violation/reviews/label_repair/review.md)
- [Verification evidence](campaigns/hitting-set-bcnf-violation/work/verification.md)

## Scope

The independent agent review advanced this candidate to expert review. The board records it as a submitted solution; formal certification, human expert acceptance, upstream integration, and historical priority are not claimed.
