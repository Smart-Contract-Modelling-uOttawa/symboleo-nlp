import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract

from app.classes.spec.helpers import TimeUnitStr, TimeValueInt
from app.classes.spec.sym_point import PointFunction, PointVDE
from app.classes.processing.scored_components import ScoredPrimitive
from app.src.rules.contract_spec.recursive_identifier import IIdentifyParametersRecursively
from app.src.rules.contract_spec.all_primitives_scorer import IScoreAllPrimitives
from app.src.rules.contract_spec.parameter_scorer import ParameterScorer

class ParameterScorerTests(unittest.TestCase):
    def setUp(self):
        parm_types = [
            PointFunction,
            PointFunction
        ]

        self.primitive_scorer = IScoreAllPrimitives()
        fake_primitives = [
            ScoredPrimitive(TimeValueInt(10), 1)
        ]
        self.primitive_scorer.score = MagicMock(return_value=fake_primitives)

        defaults = [
            TimeUnitStr('days')
        ]

        self.identifier = IIdentifyParametersRecursively()
        fake_parms = [
            ScoredPrimitive(PointFunction(PointVDE('test'), TimeValueInt(10), TimeUnitStr('days')), 1),
            None
        ]
        self.identifier.identify = MagicMock(side_effect = fake_parms)

        self.sut = ParameterScorer(self.primitive_scorer, parm_types, self.identifier, defaults)

    def test_parameter_scorer(self):
        test_contract = get_test_contract()
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        results = self.sut.score(req)
        
        self.assertEqual(len(results), 1)
        self.assertEqual(type(results[0].obj), PointFunction)
        self.assertEqual(results[0].score, 1)
        self.assertEqual(self.identifier.identify.call_count, 2)   

  
if __name__ == '__main__':
    unittest.main()