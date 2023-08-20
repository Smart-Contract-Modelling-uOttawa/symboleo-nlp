import unittest
from unittest.mock import MagicMock

from app.classes.helpers.case_converter import CaseConverter


class CaseConverterTests(unittest.TestCase):
    def test_convert_pascal(self):
        res = CaseConverter.to_pascal('the bird in the bush')
        self.assertEqual(res, 'TheBirdInTheBush')
    
    def test_convert_snake(self):
        res = CaseConverter.to_snake('the bird in the bush')
        self.assertEqual(res, 'the_bird_in_the_bush')

if __name__ == '__main__':
    unittest.main()