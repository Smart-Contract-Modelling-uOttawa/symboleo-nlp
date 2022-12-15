import unittest
from unittest.mock import MagicMock
from app.classes.spec.helpers import TimeValueInt

from app.src.component_identifiers.time_value_int_scorer import TimeValueIntIdentifier

from tests.helpers.test_nlp import TestNLP

# TODO: More sophisticated tests
# May assume that numbers come in as digits - can use numerizer in preprocessing
test_suite = [
    ['I will arrive in 1 hour', '1', 1],
    ['I will arrive in 12 days', '12', 1],
    #['I will arrive in thirty-five minutes', 'thirty-five', 1],
    ['There are 10 things you need to know', '10', 0.7] # should be 10...
    
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
            self.assertEqual(prim.value, exp_value, f'failed: {test_sent}')
            self.assertEqual(score, exp_score, f'failed: {test_sent}')

  
if __name__ == '__main__':
    unittest.main()