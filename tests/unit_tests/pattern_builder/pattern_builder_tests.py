import unittest
from unittest.mock import MagicMock

from typing import List
from app.classes.patterns.all_patterns import *
from app.classes.patterns.pattern import DummyPattern
from app.classes.elements.element import Element
from app.classes.elements.all_elements import *
from app.src.pattern_builder.pattern_builder import PatternBuilder 
from app.src.pattern_builder.pattern_checker import ICheckPatterns
from app.src.pattern_builder.pattern_updaters.pattern_updater import IUpdatePattern


class PatternBuilderTests(unittest.TestCase):
    def setUp(self):
        self.pattern_getter = ICheckPatterns()
        self.fake_pattern = DummyPattern()
        self.pattern_getter.get_pattern = MagicMock(return_value=self.fake_pattern)

        self.updater = IUpdatePattern()
        self.updater.update = MagicMock(return_value=None)
        updater_dict = {
            Element: self.updater
        }

        self.sut = PatternBuilder(self.pattern_getter, updater_dict)
    

    def test_pattern_builder(self):
        elements = [
            Element()
        ]

        result = self.sut.build(elements)
        
        self.assertEqual(type(result), DummyPattern)
        self.assertEqual(self.pattern_getter.get_pattern.call_count, 1)
        self.assertEqual(self.updater.update.call_count, 1)    

if __name__ == '__main__':
    unittest.main()
