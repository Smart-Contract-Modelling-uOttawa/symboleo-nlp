import unittest
from unittest.mock import MagicMock

from tests.helpers.test_contract import get_test_contract

class ContractEqualityTests(unittest.TestCase):
    def test_contract_equality(self):
        c1 = get_test_contract()
        c2 = get_test_contract()
        
        self.assertEqual(c1, c2)
    
  
if __name__ == '__main__':
    unittest.main()