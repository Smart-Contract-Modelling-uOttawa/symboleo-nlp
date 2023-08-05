import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.sym_event import VariableEvent, ObligationEvent, ObligationEventName
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass

from app.src.pattern_builder.pattern_unit_fillers.obligation_action_filler import ObligationActionFiller

class ObligationActionFillerTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationActionFiller()

    def test_obligation_action_filler(self):
        pattern_class = EventPatternClass()

        contract = ISymboleoContract()

        input_list = [UserInput(UnitType.OBLIGATION_ACTION, 'violated')]

        result = self.sut.fill(pattern_class, contract, input_list, 0)

        self.assertIsInstance(result, EventPatternClass)
        result: EventPatternClass = result
        self.assertIsNone(result.nl_event)
        self.assertEqual(result.event, ObligationEvent(ObligationEventName.Violated, 'X'))


    def test_obligation_action_filler_exists(self):
        pattern_class = EventPatternClass()
        pattern_class.event = ObligationEvent(ObligationEventName.Discharged, 'test')
        pattern_class.nl_event = CustomEvents.eating_pie()

        contract = ISymboleoContract()

        input_list = [UserInput(UnitType.OBLIGATION_ACTION, 'violated')]

        result = self.sut.fill(pattern_class, contract, input_list, 0)

        self.assertIsInstance(result, EventPatternClass)
        result: EventPatternClass = result
        self.assertTrue(result.nl_event.negation)
        self.assertEqual(result.event, ObligationEvent(ObligationEventName.Violated, 'test'))

if __name__ == '__main__':
    unittest.main()
