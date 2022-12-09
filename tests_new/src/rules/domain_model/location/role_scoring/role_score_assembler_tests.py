import unittest
from unittest.mock import MagicMock
from tests.helpers.test_nlp import TestNLP

from app.src.rules.domain_model.location.role_scoring.role_score_assembler import RoleScoreAssembler 
from app.src.rules.domain_model.property_similarity_scorer import IScoreProperySimilarity

from app.classes.symboleo_contract import DomainModel
from app.classes.domain_model.domain_model import DomainProp, Role

class RoleScoreAssemblerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.prop_scorer = IScoreProperySimilarity()
        fake_scores1 = {'key1': 0.4, 'key2': 0.6}
        fake_scores2 = {'key1': 0.2, 'key3': 0.8}
        self.prop_scorer.get_scores = MagicMock(side_effect=[fake_scores1, fake_scores2])
        self.sut = RoleScoreAssembler(self.prop_scorer)

        role1 = Role('role1', [DomainProp('key1', 'val1', 'str'), DomainProp('key2', 'val2', 'str')])
        role2 = Role('role2', [DomainProp('key1', 'val1', 'str'), DomainProp('key3', 'val3', 'str')])
        self.fake_domain_model = DomainModel({'role1': role1, 'role2': role2}, {}, {})


    def test_role_score_assembler(self):
        role_score_dict = {'role1': 1, 'role2': 0.5}
        location = self.nlp('the location')
        result = self.sut.assemble(role_score_dict, self.fake_domain_model, location)

        expected_result = [
            ('role1.key1', 0.4),
            ('role1.key2', 0.6),
            ('role2.key1', 0.1),
            ('role2.key3', 0.4),
        ]
        self.assertEqual(len(result), 4)
        for x in expected_result:
            self.assertTrue(x in result)

  
if __name__ == '__main__':
    unittest.main()