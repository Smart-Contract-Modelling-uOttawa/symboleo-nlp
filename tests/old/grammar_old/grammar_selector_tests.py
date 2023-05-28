import unittest
from unittest.mock import MagicMock
from app.classes.units.input_unit import InputUnit
from app.classes.units.final_unit import FinalNode as FinalToken
from app.classes.elements.element import Element
from app.classes.elements.final_node import FinalNode

from app.src.grammar.grammar_selector2 import GrammarSelector
from app.src.grammar.token_selector import ISelectToken
from app.src.grammar.token_processor import IProcessToken

class GrammarSelectorTests(unittest.TestCase):
    def setUp(self):
        self.token_selector = ISelectToken()
        self.token_selector.select = MagicMock(side_effect = [InputUnit(), FinalToken()])
        
        self.token_processor = IProcessToken()
        self.token_processor.process = MagicMock(side_effect = [
            Element('test1'),
            FinalNode('test2')
        ])

        self.sut = GrammarSelector(self.token_selector, self.token_processor)
    

    def test_grammar_selector(self):
        result = self.sut.select(None)

        self.assertEqual(len(result), 3) # Add one for root
        self.assertEqual(result[1].value, 'test1')
        self.assertEqual(self.token_selector.select.call_count, 2)
        self.assertEqual(self.token_processor.process.call_count, 2)


if __name__ == '__main__':
    unittest.main()
