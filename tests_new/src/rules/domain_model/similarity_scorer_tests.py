import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from app.src.rules.domain_model.similarity_scorer import SimilarityScorer


class SimilarityScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.sut = SimilarityScorer()


    def test_prop_similarity_scorers(self):
        test_suite = [
            ['their warehouse', 'warehouse', 0.7, 1],
            ['its warehouse', 'warehouse', 0.7, 1],
            ['the warehouse', 'warehouse', 0.8, 1],
            ['warehouse', 'warehouse', 0.9, 1],

            ['their warehouse', 'address', 0.5, 0.7],
            ['its warehouse', 'address', 0.5, 0.7],
            ['the warehouse', 'address', 0.5, 0.7],
            ['warehouse', 'address', 0.5, 0.7],

            ['their location', 'warehouse', 0.5, 0.7],
            ['its location', 'warehouse', 0.5, 0.7],
            ['the location', 'warehouse', 0.6, 0.8],
            ['location', 'warehouse', 0.6, 0.8],

            ['their location', 'address', 0.5, 0.7],
            ['its location', 'address', 0.5, 0.7],
            ['the location', 'address', 0.6, 0.8],
            ['location', 'address', 0.6, 0.8],

            ['their address', 'warehouse', 0.5, 0.7],
            ['its address', 'warehouse', 0.5, 0.7],
            ['the address', 'warehouse', 0.5, 0.7],
            ['address', 'warehouse', 0.5, 0.7],

            ['their address', 'address', 0.8, 1],
            ['its address', 'address', 0.8, 1],
            ['the address', 'address', 0.8, 1],
            ['address', 'address', 0.9, 1],
        ]

        for s1, s2, s_min, s_max in test_suite:
            d1 = self.nlp(s1)
            d2 = self.nlp(s2)
            res = self.sut.score(d1, d2)
            self.assertGreaterEqual(res, s_min)
            self.assertLessEqual(res, s_max)

        

  
if __name__ == '__main__':
    unittest.main()