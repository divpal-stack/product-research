# Contributing

Thanks for helping. Useful contributions:

- **Rubrics** for specific surfaces (dashboards, onboarding, billing, settings) in `docs/rubrics/`.
- **Source adapters**: new review or changelog sources added to the `review-mining` and `feature-matrix` skills.
- **Example runs** in `research/examples/`, using public sources only, with every cell linked.
- **Scoring changes**: open an issue first. Changing the weights changes every ranking.

Before opening a PR:

```bash
python -m unittest discover tests
```

Keep skills short and imperative. Put the reasoning in `docs/methodology.md`, not in the prompts.
