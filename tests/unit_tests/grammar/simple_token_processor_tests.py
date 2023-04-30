import unittest
from unittest.mock import MagicMock
from app.classes.tokens.abstract_node import AbstractNode, DummyNode
from app.classes.tokens.all_nodes import *
from app.classes.tokens.final_node import FinalNode as FinalToken
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.standard_event_node import CommonEventNode
from app.classes.selection.final_node import FinalNode

from app.classes.operations.user_input import UserInput

from app.classes.template_event.common_event_dict import COMMON_EVENT_DICT
from app.classes.template_event.common_event import CommonEvent

from app.src.grammar.grammar_selector2 import GrammarSelector

from app.src.grammar.simple_token_processor import SimpleTokenProcessor
from app.src.grammar.common_event_handler import IHandleCommonEvents
from app.src.grammar.token_selector_set import ISelectTokenFromSet
from app.src.child_getters.child_getter import IGetNodeChildren

from app.src.grammar.value_getter import IGetValues
from app.src.grammar.input_converter import IConvertInput

class TokenProcessorTests(unittest.TestCase):
    def setUp(self):

        self.value_getter = IGetValues()

        self.input_converter = IConvertInput()

        self.sut = SimpleTokenProcessor(self.value_getter, self.input_converter)
    

    def test_token_processor_common(self):
        self.value_getter.get = MagicMock(return_value=UserInput(NodeType.DUMMY, 'test'))
        self.input_converter.convert = MagicMock(return_value=[SelectedNode('test_value')])

        token = AbstractNode()
        result = self.sut.process(token, None)

        self.assertEqual(result.value, 'test_value')
        self.assertEqual(self.input_converter.convert.call_count, 1)
        self.assertEqual(self.value_getter.get.call_count, 1)
    


if __name__ == '__main__':
    unittest.main()
