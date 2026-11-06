import unittest
from reasoningai.cli import build_parser

class CLITests(unittest.TestCase):
    def test_search_defaults(self):
        args = build_parser().parse_args(['search', 'reasoning models'])
        self.assertEqual(args.provider, 'openalex')
        self.assertEqual(args.limit, 10)

    def test_empty_command_is_rejected(self):
        with self.assertRaises(SystemExit):
            build_parser().parse_args([])

if __name__ == '__main__': unittest.main()
