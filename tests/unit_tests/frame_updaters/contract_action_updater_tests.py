import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.classes.frames.frame import EventFrame
from app.classes.selection.standard_event_node import *

from app.src.frame_updaters.contract_action import ContractActionUpdater

from app.classes.template_event.contract_components import ContractVerbs

class ContractActionUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ContractActionUpdater()

    def test_contract_action_updater(self):
        node = ContractActionNode(ContractEventName.Activated)
        frame = EventFrame()
        self.sut.update_frame(node, frame)
        expected_verb = ContractVerbs.contract_verb_dict[ContractEventName.Activated]()
        self.assertEqual(frame.event.verb, expected_verb)

if __name__ == '__main__':
    unittest.main()
