from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.grammar.selected_nodes.all_nodes import *

before_date_tests = [
    Spec([
            RootNode('Root',0 , None),
            BeforeNode('a',1 ,  'before'),
            TimepointNode('c', 2, 'test2.dueDate')
        ],
        'before test2.dueDate',
        'WhappensBefore(test, test2.dueDate)'
    ),
    #...
]
