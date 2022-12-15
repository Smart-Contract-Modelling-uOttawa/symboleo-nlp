import unittest
from unittest.mock import MagicMock
from app.classes.spec.helpers import TimeUnitStr

from app.src.component_identifiers.time_unit_str_scorer import TimeUnitStrIdentifier

from tests.helpers.test_nlp import TestNLP

# TODO: More sophisticated tests
test_suite = [
    ['you must pay within 10 days', 'days', 1],
    ['I will arrive in 1 hour', 'hours', 1],
    ['I will arrive in 12 days', 'days', 1],
    ['I will arrive in thirty-five minutes', 'minutes', 1],
    ['There are ten things you need to know', '', 0],
    ['I will finish in second place', 'seconds', 0.5],
    ['I will finish in second', 'seconds', 0.5],
    ['I will finish in a second', 'seconds', 1], # TODO: fix - 1
    ['I will finish in one second', 'seconds', 0.5], # TODO: fix - 1
    ['I will finish in 1 second', 'seconds', 0.5], # TODO: fix - 1
    ['It will arrive between 10-15 business days', 'days', 0.5] # TODO: fix - 1
]

class TimeUnitStrIdentifierTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.sut = TimeUnitStrIdentifier()
        

    def test_time_unit_str_identifier(self):
        for test_sent, exp_value, exp_score in test_suite:
            doc = self.nlp(test_sent)
            
            result = self.sut.identify(doc)
            prim: TimeUnitStr = result.primitive
            score = result.score
            self.assertEqual(prim.unit, exp_value, f'failed: {test_sent}')
            self.assertEqual(score, exp_score, f'failed: {test_sent}')

  
if __name__ == '__main__':
    unittest.main()