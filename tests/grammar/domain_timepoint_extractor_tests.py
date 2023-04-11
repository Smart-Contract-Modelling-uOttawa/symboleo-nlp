import unittest
from unittest.mock import MagicMock

from app.src.helpers.template_getter import get_template

from app.src.grammar.domain_timepoint_extractor import DomainTimepointExtractor

class DomainTimepointExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = DomainTimepointExtractor()

    def test_grammar_generator(self):
        contract = get_template('sample_t')
        results = self.sut.extract(contract)

        print(results)
        self.assertEqual(len(results),2)


if __name__ == '__main__':
    unittest.main()