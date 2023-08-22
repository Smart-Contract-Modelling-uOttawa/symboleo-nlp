import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_situation import *

class SymSituationTests(unittest.TestCase):
    def test_ob_state(self):
        p = ObligationState(ObligationStateName.Active, 'ob_test')
        q = ObligationState(ObligationStateName.Active, 'ob_test')
        res = p.to_sym()
        self.assertEqual(res, 'Active(obligations.ob_test)')
        self.assertEqual(p, q)
    
    def test_pow_state(self):
        p = PowerState(PowerStateName.Active, 'pow_test')
        q = PowerState(PowerStateName.Active, 'pow_test')
        res = p.to_sym()
        self.assertEqual(res, 'Active(powers.pow_test)')
        self.assertEqual(p, q)

    def test_c_state(self):
        p = ContractState(ContractStateName.Active)
        q = ContractState(ContractStateName.Active)
        res = p.to_sym()
        self.assertEqual(res, 'Active(self)')
        self.assertEqual(p, q)
    
  
if __name__ == '__main__':
    unittest.main()