import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import ContractEvent, ContractEventName
from app.classes.selection.standard_event_node import ContractSubjectNode

from app.src.sym_updaters.contract_subject_node_updater import ContractSubjectNodeUpdater

class ContractActionNodeUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ContractSubjectNodeUpdater()

    def test_updater(self):
        norm = INorm()
        node = ContractSubjectNode()
        value = ContractEventName.Activated
        result = self.sut.update_package(norm, node, value)
        self.assertEqual(type(result.new_value), ContractEvent)
        self.assertEqual(result.new_value.event_name, ContractEventName.Activated)

if __name__ == '__main__':
    unittest.main()
