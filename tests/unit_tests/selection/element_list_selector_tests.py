import unittest
from unittest.mock import MagicMock

from app.classes.units.unit_type import UnitType
from app.classes.spec.symboleo_contract import ISymboleoContract

from app.classes.units.input_unit import InputUnit
from app.classes.units.final_node import FinalNode as FinalToken
from app.classes.elements.element import Element
from app.classes.elements.final_node import FinalNode

from app.src.grammar.element_list_selector import ElementListSelector
from app.src.grammar.child_getter import IGetChildren
from app.src.grammar.token_selector_set import ISelectTokenFromSet
from app.src.grammar.value_getter import IGetValues
from app.src.grammar.input_converter import IConvertInput

class ElementListSelectorTests(unittest.TestCase):
    def setUp(self):
        self.fake_child_getter = IGetChildren()
        self.fake_child_getter.get = MagicMock(side_effect = [
            [InputUnit(), InputUnit()],
            [InputUnit()],
            [],
        ])
        
        self.fake_child_selector = ISelectTokenFromSet()
        self.fake_child_selector.select = MagicMock(return_value = InputUnit())

        self.fake_input_value_getter = IGetValues()
        self.fake_input_value_getter.get = MagicMock(side_effect = [
            'a',
            'b'
        ])

        self.fake_element_extractor = IConvertInput()
        self.fake_element_extractor.convert = MagicMock(side_effect = [
            [Element('test1')],
            [Element('test2')]
        ])

        self.sut = ElementListSelector(
            self.fake_child_getter,
            self.fake_child_selector,
            self.fake_input_value_getter,
            self.fake_element_extractor)
    

    def test_element_list_selector(self):
        contract = ISymboleoContract()
        result = self.sut.select(contract)

        self.assertEqual(len(result), 4) # Add one for root and final
        self.assertEqual(result[1].value, 'test1')
        self.assertEqual(result[2].value, 'test2')
        self.assertEqual(result[3].node_type, UnitType.FINAL_NODE)
        self.assertEqual(self.fake_child_getter.get.call_count, 3)
        self.assertEqual(self.fake_child_selector.select.call_count, 1)
        self.assertEqual(self.fake_input_value_getter.get.call_count, 2)
        self.assertEqual(self.fake_element_extractor.convert.call_count, 2)


if __name__ == '__main__':
    unittest.main()
