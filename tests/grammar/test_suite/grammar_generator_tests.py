import unittest
from unittest.mock import MagicMock

from app.src.template_getter import get_template
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.grammar.grammar_generator import GrammarGenerator


# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class GrammarGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.gg = GrammarGenerator()

    def test_grammar_generator(self):
        contract_template = get_template('meat_sale')

        root_node = self.gg.generate(contract_template)

        self.assertEqual(root_node.id, 'ROOT')
        self.assertEqual(root_node.node_type, NodeType.ROOT)


if __name__ == '__main__':
    unittest.main()