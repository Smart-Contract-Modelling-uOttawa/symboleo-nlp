import unittest
from unittest.mock import MagicMock
from app.classes.spec.helpers import TimeValueInt

from app.src.primitive_identifiers.time_value_int_identifier import TimeValueIntIdentifier

from tests.helpers.test_nlp import TestNLP

# TODO: More sophisticated tests
test_suite = [
    ['I will arrive in 1 hour', '1', 1],
    ['I will arrive in 12 days', '12', 1],
    #['I will arrive in thirty-five minutes', 'thirty-five', 1],
    ['There are ten things you need to know', 'ten', 0.7] # should be 10...
]

class TimeValueIntIdentifierTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.sut = TimeValueIntIdentifier()
        

    def test_time_value_int_identifier(self):
        for test_sent, exp_value, exp_score in test_suite:
            doc = self.nlp(test_sent)
            
            result = self.sut.identify(doc)
            prim: TimeValueInt = result.primitive
            score = result.score
            self.assertEqual(prim.value, exp_value)
            self.assertEqual(score, exp_score)

  
if __name__ == '__main__':
    unittest.main()