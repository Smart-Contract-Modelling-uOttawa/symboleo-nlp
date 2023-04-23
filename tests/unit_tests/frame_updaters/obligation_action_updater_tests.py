import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.classes.frames.frame import EventFrame
from app.classes.selection.standard_event_node import *
from app.classes.custom_event.predicate import Predicate

from app.src.frame_updaters.obligation_action_updater import ObligationActionUpdater

from app.classes.template_event.contract_components import HelperVerbs

class ContractActionUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationActionUpdater()

    def test_obligation_action_updater(self):
        node = ObligationActionNode(ObligationEventName.Violated)
        frame = EventFrame()
        self.sut.update_frame(node, frame)
        
        expected_pred = Predicate('violated')
        expected_verb = HelperVerbs.verb_is()
        
        self.assertEqual(frame.event.predicate, expected_pred)
        self.assertEqual(frame.event.verb, expected_verb)

if __name__ == '__main__':
    unittest.main()
