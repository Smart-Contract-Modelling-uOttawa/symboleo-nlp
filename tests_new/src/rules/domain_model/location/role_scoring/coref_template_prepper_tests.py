import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract
from tests.helpers.test_nlp import TestNLP
from app.src.rules.domain_model.location.role_scoring.coref_template_prepper import CorefTemplatePrepper 


class CorefTemplatePrepperTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.sut = CorefTemplatePrepper(self.nlp)


    def test_coref_template_prepper(self):
        test_contract = get_test_contract()
        test_contract.template_strings = {
            'obligations': {
                'test_ob': 'This is a test [TEST1] and this is another [TEST2]'
            }
        }
        value = 'my value for the test'
        doc = self.nlp(value)
        req = ContractUpdateRequest(test_contract, 'TEST2', value, doc)

        result = self.sut.prep(req)

        expected_string = 'This is a test and this is another my value for the test'
        expected_index = 8

        self.assertEqual(result[0].text, expected_string)
        self.assertEqual(result[1], expected_index)

  
if __name__ == '__main__':
    unittest.main()