import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.domain_object import IDomainObject
from app.classes.spec.declaration import IDeclaration

from app.src.operations.refine_parameter.parm_configs import ParameterConfig
from app.classes.operations.op_code import OpCode
from app.classes.operations.contract_updater_config import UpdateConfig
from app.src.operations.refine_parameter.parameter_refiner import IRefineParameter
from app.src.operations.termination_updater import IAddPower
from app.src.operations.domain_updater import IUpdateDomain
from app.src.operations.contract_updater import ContractUpdater



class ContractUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.contract = ISymboleoContract()

        self.parm_refiner = IRefineParameter()
        self.tp_adder = IAddPower()
        self.domain_updater = IUpdateDomain()
        self.sut = ContractUpdater(
            self.parm_refiner,
            self.tp_adder,
            self.domain_updater
        )

    def test_refine_parm(self):
        self.parm_refiner.refine = MagicMock(return_value=None)

        config = UpdateConfig(
            op_code = None,
            parm_config = ParameterConfig('a', 'b'),
            selection = ISelection(),
            parm_key='a'
        )
        self.sut.update(self.contract, OpCode.UPDATE_PARM, config)

        self.assertEqual(self.parm_refiner.refine.call_count, 1)
    

    def test_add_tp(self):
        self.tp_adder.update = MagicMock(return_value=None)

        config = UpdateConfig(
            op_code = None,
            norm_id = 'a',
            debtor = 'd',
            creditor = 'c',
            selection = ISelection()
        )
        self.sut.update(self.contract, OpCode.ADD_TERMINATION_POWER, config)

        self.assertEqual(self.tp_adder.update.call_count, 1)
    

    def test_add_dobj(self):
        self.domain_updater.update = MagicMock(return_value=None)

        config = UpdateConfig(
            op_code = None,
            domain_object = IDomainObject(),
            declaration = IDeclaration()
        )
        self.sut.update(self.contract, OpCode.ADD_DOMAIN_OBJECT, config)

        self.assertEqual(self.domain_updater.update.call_count, 1)


    def test_fail(self):
        with self.assertRaises(Exception) as context:
            self.sut.update(self.contract, None, None)
        
        self.assertTrue('Invalid operation' in str(context.exception))


if __name__ == '__main__':
    unittest.main()