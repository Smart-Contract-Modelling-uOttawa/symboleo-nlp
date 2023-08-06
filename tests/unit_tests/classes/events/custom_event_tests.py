import unittest
from unittest.mock import MagicMock
from typing import List, Tuple

from app.classes.events.conj_type import ConjType
from app.classes.events.custom_event.custom_event import CustomEvent

from tests.helpers.test_objects import CustomEvents


test_set: List[Tuple[CustomEvent,str,str,str, str,str]] = [
    (
        CustomEvents.legal_proceedings(),
        'legal proceedings become necessary',
        'legal proceedings becoming necessary',
        'legal proceedings become necessary',
        'evt_legal_proceedings_necessary',
        'LegalProceedingsNecessary'
    ),
    (
        CustomEvents.paying(),
        'buyer pays $100 to the seller with credit card',
        'buyer paying $100 to the seller with credit card',
        'buyer pays $100 to the seller with credit card',
        'evt_pay',
        'Pay'
    ),
    (
        CustomEvents.eating_pie(),
        'Bob eats apple pie noisily with the seller',
        'Bob eating apple pie noisily with the seller',
        'Bob eats apple pie noisily with the seller',
        'evt_eat_pie',
        'EatPie'
    ),
]


class CustomEventTests(unittest.TestCase):
    def setUp(self) -> None:
        x = 0
    
    def test_custom_event_to_text(self):
        
        for f, p, c, b, exp_event_key, exp_decl_name in test_set:
            res_p = f.to_text(ConjType.PRESENT)
            res_c = f.to_text(ConjType.CONTINUOUS)
            res_b = f.to_text(ConjType.BASIC)

            evt_key = f.event_key()
            decl_name = f.get_declaration_name()
            

            self.assertEqual(res_p, p)
            self.assertEqual(res_c, c)
            self.assertEqual(res_b, b)
            self.assertEqual(decl_name, exp_decl_name)
            self.assertEqual(evt_key, exp_event_key)

    
if __name__ == '__main__':
    unittest.main()