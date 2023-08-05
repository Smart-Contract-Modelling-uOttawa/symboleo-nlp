import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.sym_event import VariableEvent
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass

from app.src.pattern_builder.pattern_unit_fillers.custom_event_filler import CustomEventFiller
from app.src.custom_event_extractor.custom_event_extractor import IExtractCustomEvents

class CustomEventFillerTests(unittest.TestCase):
    def setUp(self):
        self.event_extractor = IExtractCustomEvents()
        self.sut = CustomEventFiller(self.event_extractor)

    def test_custom_event_filler(self):
        mock_event = CustomEvents.eating_pie()
        self.event_extractor.extract = MagicMock(return_value=mock_event)

        pattern_class = EventPatternClass()

        contract = ISymboleoContract()

        input_list = [UserInput(UnitType.DUMMY, 'X')]

        result = self.sut.fill(pattern_class, contract, input_list, 0)

        self.assertIsNone(pattern_class.event)
        self.assertIsNone(pattern_class.nl_event)
        self.assertIsNotNone(result.event)
        self.assertIsNotNone(result.nl_event)

        self.assertIsInstance(result, EventPatternClass)

        result: EventPatternClass = result
        self.assertEqual(result.nl_event, mock_event)
        self.assertEqual(result.event, VariableEvent(mock_event.event_key()))

if __name__ == '__main__':
    unittest.main()
