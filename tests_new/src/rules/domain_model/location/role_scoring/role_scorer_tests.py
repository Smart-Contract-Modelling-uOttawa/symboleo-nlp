import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract

from tests.helpers.test_nlp import TestNLP
from app.src.rules.domain_model.location.role_scoring.role_score_builder import IBuildRoleScores
from app.src.rules.domain_model.location.location_span_extractor import IExractLocationSpans
from app.src.rules.domain_model.location.role_scoring.role_score_assembler import IAssembleRoleScores

from app.src.rules.domain_model.location.role_scoring.role_scorer import RoleScorer 

class RoleScorerTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()

        self.location_span_extractor = IExractLocationSpans()
        fake_span = nlp('this is a test')[0:2]
        self.location_span_extractor.extract = MagicMock(return_value=fake_span)

        self.role_score_builder = IBuildRoleScores()
        fake_role_score_dict = {'seller': 0.4, 'buyer': 0.6}
        self.role_score_builder.build = MagicMock(return_value = fake_role_score_dict)

        self.role_score_assembler = IAssembleRoleScores()
        fake_role_scores = [('test1', 0.1), ('test2', 0.2)]
        self.role_score_assembler.assemble = MagicMock(return_value = fake_role_scores)

        self.sut = RoleScorer(
            self.location_span_extractor,
            self.role_score_builder,
            self.role_score_assembler
        )


    def test_role_scorer(self):
        test_contract = get_test_contract()
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        result = self.sut.score(req)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], ('test1', 0.1))
        
        self.assertEqual(self.location_span_extractor.extract.call_count, 1)
        self.assertEqual(self.role_score_builder.build.call_count, 1)
        self.assertEqual(self.role_score_assembler.assemble.call_count, 1)


    def test_role_scorer_empty(self):
        self.location_span_extractor.extract = MagicMock(return_value=None)

        test_contract = get_test_contract()
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        result = self.sut.score(req)

        self.assertEqual(len(result), 0)
        
        self.assertEqual(self.location_span_extractor.extract.call_count, 1)
        self.assertEqual(self.role_score_builder.build.call_count, 0)
        self.assertEqual(self.role_score_assembler.assemble.call_count, 0)

  
if __name__ == '__main__':
    unittest.main()