import unittest
from unittest.mock import MagicMock

from tests_new.src.grammar.test_suite.test_selection_simulator import SelectionSimulator

from app.src.template_getter import get_template
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.grammar.grammar_generator import GrammarGenerator
from app.classes.spec.sym_event import VariableEvent


# Generate the grammar and simulate a selection from the nodes in the tree
class GrammarGeneratorTests(unittest.TestCase):
    def setUp(self):
        contract_template = get_template('meat_sale')
        gg = GrammarGenerator()
        self.root_node = gg.generate(contract_template)
        self.simulator = SelectionSimulator()

    # Move this into a separate function
    def test_simulated_selection(self):
        # Can turn this into a test set with many different values
        iv_list = [
            ('Before', 'before'),
            ('Date', '2020-02-23')
        ] # List of (node_id, value)

        expected_text = 'before 2020-02-23'
        expected_sym = 'WhappensBefore(test, 2020-02-23)'

        text_result, sym_result = self.helper_func(iv_list)

        self.assertEqual(text_result, expected_text)
        self.assertEqual(sym_result, expected_sym)
    

    def helper_func(self, iv_list):
        selection = self.simulator.simulate(self.root_node, iv_list)
        text_result = selection.try_frames()[0]
        sym_result = selection.to_obj(VariableEvent('test'))
        return text_result, sym_result

        
if __name__ == '__main__':
    unittest.main()