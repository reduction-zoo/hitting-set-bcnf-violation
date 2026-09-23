# Fixed question

```json
{
  "source": "Hitting Set",
  "target": "Boyce-Codd normal form violation",
  "category": "Construction open",
  "summary": "This connects set hitting to a concrete schema-normalization question and supplies witnesses that can be checked by attribute closure.",
  "source_definition": "Given an explicit finite universe, a family of subsets and a nonnegative integer k, return at most k universe elements intersecting every member of the family. Return NO-SOLUTION exactly when no such witness exists. Graphs, families and strings are explicit; numerical parameters use binary encodings.",
  "target_definition": "Given attributes A, functional dependencies F and a subset R, return X contained in R and distinct y,z in R minus X such that y belongs to the closure of X under F but z does not. A valid output is a witness satisfying these conditions, or NO-SOLUTION exactly when none exists.",
  "required_result": "Construct deterministic polynomial-time maps F and G. F must produce a legal target instance, and G(x,y) must return a valid source output for every valid target output y, including NO-SOLUTION. A complete rule may reconstruct a published construction or give a new one; it must specify every gadget, numerical parameter and decoding step.",
  "acceptance": "Deliver executable instance construction and output recovery, a general proof covering all legal inputs and target outputs, and worst-case polynomial time and encoding-size bounds. Cite the actual proof used, or identify a newly derived argument. Check small positive and negative instances with independent solvers; finite tests alone do not establish correctness.",
  "importance": "This connects set hitting to a concrete schema-normalization question and supplies witnesses that can be checked by attribute closure.",
  "difficulty": "Difficulty is not yet established by a construction attempt. Auxiliary dependencies must create the intended partial determination inside R without accidentally making X a superkey or placing the required attributes outside R.",
  "openness": "This is a rule-completion task from the imported catalog. The requested contribution is a complete, reproducible construction, proof and implementation; the existing hardness attribution is not presented as an unsolved complexity classification. The references are leads to check, not a verified solution.",
  "literature_checked": "2026-09-18",
  "coverage": "Import inventory review of the cited sources. Primary proofs have not been independently re-audited; availability of a complete reconstruction elsewhere remains unassessed.",
  "references": [
    {
      "title": "Problem-Reductions: Hitting Set \u2192 Boyce-Codd normal form violation",
      "url": "https://github.com/CodingThrust/problem-reductions/issues/462",
      "note": "Upstream task and discussion checked on 2026-09-18. Reported reference: Garey & Johnson, *Computers and Intractability*, Appendix A4.3, p.233"
    }
  ],
  "solutions": [],
  "equation": ""
}
```
