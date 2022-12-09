import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract
from tests.helpers.test_nlp import TestNLP
from app.src.rules.domain_model.location.role_scoring.role_match_dict_builder import RoleMatchDictBuilder 

from app.src.matcher_helper import IGetMatches
from app.src.rules.domain_model.location.role_scoring.role_pattern_builder import IBuildRolePatterns

class RoleMatchDictBuilderTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        init_scores = {'role1': 0.5, 'role2': 0.9}

        self.pattern_builder = IBuildRolePatterns()
        fake_pattern = []
        self.pattern_builder.build = MagicMock(return_value=fake_pattern) 

        self.matcher = IGetMatches()
        fake1 = self.nlp('role1')
        self.matcher.match = MagicMock(side_effect=[fake1,None])

        self.sut = RoleMatchDictBuilder(init_scores, self.pattern_builder, self.matcher)


    def test_role_match_dict_builder(self):
        test_contract = get_test_contract()
        value = 'at role1\'s address'
        doc = self.nlp(value)
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', value, doc)

        result = self.sut.build(req)

        self.assertEqual(result['role1'], 1)
        self.assertEqual(result['role2'], 0.9)
  
if __name__ == '__main__':
    unittest.main()