---
name: feature-matrix
description: Build an evidence-graded feature matrix (strong/adequate/weak/missing/unknown) for our product and each competitor, framed as user needs. Writes matrix.csv in the run folder.
---

# Feature matrix

Input: `brief.yaml`, `competitors.md`. Rubric: `docs/methodology.md` §1–2.

## Steps

1. **Draft the feature list as user needs** (15–40 rows), grouped into categories. Seed it from:
   - `must_have_features` and `questions` in the brief
   - the union of headline features on each competitor's product and docs pages
   - the jobs implied by the surface, e.g. for a dashboard: build, explore, explain, share, alert, govern, perform
   Merge differently named versions of the same capability into one row.
2. **Research each product** (ours included). For each one, read in order: the product page, the docs index, the changelog or release notes for the last 12 months, and the pricing page (for gating).
3. **Grade every cell** with `strong | adequate | weak | missing | unknown`, and give an `evidence_url`. Put gating and caveats in `notes` (`enterprise-only`, `beta`, `paid add-on`).
4. **Sanity check**: if over 30% of cells are `unknown`, tell the user which products are opaque and why, rather than guessing.

## Output: `matrix.csv` (long format, one row per feature × product)

```csv
feature,category,product,grade,evidence_url,notes
See why a metric moved,Insight,Acme,weak,https://docs.acme.com/...,manual drill-down only
See why a metric moved,Insight,Amplitude,strong,https://amplitude.com/docs/...,Root cause analysis
```

Quote any field that contains a comma. Product names must match `competitors.md` and the brief's `our_product.name`.
