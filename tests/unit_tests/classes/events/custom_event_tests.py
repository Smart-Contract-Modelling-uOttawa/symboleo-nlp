import unittest
from unittest.mock import MagicMock
from typing import List, Tuple

from app.classes.events.conj_type import ConjType
from app.classes.events.custom_event.custom_event import CustomEvent

from tests.helpers.test_objects import CustomEvents


test_set: List[Tuple[CustomEvent,str,str]] = [
    (
        CustomEvents.legal_proceedings(),
        'evt_legal_proceedings_necessary',
        'LegalProceedingsNecessary'
    ),
    (
        CustomEvents.paying(),
        'evt_pay',
        'Pay'
    ),
    (
        CustomEvents.eating_pie(),
        'evt_eat_pie',
        'EatPie'
    ),
]


class CustomEventTests(unittest.TestCase):
    def setUp(self) -> None:
        x = 0
    
    def test_custom_event_to_text(self):
        
        for f,  exp_event_key, exp_decl_name in test_set:
            evt_key = f.event_key()
            decl_name = f.get_declaration_name()
            
            self.assertEqual(decl_name, exp_decl_name)
            self.assertEqual(evt_key, exp_event_key)

    
if __name__ == '__main__':
    unittest.main()