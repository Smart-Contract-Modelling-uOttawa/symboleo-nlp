import unittest
from unittest.mock import MagicMock

from app.classes.frames.all_frames import *
from app.classes.tokens.node_type import NodeType
from app.classes.selection.all_nodes import *
from app.src.frame_updaters.inner_frame_checker import InnerFrameChecker

class InnerFrameCheckerTests(unittest.TestCase):
    def setUp(self):
        self.sut = InnerFrameChecker()
    
    def test_inner_frame_checker1(self):
        node_list = [RootNode(), BeforeNode(), EventNode(), CustomEventNode()]
        frame_pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.EVENT]

        result = self.sut.check_frame(node_list, frame_pattern)
        self.assertTrue(result)
    
    def test_inner_frame_checker2(self):
        node_list = [RootNode(), BeforeNode()]
        frame_pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.EVENT]

        result = self.sut.check_frame(node_list, frame_pattern)
        self.assertFalse(result)

    def test_inner_frame_checker1(self):
        node_list = [RootNode(), BeforeNode(), EventNode(), CustomEventNode()]
        frame_pattern = [NodeType.ROOT, NodeType.AFTER, NodeType.EVENT]

        result = self.sut.check_frame(node_list, frame_pattern)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
