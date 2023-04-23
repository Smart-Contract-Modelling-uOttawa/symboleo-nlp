import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_event import VariableEvent
from app.classes.selection.before_node import BeforeNode

from app.src.sym_updaters.if_node_updater import IfNodeUpdater

from tests.helpers.sample_norm_lib import SampleNorms

class IfNodeUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = IfNodeUpdater()

    def test_before_node_updater_event(self):
        norm = SampleNorms.get_sample_norm()
        node = BeforeNode()
        value = VariableEvent('test')

        result = self.sut.update_package(norm, node, value)

        self.assertEqual(len(result.update_obj.norms), 1)
        target_sym = 'Happens(test) ->'
        new_norm = result.update_obj.norms[0]
        self.assertTrue(target_sym in new_norm.to_sym())
    

if __name__ == '__main__':
    unittest.main()
