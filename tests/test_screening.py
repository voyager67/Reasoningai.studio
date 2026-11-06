import tempfile
import unittest
from pathlib import Path
from reasoningai.screening import initialise_screening, summarise_screening

class ScreeningTests(unittest.TestCase):
    def test_initialise_and_summarise(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d)/'in.csv'; target = Path(d)/'out.csv'
            source.write_text('title,doi\nPaper A,10.1/a\nPaper B,\n', encoding='utf-8')
            self.assertEqual(initialise_screening(source, target), 2)
            target.write_text('record_id,title,title_abstract_decision,title_abstract_reason,full_text_available,full_text_decision,full_text_exclusion_reason\n1,A,include,,yes,include,\n2,B,exclude,wrong population,,,\n', encoding='utf-8')
            result = summarise_screening(target)
            self.assertEqual(result['records_imported'], 2)
            self.assertEqual(result['title_abstract_excluded'], 1)
            self.assertEqual(result['studies_marked_included'], 1)

if __name__ == '__main__': unittest.main()
