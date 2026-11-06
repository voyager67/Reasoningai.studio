import tempfile
import unittest
from pathlib import Path
from reasoningai.bibtex import parse_entries, audit_file

class BibTeXTests(unittest.TestCase):
    def test_parse_two_entries(self):
        text = '''@article{a, title={A {nested} title}, doi={10.1/a}}
@inproceedings{b, title={B}}'''
        rows = parse_entries(text)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]['key'], 'a')
        self.assertEqual(rows[0]['doi'], '10.1/a')

    def test_duplicate_doi_detected(self):
        text = '''@article{a, doi={10.1/a}}
@article{b, doi={10.1/a}}'''
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'r.bib'
            p.write_text(text, encoding='utf-8')
            result = audit_file(p)
        self.assertFalse(result['passed'])
        self.assertIn('duplicate_doi', [x['kind'] for x in result['issues']])

if __name__ == '__main__': unittest.main()
