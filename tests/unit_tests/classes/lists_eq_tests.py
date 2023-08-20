import unittest
from unittest.mock import MagicMock
from typing import List, Tuple

from app.classes.helpers.list_eq import ClassHelpers

class TestClass:
    def __init__(self, s):
        self.s = s
    
    def __eq__(self, __value: object) -> bool:
        return self.s == __value.s

class ListEqualityTests(unittest.TestCase):
    def setUp(self) -> None:
        x = 0
    
    def test_simple_list_equality(self):
        a = [1,2,3]
        b = [1,2,3]

        res = ClassHelpers.simple_lists_eq(a,b)
        self.assertTrue(res)
    
    def test_simple_list_equality2(self):
        a = [1,2,3]
        b = [1]

        res = ClassHelpers.simple_lists_eq(a,b)
        self.assertFalse(res)

    
    def test_simple_list_equality2(self):
        a = [1,2,3]
        b = [1,2, 4]

        res = ClassHelpers.simple_lists_eq(a,b)
        self.assertFalse(res)
    
    def test_list_equality(self):
        a = [TestClass('a1'), TestClass('a2')]
        b = [TestClass('a2'), TestClass('a1')]

        res = ClassHelpers.lists_eq(a, b, 's')
        self.assertTrue(res)

    def test_list_equality2(self):
        a = [TestClass('a1'), TestClass('a2')]
        b = [TestClass('a2')]

        res = ClassHelpers.lists_eq(a, b, 's')
        self.assertFalse(res)

    def test_list_equality3(self):
        a = [TestClass('a1'), TestClass('a2')]
        b = [TestClass('a2'), TestClass('x')]

        res = ClassHelpers.lists_eq(a, b, 's')
        self.assertFalse(res)
    
    def test_dict_equality(self):
        a = {
            'a': TestClass('a')
        }
        b = {
            'a': TestClass('a')
        }

        res = ClassHelpers.dicts_eq(a, b)
        self.assertTrue(res)
    
    def test_dict_equality2(self):
        a = {
            'a': TestClass('a')
        }
        b = {
        }

        res = ClassHelpers.dicts_eq(a, b)
        self.assertFalse(res)
    
    def test_dict_equality3(self):
        a = {
            'a': TestClass('a')
        }
        b = {
            'a': TestClass('b')
        }

        res = ClassHelpers.dicts_eq(a, b)
        self.assertFalse(res)
    
    def test_dict_equality4(self):
        a = {
            'a': TestClass('a')
        }
        b = {
            'b': TestClass('b')
        }

        res = ClassHelpers.dicts_eq(a, b)
        self.assertFalse(res)
    
if __name__ == '__main__':
    unittest.main()