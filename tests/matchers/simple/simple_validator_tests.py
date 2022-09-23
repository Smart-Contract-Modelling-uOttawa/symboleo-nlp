import unittest
from unittest.mock import MagicMock

from app.lib.matchers.spacy_matcher_wrapper import IWrapSpacyMatchers
from app.lib.matchers.simple.simple_validator import SimpleValidator

from tests.helpers.test_nlp import TestNLP


class SimpleValidatorTests(unittest.TestCase):
    def setUp(self):
        self.key = 'test_key'
        self.nlp = TestNLP.get_nlp()


    def test_simple_validator_pass(self):
        sm_wrapper = IWrapSpacyMatchers()
        fake_sm_results: list[tuple[str,int,int]] = [(self.key, 0, 4)]
        sm_wrapper.match = MagicMock(return_value = fake_sm_results)
        sut = SimpleValidator(self.key, self.nlp, sm_wrapper)

        test_sentence = 'the sky is blue'
        doc = self.nlp(test_sentence)
        result = sut.validate(doc)
        self.assertTrue(result)
    

    def test_simple_validator_fail_length(self):
        sm_wrapper = IWrapSpacyMatchers()
        fake_sm_results: list[tuple[str,int,int]] = []
        sm_wrapper.match = MagicMock(return_value = fake_sm_results)
        sut = SimpleValidator(self.key, self.nlp, sm_wrapper)

        test_sentence = 'the sky is blue'
        doc = self.nlp(test_sentence)
        result = sut.validate(doc)
        self.assertFalse(result)


    def test_simple_validator_fail_key(self):
        sm_wrapper = IWrapSpacyMatchers()
        fake_sm_results: list[tuple[str,int,int]] = [(self.key, 0, 4)]
        sm_wrapper.match = MagicMock(return_value = fake_sm_results)
        sut = SimpleValidator('xxxx', self.nlp, sm_wrapper)

        test_sentence = 'the sky is blue'
        doc = self.nlp(test_sentence)
        result = sut.validate(doc)
        self.assertFalse(result)

  
if __name__ == '__main__':
    unittest.main()