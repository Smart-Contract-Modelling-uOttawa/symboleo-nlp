import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP

from app.src.element_extractors.verb.lemmatizer import Lemmatizer

test_suite = [
    ('receiving', 'receive'),
    ('authorizes', 'authorize'),
    ('completes', 'complete'),
    ('starts', 'start'),
    ('terminates', 'terminate'),
    ('terminating', 'terminate'),
    ('beginning', 'begin'),
    ('disrupts', 'disrupt'),
    ('occupying', 'occupy'),
    ('provides', 'provide'),
]

# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class LemmatizerTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        self.sut = Lemmatizer(nlp)

    def test_lemmatizer(self):
        for test_val, exp_val in test_suite:
            res = self.sut.lemmatize(test_val)
            self.assertEqual(res, exp_val)

if __name__ == '__main__':
    unittest.main()