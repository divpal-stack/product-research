#!/usr/bin/env python3
"""Score feature gaps from an evidence-graded matrix.

Standard library only. See docs/methodology.md for the formula.

Usage:
  python scripts/score_gaps.py research/run/matrix.csv --us Acme \
      [--reviews research/run/reviews.csv] [--effort research/run/effort.csv] \
      [--out research/run/gaps.csv] [--markdown research/run/gaps.md]
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

GRADES = {"strong": 3, "adequate": 2, "weak": 1, "missing": 0}
EFFORT = {"s": 1, "m": 2, "l": 3, "1": 1, "2": 2, "3": 3}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return [{k.strip(): (v or "").strip() for k, v in row.items() if k} for row in csv.DictReader(f)]


def load_matrix(path: Path):
    """Return {feature: {"category": str, "grades": {product: int|None}}} and the ordered product list."""
    features: dict[str, dict] = {}
    products: list[str] = []
    for row in read_csv(path):
        feat, prod = row.get("feature", ""), row.get("product", "")
        if not feat or not prod:
            continue
        grade_txt = row.get("grade", "").lower()
        if grade_txt and grade_txt != "unknown" and grade_txt not in GRADES:
            sys.exit(f"Unknown grade '{grade_txt}' for {feat} / {prod}. Use strong|adequate|weak|missing|unknown.")
        entry = features.setdefault(feat, {"category": row.get("category", ""), "grades": {}})
        entry["grades"][prod] = GRADES.get(grade_txt)  # None == unknown
        if prod not in products:
            products.append(prod)
    return features, products


def load_reviews(path: Path | None) -> dict[str, tuple[float, float]]:
    if not path or not path.exists():
        return {}
    out = {}
    for row in read_csv(path):
        try:
            out[row["feature"]] = (float(row.get("mentions") or 0), float(row.get("sentiment") or 0))
        except (KeyError, ValueError):
            continue
    return out


def load_effort(path: Path | None) -> dict[str, int]:
    if not path or not path.exists():
        return {}
    return {r["feature"]: EFFORT.get(r.get("effort", "").lower(), 2) for r in read_csv(path) if r.get("feature")}


def score(features, products, us, reviews, efforts, w_gap, w_cov, w_dem, table_stakes_cov, open_field_demand):
    if us not in products:
        sys.exit(f"--us '{us}' not found in matrix products: {', '.join(products)}")
    competitors = [p for p in products if p != us]
    if not competitors:
        sys.exit("Matrix has no competitor rows.")

    max_mentions = max((m for m, _ in reviews.values()), default=0)
    rows = []
    for feat, info in features.items():
        g = info["grades"]
        ours_raw = g.get(us)
        ours = ours_raw if ours_raw is not None else 0
        comp_grades = [g.get(c) for c in competitors]
        known = [x for x in comp_grades if x is not None]
        best = max(known) if known else 0
        best_names = [c for c in competitors if g.get(c) == best and known] if best > 0 else []
        coverage = sum(1 for x in known if x >= 2) / len(competitors)
        gap = max(0, best - ours) / 3

        mentions, sentiment = reviews.get(feat, (0.0, 0.0))
        demand = (mentions / max_mentions) if max_mentions else 0.0
        demand = min(1.0, demand + 0.25 * max(0.0, -sentiment)) if mentions else 0.0

        effort = efforts.get(feat, 2)
        priority = (w_gap * gap + w_cov * coverage + w_dem * demand) / effort

        if coverage >= table_stakes_cov and ours < 2:
            label = "Table stakes – missing"
        elif ours > best:
            label = "We lead"
        elif best - ours >= 1:
            label = "Behind"
        elif best <= 1 and demand >= open_field_demand:
            label = "Open field"
        else:
            label = "Parity"

        unknowns = [p for p in products if g.get(p) is None]
        rows.append({
            "feature": feat,
            "category": info["category"],
            "label": label,
            "priority": round(priority, 3),
            "ours": ours_raw if ours_raw is not None else "unknown",
            "best": best,
            "best_competitors": "; ".join(best_names),
            "coverage": round(coverage, 2),
            "gap": round(gap, 2),
            "demand": round(demand, 2),
            "effort": effort,
            "unknown_for": "; ".join(unknowns),
        })
    rows.sort(key=lambda r: r["priority"], reverse=True)
    return rows


def to_markdown(rows, top: int) -> str:
    lines = ["| # | feature | label | priority | us | best | best at it | coverage | demand |",
             "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows[:top], 1):
        lines.append(f"| {i} | {r['feature']} | {r['label']} | {r['priority']} | {r['ours']} | {r['best']} | "
                     f"{r['best_competitors'] or '–'} | {r['coverage']} | {r['demand']} |")
    by_label = defaultdict(int)
    for r in rows:
        by_label[r["label"]] += 1
    summary = ", ".join(f"{k}: {v}" for k, v in sorted(by_label.items()))
    return f"**{len(rows)} features**. {summary}\n\n" + "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("matrix", type=Path)
    ap.add_argument("--us", required=True, help="our product name, as written in matrix.csv")
    ap.add_argument("--reviews", type=Path)
    ap.add_argument("--effort", type=Path)
    ap.add_argument("--out", type=Path, help="write gaps.csv here (default: stdout markdown only)")
    ap.add_argument("--markdown", type=Path, help="also write a markdown summary here")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--w-gap", type=float, default=0.40)
    ap.add_argument("--w-coverage", type=float, default=0.30)
    ap.add_argument("--w-demand", type=float, default=0.30)
    ap.add_argument("--table-stakes-coverage", type=float, default=0.6)
    ap.add_argument("--open-field-demand", type=float, default=0.5)
    a = ap.parse_args(argv)

    features, products = load_matrix(a.matrix)
    if not features:
        sys.exit(f"No rows in {a.matrix}")
    rows = score(features, products, a.us, load_reviews(a.reviews), load_effort(a.effort),
                 a.w_gap, a.w_coverage, a.w_demand, a.table_stakes_coverage, a.open_field_demand)

    if a.out:
        with a.out.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    md = to_markdown(rows, a.top)
    if a.markdown:
        a.markdown.write_text(md, encoding="utf-8")
    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
