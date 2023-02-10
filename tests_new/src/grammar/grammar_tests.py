import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.generator.grammar_selector import GrammarSelector

class GrammarTests(unittest.TestCase):
    def setUp(self):
        f = 0

    def test_grammar1(self):
        # Choose a set of nodes/values and verify NL and symboleo are expected
        selected_nodes: List[SelectedNode] = [
            RootNode('Root', None),
            WithinNode('a', None, 'within'),
            TimespanNode('b', None, '3 days'),
            EventNode('c', None, None),
            ObligationEventNode('d', None, None),
            ObligationEventVarNode('e', None, 'delivery'),
            ObligationEventActionNode('f', None,'suspended')
        ]
        SelectedNode.organize_list(selected_nodes)

        nl_result = GrammarSelector
        sym_result = selected_nodes[0].to_obj().to_sym()

        exp_nl = 'within 3 days of the delivery obligation being suspended'
        exp_sym = 'WhappensBefore(test, Date.add(suspended(obligations.delivery), 3, days))'

        self.assertEqual(exp_nl, nl_result)
        self.assertEqual(exp_sym, sym_result)
        
    
    def test_grammar2(self):
        # Choose a set of nodes/values and verify NL and symboleo are expected
        selected_nodes: List[SelectedNode] = [
            RootNode('Root', None),
            WithinNode('a', None, 'within'),
            TimespanNode('b', None, '2 weeks'),
            EventNode('c', None, None),
            ContractEventNode('d', None, None),
            ContractEventActionNode('e', None, 'termination')
        ]
        SelectedNode.organize_list(selected_nodes)

        nl_result = GrammarSelector._get_full_text(selected_nodes)
        sym_result = selected_nodes[0].to_obj().to_sym()

        exp_nl = 'within 2 weeks of contract termination'
        exp_sym = 'WhappensBefore(test, Date.add(suspended(obligations.delivery), 3, days))'

        self.assertEqual(exp_nl, nl_result)
        self.assertEqual(exp_sym, sym_result)
        
    
    def test_grammar3(self):
        # Choose a set of nodes/values and verify NL and symboleo are expected
        selected_nodes: List[SelectedNode] = [
            RootNode('Root', None),
            BeforeNode('a', None, 'before'),
            EventNode('c', None, None),
            DomainEventNode('d', None, None),
            DomainEventNameNode('e', None, 'payment')
        ]
        SelectedNode.organize_list(selected_nodes)

        nl_result = GrammarSelector._get_full_text(selected_nodes)
        sym_result = selected_nodes[0].to_obj().to_sym()

        exp_nl = 'before payment is completed'
        exp_sym = 'WhappensBefore(test, Date.add(suspended(obligations.delivery), 3, days))'

        self.assertEqual(exp_nl, nl_result)
        self.assertEqual(exp_sym, sym_result)
        


if __name__ == '__main__':
    unittest.main()