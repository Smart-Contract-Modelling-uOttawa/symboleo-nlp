import unittest
from unittest.mock import MagicMock

from app.classes.spec.other_predicates import *

class OtherPredicateTests(unittest.TestCase):
    def test_predicate_equal(self):
        other_func = PredicateFunctionIsEqual('x','y')
        res = other_func.to_sym()
        self.assertEqual(res, 'IsEqual(x, y)')
    
    def test_predicate_owner(self):
        other_func = PredicateFunctionIsOwner('x','y')
        res = other_func.to_sym()
        self.assertEqual(res, 'IsOwner(x, y)')

    def test_predicate_not_assigned(self):
        other_func = PredicateFunctionCannotBeAssigned('x')
        res = other_func.to_sym()
        self.assertEqual(res, 'CannotBeAssigned(x)')


    
  
if __name__ == '__main__':
    unittest.main()