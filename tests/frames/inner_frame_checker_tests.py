import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.frames.all_frames import *
from app.classes.tokens.node_type import NodeType
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.all_nodes import *
from app.src.frames.inner_frame_checker import InnerFrameChecker

class InnerFrameCheckerTests(unittest.TestCase):
    def setUp(self):
        self.sut = InnerFrameChecker()
    

    def test_inner_frame_checker_true1(self):
        node_list: List[SelectedNode] = [
            WithinNode('a', 0),
            TimespanNode('b', 1),
            EventNode('c', 2),
            BeforeNode('d', 3),
        ]
        pattern: List[NodeType] = [NodeType.WITHIN, NodeType.TIMESPAN, NodeType.EVENT]
        result = self.sut.check_frame(node_list, pattern)
        self.assertTrue(result)
    

    def test_inner_frame_checker_true2(self):
        node_list: List[SelectedNode] = [
            WithinNode('a', 0),
            TimespanNode('b', 1),
            EventNode('c', 2),
            BeforeNode('d', 3),
        ]
        pattern: List[NodeType] = [NodeType.TIMESPAN, NodeType.EVENT, NodeType.BEFORE]
        result = self.sut.check_frame(node_list, pattern)
        self.assertTrue(result)
    

    def test_inner_frame_checker_false(self):
        node_list: List[SelectedNode] = [
            BeforeNode('a', 0),
            TimespanNode('b', 1),
            EventNode('c', 2)
        ]
        pattern: List[NodeType] = [NodeType.WITHIN, NodeType.TIMESPAN, NodeType.EVENT]
        result = self.sut.check_frame(node_list, pattern)
        self.assertFalse(result)
    

    def test_inner_frame_checker_default(self):
        node_list: List[SelectedNode] = [
            WithinNode('a', 0),
            TimespanNode('b', 1)
        ]
        pattern: List[NodeType] = [NodeType.WITHIN, NodeType.TIMESPAN, NodeType.EVENT]
        result = self.sut.check_frame(node_list, pattern)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
