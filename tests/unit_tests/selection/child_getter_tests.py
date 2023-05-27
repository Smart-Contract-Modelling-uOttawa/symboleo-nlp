import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.selection.selected_node import SelectedNode

from app.src.child_getters.child_getter import IGetNodeChildren
from app.src.grammar.child_getter import ChildGetter

class ChildGetterTests(unittest.TestCase):
    def setUp(self):
        self.fake_getter = IGetNodeChildren()
        self.fake_getter.get = MagicMock(return_value = [AbstractNode(), AbstractNode()])
        self.fake_dict = {
            AbstractNode: self.fake_getter
        }

        self.sut = ChildGetter(self.fake_dict)


    def test_child_getter(self):
        contract = ISymboleoContract()
        result = self.sut.get(AbstractNode(), SelectedNode(), contract)

        self.assertEqual(len(result), 2) 


if __name__ == '__main__':
    unittest.main()
