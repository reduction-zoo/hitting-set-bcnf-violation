"""Independent end-to-end checks for explicit element labels and all target outputs."""
import itertools
import json
import subprocess
import sys
from pathlib import Path


CANDIDATE = Path(__file__).resolve().parents[2] / "work/algorithm.py"
SOURCES = [
    {"universe": [2, 4], "family": [[4]], "k": 1},
    {"universe": [2, 4], "family": [[2], [4]], "k": 1},
    {"universe": ["z", -7, "2"], "family": [["2"], ["z", -7]], "k": 2},
]


def run(value, extract=False):
    cmd = [sys.executable, str(CANDIDATE)] + (["--extract"] if extract else [])
    process = subprocess.run(cmd, input=json.dumps(value), text=True,
                             capture_output=True, check=True)
    return json.loads(process.stdout)


def closure(target, selected):
    reached = set(selected)
    while True:
        old = reached.copy()
        for fd in target["fds"]:
            if set(fd["lhs"]) <= reached:
                reached.update(fd["rhs"])
        if reached == old:
            return reached


for source in SOURCES:
    target = run(source)
    names, relation = target["attributes"], target["R"]
    assert len(names) == len(set(names)) and set(relation) <= set(names)
    assert all(set(fd["lhs"] + fd["rhs"]) <= set(names) for fd in target["fds"])
    valid_sets = [list(subset) for size in range(min(source["k"], len(source["universe"])) + 1)
                  for subset in itertools.combinations(source["universe"], size)
                  if all(set(subset) & set(edge) for edge in source["family"])]
    outputs = []
    for mask in itertools.product((False, True), repeat=len(relation)):
        chosen = [name for name, keep in zip(relation, mask) if keep]
        reached = closure(target, chosen)
        outputs.extend({"X": chosen, "y": y, "z": z}
                       for y in relation if y not in chosen and y in reached
                       for z in relation if z not in chosen and z not in reached)
    for output in outputs or [{"no_solution": True}]:
        recovered = run({"source": source, "target_solution": output}, True)
        if output == {"no_solution": True}:
            assert not valid_sets and recovered == {"no_solution": True}
        else:
            assert recovered.get("set") in valid_sets, (source, output, recovered)
    assert bool(outputs) == bool(valid_sets)
    print(json.dumps({"source": source, "target_outputs": len(outputs),
                      "source_solutions": len(valid_sets)}, sort_keys=True))
