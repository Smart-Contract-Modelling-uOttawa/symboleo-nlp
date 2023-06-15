import unittest
from unittest.mock import MagicMock
from app.classes.events.custom_event.predicate import Predicate
from app.src.element_extractors.predicate_extractor import PredicateExtractor

class PredicateExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = PredicateExtractor()
    

    def test_adverb_extractor(self):
        str_val = 'happy'
        result = self.sut.extract(str_val)
        expected = Predicate('happy')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
