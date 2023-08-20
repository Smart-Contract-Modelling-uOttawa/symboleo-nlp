import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass

from app.src.pattern_builder.pattern_unit_fillers.contract_action_filler import ContractActionFiller, ILemmatize

class ContractActionFillerTests(unittest.TestCase):
    def setUp(self):
        self.lemmatizer = ILemmatize()
        self.lemmatizer.lemmatize = MagicMock(return_value='terminate')
        self.sut = ContractActionFiller(self.lemmatizer)

    def test_contract_action_filler(self):
        pattern_class = EventPatternClass()

        contract = ISymboleoContract()

        input_list = [UserInput(UnitType.CONTRACT_ACTION, 'terminated')]

        result = self.sut.fill(pattern_class, contract, input_list, 0)

        self.assertIsInstance(result, EventPatternClass)
        result: EventPatternClass = result
        self.assertEqual(result.event, ContractEvent(ContractEventName.Terminated))


if __name__ == '__main__':
    unittest.main()
