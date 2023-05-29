import unittest
from unittest.mock import MagicMock
from app.classes.custom_event.base_event import StandardContractEvent
from app.classes.spec.sym_event import ContractEventName
from app.classes.patterns.pattern import EventPattern
from app.classes.elements.standard_event_elements import *

from app.src.pattern_updaters.contract_action_updater import ContractActionUpdater

from app.classes.template_event.contract_components import ContractVerbs

class ContractActionUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ContractActionUpdater()

    def test_contract_action_updater(self):
        element = ContractActionElement(ContractEventName.Activated)
        pattern = EventPattern()
        self.sut.update(element, pattern)
        
        if isinstance(pattern.event, StandardContractEvent):
            self.assertEqual(pattern.event.action, 'Activated')
        else:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
