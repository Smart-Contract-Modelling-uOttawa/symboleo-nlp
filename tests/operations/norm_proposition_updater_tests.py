import unittest
from unittest.mock import MagicMock
from app.classes.spec.proposition import PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent

from app.src.operations.helpers.norm_proposition_updater import NormPropositionUpdater

from tests.helpers.sample_norm_lib import SampleNorms


class NormPropositionUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = NormPropositionUpdater()


    def test_norm_updater_new(self):
        norm = SampleNorms.get_sample_norm()
        init_sym = norm.to_sym()

        new_atom = PAtomPredicate(
            PredicateFunctionHappens(
                VariableEvent('action2')
            )
        )

        result = self.sut.update(norm, 'trigger', new_atom)

        self.assertEqual(norm.to_sym(), init_sym)
        self.assertNotEqual(result.to_sym(), init_sym)

        self.assertEqual(len(result.trigger.p_ands), 1)
    

    def test_norm_updater_replace(self):
        norm = SampleNorms.get_sample_norm()
        init_sym = norm.to_sym()

        new_atom = PNegAtom(
            PAtomPredicate(
                PredicateFunctionHappens(
                    VariableEvent('action2')
                )
            )
        )

        result = self.sut.update(norm, 'consequent', new_atom)

        self.assertEqual(norm.to_sym(), init_sym)
        self.assertNotEqual(result.to_sym(), init_sym)
        self.assertEqual(len(result.consequent.p_ands), 1)

  
if __name__ == '__main__':
    unittest.main()