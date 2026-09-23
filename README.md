# Hitting Set → Boyce-Codd normal form violation

Independent research campaign. Status: **ready_for_expert_review**. One threshold-gated construction gives deterministic polynomial-time instance construction and recovery from every valid BCNF-violation output, including NO-SOLUTION. The claim is supported by a general proof, finite end-to-end checks, and an independent advance review. Historical priority remains open because the full 1979 Beeri–Bernstein journal construction was unavailable for comparison.

[State](campaigns/hitting-set-bcnf-violation/state.md) · [Question](campaigns/hitting-set-bcnf-violation/question.md) · [Proof](campaigns/hitting-set-bcnf-violation/work/proof.md) · [Paper](campaigns/hitting-set-bcnf-violation/work/manuscript.pdf) · [Independent review](campaigns/hitting-set-bcnf-violation/reviews/label_repair/review.md)

Reproduce the checks from this repository root:

```sh
uv sync --locked
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --self-test
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --candidate campaigns/hitting-set-bcnf-violation/work/algorithm.py
uv run python campaigns/hitting-set-bcnf-violation/work/verify.py --candidate campaigns/hitting-set-bcnf-violation/work/algorithm.py
```

Board source commit: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.
