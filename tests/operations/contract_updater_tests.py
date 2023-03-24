import unittest
from unittest.mock import MagicMock

from app.src.operations.contract_updater import ContractUpdater, ContractOperation, IUpdateContractOp, OpCode
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

from tests.helpers.test_contract import get_test_contract

# IN PROGRESSS

class ContractUpdaterTests(unittest.TestCase):
    def setUp(self):
        new_contract = get_test_contract()
        new_contract.contract_spec.id = 'Updated!'
        self.fake1 = IUpdateContractOp()
        self.fake1.update = MagicMock(return_value = new_contract)

        self.fake2 = IUpdateContractOp()
        self.fake3 = IUpdateContractOp()
        self.sut = ContractUpdater(self.fake1, self.fake2, self.fake3)

    def test_true(self):
        contract = get_test_contract()

        contract_op = ContractOperation(OpCode.UPDATE_PARM, None)

        result = self.sut.update(contract, contract_op)

        self.assertEqual(result.contract_spec.id, 'Updated!')
        self.assertEqual(self.fake1.update.call_count, 1)

  
if __name__ == '__main__':
    unittest.main()