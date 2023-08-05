import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents
from tests.helpers.test_contract import get_test_contract


class TryGetEventTests(unittest.TestCase):
    def test_try_get_event(self):
        contract = get_test_contract()

        evt = contract.try_get_event('test_obligation', 'obligations', 'consequent')

        exp_evt = CustomEvents.eating_pie()
        self.assertEqual(evt, exp_evt)

  
if __name__ == '__main__':
    unittest.main()