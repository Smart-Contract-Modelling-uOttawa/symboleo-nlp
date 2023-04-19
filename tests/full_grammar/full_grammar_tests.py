import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.spec.sym_event import VariableEvent
from app.classes.selection.selected_node import SelectedNode
from app.src.grammar.selection import Selection
from app.classes.selection.all_nodes import *
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor

from tests.helpers.sample_norm_lib import SampleNorms

from tests.full_grammar.before_date_tests import before_date_tests
from tests.full_grammar.before_event_tests import before_event_tests
from tests.full_grammar.within_timespan_event_tests import within_timespan_event_tests
from tests.full_grammar.if_event_tests import if_event_tests
from tests.full_grammar.after_event_tests import after_event_tests
from tests.full_grammar.after_date_tests import after_date_tests
from tests.full_grammar.until_event_tests import until_event_tests
from tests.full_grammar.using_instrument_tests import using_instrument_tests

class FullGrammarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.frame_checker = FrameCheckerConstructor.construct()
        self.default_event = VariableEvent('test')
        all_tests = [
            before_date_tests,
            before_event_tests,
            within_timespan_event_tests,
            if_event_tests,
            after_event_tests,
            after_date_tests,
            until_event_tests,
            using_instrument_tests
            #...
        ]
        self.test_suite = sum(all_tests, [])

    @unittest.skip('reorg')
    def test_full_grammar(self):
        for x in self.test_suite:
            selected_nodes: List[SelectedNode] = x.selected_nodes
            exp_nl = x.exp_nl
            exp_sym = x.exp_sym

            selection = Selection.from_nodes(selected_nodes)
            nodes = selection.get_nodes()
            frame = self.frame_checker.get_frame(nodes)
            nl_result = frame.to_text()


            sym_result = selected_nodes[0].to_obj().to_sym()

            self.assertEqual(exp_nl, nl_result)
            self.assertEqual(exp_sym, sym_result)
        

if __name__ == '__main__':
    unittest.main()