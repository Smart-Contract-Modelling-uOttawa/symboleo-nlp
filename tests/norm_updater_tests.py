import unittest
from unittest.mock import MagicMock
from app.classes.spec.atoms import SituationProposition
from app.classes.spec.helpers import Interval, Situation
from app.classes.spec.symboleo_spec import NegAtom

from app.lib.norm_updater import NormUpdater

from tests.helpers.sample_norm_lib import SampleNorms


class NormUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = NormUpdater()


    def test_norm_updater_new(self):
        norm = SampleNorms.get_sample_norm()
        init_sym = norm.to_sym()

        new_atom = NegAtom(
            SituationProposition(
                Situation('is_blue(sky)'),
                Interval('X')
            )
        )

        result = self.sut.update(norm, 'trigger', new_atom)

        self.assertEqual(norm.to_sym(), init_sym)
        self.assertNotEqual(result.to_sym(), init_sym)
        self.assertEqual(len(result.trigger.junctions), 1)
        self.assertEqual(len(result.trigger.junctions[0].negAtoms), 1)
    

    def test_norm_updater_append(self):
        norm = SampleNorms.get_sample_norm()
        init_sym = norm.to_sym()

        new_atom = NegAtom(
            SituationProposition(
                Situation('is_blue(sky)'),
                Interval('X')
            )
        )

        result = self.sut.update(norm, 'consequent', new_atom)

        self.assertEqual(norm.to_sym(), init_sym)
        self.assertNotEqual(result.to_sym(), init_sym)
        self.assertEqual(len(result.consequent.junctions[0].negAtoms), 2)

  
if __name__ == '__main__':
    unittest.main()