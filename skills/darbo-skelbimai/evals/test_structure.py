"""Statinė įgūdžio struktūros ir vertinimo scenarijų patikra (be tinklo)."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTests(unittest.TestCase):
    def test_frontmatter_name_and_description(self):
        doc = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(doc.startswith("---\n"))
        header = doc.split("---", 2)[1]
        self.assertIn("name: darbo-skelbimai", header)
        self.assertIn("description:", header)

    def test_required_resources(self):
        for path in ("agents/openai.yaml", "references/sources.md", "evals/evals.json"):
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file())

    def test_agent_interface(self):
        doc = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertIn("interface:", doc)
        self.assertIn("display_name:", doc)
        self.assertIn("short_description:", doc)

    def test_eval_cases(self):
        data = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
        self.assertEqual(data["skill_name"], "darbo-skelbimai")
        self.assertGreaterEqual(len(data["evals"]), 3)
        for case in data["evals"]:
            self.assertTrue(case["prompt"])
            self.assertTrue(case["expected_output"])


if __name__ == "__main__":
    unittest.main()
