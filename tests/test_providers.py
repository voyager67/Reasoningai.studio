import unittest
from unittest.mock import patch
from reasoningai.providers.openalex import normalize, search

class ProviderTests(unittest.TestCase):
    def test_openalex_normalize(self):
        row = normalize({
            'id':'https://openalex.org/W1','doi':'https://doi.org/10.1/x','title':'Title',
            'publication_year':2024,'type':'article','cited_by_count':3,
            'authorships':[{'author':{'display_name':'A Author'}}],
            'primary_location':{'landing_page_url':'https://example.org','source':{'display_name':'Journal'}},
            'open_access':{'is_oa':True},'abstract_inverted_index':{'clear':[0],'evidence':[1]}
        })
        self.assertEqual(row['authors'], 'A Author')
        self.assertEqual(row['abstract'], 'clear evidence')
        self.assertTrue(row['is_open_access'])

    @patch('reasoningai.providers.openalex.request_json')
    def test_search_calls_provider_and_normalizes(self, mock_request):
        mock_request.return_value = {'results':[{'title':'A'}]}
        rows = search('test', 1)
        self.assertEqual(rows[0]['title'], 'A')
        self.assertIn('search=test', mock_request.call_args.args[0])

if __name__ == '__main__': unittest.main()
