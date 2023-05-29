import unittest
from unittest.mock import MagicMock
from typing import Dict

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.domain_object import IDomainObject
from app.classes.spec.declaration import IDeclaration
from app.classes.units.unit_type import UnitType
from app.classes.operations.user_input import UserInput

from app.classes.operations.op_code import OpCode
from app.classes.operations.contract_updater_config import UpdateConfig
from app.src.operations.refine_parameter.parameter_refiner import IRefineParameter
from app.src.operations.termination_updater import IAddPower
from app.src.operations.domain_updater import IUpdateDomain
from app.src.operations.contract_updater import ContractUpdater

from app.src.extractors.value_extractor import IExtractValue
from app.src.grammar.element_extractor import ElementExtractor

# TODO: ...
class ElementExtractorTests(unittest.TestCase):
    def setUp(self):
        self.extractor1 = IExtractValue()
        self.extractor2 = IExtractValue()
        self.extractor_dict: Dict[UnitType, IExtractValue] = {
            UnitType.BEFORE: self.extractor1,
            UnitType.CONTRACT_SUBJECT: self.extractor2
        }
        self.sut = ElementExtractor(self.extractor_dict)

    @unittest.skip('TODO')
    def test_refine_parm(self):
        # Arbitrary
        test_input = [
            UserInput(UnitType.BEFORE),
            UserInput(UnitType.CONTRACT_SUBJECT)
        ]

        self.extractor1.extract = MagicMock(return_value='Test')
        self.extractor2.extract = MagicMock(return_value='Test2')

        result = self.sut.convert(test_input)

        
if __name__ == '__main__':
    unittest.main()