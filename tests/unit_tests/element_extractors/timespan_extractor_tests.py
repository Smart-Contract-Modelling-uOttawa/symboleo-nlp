import unittest
from unittest.mock import MagicMock
from app.classes.spec.point_function import TimeUnit
from app.classes.elements.timespan import Timespan
from app.src.selection.element_extractors.timespan_extractor import TimespanExtractor

class TimespanExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = TimespanExtractor()
    
    def test_timespan_extractor(self):
        str_val = '2 weeks'
        result = self.sut.extract(str_val)
        expected = Timespan(2, TimeUnit.Weeks)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
