import unittest
from unittest.mock import MagicMock
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_nlp import TestNLP

from app.src.template_getter import get_template
from tests_new.test_suites.meat_sale.test_setup import MeatSaleTestSetup
from tests_new.test_suites.meat_sale.expected_contract import expected_contract


class MeatSaleTest(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        builder = MeatSaleTestSetup()
        self.updater = builder.setup()

        self.customizations = [
            ('DELIVERY_TIMEFRAME', 'within 2 weeks'),
            ('DELIVERY_LOCATION', 'at the buyer\'s warehouse'),
            ('PAYMENT_DETAILS', '$100.00 CAD'),
            ('PAYMENT_TIMEFRAME', 'before April 17, 2022'),
            ('INTEREST_DETAILS', '10% of the amount owed'),
            ('CONFIDENTIALITY_TIMEFRAME', 'until 6 months after termination of the contract'),
            ('DELIVERY_SUSPENSION_CONDITION', 'if payment is not made'),
            ('DELIVERY_RESUMPTION_CONDITION', 'until payment is made'), # This is a timeframe...can be both?
            ('TERMINATION_CONDITION', 'unless such delay exceeds 10 days')
        ]

    def test_suite(self):
        contract = get_template()

        for key, value in self.customizations:
            doc = self.nlp(value)

            req = ContractUpdateRequest(contract, key, value, doc)
            contract = self.updater.update(req)
        

        self.maxDiff = None
        # could save actual and expected to files for comparison
        self.assertEqual(expected_contract.to_sym(), contract.to_sym())
         

if __name__ == '__main__':
    unittest.main()