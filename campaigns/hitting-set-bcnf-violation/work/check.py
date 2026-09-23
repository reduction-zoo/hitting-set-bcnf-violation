"""Independent source and target oracles for the fixed reduction contract."""
import argparse
import itertools
import json
import subprocess
import sys
from pathlib import Path

from z3 import Bool, Or, Solver, is_true, sat, unsat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def source_valid(a, out):
    if type(out) is not dict:
        return False
    if set(out) == {"no_solution"} and out["no_solution"] is True:
        return source_oracle(a) is None
    if set(out) != {"set"} or type(out["set"]) is not list:
        return False
    chosen = out["set"]
    return (all(type(i) is int for i in chosen)
            and len(chosen) == len(set(chosen)) and chosen == sorted(chosen)
            and set(chosen) <= set(a["universe"]) and len(chosen) <= a["k"]
            and all(set(chosen) & set(edge) for edge in a["family"]))


def source_oracle(a):
    vars_ = {i: Bool(f"chosen_{i}") for i in a["universe"]}
    solver = Solver()
    for edge in a["family"]:
        solver.add(Or(*(vars_[i] for i in edge)))
    solver.add(sum(vars_.values()) <= a["k"])
    result = solver.check()
    if result == unsat:
        return None
    if result != sat:
        raise RuntimeError(f"source solver returned {result}")
    witness = sorted(i for i, var in vars_.items() if is_true(solver.model().eval(var)))
    if not source_valid(a, {"set": witness}):
        raise AssertionError("solver supplied invalid hitting set")
    return witness


def brute_source(a):
    u = a["universe"]
    return next((list(c) for r in range(min(len(u), a["k"]) + 1)
                 for c in itertools.combinations(u, r)
                 if all(set(c) & set(edge) for edge in a["family"])), None)


def closure(t, selected):
    result = set(selected)
    while True:
        old = len(result)
        for fd in t["fds"]:
            if set(fd["lhs"]) <= result:
                result.update(fd["rhs"])
        if len(result) == old:
            return result


def target_outputs(t):
    r = t["R"]
    for bits in itertools.product((False, True), repeat=len(r)):
        x = [i for i, present in zip(r, bits) if present]
        c = closure(t, x)
        for y in r:
            if y in c and y not in x:
                for z in r:
                    if z not in c and z not in x and y != z:
                        yield {"X": x, "y": y, "z": z}


def target_valid(t, out):
    if type(out) is not dict:
        return False
    if set(out) == {"no_solution"} and out["no_solution"] is True:
        return next(target_outputs(t), None) is None
    if set(out) != {"X", "y", "z"} or type(out["X"]) is not list:
        return False
    x, y, z = out["X"], out["y"], out["z"]
    if not all(type(i) is str for i in x) or len(x) != len(set(x)) or not set(x) <= set(t["R"]):
        return False
    c = closure(t, x)
    return y != z and y in t["R"] and z in t["R"] and y not in x and z not in x and y in c and z not in c


def target_instance_valid(t):
    if type(t) is not dict or set(t) != {"attributes", "fds", "R"}:
        return False
    a = t["attributes"]
    if type(a) is not list or not all(type(x) is str for x in a) or len(a) != len(set(a)):
        return False
    if type(t["R"]) is not list or len(t["R"]) != len(set(t["R"])) or not set(t["R"]) <= set(a):
        return False
    return type(t["fds"]) is list and all(type(fd) is dict and set(fd) == {"lhs", "rhs"}
            and type(fd["lhs"]) is list and type(fd["rhs"]) is list
            and set(fd["lhs"]) <= set(a) and set(fd["rhs"]) <= set(a) for fd in t["fds"])


def run(candidate, value, extract=False):
    cmd = [sys.executable, str(candidate)] + (["--extract"] if extract else [])
    proc = subprocess.run(cmd, input=json.dumps(value), text=True, capture_output=True)
    if proc.returncode:
        raise RuntimeError(f"{cmd}: {proc.stderr}")
    return json.loads(proc.stdout)


def self_test():
    proc = subprocess.run([sys.executable, str(ROOT / "research/validate_preparation.py"), str(HERE / "cases.json")], capture_output=True, text=True)
    if proc.returncode:
        raise AssertionError(proc.stderr)
    cases = json.loads((HERE / "cases.json").read_text())
    from generate_cases import random_source
    yes = no = 0
    for case in cases:
        a = case["source"]
        if case["kind"] == "random" and json.loads(json.dumps(random_source(case["seed"]))) != a:
            raise AssertionError("seed does not reproduce case")
        found = source_oracle(a)
        if found != None:
            yes += 1
            assert source_valid(a, {"set": found})
            assert not source_valid(a, {"no_solution": True})
            assert not source_valid(a, {"set": [len(a["universe"])]})
        else:
            no += 1
            assert source_valid(a, {"no_solution": True})
        assert (found is None) == (brute_source(a) is None)
        assert case["expected"] == ("no_solution" if found is None else "witness")
    assert source_oracle({"universe": [0, 1], "family": [[0], [1]], "k": 1}) is None
    assert source_oracle({"universe": [0, 1], "family": [[0, 1]], "k": 1}) is not None
    t = {"attributes": ["a", "b", "c"], "R": ["a", "b", "c"], "fds": [{"lhs": ["a"], "rhs": ["b"]}]}
    assert target_valid(t, {"X": ["a"], "y": "b", "z": "c"})
    assert not target_valid(t, {"X": ["a"], "y": "c", "z": "b"})
    assert not target_valid(t, {"no_solution": True})
    assert target_valid({"attributes": ["a", "b"], "R": ["a", "b"], "fds": []}, {"no_solution": True})
    print(f"self-test passed: {len(cases)} source cases, {yes} solvable, {no} unsolvable; Z3 and brute force agree")


def candidate_test(candidate):
    cases = json.loads((HERE / "cases.json").read_text())
    outputs = 0
    kinds = set()
    for case in cases:
        a = case["source"]
        t = run(candidate, a)
        assert target_instance_valid(t), (a, t)
        witnesses = list(itertools.islice(target_outputs(t), 3))
        selected = witnesses or [{"no_solution": True}]
        for y in selected:
            assert target_valid(t, y), (a, y)
            recovered = run(candidate, {"source": a, "target_solution": y}, extract=True)
            assert source_valid(a, recovered), (a, y, recovered)
            outputs += 1
            kinds.add("no_solution" if "no_solution" in y else "witness")
    print(f"candidate check passed: {len(cases)} instances, {outputs} target outputs, kinds={sorted(kinds)}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-test", action="store_true")
    group.add_argument("--candidate", type=Path)
    args = p.parse_args()
    self_test() if args.self_test else candidate_test(args.candidate)
