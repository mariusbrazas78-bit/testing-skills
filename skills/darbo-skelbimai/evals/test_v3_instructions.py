"""Statiniai v3 darbo-skelbimai instrukcijų regressijos testai."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class V3InstructionsTests(unittest.TestCase):
    def test_official_career_reference(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/employer-check.md", skill)
        self.assertIn("v3", skill)
    def test_official_check_document(self):
        doc = (ROOT / "references/employer-check.md").read_text(encoding="utf-8")
        for phrase in ("konkretaus darbo", "miestą", "patikros datą", "nepateik paraiškos"):
            self.assertIn(phrase.lower(), doc.lower())
    def test_eval_cases(self):
        data = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
        self.assertEqual(data["skill_name"], "darbo-skelbimai")
        self.assertGreaterEqual(len(data["evals"]), 5)
        self.assertEqual(len({e["id"] for e in data["evals"]}),len(data["evals"]))
