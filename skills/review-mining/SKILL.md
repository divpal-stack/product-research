---
name: review-mining
description: Mine public reviews and discussions for demand, pain points and feature requests per feature in the matrix. Writes reviews.csv in the run folder.
---

# Review mining

Input: `matrix.csv` (for the feature list) and `competitors.md`.

## Sources (last ~18 months)
G2 and Capterra review pages, Reddit (`site:reddit.com <product> <feature>`), Hacker News, app store reviews, the product's public GitHub issues or community forum, and "switched from X to Y" posts.

## Steps

1. For each feature row, search across products for complaints ("can't", "wish", "missing", "slow", "switched because") and praise.
2. Count distinct mentions you actually read. Don't extrapolate from search-result counts.
3. Score `sentiment` from -1 (mostly complaints or requests) to +1 (mostly praise).
4. Keep a short list of **unmet needs** that no feature row covers. Add them to `matrix.csv` as new rows (graded for every product) if there are 3 or more mentions.

## Output: `reviews.csv`

```csv
feature,mentions,sentiment,sample_url
See why a metric moved,14,-0.6,https://www.reddit.com/r/...
```

Paraphrase what reviewers said. Don't paste long quotes into the report.
