import unittest
from unittest.mock import MagicMock
from typing import List, Tuple

from app.classes.events.custom_event.custom_event import CustomEvent, Predicate

from tests.helpers.test_objects import CustomEvents, NounPhrases, Verbs


test_set: List[Tuple[CustomEvent,str,str]] = [
    (
        CustomEvent(
            NounPhrases.bob(),
            Verbs.become(),
            predicate = Predicate('happy')
        ),
        'evt_agent_happy',
        'AgentHappy'
    ),
    (
        CustomEvent(
            NounPhrases.bob(),
            Verbs.complies()
        ),
        'evt_agent_comply',
        'AgentComply'
    ),
    (
        CustomEvent(
            NounPhrases.bob(),
            Verbs.pays(),
            dobj = NounPhrases.test_value_parm()
        ),
        'evt_pay_test_value',
        'PayTestValue'
    ),
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
        'evt_eat_pie_noisily',
        'EatPieNoisily'
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