import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract

from app.classes.domain_model.domain_model import DomainEvent, DomainProp

from app.src.rules.domain_model.domain_event_prop_scorer import IScoreDomainEventProps
from app.src.rules.domain_model.domain_reference_scorer import DomainReferenceScorer


class DomainReferenceScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        prop_name = 'abcd' # May change this to a full DomainProp...

        self.domain_event_prop_scorer = IScoreDomainEventProps()
        self.domain_event_prop_scorer.score = MagicMock(return_value=[('a',1),('b',0.5)])

        self.sut = DomainReferenceScorer(self.nlp, prop_name, self.domain_event_prop_scorer)

    
    def test_domain_reference_scorer(self):
        test_contract = get_test_contract()
        test_contract.domain_model.events['test_event'] = DomainEvent('test_event', [
            DomainProp('abcd', 'XXX', 'str')
        ])

        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'Test value', None)

        result = self.sut.score(req)
        self.assertEqual(len(result),2)

        

  
if __name__ == '__main__':
    unittest.main()