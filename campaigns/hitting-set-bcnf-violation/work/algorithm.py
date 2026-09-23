"""Hitting Set to BCNF violation, including recovery of every valid answer."""
import json
import sys


def forward(source):
    universe, family, k = source["universe"], source["family"], source["k"]
    elements = [f"a{i}" for i in universe]
    sets = [f"b{j}" for j in range(len(family))]
    attributes = elements + sets + ["C", "D"]
    fds = []

    def add(lhs, rhs):
        fds.append({"lhs": lhs, "rhs": rhs})

    for j, edge in enumerate(family):
        for i in edge:
            add([f"a{i}"], [f"b{j}"])
    add(sets, ["C"])

    if k < len(universe):
        limit = k + 1
        for i in range(1, len(universe) + 1):
            for j in range(1, min(i, limit) + 1):
                name = f"t{i}_{j}"
                attributes.append(name)
                if j <= i - 1:
                    add([f"t{i-1}_{j}"], [name])
                add(([f"t{i-1}_{j-1}"] if j > 1 else []) + [f"a{i-1}"], [name])
        add(["C", f"t{len(universe)}_{limit}"], ["D"])
    add(["C", "D"], elements)
    return {"attributes": attributes, "fds": fds, "R": elements + ["C", "D"]}


def extract(source, target_solution):
    if target_solution == {"no_solution": True}:
        return {"no_solution": True}
    x = set(target_solution["X"])
    selected = [i for i in source["universe"] if f"a{i}" in x]
    if len(selected) > source["k"] or any(not set(selected).intersection(edge) for edge in source["family"]):
        raise ValueError("target witness does not decode to a hitting set")
    return {"set": selected}


if __name__ == "__main__":
    try:
        request = json.load(sys.stdin)
        answer = extract(request["source"], request["target_solution"]) if sys.argv[1:] == ["--extract"] else forward(request)
        json.dump(answer, sys.stdout)
        sys.stdout.write("\n")
    except (KeyError, TypeError, ValueError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
