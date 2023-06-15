import unittest
from unittest.mock import MagicMock

from app.classes.operations.user_input import UserInput, UnitType
from app.classes.patterns.pattern_classes import PatternClass

from app.src.pattern_builder.pattern_class_builder import PatternClassBuilder
from app.src.pattern_builder.pattern_class_extractor import IExtractPatternClass
from app.src.pattern_builder.pattern_class_filler import IFillPatternClass

class PatternBuilderTests(unittest.TestCase):
    def setUp(self):

        self.pattern_class_extractor = IExtractPatternClass()
        fake_pattern_class = PatternClass()
        self.pattern_class_extractor.extract = MagicMock(return_value=fake_pattern_class)

        self.pattern_class_filler = IFillPatternClass()
        fake_pattern_fill = PatternClass()
        self.pattern_class_filler.fill = MagicMock(return_value = fake_pattern_fill)

        self.sut = PatternClassBuilder(
            self.pattern_class_extractor,
            self.pattern_class_filler
        )

    def test_operation_mapper(self):
        test_input = [
            UserInput(UnitType.DUMMY, 'TEST')
        ]

        result = self.sut.build(test_input)

        self.assertTrue(isinstance(result, PatternClass))
        self.assertEqual(self.pattern_class_extractor.extract.call_count, 1)
        self.assertEqual(self.pattern_class_filler.fill.call_count, 1)


if __name__ == '__main__':
    unittest.main()
