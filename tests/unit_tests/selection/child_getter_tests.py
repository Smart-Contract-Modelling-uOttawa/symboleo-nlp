import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

from app.src.selection.child_getters.child_getter import IGetUnitChildren
from app.src.selection.child_node_getter import ChildNodeGetter

class ChildGetterTests(unittest.TestCase):
    def setUp(self):
        self.fake_getter = IGetUnitChildren()
        self.fake_getter.get = MagicMock(return_value = [InputUnit(), InputUnit()])
        self.fake_dict = {
            InputUnit: self.fake_getter
        }

        self.sut = ChildNodeGetter(self.fake_dict)


    def test_child_getter(self):
        contract = ISymboleoContract()
        result = self.sut.get(InputUnit(), contract)

        self.assertEqual(len(result), 2) 


if __name__ == '__main__':
    unittest.main()
