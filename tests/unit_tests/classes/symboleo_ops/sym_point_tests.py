import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_point import *
from app.classes.spec.sym_event import ContractEvent, PowerEvent, ObligationEvent, ContractEventName, PowerEventName, ObligationEventName

class SymPointTests(unittest.TestCase):
    def test_pace(self):
        p = PointAtomContractEvent(ContractEvent(ContractEventName.Activated))
        q = PointAtomContractEvent(ContractEvent(ContractEventName.Activated))
        res = p.to_sym()
        self.assertEqual(res, 'Activated(self)')
        self.assertEqual(p, q)
    
    def test_paoe(self):
        p = PointAtomObligationEvent(ObligationEvent(ObligationEventName.Activated, 'test_ob'))
        q = PointAtomObligationEvent(ObligationEvent(ObligationEventName.Activated, 'test_ob'))
        res = p.to_sym()
        self.assertEqual(res, 'Activated(obligations.test_ob)')
        self.assertEqual(p, q)
    
    def test_pape(self):
        p = PointAtomPowerEvent(PowerEvent(PowerEventName.Activated, 'test_pow'))
        q = PointAtomPowerEvent(PowerEvent(PowerEventName.Activated, 'test_pow'))
        res = p.to_sym()
        self.assertEqual(res, 'Activated(powers.test_pow)')
        self.assertEqual(p, q)
    

if __name__ == '__main__':
    unittest.main()