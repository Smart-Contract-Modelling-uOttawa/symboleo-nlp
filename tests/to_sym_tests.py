import unittest
from app.src.helpers.template_getter import get_template

test_suite = {
    'obligations': {
        'delivery': 'delivery: O(seller, buyer, true, Happens(delivered))',
        'payment': 'payment: O(buyer, seller, true, Happens(paid))',
        'latePayment': 'latePayment: Happens(Violated(obligations.payment)) -> O(buyer, seller, true, Happens(paidLate))',
        'disclosure1': 'disclosure1: O(seller, buyer, true, not Happens(disclosed))',
        'disclosure2': 'disclosure2: O(buyer, seller, true, not Happens(disclosed))'
    },
    'powers': {
        'suspendDelivery': 'suspendDelivery: P(seller, buyer, true, Suspended(obligations.delivery))',
        'resumeDelivery': 'resumeDelivery: Happens(NEVER) -> P(buyer, seller, true, Resumed(obligations.delivery))',
        'terminateContract': 'terminateContract: Occurs(Violation(obligations.delivery), NEVER) -> P(buyer, seller, true, Terminated(self))'
    }
}

class ToSymTests(unittest.TestCase):
    def setUp(self):
        contract = get_template('meat_sale')
        self.contract_spec = contract.contract_spec

    def test_obligations(self):
        obs = self.contract_spec.obligations
        expected_obs = test_suite['obligations']
        for ob_id in obs:
            next_ob = obs[ob_id]
            result = next_ob.to_sym()
            expected = expected_obs[ob_id]
            self.assertEqual(result, expected)
    
    def test_powers(self):
        pows = self.contract_spec.powers
        expected_pows = test_suite['powers']
        for p_id in pows:
            next_pow = pows[p_id]
            result = next_pow.to_sym()
            expected = expected_pows[p_id]
            self.assertEqual(result, expected)

  
if __name__ == '__main__':
    unittest.main()