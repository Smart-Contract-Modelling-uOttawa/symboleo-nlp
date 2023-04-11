from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.selection.all_nodes import *

before_date_tests = [
    Spec([
            RootNode('Root',0 , None),
            BeforeNode('a',1 ,  'before'),
            DateNode('c', 2, '2022/02/25')
        ],
        'before 2022/02/25',
        'WhappensBefore(test, 2022/02/25)'
    ),
    #...
]
