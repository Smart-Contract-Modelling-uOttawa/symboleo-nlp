import unittest
from unittest.mock import MagicMock

from app.src.rules.shared.match_validator import IValidateMatches
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.shared.score_based_extractor import ScoreBasedExtractor

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
        
        self.sut = ScoreBasedExtractor(self.nlp, self.validator, self.scorers)


    def test_score_based_extractor(self):
        test_contract = get_test_contract()

        doc = self.nlp('value')
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', doc)

        result = self.sut.extract(req)

        self.assertEqual(result, 'test_score2a')
        self.assertEqual(self.scorer1.score.call_count, 1)
        self.assertEqual(self.scorer2.score.call_count, 1)
        

  
if __name__ == '__main__':
    unittest.main()