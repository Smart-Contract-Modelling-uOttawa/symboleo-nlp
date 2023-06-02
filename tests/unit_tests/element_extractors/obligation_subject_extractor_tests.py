import unittest
from unittest.mock import MagicMock
from app.classes.elements.obligation_subject import ObligationSubject
from app.src.selection.element_extractors.obligation_subject_extractor import ObligationSubjectExtractor

class ObligationActionExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = ObligationSubjectExtractor()
    
    def test_obligation_subject_extractor(self):
        str_val = 'test_ob'
        result = self.sut.extract(str_val)
        expected = ObligationSubject('test_ob')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
