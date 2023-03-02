import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.frames.all_frames import *
from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.frames.frame_builder import FrameBuilder 

from app.classes.frames.all_frames import BeforeDateFrame

class FrameBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = FrameBuilder()
    

    def test_frame_Builder(self):
        node_list: List[SelectedNode] = [
            BeforeNode('a', 0, 'xxx'),
            DateNode('b', 1, '2020/02/22')    
        ]
        result = self.sut.build(BeforeDateFrame(), node_list)

        self.assertTrue(result.is_complete())
        self.assertEqual(result.to_text(), 'before 2020/02/22')



if __name__ == '__main__':
    unittest.main()
