import unittest
from unittest.mock import MagicMock
from typing import Tuple
from app.classes.events.custom_event.custom_event import CustomEvent
from tests.helpers.test_objects import CustomEvents

# TODO: Will add many more examples from real test cases...
## Or may remove these, if we get rid of the event.to_text functionality...
test_suite: Tuple[CustomEvent, str] = [
    (
        CustomEvents.abandon_property(),
        'renter abandons property'
    ),
    (
        CustomEvents.eating_pie(),
        'Bob eats apple pie noisily with the seller'
    ),
    (
        CustomEvents.legal_pie(),
        'a legal professional sues the seller for apple pie in Canada'
    ),
    (
        CustomEvents.fails_occupy_property(),
        'renter fails to occupy property'
    )
]

class EventToTextTests(unittest.TestCase):
    def test_event_to_text(self):
        for test_val, exp_res in test_suite:
            res = test_val.to_text()
            
            # print(res)
            # print(exp_res)

            self.assertEqual(res, exp_res)

if __name__ == '__main__':
    unittest.main()
