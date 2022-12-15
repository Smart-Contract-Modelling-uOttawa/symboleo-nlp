import unittest
from unittest.mock import MagicMock
from app.src.component_identifiers.helpers.event_scorer import EventScorer
from tests.helpers.test_nlp import TestNLP

test_suite = [
    ['this is a test', ('be', 1)], 
    ['Bob has eaten three apples.', ('ate', 0.5)],
    ['The birds gathered on the tree', ('', 0)],
    ['Delivery of goods has been completed', ('terminated', 1)]
]

class EventScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        d1 = {
            'be': ['be'],
            'terminated': ['complete']
        }
        d2 = {
            'ate': ['eat']
        }
        dict_set = [
            (d1, 1),
            (d2, 0.5)
        ]
        self.sut = EventScorer(dict_set)
        

    def test_event_scorer(self):
        for sentence, expected_result in test_suite:
            doc = self.nlp(sentence)
            result = self.sut.score(doc)
            self.assertEqual(result, expected_result)
    

        

        
  
  
if __name__ == '__main__':
    unittest.main()