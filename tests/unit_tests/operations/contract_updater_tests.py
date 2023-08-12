import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.parameter_config import ParameterConfig
from app.classes.operations.op_code import OpCode
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.spec.norm import INorm
from app.classes.operations.contract_update_obj import ContractUpdateObj

from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.operation_mapper import IMapCnlToOperations

class ContractUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.operation_mapper = IMapCnlToOperations()

        self.sut = ContractUpdater(self.operation_mapper)


    def test_contract_updater(self):
        contract = ISymboleoContract()
        fake_configs = [NormConfig(INorm(), ParameterConfig('a', 'b', 'c'))]
        contract.get_norm_configs_by_key = MagicMock(return_value=fake_configs)

        contract.run_updates = MagicMock(return_value = None)
        contract.update_nl = MagicMock(return_value = None)

        self.operation_mapper.map = MagicMock(return_value=ContractUpdateObj())

        self.sut.update(contract, OpCode.UPDATE_PARM, UpdateConfig())

        self.assertEqual(contract.run_updates.call_count, 1)
        self.assertEqual(contract.update_nl.call_count, 1)
        self.assertEqual(contract.get_norm_configs_by_key.call_count, 1)
        self.assertEqual(self.operation_mapper.map.call_count, 1)


if __name__ == '__main__':
    unittest.main()
