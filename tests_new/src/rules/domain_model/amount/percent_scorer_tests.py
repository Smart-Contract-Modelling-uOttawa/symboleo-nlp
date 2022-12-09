import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract

from tests.helpers.test_nlp import TestNLP
from app.src.matcher_helper import IGetMatches
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.domain_model.domain_event_prop_scorer import IScoreDomainEventProps
from app.src.rules.domain_model.amount.percent_scorer import PercentScorer 

class PercentScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.matcher = IGetMatches()
        fake_match = self.nlp('10% of')
        self.matcher.match = MagicMock(return_value=fake_match)

        self.domain_event_prop_scorer = IScoreDomainEventProps()
        self.domain_event_prop_scorer.score = MagicMock(return_value=[('key1.event1', 1), ('key2.event2', 0.5)])
        self.sut = PercentScorer(self.nlp, self.matcher, self.domain_event_prop_scorer)


    def test_simple_amount_scorer(self):
        test_contract = get_test_contract()
        value = '10% of the amount owed'
        doc = self.nlp(value)
        req = ContractUpdateRequest(test_contract, 'TEST_KEY', value, doc)

        results = self.sut.score(req)

        expected_results = [('10% * key1.event1', 1), ('10% * key2.event2', 0.5)]

        self.assertEqual(len(results), len(expected_results))

        for x in expected_results:
            self.assertTrue(x in results)

  
if __name__ == '__main__':
    unittest.main()