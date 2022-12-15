import unittest
from unittest.mock import MagicMock
from app.classes.processing.components import Primitive
from app.classes.spec.sym_event import ContractEvent
from app.src.component_identifiers.helpers.event_scorer import IScoreEvents

from app.src.component_identifiers.contract_event_scorer import ContractEventIdentifier

from tests.helpers.test_nlp import TestNLP

class ContractEventIdentifierTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.event_name_scorer = IScoreEvents()
        self.fake_event_name = ('event_x', 0.8)
        self.event_name_scorer.score = MagicMock(return_value = self.fake_event_name)

        self.sut = ContractEventIdentifier(
            self.event_name_scorer,
        )
        

    def test_contract_event_identifier(self):
        sentence = 'this is a test'
        doc = self.nlp(sentence)

        result = self.sut.identify(doc)
        prim: ContractEvent = result.primitive
        score = result.score
        self.assertEqual(prim.event_name, 'event_x')
        self.assertEqual(score, 0.56)

  
if __name__ == '__main__':
    unittest.main()