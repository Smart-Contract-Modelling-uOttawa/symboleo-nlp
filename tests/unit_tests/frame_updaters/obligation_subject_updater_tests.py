import unittest
from unittest.mock import MagicMock
from app.classes.patterns.pattern import EventPattern
from app.classes.custom_event.base_event import StandardObligationEvent
from app.classes.elements.standard_event_elements import *
from app.classes.template_event.obligation_subject import ObligationSubject
from app.classes.custom_event.noun_phrase import NounPhrase

from app.src.pattern_updaters.obligation_subject_updater import ObligationSubjectUpdater

from app.classes.template_event.contract_components import ContractNouns

class ObligationSubjectUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationSubjectUpdater()

    def test_obligation_subject_updater(self):
        val = ObligationSubject('test')
        node = ObligationSubjectElement(val)
        pattern = EventPattern()
        self.sut.update(node, pattern)

        if isinstance(pattern.event, StandardObligationEvent):
            self.assertEqual(pattern.event.ob_var, 'test')
        else:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
