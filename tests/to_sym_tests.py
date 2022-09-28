import unittest
from app.classes.spec.symboleo_spec import Obligation, Power
from app.templates.meat_sale.norms import meat_sale_norms as norms

test_suite = {
    'obligations': {
        'delivery': 'delivery: O(seller, buyer, true, WhappensBefore(delivered, delivered.delDueDate))',
        'payment': 'payment: O(buyer, seller, true, WhappensBefore(paid, paid.payDueDate))',
        'latePayment': 'latePayment: Happens(Violated(obligations.payment)) -> O(buyer, seller, true, Happens(paidLate))'
    },
    'surviving_obligations': {
        'so1': 'so1: O(seller, buyer, true, not WhappensBefore(disclosed, Date.add(Activated(self), 6, months)))',
        'so2': 'so2: O(buyer, seller, true, not WhappensBefore(disclosed, Date.add(Activated(self), 6, months)))'
    },
    'powers': {
        'suspendDelivery': 'suspendDelivery: Happens(Violated(obligations.payment)) -> P(seller, buyer, true, Suspended(obligations.delivery))',
        'resumeDelivery': 'resumeDelivery: HappensWithin(paidLate, Suspension(obligations.delivery)) -> P(buyer, seller, true, Resumed(obligations.delivery))',
        'terminateContract': 'terminateContract: Happens(Violated(obligations.delivery)) -> P(buyer, seller, true, Terminated(self))'
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