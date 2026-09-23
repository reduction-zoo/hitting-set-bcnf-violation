"""Independent Z3 target closure search and end-to-end recovery check."""
import argparse
import itertools
import json
import random
import subprocess
import sys
from pathlib import Path

from z3 import And, Bool, BoolVal, Not, Or, Solver, is_true, sat, unsat


def closure(target, x):
    got = set(x)
    while True:
        size = len(got)
        for fd in target["fds"]:
            if set(fd["lhs"]) <= got:
                got.update(fd["rhs"])
        if len(got) == size:
            return got


def target_answers(target, limit=3):
    names, r = target["attributes"], target["R"]
    choose = {a: Bool(f"pick_{a}") for a in r}
    reached = [{a: Bool(f"reach_{step}_{a}") for a in names} for step in range(len(names) + 1)]
    solver = Solver()
    for a in names:
        solver.add(reached[0][a] == (choose[a] if a in choose else BoolVal(False)))
    for step in range(len(names)):
        for a in names:
            reasons = [And(*(reached[step][b] for b in fd["lhs"]))
                       for fd in target["fds"] if a in fd["rhs"]]
            solver.add(reached[step + 1][a] == Or(reached[step][a], *reasons))
    solver.add(Or(*(And(Not(choose[y]), Not(choose[z]), reached[-1][y], Not(reached[-1][z]))
                    for y in r for z in r if y != z)))
    answers = []
    for _ in range(limit):
        status = solver.check()
        if status == unsat:
            break
        if status != sat:
            raise RuntimeError(f"target Z3 returned {status}")
        model = solver.model()
        x = [a for a in r if is_true(model.eval(choose[a]))]
        got = closure(target, x)
        y = next(a for a in r if a not in x and a in got)
        z = next(a for a in r if a not in x and a not in got)
        answers.append({"X": x, "y": y, "z": z})
        solver.add(Or(*(choose[a] != model.eval(choose[a]) for a in r)))
    return answers or [{"no_solution": True}]


def source_answers(source):
    u = source["universe"]
    return [list(h) for size in range(min(len(u), source["k"]) + 1)
            for h in itertools.combinations(u, size)
            if all(set(h) & set(edge) for edge in source["family"])]


def run(candidate, obj, extract=False):
    process = subprocess.run([sys.executable, str(candidate)] + (["--extract"] if extract else []),
                             input=json.dumps(obj), text=True, capture_output=True)
    if process.returncode:
        raise RuntimeError(process.stderr)
    return json.loads(process.stdout)


def generated_cases():
    yield {"universe": [2, 4], "family": [[4]], "k": 1}
    yield {"universe": ["red", "blue"], "family": [["red"], ["blue"]], "k": 2}
    seeds = range(3021, 3071)
    for seed in seeds:
        rng = random.Random(seed)
        n = rng.randrange(0, 6)
        universe = list(range(n))
        family = [sorted(rng.sample(universe, rng.randrange(n + 1)))
                  for _ in range(rng.randrange(0, 7))]
        yield {"universe": universe, "family": family, "k": rng.randrange(n + 3)}


def main(candidate):
    kinds = set()
    count = 0
    for source in generated_cases():
        target = run(candidate, source)
        assert set(target) == {"attributes", "fds", "R"}
        assert set(target["R"]) <= set(target["attributes"])
        expected = source_answers(source)
        answers = target_answers(target)
        for answer in answers:
            got = run(candidate, {"source": source, "target_solution": answer}, True)
            if answer == {"no_solution": True}:
                assert not expected and got == {"no_solution": True}, (source, answer, got)
                kinds.add("no_solution")
            else:
                x = answer["X"]
                c = closure(target, x)
                assert answer["y"] in c and answer["z"] not in c
                assert answer["y"] not in x and answer["z"] not in x
                assert got.get("set") in expected, (source, answer, got)
                kinds.add("witness")
            count += 1
    print(f"verification passed: 52 instances (50 fresh seeded, 2 labeled), {count} target outputs, kinds={sorted(kinds)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    main(parser.parse_args().candidate)
