"""Rebuild the fixed preconstruction source corpus."""
import json
import random
import itertools
from pathlib import Path

HERE = Path(__file__).resolve().parent


def source(n, family, k):
    return {"universe": list(range(n)), "family": sorted({tuple(sorted(s)) for s in family}), "k": k}


def random_source(seed):
    rng = random.Random(seed)
    n = rng.randrange(1, 7)
    m = rng.randrange(0, 9)
    family = [rng.sample(range(n), rng.randrange(n + 1)) for _ in range(m)]
    return source(n, family, rng.randrange(n + 1))


def main():
    edges = [
        source(0, [], 0), source(1, [], 0), source(1, [[]], 0),
        source(1, [[0]], 0), source(1, [[0]], 1),
        source(2, [[0], [1]], 1), source(2, [[0], [1]], 2),
        source(3, [[0, 1], [1, 2]], 1), source(3, [[0, 1], [1, 2]], 0),
        source(3, [[0, 1], [1, 2]], 2), source(3, [[]], 3),
        source(3, [[0, 1, 2]], 1), source(4, [[0], [1], [2], [3]], 4),
        source(4, [[0], [1], [2], [3]], 3),
    ]
    cases = [{"kind": "edge", "source": x} for x in edges]
    seen = {json.dumps(x, sort_keys=True) for x in edges}
    seed = 0
    while sum(c["kind"] == "random" for c in cases) < 106:
        x = random_source(seed)
        key = json.dumps(x, sort_keys=True)
        if key not in seen:
            cases.append({"kind": "random", "seed": seed, "source": x})
            seen.add(key)
        seed += 1
    for case in cases:
        a = case["source"]
        feasible = any(all(set(choice) & set(edge) for edge in a["family"])
                       for size in range(a["k"] + 1)
                       for choice in itertools.combinations(a["universe"], size))
        case["expected"] = "witness" if feasible else "no_solution"
    (HERE / "cases.json").write_text(json.dumps(cases, indent=2) + "\n")
    print(f"{len(cases)} cases; random seeds 0..{seed-1}")


if __name__ == "__main__":
    main()
