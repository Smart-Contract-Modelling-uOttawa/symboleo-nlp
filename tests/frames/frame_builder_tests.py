import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.frames.all_frames import *
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.all_nodes import *
from app.src.frames.frame_builder import FrameBuilder 

from app.classes.frames.all_frames import BeforeDateFrame

test_set = [
    (
        [
            RootNode(),
            BeforeNode(),
            EventNode(),
            CustomEventNode(),
            SubjectNode('Bob'),
            VerbNode('eats'),
            DobjNode('Apple pie'),
            AdverbNode('noisily'),
            PrepNode('with mary')
        ],
        BeforeEventFrame()
    )
]


class FrameBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = FrameBuilder()
    

    def test_frame_builder(self):
        for node_list, f in test_set:
            result = self.sut.build(f, node_list)
            print(result.to_text())
            

if __name__ == '__main__':
    unittest.main()
