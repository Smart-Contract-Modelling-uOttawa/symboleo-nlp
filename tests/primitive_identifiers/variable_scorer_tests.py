import unittest
from unittest.mock import MagicMock
from app.src.component_identifiers.helpers.similarity_calculator import ICalculateSentenceSimilarity
from app.src.component_identifiers.helpers.variable_scorer import VariableScorer
from tests.helpers.test_nlp import TestNLP

class VariableScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.sentence_dict = {
            'a': 'test a',
            'b': 'test b'
        }

        self.similarity_calculator = ICalculateSentenceSimilarity()
        fake_similarities = [0.4, 0.6]
        self.similarity_calculator.calculate = MagicMock(side_effect = fake_similarities) 
        self.sut = VariableScorer(self.nlp, self.sentence_dict, self.similarity_calculator)
        

    def test_variable_scorer(self):
        s = 'this is a test'
        doc = self.nlp(s)
        result = self.sut.score(doc)

        self.assertEqual(result[0], 'b')
        self.assertEqual(result[1], 0.6)
  
  
if __name__ == '__main__':
    unittest.main()