"""Check forward legality on an explicitly labelled source universe."""
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
CANDIDATE = ROOT / "campaigns/hitting-set-bcnf-violation/work/algorithm.py"
source = {"universe": [2, 4], "family": [[4]], "k": 1}
run = subprocess.run([sys.executable, str(CANDIDATE)], input=json.dumps(source),
                     capture_output=True, text=True, check=True)
target = json.loads(run.stdout)
attributes = set(target["attributes"])
unknown = sorted({name for fd in target["fds"]
                  for name in fd["lhs"] + fd["rhs"] if name not in attributes})
print(json.dumps({"source": source, "attributes": target["attributes"],
                  "unknown_fd_attributes": unknown}, sort_keys=True))
assert not unknown, f"FD refers to attributes outside A: {unknown}"
