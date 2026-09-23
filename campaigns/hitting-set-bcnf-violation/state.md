# Campaign state

Budget: 20 rounds. Used: 1. Remaining: 19. Distinct mechanisms: 1.
Board source: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.

Capability probe (2026-09-23): Python 3.12.14 at `/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at `/Users/xiweipan/.local/bin/uv`; SAT Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; SMT Z3 5.1.0 at `/opt/homebrew/bin/z3`; Z3 Python binding 5.1.0 from locked `z3-solver` 5.1.0.0; CP-SAT executable absent; Typst 0.15.1 at `/opt/homebrew/bin/typst`; Lean 4.34.0 and Lake 5.0.0 at `/opt/homebrew/bin`; Mathlib pending (not needed for requested stages); external writing skill `sci-brain:how-to-technical-writing` present at `/Users/xiweipan/.codex/plugins/cache/sci-brain/sci-brain/0.5.0/skills/how-to-technical-writing/SKILL.md`.

Prepare complete: [contract](work/contract.md), [corpus and oracle evidence](work/preparation.md). `uv run python campaigns/hitting-set-bcnf-violation/work/check.py --self-test` passed on 121 cases (44 solvable, 77 unsolvable). The fixed input domain includes `k > n`; see the preparation repair note. Round 001 candidate is under test.

Current claim: [round 001 threshold-gated construction](work/proof.md) has executable [F and G](work/algorithm.py), and the [prepared and independent checks](work/verification.md) pass. Correctness is argued generally but independent review is pending; novelty and significance are undecided. Main obstacle: primary-literature comparison and independent audit.

Next action: registered independent review of the committed candidate, then writing if it advances. Prospect of completing within 19 remaining rounds: medium (uncalibrated judgment, conditional on review).

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Threshold-gated projected dependency (first mechanism) | Prepared candidate loop on 121 cases | Supported; review pending | [round](rounds/001/round.md) |
