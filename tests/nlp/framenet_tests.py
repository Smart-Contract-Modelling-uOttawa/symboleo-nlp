import unittest
from unittest.mock import MagicMock

from nltk.corpus import framenet as fn
from app.src.nlp.framenet import MyFramenet

class FramenetExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = MyFramenet(fn)

    def test_get_flus(self):
        result = self.sut.get_lus('walk')
        nameset = [x.name for x in result] 
        self.assertIn('walk.n', nameset)
        self.assertIn('walk.v', nameset)
    
if __name__ == '__main__':
    unittest.main()