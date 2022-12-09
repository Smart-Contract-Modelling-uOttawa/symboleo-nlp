import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP

from app.classes.domain_model.domain_model import DomainProp

from app.src.rules.domain_model.property_similarity_scorer import PropertySimilarityScorer
from app.src.rules.domain_model.similarity_scorer import IScoreSimilarity


class PropSimilarityScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.similarity_scorer = IScoreSimilarity()
        self.similarity_scorer.score = MagicMock(side_effect=[0.5,0.4,0.2,0.1])

        self.sut = PropertySimilarityScorer(self.nlp, self.similarity_scorer)


    def test_prop_similarity_scorers(self):
        props = [
            DomainProp('key1', 'value1', 'str'),
            DomainProp('key2', 'value2', 'str')
        ]
        span = self.nlp('test value')
        
        result = self.sut.get_scores(props, span)

        self.assertEqual(result['key1'], 0.5)
        self.assertEqual(result['key2'], 0.2)

        self.assertEqual(self.similarity_scorer.score.call_count, 4)
        

  
if __name__ == '__main__':
    unittest.main()