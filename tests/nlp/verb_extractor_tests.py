
import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.frames.frame_event import FrameEvent, FrameEventProp

from app.src.nlp.verb_extractor import VerbExtractor, Verb
from app.src.nlp.event_converter import DeclarationToEventConverter

test_set = [
    ('Paid', Verb('pay')),
    ('PaidLate', Verb('pay', 'late')),
]

class VerbExtractorTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        self.sut = VerbExtractor(nlp)

    # Basic test
    def test_verb_extractor(self):
        for text, expected in test_set:
            result = self.sut.extract(text)
            self.assertEqual(result, expected, f'error on verb extraction: {text}')

    
if __name__ == '__main__':
    unittest.main()


