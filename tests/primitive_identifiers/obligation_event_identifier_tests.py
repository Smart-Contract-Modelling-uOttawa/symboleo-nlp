import unittest
from unittest.mock import MagicMock
from app.classes.spec.primitive import Primitive
from app.classes.spec.sym_event import ObligationEvent
from app.src.primitive_identifiers.event_scorer import IScoreEvents

from app.src.primitive_identifiers.obligation_event_identifier import ObligationEventIdentifier
from app.src.primitive_identifiers.variable_scorer import IScoreVariables

from tests.helpers.test_nlp import TestNLP

class ObligationEventIdentifierTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.event_name_scorer = IScoreEvents()
        self.fake_event_name = ('event_x', 0.8)
        self.event_name_scorer.score = MagicMock(return_value = self.fake_event_name)

        self.variable_scorer = IScoreVariables()
        self.fake_variable = ()
        self.fake_variable = ('var_x', 0.4)
        self.variable_scorer.score = MagicMock(return_value = self.fake_variable)

        self.sut = ObligationEventIdentifier(
            self.event_name_scorer,
            self.variable_scorer
        )
        

    def test_obligation_event_identifier(self):
        sentence = 'this is a test'
        doc = self.nlp(sentence)

        result = self.sut.identify(doc)
        prim: ObligationEvent = result.primitive
        score = result.score
        self.assertEqual(prim.event_name, 'event_x')
        self.assertEqual(prim.obligation_variable, 'var_x')
        self.assertEqual(score, 0.32)

  
if __name__ == '__main__':
    unittest.main()