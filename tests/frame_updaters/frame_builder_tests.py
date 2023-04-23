import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.frames.all_frames import *
from app.classes.frames.frame import DummyFrame
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.all_nodes import *
from app.src.frame_updaters.frame_builder import FrameBuilder 
from app.src.frame_updaters.frame_getter import IGetFrame
from app.src.frame_updaters.frame_updater import IUpdateFrame


class FrameBuilderTests(unittest.TestCase):
    def setUp(self):
        self.frame_getter = IGetFrame()
        self.fake_frame = DummyFrame()
        self.frame_getter.get_frame = MagicMock(return_value=self.fake_frame)

        self.updater = IUpdateFrame()
        self.updater.update_frame = MagicMock(return_value=None)
        updater_dict = {
            SelectedNode: self.updater
        }

        self.sut = FrameBuilder(self.frame_getter, updater_dict)
    

    def test_frame_builder(self):
        node_list = [
            SelectedNode()
        ]

        result = self.sut.build(node_list)
        
        self.assertEqual(type(result), DummyFrame)
        self.assertEqual(self.frame_getter.get_frame.call_count, 1)
        self.assertEqual(self.updater.update_frame.call_count, 1)    

if __name__ == '__main__':
    unittest.main()
