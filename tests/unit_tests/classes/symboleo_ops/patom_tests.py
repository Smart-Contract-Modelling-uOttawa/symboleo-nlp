import unittest
from unittest.mock import MagicMock

from app.classes.spec.p_atoms import *


class PatomTests(unittest.TestCase):
    def test_patom_false(self):
        p = PAtomPredicateFalseLiteral()
        q = PAtomPredicateFalseLiteral()

        res = p.to_sym()

        self.assertEqual(res, 'false')
        self.assertEqual(p, q)

    

    
  
if __name__ == '__main__':
    unittest.main()