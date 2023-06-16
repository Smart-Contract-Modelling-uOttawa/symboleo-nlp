import unittest
from unittest.mock import MagicMock

from app.classes.units.unit_type import UnitType
from app.classes.spec.symboleo_contract import ISymboleoContract

from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

from app.src.selection.element_list_selector import ElementListSelector
from app.src.selection.child_node_getter import IGetNodeChildren
from app.src.selection.token_selector_set import ISelectNode
from app.src.selection.input_value_getter import IGetInputValues
from app.src.selection.element_extractor import IExtractElements

class ElementListSelectorTests(unittest.TestCase):
    def setUp(self):
        self.fake_child_getter = IGetNodeChildren()
        self.fake_child_getter.get = MagicMock(side_effect = [
            [InputUnit(), InputUnit()],
            [InputUnit()],
            [],
        ])
        
        self.fake_child_selector = ISelectNode()
        self.fake_child_selector.select = MagicMock(return_value = InputUnit())

        self.fake_input_value_getter = IGetInputValues()
        self.fake_input_value_getter.get = MagicMock(side_effect = [
            'a',
            'b'
        ])

        self.fake_element_extractor = IExtractElements()
        self.fake_element_extractor.extract_single = MagicMock(side_effect = [
            Element('test1'),
            Element('test2')
        ])

        self.sut = ElementListSelector(
            self.fake_child_getter,
            self.fake_child_selector,
            self.fake_input_value_getter,
            self.fake_element_extractor)
    

    @unittest.skip('fix')
    def test_element_list_selector(self):
        contract = ISymboleoContract()
        result = self.sut.select(contract)

        self.assertEqual(len(result), 4) # Add one for root and final
        self.assertEqual(result[1].value, 'test1')
        self.assertEqual(result[2].value, 'test2')
        self.assertEqual(result[3].unit_type, UnitType.FINAL_NODE)
        self.assertEqual(self.fake_child_getter.get.call_count, 3)
        self.assertEqual(self.fake_child_selector.select.call_count, 1)
        self.assertEqual(self.fake_input_value_getter.get.call_count, 2)
        self.assertEqual(self.fake_element_extractor.extract_single.call_count, 2)


if __name__ == '__main__':
    unittest.main()
