import unittest
from unittest.mock import MagicMock

from app.classes.frames.all_frames import *
from app.classes.selection.all_nodes import *
from app.src.frames.frame_getter import FrameGetter
from app.src.frames.inner_frame_checker import InnerFrameChecker


test_set = [
    (
        [
            RootNode(),
            BeforeNode(),
            EventNode(),
            NewEventNode()
        ],
        BeforeEventFrame
    ),

]

class FullFrameGetterTests(unittest.TestCase):
    def setUp(self):
        frame_list = get_all_frames()
        self.inner = InnerFrameChecker()
        self.sut = FrameGetter(frame_list, self.inner)

    def test_full_frame_getter(self):
        for node_list, expected_frame_type in test_set:
            res = self.sut.get_frame(node_list)
            self.assertEqual(type(res), expected_frame_type)
        

    def test_full_frame_getter_none(self):
        node_list = [
            BeforeNode(),
            EventNode(),
            NewEventNode()
        ]

        with self.assertRaises(ValueError) as context:
            self.sut.get_frame(node_list)

        self.assertTrue('No frames' in str(context.exception))


        

    



        


if __name__ == '__main__':
    unittest.main()
