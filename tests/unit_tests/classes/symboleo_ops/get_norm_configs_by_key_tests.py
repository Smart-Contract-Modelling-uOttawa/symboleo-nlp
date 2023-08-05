import unittest
from unittest.mock import MagicMock

from tests.helpers.test_contract import get_test_contract

class GetNormConfigsTests(unittest.TestCase):
    def test_get_norm_configs(self):
        contract = get_test_contract()
        
        results = contract.get_norm_configs_by_key('test_nl_key', 'P1')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].norm.id, 'test_obligation')
    
  
if __name__ == '__main__':
    unittest.main()