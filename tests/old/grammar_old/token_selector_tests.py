import unittest
from unittest.mock import MagicMock
from app.classes.units.input_unit import InputUnit, DummyNode
from app.classes.units.final_unit import FinalNode as FinalToken

from app.src.grammar.token_selector import TokenSelector
from app.src.grammar.token_selector_set import ISelectTokenFromSet
from app.src.child_getters.child_getter import IGetNodeChildren

class TokenSelectorTests(unittest.TestCase):
    def setUp(self):

        self.fake_child_getter = IGetNodeChildren()

        self.fake_dict = {
            InputUnit: self.fake_child_getter
        }

        self.inner_selector = ISelectTokenFromSet()
        self.inner_selector.select = MagicMock(return_value = DummyNode())

        self.sut = TokenSelector(self.fake_dict, self.inner_selector)
    

    def test_token_selector(self):
        self.fake_child_getter.get = MagicMock(return_value=[DummyNode()])
        
        token = InputUnit()
        result = self.sut.select(token, None, None)

        self.assertEqual(result.prompt, 'dummy')
        self.assertEqual(self.fake_child_getter.get.call_count, 1)
        self.assertEqual(self.inner_selector.select.call_count, 1)
    
    def test_token_selector_empty(self):
        self.fake_child_getter.get = MagicMock(return_value=[])
        
        token = InputUnit()
        result = self.sut.select(token, None, None)

        self.assertEqual(type(result), FinalToken)
        self.assertEqual(self.fake_child_getter.get.call_count, 1)
        self.assertEqual(self.inner_selector.select.call_count, 0)


if __name__ == '__main__':
    unittest.main()
