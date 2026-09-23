# Threshold-gated reduction: construction and proof

Let a source instance be an explicit universe `U={0,...,n-1}`, a family `E_0,...,E_{m-1} ⊆ U`, and a binary nonnegative integer `k`. Repeated sets and arbitrary explicit element names can be canonicalized by a polynomial relabeling without changing solutions; the executable contract uses the canonical names. We give deterministic maps `F` and `G` satisfying the repository's recovery contract. The argument below is newly derived here; the known Beeri–Bernstein hardness attribution is background, not a premise.

## Forward map

For each `i ∈ U`, create attribute `a_i`; for each family set `E_j`, create auxiliary attribute `b_j`. Create markers `C,D`. Let `R={a_i:i∈U}∪{C,D}`; the `b_j` and all threshold attributes are outside `R`. Add `a_i → b_j` for every incidence `i∈E_j`, then `{b_0,...,b_{m-1}} → C`. The latter has empty left side when the family is empty.

When `k<n`, put `q=k+1` and create `t_{i,j}` for `1≤i≤n` and `1≤j≤min(i,q)`. Add `a_{i-1} → t_{i,1}` for every `i`; add `t_{i-1,j} → t_{i,j}` whenever `1≤j≤min(i-1,q)`; add `{t_{i-1,j-1},a_{i-1}} → t_{i,j}` for `2≤j≤min(i,q)`. Add `{C,t_{n,q}} → D`. When `k≥n`, omit all threshold attributes and this last dependency. Always add `{C,D} → {a_i:i∈U}`. This also specifies the `n=0` and empty-family cases without exceptions.

## Closure lemmas

For any `X⊆R`, let `H={i:a_i∈X}`. Before the rule `{C,D} → {a_i}` fires, the threshold attributes are derived solely from the initially present element attributes. Induction on `i` shows `t_{i,j}` is derived in that phase iff at least `j` among `a_0,...,a_{i-1}` lie in `X`. Base `j=1` follows from each direct element rule and carry rules. For `j>1`, either the first `i-1` positions already meet `j`, or they meet `j-1` and the last element is selected. Thus, before both markers are present, `t_{n,q}` is derivable iff `|H|>k`. Later derivations after `{C,D}` fires do not affect whether the closure inside `R` is partial.

Until both `C,D` have been derived, no element attribute outside `X` can be derived. In this phase `b_j` is derived iff `H∩E_j≠∅`, since its only incoming rules are incidences. Consequently `C` is derived iff `C∈X` or `H` hits every family set. If `C∉X`, the only way to derive `D` beyond initial membership is `C` together with the threshold. If both markers are derived, the final dependency yields every element attribute, hence all of `R`.

Now classify the closure inside `R`. If `C∈X` or `D∈X`, either no new attribute of `R` is derived or all of `R` is derived: the only possible new marker completes `{C,D}`, and only that pair can derive new elements. If neither marker belongs to `X`, a nonhitting `H` gives `X⁺∩R=X`; a hitting `H` with `|H|>k` gives `X⁺∩R=R`; and a hitting `H` with `|H|≤k` gives `X⁺∩R=X∪{C}`, with `D∉X⁺`. The last case remains true for `k≥n`, since then every `H` has size at most `k` and no threshold is built.

## Recovery theorem

If `H` is a hitting set of size at most `k`, choose `X={a_i:i∈H}`. The last closure case provides a valid target output `(X,C,D)`. Conversely, let `(X,y,z)` be *any* valid target output. Its closure inside `R` must be partial: it gains some `y∈R\X` but misses some `z∈R\X`. The classification shows this is possible only when `X` contains neither marker and `H={i:a_i∈X}` hits every family set with `|H|≤k`. `G` returns `H`, independently of `y,z`. If the valid target output is `NO-SOLUTION`, no target violation exists, hence no source hitting set of size at most `k` exists; `G` returns `NO-SOLUTION`. Thus every valid target output recovers a valid source output, including the negative answer. The target always has a valid output by its explicit no-solution convention.

## Complexity and scope

Let `L` be the bit length of the explicit source encoding, including binary `k`. Comparison `k<n` costs polynomial bit time. If `k<n`, then `q≤n`, so there are at most `n²` threshold attributes and `O(n²)` threshold FDs. The incidence rules number at most the explicit incidence count `s≤L`; all other rules have total side length `O(n+m)`. Attribute names have `O(log(n+m))` bits. Forward output size is `O((n²+s+m)log(n+m))⊆O(L² log L)` bits, and construction time is polynomial in `L`. Recovery scans `X` and the source encoding and returns at most `n` original members in polynomial time in `L+|y|`; validation in the implementation also scans the family. Neither map calls an oracle, uses randomness, or retains process state. Exhaustive target solving is only a test oracle and does not affect these bounds.

## Relation to previous work

Beeri and Bernstein, *Computational Problems Related to the Design of Normal Form Relational Schemas*, ACM TODS 4(1), 1979, 30–59, is the historical hardness attribution for BCNF violation via Hitting Set, as catalogued by the [upstream problem model](https://github.com/CodingThrust/problem-reductions/issues/447). The exact construction and witness recovery in that primary paper have not yet been checked; this proof does not claim a new complexity classification or precedence over its construction. A later [survey](https://citeseerx.ist.psu.edu/document?doi=6299eb184fd26dfb159e23fba549443abe8f70ff&repid=rep1&type=pdf) includes a schema-level hitting-set sketch, but its displayed rules do not visibly enforce binary `k`; it does not establish this theorem as written. Primary comparison remains an independent-review obligation.
