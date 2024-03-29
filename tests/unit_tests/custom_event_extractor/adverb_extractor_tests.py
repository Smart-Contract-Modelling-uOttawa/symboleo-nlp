import unittest
from unittest.mock import MagicMock
from app.classes.events.custom_event.adverb import Adverb, AdverbType
from app.src.custom_event_extractor.adverb_extractor import AdverbExtractor

class AdverbExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = AdverbExtractor()
    

    def test_adverb_extractor(self):
        str_val = 'below'
        result = self.sut.extract(str_val)
        expected = Adverb('below', [AdverbType.PLACE])
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
