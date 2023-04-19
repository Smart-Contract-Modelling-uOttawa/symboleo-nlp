
import unittest
from unittest.mock import MagicMock

from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.frames.frame_event import FrameEvent, FrameEventProp

from app.src.nlp.verb_extractor import IExtractVerb, Verb
from app.src.nlp.event_converter import DeclarationToEventConverter


class DeclarationToEventTests(unittest.TestCase):
    def setUp(self):
        self.verb_extractor = IExtractVerb()

        self.sut = DeclarationToEventConverter(self.verb_extractor)

    # Basic test
    @unittest.skip('reorg')
    def test1(self):
        declaration = Declaration('evt_paid', 'events', 'Paid', [
            DeclarationProp('amount', '100', 'Number'),
            DeclarationProp('currency', 'CAD', 'Currency'),
            DeclarationProp('from', 'buyer', 'Role'),
            DeclarationProp('to', 'seller', 'Role'),
            DeclarationProp('payDueDate', 'March 15, 2024', 'Date')
        ])

        fake_verb = Verb('pay')
        self.verb_extractor.extract = MagicMock(return_value = fake_verb)
        expected = FrameEvent('buyer', fake_verb, '100', [
            FrameEventProp('to', 'seller', 'Role'),
            FrameEventProp('currency', 'CAD', 'Currency'),
            FrameEventProp('payDueDate', 'March 15, 2024', 'Date')
        ])

        result = self.sut.convert(declaration)
        self.assertEqual(result, expected)
        
    # Complex verb (adverb included)
    @unittest.skip('reorg')
    def test2(self):
        declaration = Declaration('evt_paid_late', 'events', 'PaidLate', [
            DeclarationProp('amount', '10%', 'Number'),
            DeclarationProp('currency', 'CAD', 'Currency'),
            DeclarationProp('from', 'buyer', 'Role'),
            DeclarationProp('to', 'seller', 'Role'),
        ])

        fake_verb = Verb('pay', 'late')
        self.verb_extractor.extract = MagicMock(return_value = fake_verb)
        expected = FrameEvent('buyer', fake_verb, '10%', [
            FrameEventProp('to', 'seller', 'Role'),
            FrameEventProp('currency', 'CAD', 'Currency')
        ])

        result = self.sut.convert(declaration)
        self.assertEqual(result, expected)

    @unittest.skip('reorg')
    def test3(self):
        declaration =Declaration('evt_pay_rent', 'events', 'Paid', [
            DeclarationProp('amount', '500', 'Number'),
            DeclarationProp('currency', 'CAD', 'Currency'),
            DeclarationProp('paymentMethod', 'credit card', 'PaymentMethod'),
            DeclarationProp('from', 'renter', 'Role'),
            DeclarationProp('to', 'landlord', 'Role'),
        ])

        fake_verb = Verb('pay')
        self.verb_extractor.extract = MagicMock(return_value = fake_verb)

        expected = FrameEvent('renter', fake_verb, '500', [
            FrameEventProp('to', 'landlord', 'Role'),
            FrameEventProp('currency', 'CAD', 'Currency'),
            FrameEventProp('paymentMethod', 'credit card', 'PaymentMethod'),
        ])

        result = self.sut.convert(declaration)
        self.assertEqual(result, expected)

    
if __name__ == '__main__':
    unittest.main()


