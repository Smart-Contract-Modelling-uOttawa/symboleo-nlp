import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract
from app.src.rules.domain_model.location.role_scoring.role_score_builder import RoleScoreBuilder, IBuildRoleScores 

class RoleScorerTests(unittest.TestCase):
    def setUp(self):
        self.inner1 = IBuildRoleScores()
        fake1 = {'test1': 0.1, 'test2': 0.4}
        self.inner1.build = MagicMock(return_value=fake1)

        self.inner2 = IBuildRoleScores()
        fake2 = {'test1': 0.2, 'test2': 0.1}
        self.inner2.build = MagicMock(return_value=fake2)

        inner_scorers = [self.inner1, self.inner2]
        init_scores = {'test1': 0, 'test2':0.5}
        self.sut = RoleScoreBuilder(init_scores, inner_scorers )


    def test_role_score_builder(self):
        test_contract = get_test_contract()
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        result = self.sut.build(req)

        self.assertEqual(len(result), 2)
        self.assertEqual(result['test1'], 0.2)
        self.assertEqual(result['test2'], 0.4)
        
        self.assertEqual(self.inner1.build.call_count, 1)
        self.assertEqual(self.inner2.build.call_count, 1)

  
if __name__ == '__main__':
    unittest.main()