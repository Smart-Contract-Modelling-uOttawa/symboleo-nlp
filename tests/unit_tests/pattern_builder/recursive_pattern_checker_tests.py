import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV

from app.src.pattern_builder.recursive_pattern_checker import RecursivePatternChecker

# TODO: Add tests
class RecursivePatternCheckerTests(unittest.TestCase):
    def setUp(self):
        self.sut = RecursivePatternChecker()

    def test_recursive_pattern_checker(self):
        return
    
    



if __name__ == '__main__':
    unittest.main()
