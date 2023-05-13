import unittest
from unittest.mock import MagicMock
from tests.helpers.test_objects import CustomEvents

class EventToTextTests(unittest.TestCase):
    def test_event_to_text(self):
        evt = CustomEvents.abandon_property()
        result = evt.to_text()
        #print(result)
        expected = 'renter abandons property'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
