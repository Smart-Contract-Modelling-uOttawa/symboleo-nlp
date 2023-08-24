import unittest
from unittest.mock import MagicMock

from app.classes.operations.user_input import UserInput, UnitType
from app.classes.pattern_classes.pattern_class import PatternClass

from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter, PatternClassType

class PatternClassGetterTests(unittest.TestCase):
    def setUp(self):
        self.sut = AllPatternClassGetter()

    def test_pattern_builder(self):
        config = [PatternClassType.CONDITIONAL, PatternClassType.EXCEPTION, PatternClassType.TEMPORAL, PatternClassType.UNTIL]
        result = self.sut.get(config)
        self.assertEqual(len(result), len(set(result)))
    
    def test_pattern_builder1(self):
        config = [PatternClassType.CONDITIONAL]
        result = self.sut.get(config)
        self.assertEqual(len(result), len(set(result)))
    
    def test_pattern_builder2(self):
        config = [PatternClassType.EXCEPTION]
        result = self.sut.get(config)
        self.assertEqual(len(result), len(set(result)))
    
    def test_pattern_builder3(self):
        config = [PatternClassType.TEMPORAL]
        result = self.sut.get(config)
        self.assertEqual(len(result), len(set(result)))
    
    def test_pattern_builder4(self):
        config = [PatternClassType.UNTIL]
        result = self.sut.get(config)
        self.assertEqual(len(result), len(set(result)))
    

    def test_pattern_builder_all(self):
        result = self.sut.get()
        self.assertEqual(len(result), len(set(result)))


if __name__ == '__main__':
    unittest.main()
