import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_interval import *
from app.classes.spec.sym_situation import ContractState, ContractStateName

class SymIntervalTests(unittest.TestCase):
    def test_situation(self):
        p = SituationExpression(ContractState(ContractStateName.Active))
        res = p.to_sym()
        self.assertEqual(res, 'Active(self)')
    
  
if __name__ == '__main__':
    unittest.main()