import unittest
from unittest.mock import MagicMock

from app.classes.patterns.all_patterns import *
from app.classes.patterns.pattern import DummyPattern
from app.classes.elements.all_elements import *
from app.src.pattern_updaters.pattern_getter import PatternGetter
from app.src.pattern_updaters.inner_pattern_checker import IInnerPatternChecker
from app.src.pattern_updaters.all_patterns_getter import IGetAllPatterns
from app.classes.patterns.all_patterns import BeforeDate


class PatternGetterTests(unittest.TestCase):
    def setUp(self):
        pattern_list = [
            DummyPattern(),
            DummyPattern(),
            BeforeDate()
        ]
        self.fake_getter = IGetAllPatterns()
        self.fake_getter.get = MagicMock(return_value=pattern_list)
        self.fake_inner = IInnerPatternChecker()
        
        self.sut = PatternGetter(self.fake_getter, self.fake_inner)

    def test_pattern_getter(self):
        self.fake_inner.check_pattern = MagicMock(side_effect=[False, False, True])

        res = self.sut.get_pattern([DummyElement(), DummyElement(), DummyElement()])

        self.assertEqual(type(res), BeforeDate)
        self.assertEqual(self.fake_getter.get.call_count, 1)
        self.assertEqual(self.fake_inner.check_pattern.call_count, 3)
    

    def test_pattern_getter_too_many(self):
        self.fake_inner.check_pattern = MagicMock(side_effect=[False, True, True])

        with self.assertRaises(ValueError) as context:
            self.sut.get_pattern([DummyElement(), DummyElement(), DummyElement()])

        self.assertTrue('Too many' in str(context.exception))
        self.assertEqual(self.fake_inner.check_pattern.call_count, 3)

    
    def test_pattern_getter_none(self):
        self.fake_inner.check_pattern = MagicMock(side_effect=[False, False, False])

        with self.assertRaises(ValueError) as context:
            self.sut.get_pattern([DummyElement(), DummyElement(), DummyElement()])

        self.assertTrue('No patterns' in str(context.exception))
        self.assertEqual(self.fake_inner.check_pattern.call_count, 3)


        


if __name__ == '__main__':
    unittest.main()
