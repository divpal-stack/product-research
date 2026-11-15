#!/usr/bin/env python3
"""Render a graded matrix (matrix.csv or journey.csv) as a shareable heatmap PNG.

Every cell is labeled with its grade, so the image doesn't rely on color alone.
The palette is a validated single-hue ordinal ramp; unknown cells are hatched gray.

Usage:
  python scripts/render_matrix.py research/run/matrix.csv --title "AI coding tools (Nov 2026)" \
      [--subtitle "..."] [--products "A,B,C"] [--out research/run/matrix.png]

Requires matplotlib (pip install matplotlib).
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

COLORS = {"missing": "#86b6ef", "weak": "#3987e5", "adequate": "#1c5cab", "strong": "#0d366b"}
TEXT = {"missing": "#0b1f3a", "weak": "#ffffff", "adequate": "#ffffff", "strong": "#ffffff"}
LABEL = {"missing": "Missing", "weak": "Weak", "adequate": "Adequate", "strong": "Strong"}
SURFACE, INK, MUTED, UNK_FILL, UNK_EDGE = "#fcfcfb", "#1a1a19", "#5f5e5a", "#f0efec", "#c9c8c3"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("matrix", type=Path)
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default="Every cell graded from a cited source")
    ap.add_argument("--products", help="comma-separated column order (default: order in the CSV)")
    ap.add_argument("--out", type=Path, help="output PNG (default: next to the CSV)")
    a = ap.parse_args()

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch

    rows = list(csv.DictReader(a.matrix.open(encoding="utf-8")))
    feats, prods = [], []
    for r in rows:
        if r["feature"] not in feats:
            feats.append(r["feature"])
        if r["product"] not in prods:
            prods.append(r["product"])
    if a.products:
        prods = [p.strip() for p in a.products.split(",")]
    grade = {(r["feature"], r["product"]): (r.get("grade") or "unknown").lower() for r in rows}

    cw, ch, gap = 1.0, 0.42, 0.04
    left = max(3.0, 0.075 * max(len(f) for f in feats) + 0.4)
    top = 1.55
    W = left + len(prods) * cw + 0.3
    H = top + len(feats) * ch + 0.6
    fig = plt.figure(figsize=(W * 1.25, H * 1.25), dpi=110)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    fig.patch.set_facecolor(SURFACE)

    ax.text(0.2, 0.42, a.title, fontsize=15, weight="bold", color=INK, va="center")
    ax.text(0.2, 0.8, a.subtitle, fontsize=8.5, color=MUTED, va="center")
    for j, p in enumerate(prods):
        ax.text(left + j * cw + cw / 2, top - 0.18, p, ha="center", va="bottom", fontsize=8.5, weight="bold", color=INK)

    def cell(x, y, w, h, g):
        if g in COLORS:
            ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.05", fc=COLORS[g], ec="none"))
        else:
            ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.05",
                                        fc=UNK_FILL, ec=UNK_EDGE, lw=0.6, hatch="////"))

    for i, f in enumerate(feats):
        y = top + i * ch
        ax.text(left - 0.12, y + ch / 2, f, ha="right", va="center", fontsize=8, color=INK)
        for j, p in enumerate(prods):
            g = grade.get((f, p), "unknown")
            x = left + j * cw
            cell(x + gap, y + gap, cw - 2 * gap, ch - 2 * gap, g)
            ax.text(x + cw / 2, y + ch / 2, LABEL.get(g, "Unverified"), ha="center", va="center",
                    fontsize=7.2, color=TEXT.get(g, MUTED))

    yb = top + len(feats) * ch + 0.3
    xs = left
    for k in ["strong", "adequate", "weak", "missing", "unknown"]:
        cell(xs, yb - 0.11, 0.22, 0.22, k)
        name = LABEL.get(k, "Unverified")
        ax.text(xs + 0.3, yb, name, va="center", fontsize=8, color=INK)
        xs += 1.05 if k != "missing" else 1.1

    out = a.out or a.matrix.with_suffix(".png")
    fig.savefig(out, facecolor=fig.get_facecolor())
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
