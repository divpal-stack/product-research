# product-research

This repo runs competitive product-design research. For any request like "research competitors for X" or "what features should we add to Y", use the `product-research` skill in `skills/` (run `./scripts/setup.sh` once so Claude Code finds it).

- Rubric and scoring: `docs/methodology.md`. Follow it exactly.
- Each run goes in `research/<slug>/`. Never write research outputs anywhere else.
- Rank only with `scripts/score_gaps.py`. Never rank by hand.
- Every grade and claim needs a source URL. Use `unknown` rather than a guess.
- Run `python -m unittest discover tests` after changing the scripts.
