import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.frames.all_frames import *
from app.classes.frames.frame import DummyFrame
from app.classes.tokens.node_type import NodeType
from app.classes.selection.all_nodes import *
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor
from app.src.frames.frame_checker import FrameChecker
from app.src.frames.inner_frame_checker import IInnerFrameChecker
from app.src.frames.frame_builder import IBuildFrames 

from app.classes.frames.all_frames import BeforeDateFrame, BeforeEventFrame

# Have all the  test cases
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
        BeforeEventFrame
    )
]


class FullFrameCheckerTests(unittest.TestCase):
    def setUp(self):
        self.sut = FrameCheckerConstructor.construct()

    
    def test_frame_checker(self):
        for node_list, exp in test_set:
            result = self.sut._check_all_frames(node_list)
            print(len(result))
    



if __name__ == '__main__':
    unittest.main()
