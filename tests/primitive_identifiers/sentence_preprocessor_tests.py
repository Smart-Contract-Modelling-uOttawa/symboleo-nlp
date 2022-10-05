import unittest
from unittest.mock import MagicMock
from app.src.primitive_identifiers.sentence_preprocessor import SentencePreprocessor
from tests.helpers.test_nlp import TestNLP

test_suite = [
    ('this is a test', 'test'),
    ('The quick brown fox jumped over the lazy dog', 'quick brown fox jump lazy dog'),
    # Can add more here...
]

class SentencePreprocessorTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.sut = SentencePreprocessor(self.nlp)
        

    def test_sentence_preprocessor(self):
        for s in test_suite:
            doc = self.nlp(s[0])
            expected_result = s[1]
            result = self.sut.preprocess(doc)
            sentence_result = ' '.join([x.text for x in result])
            self.assertEqual(expected_result, sentence_result)
  
  
if __name__ == '__main__':
    unittest.main()