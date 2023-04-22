import unittest
from unittest.mock import MagicMock
from app.classes.custom_event.conj_type import ConjType

from app.classes.selection.all_nodes import *
from app.classes.custom_event.custom_event import CustomEvent 
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.verb import Verb, VerbConjugations, VerbType
from app.classes.custom_event.prep_phrase import PrepPhrase

from tests.nlp.test_objects import CustomEvents

test_set = [
    (
        CustomEvents.legal_proceedings(),
        'legal proceedings become necessary',
        'legal proceedings becoming necessary'
    ),
    (
        CustomEvents.paying(),
        'buyer pays $100 to seller with credit card', # "THE" seller?
        'buyer paying $100 to seller with credit card'
    ),
    (
        CustomEvents.eating_pie(),
        'Bob eats apple pie noisily with seller',
        'Bob eating apple pie noisily with seller'
    ),
]


class CustomEventTests(unittest.TestCase):
    def setUp(self) -> None:
        x = 0
    
    #@unittest.skip('..')
    def test_custom_event_to_text(self):
        
        for f, p, c in test_set:
            res_p = f.to_text(ConjType.PRESENT)
            res_c = f.to_text(ConjType.CONTINUOUS)

            self.assertEqual(res_p, p)
            self.assertEqual(res_c, c)

    
if __name__ == '__main__':
    unittest.main()