from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.grammar.selected_nodes.all_nodes import *

within_tests = [
    Spec([
            RootNode('Root', 0),
            WithinNode('a', 1, 'within'),
            TimespanNode('b', 2, '3 days'),
            EventNode('c', 3, None),
            ObligationEventNode('d', 4, None),
            ObligationEventVarNode('e', 5, 'delivery'),
            ObligationEventActionNode('f', 6,'suspended')
        ],
        'within 3 days of the delivery obligation being suspended',
        'WhappensBefore(test, Date.add(suspended(obligations.delivery), 3, days))'
    ),
    Spec([
            RootNode('Root', 0),
            WithinNode('a', 1, 'within'),
            TimespanNode('b', 2, '2 weeks'),
            EventNode('c', 3, None),
            ContractEventNode('d', 4, None),
            ContractEventActionNode('e', 5, 'terminated')
        ],
        'within 2 weeks of the contract being terminated',
        'WhappensBefore(test, Date.add(terminated(self), 2, weeks))'
    ),
    ###...
]
