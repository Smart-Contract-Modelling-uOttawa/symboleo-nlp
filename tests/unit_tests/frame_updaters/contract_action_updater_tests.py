import unittest
from unittest.mock import MagicMock
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
        expected_verb = ContractVerbs.contract_verb_dict[ContractEventName.Activated]()
        self.assertEqual(pattern.event.verb, expected_verb)

if __name__ == '__main__':
    unittest.main()
