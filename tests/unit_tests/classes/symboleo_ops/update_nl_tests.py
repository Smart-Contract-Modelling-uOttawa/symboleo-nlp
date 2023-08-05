import unittest
from unittest.mock import MagicMock

from tests.helpers.test_contract import get_test_contract

class UpdateNLTests(unittest.TestCase):
    def test_run_update(self):
        contract = get_test_contract()

        contract.update_nl('test_nl_key', 'P1', 'before Y happens')

        self.assertTrue(contract.nl_template.template_dict['test_nl_key'].parameters['P1'][0].filled)
        self.assertEqual(contract.nl_template.template_dict['test_nl_key'].str_val, 'Event X happens before Y happens')
  
if __name__ == '__main__':
    unittest.main()