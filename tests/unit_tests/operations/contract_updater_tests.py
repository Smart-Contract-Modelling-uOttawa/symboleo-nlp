import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.domain_object import IDomainObject
from app.classes.spec.declaration import IDeclaration

from app.classes.operations.op_code import OpCode
from app.classes.operations.contract_updater_config import UpdateConfig
from app.src.operations.refine_parameter.parameter_refiner import IRefineParameter
from app.src.operations.termination_updater import IAddPower
from app.src.operations.domain_updater import IUpdateDomain
from app.src.grammar.input_converter import IConvertInput

from app.src.operations.contract_updater import ContractUpdater

class ContractUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.contract = ISymboleoContract()

        self.input_converter = IConvertInput()
        self.input_converter.convert = MagicMock(return_value=[])

        self.parm_refiner = IRefineParameter()
        self.tp_adder = IAddPower()
        self.domain_updater = IUpdateDomain()
        self.sut = ContractUpdater(
            self.input_converter,
            self.parm_refiner,
            self.tp_adder,
            self.domain_updater
        )

    def test_refine_parm(self):
        self.parm_refiner.refine = MagicMock(return_value=None)

        config = UpdateConfig(
            node_list = [],
            parm_key='a'
        )
        self.sut.update(self.contract, OpCode.UPDATE_PARM, config)

        self.assertEqual(self.parm_refiner.refine.call_count, 1)
    

    def test_add_tp(self):
        self.tp_adder.update = MagicMock(return_value=None)

        config = UpdateConfig(
            norm_id = 'a',
            debtor = 'd',
            creditor = 'c',
            node_list = []
        )
        self.sut.update(self.contract, OpCode.ADD_TERMINATION_POWER, config)

        self.assertEqual(self.tp_adder.update.call_count, 1)
    

    def test_add_dobj(self):
        self.domain_updater.update = MagicMock(return_value=None)

        config = UpdateConfig(
            domain_object = IDomainObject(),
            declaration = IDeclaration()
        )
        self.sut.update(self.contract, OpCode.ADD_DOMAIN_OBJECT, config)

        self.assertEqual(self.domain_updater.update.call_count, 1)


if __name__ == '__main__':
    unittest.main()