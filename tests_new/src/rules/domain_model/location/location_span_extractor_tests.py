import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP

from app.classes.domain_model.domain_model import DomainProp

from app.src.rules.domain_model.location.location_span_extractor import LocationSpanExtractor



class LocationSpanExtractorTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.sut = LocationSpanExtractor()


    def test_location_span_extractor(self):
        test_suite = [
            ['at their warehouse', 'their warehouse'],
            ['playing', None]
        ]
        for s, exp in test_suite:
            doc = self.nlp(s)
            res = self.sut.extract(doc)
            if exp != None:
                self.assertEqual(res.text, exp)
            else:
                self.assertEqual(res, None)

        

  
if __name__ == '__main__':
    unittest.main()