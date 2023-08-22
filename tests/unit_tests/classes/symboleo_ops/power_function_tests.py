import unittest
from unittest.mock import MagicMock

from app.classes.spec.power_function import *


class PatomTests(unittest.TestCase):
    def test_power_func_ob(self):
        p = PFObligation(PFObligationName.Suspended, 'test_ob')
        self.assertEqual(p.to_sym(), 'Suspended(obligations.test_ob)')

    def test_power_func_c(self):
        p = PFContract(PFContractName.Terminated)
        q = PFContract(PFContractName.Terminated)
        self.assertEqual(p.to_sym(), 'Terminated(self)')
        self.assertEqual(p, q)

    

    
  
if __name__ == '__main__':
    unittest.main()