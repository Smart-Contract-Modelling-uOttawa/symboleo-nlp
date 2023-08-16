import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from app.src.nlp.lemmatizer import Lemmatizer
from app.src.nlp.fake_lemmatizer import FakeLemmatizer

class LemmatizerTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        self.sut = Lemmatizer(nlp)

    def test_lemmatizer(self):
        fl = FakeLemmatizer()
        test_dict = fl.get_dict()

        for x in test_dict:
            exp_val = test_dict[x]
            result = self.sut.lemmatize(x)
            self.assertEqual(result, exp_val)

if __name__ == '__main__':
    unittest.main()