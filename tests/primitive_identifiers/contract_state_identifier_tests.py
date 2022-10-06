import unittest
from unittest.mock import MagicMock
from app.classes.spec.primitive import Primitive
from app.classes.spec.sym_situation import ContractState
from app.src.primitive_identifiers.event_scorer import IScoreEvents

from app.src.primitive_identifiers.contract_state_identifier import ContractStateIdentifier

from tests.helpers.test_nlp import TestNLP

class ContractStateIdentifierTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.event_name_scorer = IScoreEvents()
        self.fake_event_name = ('state_x', 0.8)
        self.event_name_scorer.score = MagicMock(return_value = self.fake_event_name)

        self.sut = ContractStateIdentifier(
            self.event_name_scorer,
        )
        

    def test_contract_state_identifier(self):
        sentence = 'this is a test'
        doc = self.nlp(sentence)

        result = self.sut.identify(doc)
        prim: ContractState = result.primitive
        score = result.score
        self.assertEqual(prim.state_name, 'state_x')
        self.assertEqual(score, 0.56)

  
if __name__ == '__main__':
    unittest.main()