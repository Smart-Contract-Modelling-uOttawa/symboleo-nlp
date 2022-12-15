import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract

from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens

from app.classes.processing.scored_components import ScoredPredicate, ScoredPredicateType, ScoredParameter
from app.src.rules.contract_spec.predicate_scorer import IScorePredicates
from app.src.rules.contract_spec.parameter_scorer import IScoreParameters
from app.src.rules.contract_spec.pred_parm_combiner import ICombinePredsParms

from app.src.rules.contract_spec.predicate_extractor import PredicateExtractor

class PredExtractorTests(unittest.TestCase):
    def setUp(self):
        self.pred_scorer = IScorePredicates()
        fake_preds = [ScoredPredicateType(PredicateFunctionHappens,1)]
        self.pred_scorer.score = MagicMock(side_effect = [[], fake_preds, fake_preds])

        self.parm_scorer = IScoreParameters()
        fake_parms = [ScoredParameter(VariableEvent, 1)]
        self.parm_scorer.score = MagicMock(side_effect = [[], fake_parms])

        self.combiner = ICombinePredsParms()
        fake_res = [ScoredPredicate(PredicateFunctionHappens(VariableEvent('test')), 1)]
        self.combiner.combine = MagicMock(side_effect = [fake_res])

        self.sut = PredicateExtractor(self.pred_scorer, self.parm_scorer, self.combiner)


    def test_pred_extractor(self):
        test_contract = get_test_contract()
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        results1 = self.sut.extract(req)
        self.assertEqual(len(results1), 0)

        results2 = self.sut.extract(req)
        self.assertEqual(len(results2), 0)

        results3 = self.sut.extract(req)
        self.assertEqual(len(results3), 1)
        self.assertEqual(type(results3[0].obj), PredicateFunctionHappens)

        self.assertEqual(self.pred_scorer.score.call_count, 3) 
        self.assertEqual(self.parm_scorer.score.call_count, 2)    
        self.assertEqual(self.combiner.combine.call_count, 1)        

  
if __name__ == '__main__':
    unittest.main()