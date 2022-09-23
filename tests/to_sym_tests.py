import unittest
from app.classes.spec.symboleo_spec import Obligation, Power
from app.templates.meat_sale.norms import meat_sale_norms as norms

test_suite = {
    'obligations': {
        'O1': 'O1: O(Seller, Buyer, T, happens(delivered, BEFORE delivered.delDueD))',
        'O2': 'O2: O(Buyer, Seller, T, happens(paid, PayDueD))',
        'O3': 'O3: occurs(oVIOLATION(O2), X) => O(Buyer, Seller, T, happens(PaidLate, X))'
    },
    'surviving_obligations': {
        'SO1': 'SO1: O(Seller, Buyer, T, NOT happens(disclosed, t) AND t within 6 Months after cActivated(meatSaleC))',
        'SO2': 'SO2: O(Buyer, Seller, T, NOT happens(disclosed, t) AND t within 6 Months after cActivated(meatSaleC))'
    },
    'powers': {
        'P1': 'P1: occurs(oViolation(O2), X) => P(Seller, Buyer, T, occurs(oSuspension(O1), X))',
        'P2': 'P2: happens(PaidLate, Within oSuspension(O1)) => P(Buyer, Seller, T, occurs(oInEffect(O1), X))',
        'P3': 'P3: NOT happens(Delivered, 10 days after DelDueDate) => P(Buyer, Seller, T, occurs(oDischarge(O2), X) AND occurs(oDischarge(O3), X) AND occurs(cUnsuccessfTulermination(meatSaleC), X))'
    }
}

class ToSymTests(unittest.TestCase):
    def test_obligations(self):
        obs: list[Obligation] = norms['obligations']
        expected_obs = test_suite['obligations']
        for x in obs:
            result = x.to_sym()
            expected = expected_obs[x.id]
            self.assertEqual(result, expected)
    
    def test_surviving_obligations(self):
        obs: list[Obligation] = norms['surviving_obligations']
        expected_obs = test_suite['surviving_obligations']
        for x in obs:
            result = x.to_sym()
            expected = expected_obs[x.id]
            self.assertEqual(result, expected)
    
    def test_powers(self):
        obs: list[Power] = norms['powers']
        expected_obs = test_suite['powers']
        for x in obs:
            result = x.to_sym()
            expected = expected_obs[x.id]
            self.assertEqual(result, expected)

  
if __name__ == '__main__':
    unittest.main()