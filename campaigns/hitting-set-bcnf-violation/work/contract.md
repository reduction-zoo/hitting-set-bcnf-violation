# Executable contract

Source JSON: `{"universe":[0,...,n-1],"family":[[i,...],...],"k":integer}`. Members and sets are distinct, listed in increasing order; the family may be empty or contain the empty set. `k >= 0` is binary encoded and may exceed `n`. A source output is `{"set":[i,...]}` with at most `k` members hitting every set, or `{"no_solution":true}` exactly when none exists.

Target JSON: `{"attributes":[string,...],"fds":[{"lhs":[string,...],"rhs":[string,...]},...],"R":[string,...]}`. Names are distinct, FD sides and R are subsets of attributes. A target output is `{"X":[string,...],"y":string,"z":string}` with `X ⊆ R`, distinct `y,z ∈ R\\X`, `y ∈ X⁺` and `z ∉ X⁺`, or `{"no_solution":true}` exactly when no witness exists. Closure uses all given FDs, including attributes outside R.

`algorithm.py` reads one source JSON object from stdin and writes one target JSON object to stdout. `algorithm.py --extract` reads `{"source":...,"target_solution":...}` and writes a source output. Errors exit nonzero; diagnostics go to stderr. Recovery is stateless and deterministic.
