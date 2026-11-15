# Methodology

## 1. Frame features as user needs

Before grading anything, write the feature list as **jobs** the user is trying to do, grouped by category:

| category | feature (the job) | example implementations |
|---|---|---|
| Insight | See *why* a metric moved | root-cause panel, anomaly explanations, drill-down |
| Sharing | Get a dashboard in front of execs weekly | scheduled email/Slack digests, public links |
| Setup | Get first useful chart in under 10 minutes | templates, auto-generated starter dashboard |

This stops a product from losing points because it names something differently, and it keeps the matrix to roughly 15–40 rows.

## 2. Grade every cell from evidence

| grade | value | meaning | evidence needed |
|---|:-:|---|---|
| `strong` | 3 | Does the job well; a headline capability | Docs or demo showing depth; positive review mentions |
| `adequate` | 2 | Does the job with limits | Docs page or changelog entry |
| `weak` | 1 | Workaround, beta, or clearly painful | Docs plus complaints, or "beta" or "coming soon" labels |
| `missing` | 0 | Can't do the job | Absence in docs plus an explicit statement, a review or a forum request |
| `unknown` | – | Couldn't verify (paywalled, enterprise-only, no docs) | Note *why* it's unknown |

Rules:
- One `evidence_url` per cell minimum. No URL means `unknown`.
- Grade **our own product the same way**, from our public docs, so the comparison is fair. Internal knowledge can go in `notes`.
- Flag gating in `notes`: `enterprise-only`, `paid add-on`, `region-locked`.

## 3. Mine demand from reviews

For each feature, count mentions in public reviews and discussions (G2, Capterra, Reddit, Hacker News, app stores, GitHub issues, community forums) over the last ~18 months:

`reviews.csv`: `feature, mentions, sentiment, sample_url`

- `sentiment` runs from -1 (complaints or requests: "I wish it could…") to +1 (praise).
- Complaints about competitors are as valuable as complaints about us. They mark the places where nobody is good yet.

## 4. Score gaps (deterministic)

`scripts/score_gaps.py` computes, per feature:

| term | definition |
|---|---|
| `ours` | our grade (unknown → 0, flagged) |
| `best` | best competitor grade |
| `coverage` | share of competitors at `adequate` or better |
| `gap` | `max(0, best − ours) / 3` |
| `demand` | review mentions, min-max normalized to 0–1; plus 0.25 × max(0, −sentiment) so pain counts extra, capped at 1 |
| `effort` | 1 (S), 2 (M) or 3 (L); defaults to 2 unless set in `effort.csv` |

```
priority = (0.40·gap + 0.30·coverage + 0.30·demand) / effort
```

Each feature is labeled (first matching rule wins):

| label | rule | what to do |
|---|---|---|
| **Unverified** | our own grade is `unknown` | Verify before acting. Never report it as missing. |
| **Table stakes – missing** | coverage ≥ 0.6 and ours < adequate | Close it. Buyers expect it. |
| **Behind** | best − ours ≥ 1 | Improve if demand is high. |
| **Open field** | best ≤ weak and demand ≥ 0.5 | Differentiate. Nobody does this well. |
| **We lead** | ours > best | Protect and market it. |
| **Parity** | otherwise | Leave it. |

All weights and thresholds are CLI flags. Change them openly in the report rather than silently.

## 5. Write the report

Use `templates/report.md`. Every claim links to a row in `matrix.csv` or `reviews.csv`. The roadmap section lists the top items by priority, each with the user need, evidence, label and a one-line build suggestion.

## 6. Journey teardowns (stage-by-stage)

A journey teardown grades how well each product gets a user through **one specific job on one surface** (for example, desktop onboarding from nothing to a first reviewed change). Rows are stages instead of features. It uses the same CSV format, scorer and grades, plus an `evidence_type` column (`logged-in`, `public` or `measured`).

| grade | for a journey stage |
|---|---|
| `strong` | The user gets through the stage without a decision they aren't equipped to make, and the product does part of the work for them (pre-filled choices, a suggested next action, one-click completion) |
| `adequate` | Clear and documented, but the user does the work (pick a folder, write the first prompt, find the diff) |
| `weak` | A wall or detour: a paywall or checkout before any value, a prerequisite to install, a confusing choice, or a known dead end |
| `missing` | The stage isn't supported (no way to keep or share the result, say) |
| `unknown` | Not covered by any source read |

Rules:
- **Logged-in observations beat docs**, but record the date, the account type and anything about your setup that could distort them (for example, an embedded browser that blocks popups).
- **Name the mechanism, not the feeling.** Every note says *what* earned the grade.
- **Each fix copies a best-in-class example.** Recommendations name the product that already solves that stage.

See `skills/journey-teardown/SKILL.md` and the worked example in `research/examples/desktop-onboarding-2026-11/`.
