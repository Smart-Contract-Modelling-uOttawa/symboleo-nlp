import unittest
from unittest.mock import MagicMock

from app.templates.template_getter import get_template

from app.src.child_getters.domain_timepoint_extractor import DomainTimepointExtractor

class DomainTimepointExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = DomainTimepointExtractor()

    # TODO: Better test
    @unittest.skip('todo')
    def test_grammar_generator(self):
        contract = get_template('sample_t')

        results = self.sut.extract(contract)

        self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()