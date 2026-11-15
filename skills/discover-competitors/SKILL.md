---
name: discover-competitors
description: Find and select the competitor set for a product or feature surface, from a description, a URL or a user-supplied list. Writes competitors.md in the run folder.
---

# Discover competitors

Input: `brief.yaml` (our product, surface, ICP, known competitors).

## Steps

1. **Start with what the user gave you.** Always include `known_competitors` from the brief.
2. **Search for more**, using several angles (5–8 searches):
   - "<category> software", "<our product> alternatives", "<known competitor> alternatives/competitors"
   - review-site category pages (G2, Capterra), "best <surface> tools <year>"
   - open-source alternatives (GitHub topics, "open source <category>")
   - adjacent products that solve the same *job* in a different way (a spreadsheet, a BI tool, an in-house build)
3. **Classify** each candidate:
   - `direct`: same buyer, same job
   - `adjacent`: same job, different buyer or packaging
   - `aspirational`: best-in-class at this surface, even outside the category (e.g. Linear for issue UX)
4. **Select** up to `max_competitors` from the brief (default 6): mostly direct, plus 1–2 aspirational. Drop anything dead (no updates in 12+ months, shut down, acquired and sunset).

## Output: `competitors.md`

```markdown
# Competitors: <surface>

| product | type | url | why included | source |
|---|---|---|---|---|
| ... | direct | https://... | ... | https://... |

## Considered but excluded
- <name>: <reason> (<url>)
```

Use the same product names exactly in later CSVs.
