import unittest
from unittest.mock import MagicMock
from app.src.selection.element_extractors.custom_event.verb.lemmatizer import Lemmatizer

# TODO: Need FakeNLP
class LemmatizerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = None
        self.sut = Lemmatizer()
    
    @unittest.skip('Need Fake NLP')
    def test_lemmatizer(self):
        return
        #result = self.sut.lemmatize('testing')


if __name__ == '__main__':
    unittest.main()
