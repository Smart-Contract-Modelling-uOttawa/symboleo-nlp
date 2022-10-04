import unittest
from unittest.mock import MagicMock
from tests.helpers.test_nlp import TestNLP
from app.src.primitive_extractor import PrimitiveExtractor

class PrimitiveExtractorTests(unittest.TestCase):
    def setUp(self):
        # TODO: Will have many more inputs here...
        # self.nlp = TestNLP.get_nlp()
        self.sut = PrimitiveExtractor()

    def test_primitive_extractor(self):
        # sentence = 'this is a test'
        # doc = self.nlp(sentence)

        # result = self.sut.extract(doc)
        # TODO: Add tests
        return
        

  
if __name__ == '__main__':
    unittest.main()