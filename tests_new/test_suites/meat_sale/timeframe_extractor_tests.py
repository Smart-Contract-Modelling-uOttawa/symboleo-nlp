import unittest
from unittest.mock import MagicMock
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_nlp import TestNLP
from app.templates.meat_sale.symboleo.contract_template import get_template

from app.src.rules.contract_spec.timeframe.timeframe_extractor_builder import TimeFrameExtractorBuilder
from app.templates.meat_sale.test_suites.timeframe_extraction import test_suite
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent, EventVDE

class DeliveryTimeframeTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        template = PredicateFunctionHappens(VariableEvent(EventVDE('test'))) ##?
        self.sut = TimeFrameExtractorBuilder.build(self.nlp, template)

    def test_suite(self):
        for x in test_suite:
            contract = get_template()
            doc = self.nlp(x.input_value)
            req = ContractUpdateRequest(contract, '', x.input_value, doc)
            result = self.sut.extract(req)
            self.assertTrue(result.to_sym() in x.expected_sym, f'{result.to_sym()} not in expected result set')
         

if __name__ == '__main__':
    unittest.main()