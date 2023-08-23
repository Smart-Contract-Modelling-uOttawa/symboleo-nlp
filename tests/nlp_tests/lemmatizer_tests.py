import unittest
from unittest.mock import MagicMock

from app.src.nlp.nlp_getter import NLPGetter
from app.src.nlp.lemmatizer import Lemmatizer
from app.src.nlp.fake_lemmatizer import FakeLemmatizer

class LemmatizerTests(unittest.TestCase):
    def setUp(self):
        nlp = NLPGetter.get()
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