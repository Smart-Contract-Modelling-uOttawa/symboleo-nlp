
import unittest
from unittest.mock import MagicMock
from app.classes.events.contract_events.standard_obligation_event import StandardObligationEvent
from app.classes.patterns.pattern import EventPattern
from app.classes.elements.standard_event_elements import *

from app.src.pattern_builder.pattern_updaters.obligation_action_updater import ObligationActionUpdater

class ContractActionUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationActionUpdater()

    def test_obligation_action_updater(self):
        node = ObligationActionElement(ObligationEventName.Violated)
        pattern = EventPattern()
        self.sut.update(node, pattern)

        if isinstance(pattern.event, StandardObligationEvent):
            self.assertEqual(pattern.event.action, 'Violated')
        else:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
