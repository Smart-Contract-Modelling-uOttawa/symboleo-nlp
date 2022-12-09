import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract

from app.classes.domain_model.domain_model import DomainEvent, DomainProp

from app.src.rules.domain_model.property_similarity_scorer import IScoreProperySimilarity
from app.src.rules.domain_model.domain_event_prop_scorer import DomainEventPropScorer


class DomainEventPropScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.prop_scorer = IScoreProperySimilarity()
        self.prop_scorer.get_scores = MagicMock(side_effect=[{'p3': 0, 'p1': 1}, {'p2': 0.5}])
        self.sut = DomainEventPropScorer(self.prop_scorer)


    def test_domain_event_prop_scorer(self):
        test_contract = get_test_contract()
        test_contract.domain_model.events = {
            'key1': DomainEvent('key1', []),
            'key2': DomainEvent('key2', [])
        }
        
        result = self.sut.score(test_contract.domain_model.events, None)
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], ('key1.p1', 1))
        self.assertEqual(result[1], ('key2.p2', 0.5))
        self.assertEqual(result[2], ('key1.p3', 0))

        

  
if __name__ == '__main__':
    unittest.main()