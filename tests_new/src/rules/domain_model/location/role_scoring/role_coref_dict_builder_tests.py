import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract
from app.src.rules.domain_model.location.coref_getter import IGetCorefs
from app.src.rules.domain_model.location.role_scoring.coref_template_prepper import IPrepCorefTemplates
from tests.helpers.test_nlp import TestNLP
from app.src.rules.domain_model.location.role_scoring.role_coref_dict_builder import RoleCorefDictBuilder 

class RoleCorefDictBuilderTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        init_scores = {'role1': 0.5, 'role2': 0.8}

        self.coref_getter = IGetCorefs()
        fake_corefs = {'1': ['their', 'role1']}
        self.coref_getter.get = MagicMock(return_value=fake_corefs)

        self.coref_prepper = IPrepCorefTemplates()
        fake_coref_prep = (self.nlp('test'), 1)
        self.coref_prepper.prep = MagicMock(return_value=fake_coref_prep)

        self.sut = RoleCorefDictBuilder(init_scores, self.coref_prepper, self.coref_getter)


    def test_role_coref_dict_builder(self):
        test_contract = get_test_contract()
        value = 'at their address'
        doc = self.nlp(value)
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', value, doc)

        result = self.sut.build(req)

        self.assertEqual(result['role1'], 0.9)
        self.assertEqual(result['role2'], 0.8)
  
if __name__ == '__main__':
    unittest.main()