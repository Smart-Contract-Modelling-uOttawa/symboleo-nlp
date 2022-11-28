import unittest
from unittest.mock import MagicMock
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_nlp import TestNLP

from app.src.rules.domain_model.amount.amount_extractor_builder import AmountExtractorBuilder
from app.templates.meat_sale.test_suites.amount_extraction import test_suite
from app.templates.meat_sale.symboleo.contract_template import get_template

class AmountExtractorTests(unittest.TestCase):
    def setUp(self):
        self.key = 'TEST'
        self.nlp = TestNLP.get_nlp()
        self.sut = AmountExtractorBuilder.build(self.nlp)

    def test_suite(self):
        for x in test_suite:
            contract = get_template()
            doc = self.nlp(x.input_value)
            req = ContractUpdateRequest(contract, self.key, x.input_value, doc)
            result = self.sut.extract(req)
            self.assertTrue(result in x.expected_property, f'{result} not in {x.expected_property}')
         

if __name__ == '__main__':
    unittest.main()