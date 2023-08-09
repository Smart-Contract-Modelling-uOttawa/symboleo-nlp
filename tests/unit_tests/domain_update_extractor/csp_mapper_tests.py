import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents, AssetDeclarations
from tests.helpers.test_contract import get_test_contract

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.src.domain_update_extractor.contract_parm_mapper import ContractParmMapper

class AssetDeclarationMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ContractParmMapper()

    def test_csp_mapper_empty(self):
        # no dobj
        test_evt = CustomEvents.legal_proceedings()
        pc = EventPatternClass()
        pc.nl_event = test_evt

        results = self.sut.map(pc)
        self.assertEqual(len(results), 0)
    
    def test_csp_mapper_dobj(self):
        test_evt = CustomEvents.eating_parm()
        pc = EventPatternClass()
        pc.nl_event = test_evt

        results = self.sut.map(pc)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, 'test_value')
        self.assertEqual(results[0].type, 'String')
    
    def test_csp_mapper_date(self):
        pc = PatternClass({
            PV.DATE: '[TEST_DATE]'
        })
        results = self.sut.map(pc)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, 'test_date')
        self.assertEqual(results[0].type, 'Date')

    def test_csp_mapper_real_date(self):
        pc = PatternClass({
            PV.DATE: 'March 20, 2024'
        })
        results = self.sut.map(pc)
        self.assertEqual(len(results), 0)

    
if __name__ == '__main__':
    unittest.main()