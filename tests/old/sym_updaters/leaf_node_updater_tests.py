import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_event import VariableEvent
from app.classes.elements.element import DummyNode

from app.src.sym_updaters.leaf_node_updater import LeafNodeUpdater

from tests.helpers.sample_norm_lib import SampleNorms

class IfNodeUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = LeafNodeUpdater()

    def test_before_node_updater_event(self):
        norm = SampleNorms.get_sample_norm()
        node = DummyNode('test_node')
        value = VariableEvent('test')

        result = self.sut.update_package(norm, node, value)

        self.assertEqual(result.new_value, 'test_node')
    

if __name__ == '__main__':
    unittest.main()
