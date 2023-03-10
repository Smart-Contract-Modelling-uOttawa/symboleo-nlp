import unittest
from unittest.mock import MagicMock
from app.classes.spec.proposition import PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent

from app.src.operations.helpers.negation_extractor import NegationExtractor

from tests.helpers.sample_norm_lib import SampleNorms


class NegationExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = NegationExtractor()


    def test_true(self):
        norm = SampleNorms.get_sample_obligation('test_id', True)
        result = self.sut.extract(norm, 'consequent')
        self.assertTrue(result)
    

    def test_false(self):
        norm = SampleNorms.get_sample_obligation()
        result = self.sut.extract(norm, 'consequent')
        self.assertFalse(result)

  
if __name__ == '__main__':
    unittest.main()