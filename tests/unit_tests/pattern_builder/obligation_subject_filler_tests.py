import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents
from tests.helpers.test_contract import get_test_contract

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.sym_event import VariableEvent, ObligationEvent, ObligationEventName
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass

from app.src.pattern_builder.pattern_unit_fillers.obligation_subject_filler import ObligationSubjectFiller
from app.src.custom_event_extractor.custom_event_extractor import IExtractCustomEvents

class ObligationSubjectFillerTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationSubjectFiller()

    def test_obligation_subject_filler(self):
        pattern_class = EventPatternClass()

        mock_event = CustomEvents.eating_pie()

        contract = get_test_contract()
        contract.try_get_event = MagicMock(return_value=mock_event)

        input_list = [UserInput(UnitType.OBLIGATION_SUBJECT, 'obligations.test_obligation')]

        result = self.sut.fill(pattern_class, contract, input_list, 0)

        self.assertIsInstance(result, EventPatternClass)
        result: EventPatternClass = result
        self.assertEqual(result.nl_event, mock_event)
        self.assertEqual(result.event, ObligationEvent(ObligationEventName.Activated, 'test_obligation'))
        self.assertEqual(contract.try_get_event.call_count, 1)


    def test_obligation_subject_filler_exists(self):
        pattern_class = EventPatternClass()

        mock_event = CustomEvents.eating_pie()

        contract = get_test_contract()
        contract.try_get_event = MagicMock(return_value=mock_event)

        pattern_class.event = ObligationEvent(ObligationEventName.Discharged, 'test')
        pattern_class.nl_event = CustomEvents.eating_pie()

        input_list = [UserInput(UnitType.OBLIGATION_SUBJECT, 'obligations.test_obligation')]

        result = self.sut.fill(pattern_class, contract, input_list, 0)

        self.assertIsInstance(result, EventPatternClass)
        result: EventPatternClass = result
        self.assertEqual(result.event, ObligationEvent(ObligationEventName.Discharged, 'test_obligation'))
        
        self.assertEqual(contract.try_get_event.call_count, 1)
        self.assertEqual(result.nl_event, mock_event)

if __name__ == '__main__':
    unittest.main()
