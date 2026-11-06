import sys, tempfile, unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import verify_bibliography as vb
import audit_dataset as ad
import check_reproducibility as cr
import validate_skills as vs

class BibliographyTests(unittest.TestCase):
    def test_parse_nested_bibtex_and_doi(self):
        raw="@article{smith2024, title={A {Nested} Title}, author={Smith, Jane and Doe, John}, year={2024}, doi={10.1234/AbC.1}}"
        entries=vb.parse_bibtex(raw)
        self.assertEqual(len(entries),1)
        self.assertEqual(entries[0]['key'],'smith2024')
        self.assertEqual(vb.extract_doi(entries[0]),'10.1234/AbC.1')
    def test_parenthesized_entry_nested_braces_and_string_directive(self):
        raw='@string{venue = {Journal Name}}\n@comment{ignored {comment}}\n@article(sample, title=\"A, title (with comma)\", note={nested {braces, kept}}, year={2026})'
        entries=vb.parse_bibtex(raw)
        self.assertEqual(len(entries),1)
        self.assertEqual(entries[0]['key'],'sample')
        self.assertEqual(entries[0]['title'],'A, title (with comma)')
        self.assertEqual(entries[0]['note'],'nested {braces, kept}')
    def test_output_cannot_overwrite_bibliography(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'refs.bib'
            path.write_text('@article{x, title={Example}}',encoding='utf-8')
            with self.assertRaises(SystemExit) as exc, redirect_stderr(StringIO()):
                vb.main([str(path),'--output',str(path),'--offline'])
            self.assertEqual(exc.exception.code,2)
            self.assertIn('@article',path.read_text(encoding='utf-8'))
    def test_offline_does_not_lookup(self):
        entries=[{'type':'article','key':'a','doi':'10.1234/x','title':'Paper'}]
        with patch.object(vb,'crossref_lookup',side_effect=AssertionError('network used')):
            report=vb.audit_entries(entries,offline=True)
        self.assertEqual(report[0]['status'],'not_checked_offline')

class DatasetAuditTests(unittest.TestCase):
    def test_cross_split_duplicate_is_reported_without_raw_text(self):
        rows=[{'id':'1','text':'same example','label':'a','split':'train'},
              {'id':'2','text':'same example','label':'a','split':'test'}]
        report=ad.audit(rows)
        self.assertEqual(report['record_count'],2)
        self.assertEqual(len(report['cross_split_exact_text_groups']),1)
        self.assertNotIn('same example',str(report))
        self.assertNotIn('sha256',str(report).lower())
    def test_missing_columns_and_empty_file(self):
        report=ad.audit([{'id':'1'}])
        self.assertEqual(report['missing_values']['text'],1)

class ReproducibilityTests(unittest.TestCase):
    def test_empty_project_is_heuristic_and_reports_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=cr.check(Path(tmp))
        self.assertEqual(result['assessment'],'heuristic_preflight_not_a_reproduction')
        self.assertTrue(result['missing_checks'])

class SkillValidationTests(unittest.TestCase):
    def test_repository_skills_validate(self):
        count,errors=vs.validate(ROOT)
        self.assertGreaterEqual(count,25)
        self.assertEqual(errors,[])

if __name__=='__main__': unittest.main()
