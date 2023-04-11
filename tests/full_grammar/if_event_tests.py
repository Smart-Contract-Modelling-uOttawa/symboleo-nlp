from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.selection.all_nodes import *

if_event_tests = [
    Spec([
            RootNode('Root',0 , None),
            IfNode('a', 1),
            EventNode('c', 2, None),
            DomainEventNode('d', 3, None),
            DomainEventNameNode('e', 4, 'payment')
        ],
        'if payment has been completed',
        'Happens(payment)'
    ),
    Spec([
            RootNode('Root',0 , None),
            IfNode('a', 1),
            EventNode('c', 2, None),
            ObligationEventNode('d', 3, None),
            ObligationEventVarNode('e', 4, 'delivery'),
            ObligationEventActionNode('f', 5, 'suspended'),
        ],
        'if the delivery obligation has been suspended',
        'Happens(Suspended(obligations.delivery))'
    ),
    #...
]
