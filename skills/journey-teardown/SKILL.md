---
name: journey-teardown
description: Compare how competing products handle one specific user journey on one surface (e.g. desktop onboarding, first PR, inviting a teammate), grade each stage from evidence, name the best in class per stage, and write concrete fixes per product. Use when asked "which product does X better" or "how should we improve X".
---

# Journey teardown

A feature matrix says *whether* a product can do something. A journey teardown says *how well it gets a real user through it*, stage by stage, and what each product should copy from the best one. Rubric: `docs/methodology.md` §6.

## 0. Pin down the journey

Write one line: **who, on what surface, from what start to what finished state.**
Example: "New individual developer, on a laptop, from nothing to a first reviewed agent change."
If the user said only "onboarding", propose this line and confirm it in one question.

## 1. Define 4–7 stages

Name stages by the user's goal, not the product's screens, so different flows compare fairly. A default for onboarding:

1. Install it
2. Get in (account, plan, paywall)
3. Point it at your stuff (connect data, repo or workspace)
4. Know what to do first (guidance, templates, suggested first action)
5. Get a result you can keep (review, save, share)

## 2. Collect evidence per product, best source first

1. **Logged-in or hands-on observation** (`evidence_type: logged-in`). The user signs in themselves. Never type passwords or create accounts for them. Record what you saw, with the date and a screenshot path. If the browser blocks popups or sign-in, ask the user for screenshots instead.
2. **Official quickstart and getting-started docs** (`evidence_type: public`). Fetch them and extract the steps in order: prerequisites, walls (payment, waitlist, required installs), defaults, the first suggested action, and how the result is reviewed or kept.
3. **Reviews and tutorials** for friction the docs don't show (approval fatigue, confusing steps).

## 3. Grade each stage (strong / adequate / weak / missing / unknown)

Use the journey rubric in `docs/methodology.md` §6. Every cell needs an `evidence_url` (or screenshot path) and a note that says *what specifically* earned the grade. "Good onboarding" isn't a note; "pre-lists repos from recent GitHub activity" is.

## 4. Output: `journey.csv`

Same long format as `matrix.csv`, plus `evidence_type`:

```csv
feature,category,product,grade,evidence_type,evidence_url,notes
2. Get in without paying,Access,Acme,weak,logged-in,screenshots/acme-checkout.png,"Sign-in landed on a paid checkout"
```

## 5. Score, render and write

```bash
python scripts/score_gaps.py <run>/journey.csv --us "<product>"     # repeat per product
python scripts/render_matrix.py <run>/journey.csv --title "<journey> (<date>)"
```

`report.md` must have:
- **Verdict:** who handles the journey best, and the 2–3 specific things they do.
- **Best in class per stage:** a table of who and *what they do that others don't*.
- **What each product should change:** 2–4 numbered fixes per product, ordered by score. Each fix names the observed problem, the concrete change, and the product that already does it well. No generic advice ("improve UX").
- **Patterns worth copying:** 3–4 lessons that apply across products.
- **Blind spots:** unverified stages, how much is docs versus observed, anything not timed or tested.
