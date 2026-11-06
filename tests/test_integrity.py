import csv
import tempfile
import unittest
from pathlib import Path
from reasoningai.integrity import scan_secrets, sha256_manifest, audit_claim_ledger

class IntegrityTests(unittest.TestCase):
    def test_secret_scan_reports_location_not_value(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'secret.txt'; p.write_text('token = ghp_' + 'A'*30, encoding='utf-8')
            findings = scan_secrets([p])
        self.assertTrue(findings)
        self.assertNotIn('A'*30, str(findings))

    def test_secret_scan_recurses_directories(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)/'src'; folder.mkdir()
            p = folder/'nested.py'; p.write_text('key = ghp_' + 'B'*30, encoding='utf-8')
            findings = scan_secrets([folder])
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]['kind'], 'github_token')

    def test_manifest_hash(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'a.txt'; p.write_text('abc', encoding='utf-8')
            rows = sha256_manifest(d)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['bytes'], 3)
        self.assertEqual(len(rows[0]['sha256']), 64)

    def test_claim_ledger_flags_unverified(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'claims.csv'
            p.write_text('claim_id,claim,source_id,locator,evidence_status\nC1,Claim,S1,Table 1,unverified\n', encoding='utf-8')
            result = audit_claim_ledger(p)
        self.assertFalse(result['passed'])
        self.assertIn('claim_requires_review', [x['kind'] for x in result['issues']])

    def test_manifest_does_not_hash_its_own_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.txt").write_text("alpha", encoding="utf-8")
            output = root / "manifest.csv"
            first = sha256_manifest(root, output)
            second = sha256_manifest(root, output)
            self.assertEqual([r["path"] for r in first], ["a.txt"])
            self.assertEqual([r["path"] for r in second], ["a.txt"])

if __name__ == '__main__': unittest.main()
