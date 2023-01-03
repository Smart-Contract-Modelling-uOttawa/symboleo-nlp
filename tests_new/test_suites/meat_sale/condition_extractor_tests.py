import unittest
from unittest.mock import MagicMock
from tests.helpers.test_nlp import TestNLP

from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent, ContractEvent
from app.classes.spec.sym_point import PointAtomContractEvent

from app.templates.meat_sale.symboleo.contract_template import get_template
from app.templates.meat_sale.test_suites.condition_extraction import test_suite

from app.src.rules.contract_spec.condition.condition_patterns import get_condition_patterns
from app.src.rules.contract_spec.predicate_extractor_builder import PredicateExtractorBuilder


class DeliveryTimeframeTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        template = None
        #template = PredicateFunctionHappens(VariableEvent('test')) 
        case_patterns = get_condition_patterns(self.nlp)
        self.sut = PredicateExtractorBuilder.build(self.nlp, template, case_patterns)

    def test_suite(self):
        for x in test_suite:
            contract = get_template()
            doc = self.nlp(x.input_value)
            req = ContractUpdateRequest(contract, x.key, x.input_value, doc)
            results = self.sut.extract(req)

            for res in results:
                print('--', res.obj.to_sym(), res.score)

            first_result = results[0].obj
            self.assertTrue(first_result.to_sym() in x.expected_sym, f'{first_result.to_sym()} not in expected result set')
         

if __name__ == '__main__':
    unittest.main()