import unittest
from unittest.mock import MagicMock

from app.src.rules.shared.predicate_extractor import IExtractPredicates
from app.src.norm_proposition_updater import IUpdateNormPropositions
from app.src.rules.shared.predicate_processor import PredicateProcessor

from app.src.rules.shared.configs import PredicateProcessorConfig
from app.classes.symboleo_contract import Obligation
from app.classes.spec.sym_event import VariableDotExpression, VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.symboleo_contract import SymboleoContract
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract


class PredicateProcessorTests(unittest.TestCase):
    def setUp(self):
        self.predicate_extractor = IExtractPredicates()
        fake_predicate = PredicateFunctionHappens(VariableEvent(VariableDotExpression('test')))
        self.predicate_extractor.extract = MagicMock(return_value=fake_predicate)
        
        self.norm_updater = IUpdateNormPropositions()
        fake_norm = Obligation('new_obligation', None, None, None, None, None)
        self.norm_updater.update = MagicMock(return_value=fake_norm)
        
        config = PredicateProcessorConfig('obligations', 'test_obligation', 'consequent')
        
        self.sut = PredicateProcessor(config, self.predicate_extractor, self.norm_updater)


    def test_contract_updater(self):
        test_contract = get_test_contract()
        init_sym = test_contract.to_sym()

        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        result = self.sut.process(req)

        self.assertEqual(result.contract_spec.obligations['test_obligation'].id, 'new_obligation')

        self.assertEqual(type(result), SymboleoContract)
        self.assertEqual(self.predicate_extractor.extract.call_count, 1)
        self.assertEqual(self.norm_updater.update.call_count, 1)

        # Ensure init_contract has not changed
        self.assertEqual(test_contract.to_sym(), init_sym)
        

  
if __name__ == '__main__':
    unittest.main()