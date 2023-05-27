import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.classes.patterns.pattern import EventPattern
from app.classes.selection.standard_event_node import *
from app.classes.custom_event.predicate import Predicate

from app.src.pattern_updaters.obligation_action_updater import ObligationActionUpdater

from app.classes.template_event.contract_components import HelperVerbs

class ContractActionUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationActionUpdater()

    def test_obligation_action_updater(self):
        node = ObligationActionNode(ObligationEventName.Violated)
        pattern = EventPattern()
        self.sut.update(node, pattern)
        
        expected_pred = Predicate('violated')
        expected_verb = HelperVerbs.verb_is()
        
        self.assertEqual(pattern.event.predicate, expected_pred)
        self.assertEqual(pattern.event.verb, expected_verb)

if __name__ == '__main__':
    unittest.main()
