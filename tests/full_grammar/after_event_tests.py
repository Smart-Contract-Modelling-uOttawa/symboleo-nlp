from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.grammar.selected_nodes.all_nodes import *

after_event_tests = [
    Spec([
            RootNode('Root',0 , None),
            AfterNode('a',1 ,  None),
            EventNode('c', 2, None),
            DomainEventNode('d', 3, None),
            DomainEventNameNode('e', 4, 'payment')
        ],
        'after payment is completed',
        'WhappensBeforeE(payment, test)'
    ),
    #...
]
