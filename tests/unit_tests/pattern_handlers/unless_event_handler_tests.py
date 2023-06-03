import unittest
from unittest.mock import MagicMock

from app.classes.patterns.unless_event import UnlessEvent
from app.classes.spec.norm import Power, Obligation
from app.classes.spec.proposition import PNegAtom
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.predicate_function import PredicateFunctionHappens

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.unless_event_handler import UnlessEventHandler

from tests.helpers.test_objects import CustomEvents

class UnlessEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = UnlessEventHandler()


    # Power to Suspend Norm + UNLESS EVENT => new power to resume
    def test_resume_norm(self):
        pattern = UnlessEvent()
        pattern.event = CustomEvents.eating_pie()
        norm = Power(
            'test',
            None,
            'a',
            'b',
            PropMaker.make_default(),
            PFObligation(PFObligationName.Suspended, 'test_ob')
        )
        handle_obj = HandleObject(norm)
        result = self.sut.handle(pattern, handle_obj)

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Power)
        self.assertEqual(result[0].id, 'pow_resume_test_ob')
    
    # (NOT OB) + UNLESS EVENT => power to suspend
    def test_suspend_norm(self):
        pattern = UnlessEvent()
        pattern.event = CustomEvents.eating_pie()
        norm = Obligation(
            'test_ob',
            None,
            'a',
            'b',
            PropMaker.make_default(),
            PropMaker.make(
                PredicateFunctionHappens(CustomEvents.paying()),
                negation=True
            )
        )
        handle_obj = HandleObject(norm)
        result = self.sut.handle(pattern, handle_obj)

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Power)
        self.assertEqual(result[0].id, 'pow_suspend_test_ob')

    # (FALSE -> NOT OB) + UNLESS EVENT => new trigger
    def test_switch_false_trigger(self):
        pattern = UnlessEvent()
        pattern.event = CustomEvents.eating_pie()
        norm = Obligation(
            'test_ob',
            PropMaker.make_default(False),
            'a',
            'b',
            PropMaker.make_default(),
            PropMaker.make(
                PredicateFunctionHappens(CustomEvents.paying()),
                negation=True
            )
        )
        handle_obj = HandleObject(norm)
        result = self.sut.handle(pattern, handle_obj)

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Obligation)
        self.assertEqual(result[0].trigger.to_sym(), 'Happens(evt_eat_noisily)')
        self.assertEqual(result[0].id, 'test_ob')


if __name__ == '__main__':
    unittest.main()