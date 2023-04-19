import unittest
from unittest.mock import MagicMock

from app.classes.frames.frame_event import FrameEvent, FrameEventProp
from app.src.nlp.verb_extractor import Verb

test_set = [
    (
        FrameEvent('buyer', Verb('pay'), '100', [
            FrameEventProp('currency', 'CAD', 'Currency'),
            FrameEventProp('to', 'seller', 'Role'),
            FrameEventProp('payDueDate', 'March 15, 2024', 'Date')
        ]),
        'buyer pays 100 in CAD to seller by March 15, 2024'
    ),
    (
        FrameEvent('buyer', Verb('pay', 'late'), '10%', [
            FrameEventProp('currency', 'CAD', 'Currency'),
            FrameEventProp('to', 'seller', 'Role'),
            
        ]),
        'buyer pays 10% in CAD to seller late'
    ),
    (
        FrameEvent('renter', Verb('pay'), '500', [
            FrameEventProp('currency', 'CAD', 'Currency'),
            FrameEventProp('to', 'landlord', 'Role'),
            FrameEventProp('paymentMethod', 'credit card', 'PaymentMethod'),
        ]),
        'renter pays 500 in CAD to landlord with credit card'
    )

]

class FrameEventTests(unittest.TestCase):

    def test_frame_events(self):
        for f, expected in test_set:
            f: FrameEvent = f
            result = f.to_text()

            self.assertEqual(result, expected)
    
if __name__ == '__main__':
    unittest.main()