import unittest
from unittest.mock import MagicMock

from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract

from tests.helpers.test_nlp import TestNLP
from app.src.rules.domain_model.amount.simple_amount_scorer import SimpleAmountScorer 

class SimpleAmountScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.sut = SimpleAmountScorer(self.nlp)


    def test_simple_amount_scorer(self):
        test_contract = get_test_contract()
        test_suite = [
            ['$10.50 in USD', [('10.50', 1)]], # $, NUM, curr => 1
            ['$2000 USD', [('2000', 1)]], # $, NUM, curr
            ['500 CAD', [('500', 0.7)]], # CAD doesnt get the MONEY entity
            ['500 USD', [('500', 1)]], # USD DOES
            ['$555.55 CAD', [('555.55', 1)]],
            ['USD 787', [('787', 1)]],
            ['100 chickens', []],
            ['100 1000 USD CAD $', []],
            ['100 of your fine, crisp canadian dollars in bill form', []], # Too long
            #['100 nonsense CAD ue3iri2 $', []], 
            ## Should we handle the gibberish case? Or is that an earlier problem of grammatical correctness checking?

        ]

        for x, expected,  in test_suite:
            doc = self.nlp(x)
            req = ContractUpdateRequest(test_contract, 'TEST_KEY', x, doc)
            result = self.sut.score(req)
            self.assertEqual(result, expected)

  
if __name__ == '__main__':
    unittest.main()