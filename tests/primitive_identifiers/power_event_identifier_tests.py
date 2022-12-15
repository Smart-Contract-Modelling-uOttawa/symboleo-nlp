import unittest
from unittest.mock import MagicMock
from app.classes.processing.components import Primitive
from app.classes.spec.sym_event import PowerEvent
from app.src.component_identifiers.helpers.event_scorer import IScoreEvents

from app.src.component_identifiers.power_event_identifier import PowerEventIdentifier
from app.src.component_identifiers.helpers.variable_scorer import IScoreVariables

from tests.helpers.test_nlp import TestNLP

# This is essentially the same as ObligationEventIdentifierTests (for now...)
class PowerEventIdentifierTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.event_name_scorer = IScoreEvents()
        self.fake_event_name = ('event_x', 0.8)
        self.event_name_scorer.score = MagicMock(return_value = self.fake_event_name)

        self.variable_scorer = IScoreVariables()
        self.fake_variable = ()
        self.fake_variable = ('var_x', 0.4)
        self.variable_scorer.score = MagicMock(return_value = self.fake_variable)

        self.sut = PowerEventIdentifier(
            self.event_name_scorer,
            self.variable_scorer
        )
        

    def test_power_event_identifier(self):
        sentence = 'this is a test'
        doc = self.nlp(sentence)

        result = self.sut.identify(doc)
        prim: PowerEvent = result.primitive
        score = result.score
        self.assertEqual(prim.event_name, 'event_x')
        self.assertEqual(prim.power_variable, 'var_x')
        self.assertEqual(score, 0.32)

  
if __name__ == '__main__':
    unittest.main()