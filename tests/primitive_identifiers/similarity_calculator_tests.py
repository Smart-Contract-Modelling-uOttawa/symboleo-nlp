import unittest
from unittest.mock import MagicMock
from app.src.primitive_identifiers.sentence_preprocessor import SentencePreprocessor
from app.src.primitive_identifiers.similarity_calculator import SentenceSimilarityCalculator
from tests.helpers.test_nlp import TestNLP

test_suite = [
    ['I walked to the store yesterday', 'I ran to the shop a day ago', 0.7, 0.9],
    ## add more here...
]

class SimilarityCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.preprocessor = SentencePreprocessor(self.nlp) # not mocked
        self.sut = SentenceSimilarityCalculator(self.preprocessor)
        

    def test_sentence_preprocessor(self):
        for s1, s2, min_score, max_score in test_suite:
            d1 = self.nlp(s1)
            d2 = self.nlp(s2)
            result = self.sut.calculate(d1, d2)
            self.assertTrue(result < max_score)
            self.assertTrue(result > min_score)
  
  
if __name__ == '__main__':
    unittest.main()