import unittest
from unittest.mock import MagicMock

from app.src.rules.shared.match_validator import IValidateMatches
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.meat_sale.delivery_location.location_extractor import LocationExtractor

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_nlp import TestNLP
from tests.helpers.test_contract import get_test_contract

# TODO: Need to get nlp working on the test...
class LocationExtractorTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.validator = IValidateMatches()
        self.validator.validate = MagicMock(return_value=None)
        
        self.scorer1 = IScoreStuff()
        fake_scores1 = [('test_score1', 0.5)]
        self.scorer1.score = MagicMock(return_value = fake_scores1)

        self.scorer2 = IScoreStuff()
        fake_scores2 = [('test_score2a', 0.9), ('test_score2b', 0.1)]
        self.scorer2.score = MagicMock(return_value = fake_scores2)

        self.scorers = [
            self.scorer1,
            self.scorer2
        ]
        
        self.sut = LocationExtractor(self.nlp, self.validator, self.scorers)


    def test_location_extractor(self):
        test_contract = get_test_contract()

        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        result = self.sut.extract(req)

        self.assertEqual(result, 'test_score2a')
        self.assertEqual(self.scorer1.extract.call_count, 1)
        self.assertEqual(self.scorer2.update.call_count, 1)
        

  
if __name__ == '__main__':
    unittest.main()