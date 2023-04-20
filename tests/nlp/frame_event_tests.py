import unittest
from unittest.mock import MagicMock

from app.classes.selection.all_nodes import *
from app.classes.other.frame_event import FrameEvent, ConjType 
from app.classes.other.subject import Subject
from app.classes.other.verb import Verb, VerbConjugations, VerbType
from app.classes.other.prep_phrase import PrepPhrase

# test_set = [
#     (
#         FrameEvent('buyer', Verb('pay'), '100', [
#             FrameEventProp('currency', 'CAD', 'Currency'),
#             FrameEventProp('to', 'seller', 'Role'),
#             FrameEventProp('payDueDate', 'March 15, 2024', 'Date')
#         ]),
#         'buyer pays 100 in CAD to seller by March 15, 2024'
#     ),
#     (
#         FrameEvent('buyer', Verb('pay', 'late'), '10%', [
#             FrameEventProp('currency', 'CAD', 'Currency'),
#             FrameEventProp('to', 'seller', 'Role'),
            
#         ]),
#         'buyer pays 10% in CAD to seller late'
#     ),
#     (
#         FrameEvent('renter', Verb('pay'), '500', [
#             FrameEventProp('currency', 'CAD', 'Currency'),
#             FrameEventProp('to', 'landlord', 'Role'),
#             FrameEventProp('paymentMethod', 'credit card', 'PaymentMethod'),
#         ]),
#         'renter pays 500 in CAD to landlord with credit card'
#     )

# ]


test_set = [
    (
        FrameEvent(
            subj = Subject('legal proceedings', 'proceedings', True, adjs = ['legal']),
            verb = Verb('become', 'become', [VerbType.LINKING], VerbConjugations('become', 'becomes', 'became', 'becoming')),
            predicate=Predicate('necessary')
        ),
        'legal proceedings become necessary',
        'legal proceedings becoming necessary'
    ),
    (
        FrameEvent(
            subj = Subject('seller', 'seller', False),
            verb = Verb('pays', 'pay', [VerbType.TRANSITIVE], VerbConjugations('pay', 'pays', 'paid', 'paying')),
            dobj = DObject('$100', '$100', False),
            pps = [PrepPhrase('to the buyer', 'to', 'the buyer')]
        ),
        'seller pays $100 to the buyer',
        'seller paying $100 to the buyer'
    ),
    (
        FrameEvent(
            subj = Subject('Bob', 'Bob', False),
            verb = Verb('eats', 'eat', [VerbType.TRANSITIVE], VerbConjugations('eat', 'eats', 'ate', 'eating')),
            dobj = DObject('Apple pie', 'pie', False, None, ['Apple']),
            adverb = Adverb('noisily'),
            pps = [PrepPhrase('with Mary', 'with', 'Mary')]
        ),
        'Bob eats Apple pie noisily with Mary',
        'Bob eating Apple pie noisily with Mary'
    ),
    (
        FrameEvent(
            subj = Subject('The renter', 'renter', False),
            verb = Verb('occupies', 'occupy', [VerbType.TRANSITIVE], VerbConjugations('occupy', 'occupies', 'occupied', 'occupying')),
            dobj = DObject('the property', 'property', False, 'the')
        ),
        'renter occupies property',
        'renter occupying property'
    ),

]




class FrameEventTests(unittest.TestCase):
    def setUp(self) -> None:
        x = 0
    
    def test_frame_event_to_text(self):
        
        for f, p, c in test_set:
            res_p = f.to_text(ConjType.PRESENT)
            res_c = f.to_text(ConjType.CONTINUOUS)

            self.assertEqual(res_p, p)
            self.assertEqual(res_c, c)

    
if __name__ == '__main__':
    unittest.main()