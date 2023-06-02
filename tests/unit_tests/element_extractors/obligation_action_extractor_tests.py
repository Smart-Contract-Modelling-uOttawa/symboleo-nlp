import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ObligationEventName
from app.src.selection.element_extractors.obligation_action_extractor import ObligationActionExtractor

class ObligationActionExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationActionExtractor()
    

    def test_obligation_action_extractor(self):
        str_val = 'violated'
        result = self.sut.extract(str_val)
        expected = ObligationEventName.Violated
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
