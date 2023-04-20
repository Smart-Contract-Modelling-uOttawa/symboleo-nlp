import unittest
from unittest.mock import MagicMock

from app.classes.frames.all_frames import *
from app.classes.frames.frame import DummyFrame
from app.classes.selection.all_nodes import *
from app.src.frames.frame_getter import FrameGetter
from app.src.frames.inner_frame_checker import IInnerFrameChecker
from app.classes.frames.all_frames import BeforeDateFrame


class FrameGetterTests(unittest.TestCase):
    def setUp(self):
        frame_list = [
            DummyFrame(),
            DummyFrame(),
            BeforeDateFrame()
        ]
        self.fake_inner = IInnerFrameChecker()
        
        self.sut = FrameGetter(frame_list, self.fake_inner)

    def test_frame_getter(self):
        self.fake_inner.check_frame = MagicMock(side_effect=[False, False, True])

        res = self.sut.get_frame([DummyNode(), DummyNode(), DummyNode()])

        self.assertEqual(type(res), BeforeDateFrame)
        self.assertEqual(self.fake_inner.check_frame.call_count, 3)
    

    def test_frame_getter_too_many(self):
        self.fake_inner.check_frame = MagicMock(side_effect=[False, True, True])

        with self.assertRaises(ValueError) as context:
            self.sut.get_frame([DummyNode(), DummyNode(), DummyNode()])

        self.assertTrue('Too many' in str(context.exception))
        self.assertEqual(self.fake_inner.check_frame.call_count, 3)

    
    def test_frame_getter_none(self):
        self.fake_inner.check_frame = MagicMock(side_effect=[False, False, False])

        with self.assertRaises(ValueError) as context:
            self.sut.get_frame([DummyNode(), DummyNode(), DummyNode()])

        self.assertTrue('No frames' in str(context.exception))
        self.assertEqual(self.fake_inner.check_frame.call_count, 3)


        


if __name__ == '__main__':
    unittest.main()
