import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.classes.patterns.pattern import EventPattern
from app.classes.elements.standard_event_elements import *

from app.src.pattern_updaters.contract_subject_updater import ContractSubjectUpdater

from app.classes.template_event.contract_components import ContractNouns

class ContractSubjectUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ContractSubjectUpdater()

    def test_contract_subject_updater(self):
        element = ContractSubjectElement()
        pattern = EventPattern()
        self.sut.update(element, pattern)
        expected_np = ContractNouns.contract()
        self.assertEqual(pattern.event.subj, expected_np)

if __name__ == '__main__':
    unittest.main()
