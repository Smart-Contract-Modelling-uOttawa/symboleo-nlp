import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.frames.all_frames import *
from app.classes.tokens.node_type import NodeType
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.all_nodes import *
from app.src.frames.inner_frame_checker import InnerFrameChecker

test_set = [
    (
        [
            RootNode(),
            BeforeNode(),
            EventNode(),
            NewEventNode(),
            SubjectNode('Bob'),
            VerbNode('eats'),
            DobjNode('Apple pie'),
            AdverbNode('noisily'),
            PrepNode('with mary')
        ],
        BeforeEventFrame(),
        True
    ),
    (
        [
            RootNode(),
            BeforeNode(),
        ],
        BeforeEventFrame(),
        False
    ),
    (
        [
            RootNode(),
            BeforeNode(),
            EventNode()
        ],
        BeforeEventFrame(),
        True
    ),
    (
        [
            BeforeNode(),
            EventNode(),
        ],
        BeforeEventFrame(),
        False
    ),
    (
        [
            RootNode(),
            WithinNode(),
            TimespanNode(),
            EventNode(),
            NewEventNode()
        ],
        WithinTimespanEventFrame(),
        True
    ),
    #...
]

class InnerFrameCheckerTests(unittest.TestCase):
    def setUp(self):
        self.sut = InnerFrameChecker()
    
    def test_inner_frame_checker(self):
        for node_list, frame, exp in test_set:
            result = self.sut.check_frame(node_list, frame.pattern)
            self.assertEqual(result, exp)


if __name__ == '__main__':
    unittest.main()
