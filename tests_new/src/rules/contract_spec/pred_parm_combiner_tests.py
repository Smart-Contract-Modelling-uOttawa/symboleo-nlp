import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens

from app.classes.processing.scored_components import ScoredPredicate, ScoredPredicateType, ScoredParameter
from app.src.rules.contract_spec.dynamic_constructor import IConstructDynamicObjects
from app.src.rules.contract_spec.pred_parm_combiner import PredParmCombiner

class PredParmCombinerTests(unittest.TestCase):
    def setUp(self):
        self.constructor = IConstructDynamicObjects()
        fake_pred = ScoredPredicate(VariableEvent('test'), 0.5)
        self.constructor.construct = MagicMock(side_effect=[fake_pred, None])

        self.sut = PredParmCombiner(self.constructor)


    def test_pred_parm_combiner(self):
        preds = [
            ScoredPredicateType(PredicateFunctionHappens, 1),
            ScoredPredicateType(PredicateFunctionHappens, 1),
        ]
        parms = [
            ScoredParameter(VariableEvent('test'), 1)
        ]

        results = self.sut.combine(preds, parms)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].score, 0.5)
        self.assertEqual(self.constructor.construct.call_count, 2)        

  
if __name__ == '__main__':
    unittest.main()