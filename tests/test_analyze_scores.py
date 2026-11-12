"""Unit tests for offline scores audit, with synthetic fixtures only."""
import unittest
from scripts.analyze_scores import DISCIPLINES, analyze


def record(run="test-run", task="lv-cable-sizing", score="0.5"):
    return {
        "run_id": run, "task_id": task, "discipline": DISCIPLINES[task],
        "model_api": "google-cloud/gemini-3.8-flash", "score": score,
        "status": "measured", "cost_usd": "", "runtime_min": "",
        "input_tokens": "", "output_tokens": "", "cached_tokens": "",
    }


class AnalyzeScoresTests(unittest.TestCase):
    def test_official_task_inventory(self):
        self.assertEqual(len(DISCIPLINES), 29)
        for discipline, count in [("Electrical", 9), ("Mechanical", 7),
                                  ("Civil", 9), ("Structural", 4)]:
            self.assertEqual(list(DISCIPLINES.values()).count(discipline), count)

    def test_missing_tasks_count_zero(self):
        out = analyze([record()])
        self.assertAlmostEqual(out["runs"]["test-run"]["dev_score"], 0.5 / 29, places=6)
        self.assertEqual(len(out["runs"]["test-run"]["missing_tasks_counted_as_zero"]), 28)
        self.assertFalse(out["runs"]["test-run"]["is_complete_29"])

    def test_complete(self):
        out = analyze([record(task=t, score="1") for t in DISCIPLINES])
        self.assertEqual(out["runs"]["test-run"]["dev_score"], 1)
        self.assertTrue(out["runs"]["test-run"]["is_complete_29"])

    def test_invalid_score_rejected(self):
        for value in ["1.1", "-0.1", "nan", "inf"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                analyze([record(score=value)])

    def test_duplicate_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            analyze([record(), record()])

    def test_wrong_discipline_rejected(self):
        data = record()
        data["discipline"] = "Civil"
        with self.assertRaisesRegex(ValueError, "discipline"):
            analyze([data])

    def test_no_fake_default(self):
        with self.assertRaisesRegex(ValueError, "No measured"):
            analyze([])

    def test_cost_coverage_not_imputed(self):
        a = record()
        a["cost_usd"] = "0.25"
        b = record(task="mv-conveyance-study")
        out = analyze([a, b])["runs"]["test-run"]
        self.assertEqual(out["recorded_cost_usd"], 0.25)
        self.assertEqual(out["cost_coverage_count"], 1)


if __name__ == "__main__":
    unittest.main()
