import unittest
from unittest.mock import MagicMock
from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.primitive import ScoredPrimitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives
from tests.helpers.test_nlp import TestNLP
from app.src.primitive_extractor import PrimitiveExtractor

class PrimitiveExtractorTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()

        self.ident1 = IIdentifyPrimitives()
        self.fake_primitive1 = ScoredPrimitive(VariableDotExpression('X1'), 0.8)
        self.ident1.identify = MagicMock(return_value = self.fake_primitive1)

        self.ident2 = IIdentifyPrimitives()
        self.fake_primitive2 = ScoredPrimitive(VariableDotExpression('X2'), 0.2)
        self.ident2.identify = MagicMock(return_value = self.fake_primitive2)

        self.identifiers = [
            self.ident1,
            self.ident2
        ]

        self.sut = PrimitiveExtractor(self.identifiers)

    def test_primitive_extractor(self):
        doc = self.nlp('this is a test')
        result = self.sut.extract(doc)
        self.assertEqual(len(result), 2)

        vde: VariableDotExpression = result[0].primitive
        self.assertEqual(vde.name, 'X1')
        
  
if __name__ == '__main__':
    unittest.main()