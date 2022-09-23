import unittest
from unittest.mock import MagicMock
from app.classes.spec.atoms import SituationProposition
from app.lib.matchers.interfaces import IValidateMatches
from app.lib.matchers.simple.simple_matcher import SimpleMatcher

from tests.helpers.test_nlp import TestNLP

class SimpleMatcherTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.key = 'test_key'

        self.validator = IValidateMatches()
        self.validator.validate = MagicMock(return_value = True)
        self.sut = SimpleMatcher(self.key, self.nlp, self.validator)


    def test_simple_matcher(self):
        test_sentence = 'the sky is blue'
        doc = self.nlp(test_sentence)

        key = self.sut.key()
        self.assertEqual(key, self.key)

        result = self.sut.try_match(doc)
        res_atom: SituationProposition = result.atom

        self.assertEqual(result.negation, False)
        self.assertEqual(res_atom.situation.name, 'is_blue(sky)')
        self.assertEqual(res_atom.interval.name, 'X')

    
    def test_simple_matcher_none(self):
        validator = IValidateMatches()
        validator.validate = MagicMock(return_value = False)
        sut = SimpleMatcher(self.key, self.nlp, validator)

        test_sentence = 'the sky is blue'
        doc = self.nlp(test_sentence)

        result = sut.try_match(doc)
        self.assertIsNone(result)

  
if __name__ == '__main__':
    unittest.main()