import unittest
from unittest.mock import MagicMock

from app.src.operations.contract_updater import ContractUpdater, ContractOperation
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

from tests.helpers.sample_norm_lib import SampleNorms

# IN PROGRESSS

class ContractUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = ContractUpdaterBuilder.build()


    def test_true(self):
        self.assertTrue(True)

  
if __name__ == '__main__':
    unittest.main()