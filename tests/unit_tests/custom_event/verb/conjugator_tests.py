import unittest
from unittest.mock import MagicMock
from mlconjug3 import Conjugator as ML3Conjugator
from app.src.selection.element_extractors.custom_event.verb.conjugator import MyConjugator

# Uses a third party... May separate out the tests
# Or add more
class ConjugatorTests(unittest.TestCase):
    def setUp(self):
        self.inner_conjugator = ML3Conjugator(language='en')
        self.sut = MyConjugator(self.inner_conjugator)
    
    def test_conjugator(self):
        result = self.sut.conjugate('pay')
        self.assertEqual(result.past, 'paid')


if __name__ == '__main__':
    unittest.main()
