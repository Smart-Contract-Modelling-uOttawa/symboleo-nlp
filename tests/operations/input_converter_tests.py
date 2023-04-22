import unittest
from unittest.mock import MagicMock
from typing import Dict

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.domain_object import IDomainObject
from app.classes.spec.declaration import IDeclaration
from app.classes.tokens.node_type import NodeType
from app.classes.operations.user_input import UserInput

from app.src.operations.refine_parameter.parm_configs import ParameterConfig
from app.classes.operations.op_code import OpCode
from app.classes.operations.contract_updater_config import UpdateConfig
from app.src.operations.refine_parameter.parameter_refiner import IRefineParameter
from app.src.operations.termination_updater import IAddPower
from app.src.operations.domain_updater import IUpdateDomain
from app.src.operations.contract_updater import ContractUpdater

from app.src.extractors.value_extractor import IExtractValue
from app.src.operations.input_converter import InputConverter


class InputConverterTests(unittest.TestCase):
    def setUp(self):
        self.extractor1 = IExtractValue()
        self.extractor2 = IExtractValue()
        self.extractor_dict: Dict[NodeType, IExtractValue] = {
            NodeType.BEFORE: self.extractor1,
            NodeType.CONTRACT_SUBJECT: self.extractor2
        }
        self.sut = InputConverter(self.extractor_dict)


    def test_refine_parm(self):
        # Arbitrary
        test_input = [
            UserInput(NodeType.BEFORE),
            UserInput(NodeType.CONTRACT_SUBJECT)
        ]

        self.extractor1.extract = MagicMock(return_value='Test')
        self.extractor2.extract = MagicMock(return_value='Test2')

        result = self.sut.convert(test_input)


        print(result)
        
if __name__ == '__main__':
    unittest.main()