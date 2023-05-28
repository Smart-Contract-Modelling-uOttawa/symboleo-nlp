import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import INorm
from app.classes.template_event.obligation_subject import ObligationSubject
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName
from app.classes.elements.standard_event_elements import ObligationSubjectNode

from app.src.sym_updaters.obligation_subject_node_updater import ObligationSubjectNodeUpdater

class ObligationSubjectNodeUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationSubjectNodeUpdater()

    def test_updater(self):
        norm = INorm()
        ob_subj = ObligationSubject('test')
        node = ObligationSubjectNode(ob_subj)
        value = ObligationEventName.Violated
        result = self.sut.update_package(norm, node, value)
        self.assertEqual(type(result.new_value), ObligationEvent)

if __name__ == '__main__':
    unittest.main()
