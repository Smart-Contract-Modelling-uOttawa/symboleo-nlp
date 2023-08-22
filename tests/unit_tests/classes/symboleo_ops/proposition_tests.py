import unittest
from unittest.mock import MagicMock

from app.classes.spec.proposition import *

class PropositionTests(unittest.TestCase):
    def test_literal(self):
        p = PAtomStringLiteral('x')
        res = p.to_sym()
        self.assertEqual(res, 'x')
    
    def test_pcomparison(self):
        p = PComparison(
            curr = PAtomStringLiteral('x'),
            right = PAtomStringLiteral('y'),
            op = PComparisonOp.GEq
        )
        res = p.to_sym()
        self.assertEqual(res, 'x >= y')
    
    def test_pequality(self):
        a = PComparison(
            curr = PAtomStringLiteral('x'),
            right = PAtomStringLiteral('y'),
            op = PComparisonOp.GEq
        )
        b = PComparison(
            curr = PAtomStringLiteral('z'),
            right = PAtomStringLiteral('w'),
            op = PComparisonOp.LEq
        )
        p = PEquality(
            curr = a,
            right = b,
            op = PEqualityOp.Equal
        )
        res = p.to_sym()
        self.assertEqual(res, 'x >= y == z <= w')
    

    
  
if __name__ == '__main__':
    unittest.main()