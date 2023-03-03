from tests.full_grammar.full_grammar_test_spec import FullGrammarTestSpec as Spec
from app.classes.grammar.selected_nodes.all_nodes import *

using_instrument_tests = [
    Spec([
            RootNode('Root',0),
            UsingNode('a', 1),
            InstrumentNode('c', 2, 'a van')
        ],
        'using a van',
        'instrument (str): a van'
    ),
    #...
]
