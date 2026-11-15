---
name: gap-prioritization
description: Score feature gaps with scripts/score_gaps.py and write the final report.md (where we win, where we lose, open field, prioritized roadmap). Use after a matrix exists.
---

# Gap prioritization and report

Input: `matrix.csv`, `reviews.csv` (optional), `effort.csv` (optional), `brief.yaml`.

## Steps

1. **Effort (optional).** If the user or the brief gives sizing, write `effort.csv` (`feature,effort` with S/M/L or 1/2/3). Otherwise everything defaults to M. Say so in the report.
2. **Score.** Run:
   ```bash
   python scripts/score_gaps.py <run>/matrix.csv --us "<our name>" \
     --reviews <run>/reviews.csv [--effort <run>/effort.csv] \
     --out <run>/gaps.csv --markdown <run>/gaps.md
   ```
   Don't hand-edit `gaps.csv`. If the weights seem wrong for this product, rerun with flags and record the flags in the report.
3. **Write `report.md`** from `templates/report.md`:
   - **TL;DR:** 3–5 bullets.
   - **Where we win** (`We lead`), **where we lose** (`Table stakes – missing`, `Behind`), **open field**.
   - **Roadmap:** the top 5–10 by priority. Each item gets the user need, the label, the competitors that do it best (with links), the demand evidence, and a one-line build suggestion.
   - **Blind spots:** unknown cells, gated features, and biased sources.
   - **Method:** sources read, date range, scoring flags.
4. Link claims to sources inline. Keep it under ~4 pages.
