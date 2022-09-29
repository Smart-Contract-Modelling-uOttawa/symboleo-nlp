import unittest
from spacy.matcher import Matcher

from app.src.matchers.spacy_matcher_wrapper import SpacyMatcherWrapper

from tests.helpers.test_nlp import TestNLP

class SpacyMatcherWrapperTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.key = 'simple'
        test_pattern = [{"TAG": "DT"}, {"TAG": "NN"}, {"TAG": "VBZ"}, {"TAG": "JJ"}]
        self.sut = SpacyMatcherWrapper(self.key, self.nlp, test_pattern)


    def test_spacy_matcher_wrapper(self):
        test_sentence = 'the sky is blue'
        doc = self.nlp(test_sentence)
        result = self.sut.match(doc)

        self.assertEqual(len(result), 1)

        res1 = result[0]
        self.assertEqual(res1[0], self.key)
        self.assertEqual(res1[1], 0)
        self.assertEqual(res1[2], 4)


    def test_spacy_matcher_wrapper_empty(self):
        test_sentence = 'Call me Ishmael'
        doc = self.nlp(test_sentence)
        result = self.sut.match(doc)

        self.assertEqual(len(result), 0)

        
        
  
if __name__ == '__main__':
    unittest.main()