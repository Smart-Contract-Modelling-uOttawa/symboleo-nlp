import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import ContractEventName
from app.classes.selection.standard_event_node import ContractActionNode

from app.src.sym_updaters.contract_action_node_updater import ContractActionNodeUpdater


class ContractActionNodeUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ContractActionNodeUpdater()

    def test_updater(self):
        norm = INorm()
        node = ContractActionNode(ContractEventName.Terminated)
        result = self.sut.update_package(norm, node, None)
        self.assertEqual(result.new_value, ContractEventName.Terminated)

if __name__ == '__main__':
    unittest.main()
