import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_event import *

class SymEventTests(unittest.TestCase):
    def test_power_event(self):
        p = PowerEvent(PowerEventName.Activated, 'x')
        q = PowerEvent(PowerEventName.Activated, 'x')
        res = p.to_sym()
        self.assertEqual(res, 'Activated(powers.x)')
        self.assertEqual(p, q)
    
    def test_obligation_event(self):
        p = ObligationEvent(ObligationEventName.Activated, 'x')
        q = ObligationEvent(ObligationEventName.Activated, 'x')
        res = p.to_sym()
        self.assertEqual(res, 'Activated(obligations.x)')
        self.assertEqual(p, q)
    
    def test_contract_event(self):
        p = ContractEvent(ContractEventName.Activated)
        res = p.to_sym()
        self.assertEqual(res, 'Activated(self)')
    
  
if __name__ == '__main__':
    unittest.main()