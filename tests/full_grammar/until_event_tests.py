from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.selection.all_nodes import *

until_event_tests = [
    Spec([
            RootNode('Root',0 , None),
            UntilNode('a', 1),
            EventNode('c', 2, None),
            DomainEventNode('d', 3, None),
            DomainEventNameNode('e', 4, 'payment')
        ],
        'until payment has been completed',
        'pow_suspend_test_id: Happens(payment) -> Power(buyer, seller, true, Suspended(obligations.test_id));'
    ),
]
