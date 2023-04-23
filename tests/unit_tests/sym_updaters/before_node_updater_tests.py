import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_event import ContractEvent, ContractEventName
from app.classes.selection.before_node import BeforeNode

from app.src.sym_updaters.before_node_updater import BeforeNodeUpdater

from tests.helpers.sample_norm_lib import SampleNorms

class ContractActionNodeUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = BeforeNodeUpdater()

    def test_before_node_updater_event(self):
        norm = SampleNorms.get_sample_norm()
        node = BeforeNode()
        value = VariableEvent('test2')

        result = self.sut.update_package(norm, node, value)

        self.assertEqual(len(result.update_obj.norms), 1)
        target_sym = 'WhappensBeforeE(action, test2)'
        new_norm = result.update_obj.norms[0]
        self.assertTrue(target_sym in new_norm.to_sym())
    
    @unittest.skip('TODO')
    def test_before_node_updater_point(self):
        return

if __name__ == '__main__':
    unittest.main()
