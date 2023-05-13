import unittest
from unittest.mock import MagicMock

from app.classes.frames.all_frames import *
from app.classes.frames.frame import DummyFrame
from app.classes.selection.all_nodes import *
from app.src.frame_updaters.frame_getter import FrameGetter
from app.src.frame_updaters.inner_frame_checker import IInnerFrameChecker
from app.src.frame_updaters.all_frames_getter import IGetAllFrames
from app.classes.frames.all_frames import BeforeDateFrame


class FrameGetterTests(unittest.TestCase):
    def setUp(self):
        frame_list = [
            DummyFrame(),
            DummyFrame(),
            BeforeDateFrame()
        ]
        self.fake_getter = IGetAllFrames()
        self.fake_getter.get = MagicMock(return_value=frame_list)
        self.fake_inner = IInnerFrameChecker()
        
        self.sut = FrameGetter(self.fake_getter, self.fake_inner)

    def test_frame_getter(self):
        self.fake_inner.check_frame = MagicMock(side_effect=[False, False, True])

        res = self.sut.get_frame([DummyNode(), DummyNode(), DummyNode()])

        self.assertEqual(type(res), BeforeDateFrame)
        self.assertEqual(self.fake_getter.get.call_count, 1)
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
