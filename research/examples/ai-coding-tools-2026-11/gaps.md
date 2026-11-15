# Gap rankings per tool

Generated with `scripts/score_gaps.py` (default weights), once per tool as the focal product. Regenerate any of them with:

```bash
python scripts/score_gaps.py research/examples/ai-coding-tools-2026-11/matrix.csv --us "Cursor" --reviews research/examples/ai-coding-tools-2026-11/reviews.csv
```

## Cursor

**17 features**. Behind: 7, Parity: 10

| # | feature | label | priority | us | best | best at it | coverage | demand |
|---|---|---|---|---|---|---|---|---|
| 1 | Know what you'll pay and when you'll hit a limit | Behind | 0.333 | 1 | 3 | Cline | 0.33 | 1.0 |
| 2 | Choose any model or bring your own key | Behind | 0.278 | 2 | 3 | GitHub Copilot; Amp; Cline | 0.83 | 0.57 |
| 3 | Check its own work before handing it over | Behind | 0.268 | 2 | 3 | GitHub Copilot | 0.67 | 0.68 |
| 4 | Understand a large codebase | Parity | 0.247 | 3 | 3 | Augment Code; Amp | 0.83 | 0.82 |
| 5 | Get real work done on a free plan | Behind | 0.232 | 2 | 3 | Cline | 0.67 | 0.43 |
| 6 | Work from the terminal or headless in CI | Behind | 0.217 | 2 | 3 | GitHub Copilot; Claude Code; Amp; Cline | 1.0 | 0.0 |

## GitHub Copilot

**17 features**. Behind: 5, Parity: 11, We lead: 1

| # | feature | label | priority | us | best | best at it | coverage | demand |
|---|---|---|---|---|---|---|---|---|
| 1 | Know what you'll pay and when you'll hit a limit | Behind | 0.333 | 1 | 3 | Cline | 0.33 | 1.0 |
| 2 | Understand a large codebase | Behind | 0.314 | 2 | 3 | Cursor; Augment Code; Amp | 0.83 | 0.82 |
| 3 | Get real work done on a free plan | Behind | 0.232 | 2 | 3 | Cline | 0.67 | 0.43 |
| 4 | Choose any model or bring your own key | Parity | 0.211 | 3 | 3 | Amp; Cline | 0.83 | 0.57 |
| 5 | Remember project context across sessions | Behind | 0.21 | 2 | 3 | Augment Code | 0.5 | 0.46 |
| 6 | Check its own work before handing it over | We lead | 0.201 | 3 | 2 | Cursor; Devin Desktop; Claude Code; Augment Code | 0.67 | 0.68 |

## Devin Desktop

**17 features**. Behind: 10, Parity: 4, Unverified: 3

| # | feature | label | priority | us | best | best at it | coverage | demand |
|---|---|---|---|---|---|---|---|---|
| 1 | Remember project context across sessions | Unverified | 0.369 | unknown | 3 | Augment Code | 0.67 | 0.46 |
| 2 | Know what you'll pay and when you'll hit a limit | Behind | 0.333 | 1 | 3 | Cline | 0.33 | 1.0 |
| 3 | Share skills, plugins and rules across a team | Unverified | 0.325 | unknown | 3 | Cursor; GitHub Copilot; Claude Code | 0.83 | 0.0 |
| 4 | Understand a large codebase | Behind | 0.314 | 2 | 3 | Cursor; Augment Code; Amp | 0.83 | 0.82 |
| 5 | Start agents from Slack or the issue tracker | Unverified | 0.3 | unknown | 3 | Cursor; GitHub Copilot | 0.67 | 0.0 |
| 6 | Choose any model or bring your own key | Behind | 0.278 | 2 | 3 | GitHub Copilot; Amp; Cline | 0.83 | 0.57 |

## Claude Code

**17 features**. Behind: 6, Parity: 8, Table stakes – missing: 2, Unverified: 1

| # | feature | label | priority | us | best | best at it | coverage | demand |
|---|---|---|---|---|---|---|---|---|
| 1 | Get real work done on a free plan | Unverified | 0.39 | unknown | 3 | Cline | 0.83 | 0.43 |
| 2 | Choose any model or bring your own key | Table stakes – missing | 0.37 | 1 | 3 | GitHub Copilot; Amp; Cline | 1.0 | 0.57 |
| 3 | Know what you'll pay and when you'll hit a limit | Behind | 0.333 | 1 | 3 | Cline | 0.33 | 1.0 |
| 4 | Fast autocomplete while typing | Table stakes – missing | 0.325 | 0 | 3 | Cursor; GitHub Copilot; Devin Desktop; Augment Code | 0.67 | 0.17 |
| 5 | Understand a large codebase | Behind | 0.314 | 2 | 3 | Cursor; Augment Code; Amp | 0.83 | 0.82 |
| 6 | Check its own work before handing it over | Behind | 0.268 | 2 | 3 | GitHub Copilot | 0.67 | 0.68 |

## Augment Code

**17 features**. Behind: 8, Parity: 6, Table stakes – missing: 1, Unverified: 1, We lead: 1

| # | feature | label | priority | us | best | best at it | coverage | demand |
|---|---|---|---|---|---|---|---|---|
| 1 | Know what you'll pay and when you'll hit a limit | Behind | 0.333 | 1 | 3 | Cline | 0.33 | 1.0 |
| 2 | Run and look at the app it is building | Unverified | 0.325 | unknown | 3 | Cursor; Cline | 0.83 | 0.0 |
| 3 | Get real work done on a free plan | Table stakes – missing | 0.323 | 1 | 3 | Cline | 0.83 | 0.43 |
| 4 | Choose any model or bring your own key | Behind | 0.278 | 2 | 3 | GitHub Copilot; Amp; Cline | 0.83 | 0.57 |
| 5 | Check its own work before handing it over | Behind | 0.268 | 2 | 3 | GitHub Copilot | 0.67 | 0.68 |
| 6 | Run several agents in parallel and manage them in one place | Behind | 0.267 | 2 | 3 | Cursor; GitHub Copilot; Devin Desktop; Claude Code | 1.0 | 0.33 |

## Amp

**17 features**. Behind: 6, Parity: 3, Unverified: 8

| # | feature | label | priority | us | best | best at it | coverage | demand |
|---|---|---|---|---|---|---|---|---|
| 1 | Check its own work before handing it over | Unverified | 0.426 | unknown | 3 | GitHub Copilot | 0.83 | 0.68 |
| 2 | Remember project context across sessions | Unverified | 0.369 | unknown | 3 | Augment Code | 0.67 | 0.46 |
| 3 | Catch bugs in pull requests before merge | Unverified | 0.325 | unknown | 3 | Cursor; GitHub Copilot; Claude Code; Augment Code | 0.83 | 0.0 |
| 4 | Fast autocomplete while typing | Unverified | 0.325 | unknown | 3 | Cursor; GitHub Copilot; Devin Desktop; Augment Code | 0.67 | 0.17 |
| 5 | Share skills, plugins and rules across a team | Unverified | 0.325 | unknown | 3 | Cursor; GitHub Copilot; Claude Code | 0.83 | 0.0 |
| 6 | Use it inside JetBrains IDEs | Unverified | 0.325 | unknown | 3 | GitHub Copilot; Claude Code; Augment Code | 0.83 | 0.0 |

## Cline

**17 features**. Behind: 2, Parity: 5, Table stakes – missing: 4, Unverified: 4, We lead: 2

| # | feature | label | priority | us | best | best at it | coverage | demand |
|---|---|---|---|---|---|---|---|---|
| 1 | Understand a large codebase | Unverified | 0.472 | unknown | 3 | Cursor; Augment Code; Amp | 1.0 | 0.82 |
| 2 | Check its own work before handing it over | Table stakes – missing | 0.36 | 1 | 3 | GitHub Copilot | 0.83 | 0.68 |
| 3 | Catch bugs in pull requests before merge | Unverified | 0.325 | unknown | 3 | Cursor; GitHub Copilot; Claude Code; Augment Code | 0.83 | 0.0 |
| 4 | Fast autocomplete while typing | Unverified | 0.325 | unknown | 3 | Cursor; GitHub Copilot; Devin Desktop; Augment Code | 0.67 | 0.17 |
| 5 | Remember project context across sessions | Table stakes – missing | 0.302 | 1 | 3 | Augment Code | 0.67 | 0.46 |
| 6 | Start agents from Slack or the issue tracker | Unverified | 0.3 | unknown | 3 | Cursor; GitHub Copilot | 0.67 | 0.0 |
