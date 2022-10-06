import unittest
from unittest.mock import MagicMock
from app.classes.spec.helpers import TimeUnitStr

from app.src.primitive_identifiers.time_unit_str_identifier import TimeUnitStrIdentifier

from tests.helpers.test_nlp import TestNLP

# TODO: More sophisticated tests
test_suite = [
    ['I will arrive in 1 hour', 'hours', 1],
    ['I will arrive in 12 days', 'days', 1],
    #['I will arrive in thirty-five minutes', 'thirty-five', 1],
    ['There are ten things you need to know', '', 0] # should be 10...
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
            self.assertEqual(prim.unit, exp_value)
            self.assertEqual(score, exp_score)

  
if __name__ == '__main__':
    unittest.main()