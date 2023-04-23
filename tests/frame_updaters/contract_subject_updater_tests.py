import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.classes.frames.frame import EventFrame
from app.classes.selection.standard_event_node import *

from app.src.frame_updaters.contract_subject import ContractSubjectUpdater

from app.classes.template_event.contract_components import ContractNouns

class ContractSubjectUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ContractSubjectUpdater()

    def test_contract_subject_updater(self):
        node = ContractSubjectNode()
        frame = EventFrame()
        self.sut.update_frame(node, frame)
        expected_np = ContractNouns.contract()
        self.assertEqual(frame.event.subj, expected_np)

if __name__ == '__main__':
    unittest.main()
