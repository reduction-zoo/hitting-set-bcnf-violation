# Campaign state

Budget: 20 rounds. Used: 1. Remaining: 19. Distinct mechanisms: 1.
Board source: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.

Capability probe (2026-09-23): Python 3.12.14 at `/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at `/Users/xiweipan/.local/bin/uv`; SAT Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; SMT Z3 5.1.0 at `/opt/homebrew/bin/z3`; Z3 Python binding 5.1.0 from locked `z3-solver` 5.1.0.0; CP-SAT executable absent; Typst 0.15.1 at `/opt/homebrew/bin/typst`; Lean 4.34.0 and Lake 5.0.0 at `/opt/homebrew/bin`; Mathlib pending (not needed for requested stages); external writing skill `sci-brain:how-to-technical-writing` present at `/Users/xiweipan/.codex/plugins/cache/sci-brain/sci-brain/0.5.0/skills/how-to-technical-writing/SKILL.md`.

Prepare complete: [contract](work/contract.md), [corpus and oracle evidence](work/preparation.md). `uv run python campaigns/hitting-set-bcnf-violation/work/check.py --self-test` passed on 125 cases (47 solvable, 78 unsolvable). The fixed input domain includes `k > n` and arbitrary explicit element labels; see the preparation repair notes.

Status: **ready_for_expert_review** (agent assessment, not human certification). [Round 001 threshold-gated construction](work/proof.md) has executable [F and G](work/algorithm.py), and the [prepared and independent checks](work/verification.md) pass after an explicit-label repair. The [initial independent review](reviews/initial/review.md) returned revise for that defect; the [focused re-review](reviews/label_repair/review.md) advanced the repaired rule. Correctness: reviewed general closure and recovery proof plus finite executable checks. Novelty: a complete bounded rule relative to the inspected 1976 exact-one construction; priority remains unresolved because the 1979 journal full text was inaccessible. Significance: a closure-checkable complete rule for the fixed search question, with quadratic threshold overhead and no large-instance performance claim.

Paper: [Typst source](work/manuscript.typ), [compiled PDF](work/manuscript.pdf). Typst 0.15.1 compilation passed on 2026-09-23; all three rendered pages were inspected for clipping, notation, formula placement and code readability. The technical-writing skill was applied before drafting and in the final language pass. The forward and extract commands in the appendix were run and produced a legal target and `{"set":[4]}` for the stated example. The reviewer's labeled-instance check passed after repair.

Next action: expert review, including comparison with the full 1979 journal proof if accessible. No formal verification was requested. No publication or board change was made. Remaining research-round allocation: 19; no additional construction round is needed. Prospect assessment at completion: complete candidate (earlier medium judgment was conditional on review).

Experience closeout: one distinct [entry created and updated](../../research/experience/threshold-gated-partial-closure.md), zero pending. It originated in round 001 and was checked against the reviewer evidence. No shared board collection was edited.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Threshold-gated projected dependency (first mechanism) | Prepared candidate loop on 121 cases | Supported after label repair and advance review | [round](rounds/001/round.md) |
