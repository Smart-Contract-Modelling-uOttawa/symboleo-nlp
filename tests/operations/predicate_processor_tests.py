import unittest
from unittest.mock import MagicMock

from app.src.operations.helpers.norm_proposition_updater import IUpdateNormPropositions
from app.src.operations.helpers.predicate_processor import PredicateProcessor

from app.src.operations.configs import ParameterConfig
from app.classes.symboleo_contract import Obligation
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.symboleo_contract import SymboleoContract
from tests.helpers.test_contract import get_test_contract


class PredicateProcessorTests(unittest.TestCase):
    def setUp(self):
        self.norm_updater = IUpdateNormPropositions()
        fake_norm = Obligation('new_obligation', None, None, None, None, None)
        self.norm_updater.update = MagicMock(return_value=fake_norm)
        
        self.sut = PredicateProcessor(self.norm_updater)


    def test_predicate_processor(self):
        test_contract = get_test_contract()
        init_sym = test_contract.to_sym()

        config = ParameterConfig('obligations', 'test_obligation', 'consequent')
        result = self.sut.process(config, test_contract, None)

        self.assertEqual(result.contract_spec.obligations['test_obligation'].id, 'new_obligation')

        self.assertEqual(type(result), SymboleoContract)
        self.assertEqual(self.norm_updater.update.call_count, 1)

        # Ensure init_contract has not changed
        self.assertEqual(test_contract.to_sym(), init_sym)
        

  
if __name__ == '__main__':
    unittest.main()