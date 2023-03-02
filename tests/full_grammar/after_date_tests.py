from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.grammar.selected_nodes.all_nodes import *

after_date_tests = [
    Spec([
            RootNode('Root',0 , None),
            AfterNode('a',1 ),
            DateNode('c', 2, '2022/02/25')
        ],
        'after 2022/02/25',
        'HappensAfter(test, 2022/02/25)'
    ),
    #...
]
