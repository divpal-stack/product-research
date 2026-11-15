"""Run with: python -m unittest discover tests"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import score_gaps  # noqa: E402

FIX = ROOT / "tests" / "fixtures"


class ScoreGapsTest(unittest.TestCase):
    def setUp(self):
        features, products = score_gaps.load_matrix(FIX / "matrix.csv")
        reviews = score_gaps.load_reviews(FIX / "reviews.csv")
        rows = score_gaps.score(features, products, "Us", reviews, {}, 0.4, 0.3, 0.3, 0.6, 0.5)
        self.rows = {r["feature"]: r for r in rows}
        self.order = [r["feature"] for r in rows]

    def test_labels(self):
        self.assertEqual(self.rows["Scheduled digests"]["label"], "Table stakes – missing")
        self.assertEqual(self.rows["Explain metric changes"]["label"], "Open field")
        self.assertEqual(self.rows["Custom SQL"]["label"], "We lead")

    def test_unknown_is_flagged_not_scored(self):
        self.assertEqual(self.rows["Custom SQL"]["unknown_for"], "CompB")
        self.assertEqual(self.rows["Custom SQL"]["coverage"], 0.5)

    def test_missing_table_stakes_ranks_first(self):
        self.assertEqual(self.order[0], "Scheduled digests")


if __name__ == "__main__":
    unittest.main()
