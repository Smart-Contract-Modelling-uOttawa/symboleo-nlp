import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.frames.all_frames import *
from app.classes.frames.frame import DummyFrame
from app.classes.tokens.node_type import NodeType
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.all_nodes import *
from app.src.frames.frame_checker import FrameChecker
from app.src.frames.inner_frame_checker import IInnerFrameChecker
from app.src.frames.frame_builder import IBuildFrames 

from app.classes.frames.all_frames import BeforeDateFrame, BeforeEventFrame

class InnerFrameCheckerTests(unittest.TestCase):
    def setUp(self):
        frame_list = [
            DummyFrame(),
            DummyFrame(),
            DummyFrame()
        ]
        self.fake_inner = IInnerFrameChecker()
        self.fake_inner.check_frame = MagicMock(side_effect=[False, True, True])
        self.fake_builder = IBuildFrames()
        fake_full_frame = DummyFrame()
        fake_full_frame.test_value = 'test'
        self.fake_builder.build = MagicMock(side_effect=[
            DummyFrame(),
            fake_full_frame
        ])
        self.sut = FrameChecker(frame_list, self.fake_inner, self.fake_builder)
    

    def test_frame_checker(self):
        node_list: List[SelectedNode] = [SelectedNode('', 0, '')]
        result = self.sut.check_all_frames(node_list)

        self.assertEqual(self.fake_inner.check_frame.call_count, 3)
        self.assertEqual(self.fake_builder.build.call_count, 2)
        self.assertEqual(result[0].to_text(), 'DUMMY: test')
        self.assertEqual(len(result), 1)

    



if __name__ == '__main__':
    unittest.main()
