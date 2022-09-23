import unittest
from spacy.matcher import Matcher

from tests.helpers.test_nlp import TestNLP

class SpacyMatcherTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.key = 'test_key'
        test_pattern = [{"TAG": "DT"}, {"TAG": "NN"}, {"TAG": "VBZ"}, {"TAG": "JJ"}]
        matcher = Matcher(self.nlp.vocab)
        matcher.add('test_key', [test_pattern])
        self.sut = matcher

    def test_spacy_matcher(self):
        test_sentence = 'the sky is blue'
        doc = self.nlp(test_sentence)
        result = self.sut(doc)

        self.assertEqual(len(result), 1)
        
        res1 = result[0]
        key_ind, start, end = res1
        res1_key = self.nlp.vocab.strings[key_ind]
        
        self.assertEqual(res1_key, self.key)
        self.assertEqual(start, 0)
        self.assertEqual(end, 4)
    

    def test_spacy_matcher_empty(self):
        test_sentence = 'Call me Ishmael'
        doc = self.nlp(test_sentence)
        result = self.sut(doc)

        self.assertEqual(len(result), 0)
        
        
if __name__ == '__main__':
    unittest.main()