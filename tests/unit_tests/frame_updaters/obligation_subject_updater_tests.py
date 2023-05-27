import unittest
from unittest.mock import MagicMock
from app.classes.patterns.pattern import EventPattern
from app.classes.selection.standard_event_node import *
from app.classes.template_event.obligation_subject import ObligationSubject
from app.classes.custom_event.noun_phrase import NounPhrase

from app.src.pattern_updaters.obligation_subject_updater import ObligationSubjectUpdater

from app.classes.template_event.contract_components import ContractNouns

class ObligationSubjectUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationSubjectUpdater()

    def test_obligation_subject_updater(self):
        val = ObligationSubject('test')
        node = ObligationSubjectNode(val)
        pattern = EventPattern()
        self.sut.update(node, pattern)

        expected_np = NounPhrase('test obligation', 'test obligation')

        self.assertEqual(pattern.event.subj, expected_np)

if __name__ == '__main__':
    unittest.main()
