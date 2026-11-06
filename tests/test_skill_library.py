from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillLibraryTests(unittest.TestCase):
    def test_all_skills_are_english_and_have_valid_frontmatter(self):
        skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 64)
        self.assertFalse(list((ROOT / "skills").rglob("*.zh-CN.md")))
        for path in skills:
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), path)
            self.assertIn(f"name: {path.parent.name}\n", text, path)
            self.assertIn("description:", text, path)
            self.assertIn("## ", text, path)
            self.assertGreaterEqual(len(text), 1000, path)

    def test_prompt_pack_is_english_only(self):
        prompts = list((ROOT / "prompts/en").glob("*"))
        self.assertEqual(len(prompts), 12)
        self.assertFalse((ROOT / "prompts/zh-CN").exists())

    def test_no_chinese_translation_artifacts_remain(self):
        banned = [p for p in ROOT.rglob("*") if p.is_file() and ("zh-CN" in p.name or p.name.endswith(".zh-CN.md"))]
        self.assertEqual(banned, [])


if __name__ == "__main__":
    unittest.main()
