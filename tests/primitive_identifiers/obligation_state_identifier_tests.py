import unittest
from unittest.mock import MagicMock
from app.classes.spec.primitive import Primitive
from app.classes.spec.sym_situation import ObligationState
from app.src.primitive_identifiers.state_name_scorer import IScoreStates

from app.src.primitive_identifiers.obligation_state_identifier import ObligationStateIdentifier
from app.src.primitive_identifiers.variable_scorer import IScoreVariables

from tests.helpers.test_nlp import TestNLP

class ObligationStateIdentifierTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.state_name_scorer = IScoreStates()
        self.fake_state_name = ('state_x', 0.8)
        self.state_name_scorer.score = MagicMock(return_value = self.fake_state_name)

        self.variable_scorer = IScoreVariables()
        self.fake_variable = ()
        self.fake_variable = ('var_x', 0.4)
        self.variable_scorer.score = MagicMock(return_value = self.fake_variable)

        self.sut = ObligationStateIdentifier(
            self.state_name_scorer,
            self.variable_scorer
        )
        

    def test_obligation_state_identifier(self):
        sentence = 'this is a test'
        doc = self.nlp(sentence)

        result = self.sut.identify(doc)
        prim: ObligationState = result.primitive
        score = result.score
        self.assertEqual(prim.state_name, 'state_x')
        self.assertEqual(prim.obligation_variable, 'var_x')
        self.assertEqual(score, 0.32)

  
if __name__ == '__main__':
    unittest.main()