import unittest
from unittest.mock import MagicMock
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.symboleo_spec import PNegAtom
from app.src.matchers.interfaces import IValidateMatches
from app.src.matchers.simple.simple_matcher import SimpleMatcher

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

        result: PNegAtom = self.sut.try_match(doc)
        atom_res: PAtomPredicate = result.atom
        res_pred: PredicateFunctionHappens = atom_res.predicate_function
        res_event: VariableEvent = res_pred.event

        self.assertEqual(res_event.variable.name, 'is_blue(sky)')
    

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