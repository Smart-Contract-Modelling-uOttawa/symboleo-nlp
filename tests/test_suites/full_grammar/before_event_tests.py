from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.selection.all_nodes import *

before_event_tests = [
    Spec([
            RootNode('Root',0 , None),
            BeforeNode('a',1 ,  'before'),
            EventNode('c', 2, None),
            DomainEventNode('d', 3, None),
            DomainEventNameNode('e', 4, 'payment')
        ],
        'before payment is completed',
        'WhappensBeforeE(test, payment)'
    ),
    #...
]
