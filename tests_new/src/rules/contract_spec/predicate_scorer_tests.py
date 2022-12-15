import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract

from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionOccurs

from app.classes.processing.case_obj import CasePattern
from app.src.matcher_helper import IGetMatches
from app.src.rules.contract_spec.predicate_scorer import PredicateScorer

class PredicateScorerTests(unittest.TestCase):
    def setUp(self):
        self.matcher = IGetMatches()
        self.matcher.match = MagicMock(side_effect = [True, False]) # actual values don't matter. Just checking

        self.case_patterns = [
            CasePattern('x', PredicateFunctionHappens),
            CasePattern('y', PredicateFunctionOccurs)
        ]

        self.sut = PredicateScorer(self.case_patterns, self.matcher)


    def test_pred_extractor(self):
        test_contract = get_test_contract()
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        results = self.sut.score(req)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].obj_type, PredicateFunctionHappens)

        self.assertEqual(self.matcher.match.call_count, 2)       

  
if __name__ == '__main__':
    unittest.main()