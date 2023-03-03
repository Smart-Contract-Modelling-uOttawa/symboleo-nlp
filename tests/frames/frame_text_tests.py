import unittest
from unittest.mock import MagicMock

from app.classes.frames.all_frames import *


class FrameTextTests(unittest.TestCase):
    def setUp(self):
        x = 0

    def test_before_date_frame(self):
        f = BeforeDateFrame()
        f.date_text = '2020/02/03'
        ev = 'before 2020/02/03'
        self.assertTrue(f.is_complete())
        self.assertEqual(ev, f.to_text())
    
    def test_before_event_frame(self):
        f = BeforeEventFrame()
        f.subject = 'contract'
        f.verb = 'terminated'
        ev = 'before contract is terminated'
        self.assertTrue(f.is_complete())
        self.assertEqual(ev, f.to_text())

    def test_within_timespan_event_frame(self):
        f = WithinTimespanEventFrame()
        f.subject = 'contract'
        f.verb = 'terminated'
        f.timespan = '2 weeks'
        ev = 'within 2 weeks of contract being terminated'
        self.assertTrue(f.is_complete())
        self.assertEqual(ev, f.to_text())

    def test_if_event_frame(self):
        f = IfEventFrame()
        f.subject = 'contract'
        f.verb = 'terminated'
        ev = 'if contract has been terminated'
        self.assertTrue(f.is_complete())
        self.assertEqual(ev, f.to_text())
    
    def test_after_event_frame(self):
        f = AfterEventFrame()
        f.subject = 'contract'
        f.verb = 'terminated'
        ev = 'after contract is terminated'
        self.assertTrue(f.is_complete())
        self.assertEqual(ev, f.to_text())
    
    def test_after_date_frame(self):
        f = AfterDateFrame()
        f.date_text = '2022/02/23'
        ev = 'after 2022/02/23'
        self.assertTrue(f.is_complete())
        self.assertEqual(ev, f.to_text())
    
    def test_until_event_frame(self):
        f = UntilEventFrame()
        f.subject = 'contract'
        f.verb = 'terminated'
        ev = 'until contract has been terminated'
        self.assertTrue(f.is_complete())
        self.assertEqual(ev, f.to_text())
    
    def test_using_instrument_frame(self):
        f = UsingInstrumentFrame()
        f.instrument = 'a van'
        ev = 'using a van'
        self.assertTrue(f.is_complete())
        self.assertEqual(ev, f.to_text())

if __name__ == '__main__':
    unittest.main()
