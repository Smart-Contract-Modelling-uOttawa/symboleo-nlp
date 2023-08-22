import unittest
from unittest.mock import MagicMock
from typing import List, Tuple

from app.classes.events.custom_event.custom_event import CustomEvent, Predicate, NPTextType

from tests.helpers.test_objects import CustomEvents, NounPhrases, Verbs



class NounPhraseTests(unittest.TestCase):
    def setUp(self) -> None:
        x = 0
    
    def test_noun_phrase(self):
        np = NounPhrases.apple_pie()

        result = np.to_text(NPTextType.HEAD)
        self.assertEqual('pie', result)


if __name__ == '__main__':
    unittest.main()