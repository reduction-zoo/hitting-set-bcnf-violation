# Prepare: independent finite oracles

Date: 2026-09-23. The fixed corpus has 120 distinct source instances: 14 designed edge cases and 106 seeded random cases (accepted seeds 0–136). Universe size is 0–6, family size 0–8, and `k` ranges from 0 to universe size. There are 43 solvable and 77 unsolvable cases. The generator recomputes each expected *existence* answer by enumerating subsets. The self-test reconstructs every seeded case, compares all labels against Z3 5.1.0, and validates returned witnesses from the source definition. This is an existence label, not a fixed chosen witness.

Source Z3 encoding has one Boolean per universe member, one disjunction per family set, and a cardinality upper bound `sum(chosen) <= k`. Its satisfying assignments correspond exactly to hitting sets of size at most `k`; an empty set contributes a false disjunction. Only `sat` and `unsat` are accepted. A small exhaustive solver independently checks each label. Wrong no-solution, malformed sets and members outside the universe are rejected. The target oracle enumerates all `X ⊆ R`, computes closure by repeatedly applying FDs to a fixed point, and enumerates every ordered pair `y,z` meeting the target predicate. It therefore gives a conclusive no-solution answer on its finite domain. Deliberately swapped `y,z` and false no-solution outputs are rejected.

Commands from repository root:

```sh
uv sync --locked
uv run python campaigns/hitting-set-bcnf-violation/work/generate_cases.py
uv run python campaigns/hitting-set-bcnf-violation/work/check.py --self-test
```

The last command passed: 120 cases; 43 solvable, 77 unsolvable; Z3 and exhaustive enumeration agree. `check.py --candidate PATH` is prepared for a subsequent construction. It invokes forward and recovery modes as separate subprocesses, uses actual target outputs from its oracle, and validates recovered source outputs. Its finite target subset enumeration is only practical for small R; larger constructed targets will need a separate solver-based verification path. Finite checks provide no general reduction proof.
