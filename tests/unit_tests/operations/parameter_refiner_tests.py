import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import INorm
from app.classes.patterns.pattern import Pattern
from app.classes.operations.contract_update_obj import ContractUpdateObj
from app.classes.operations.parameter_operation import ParameterOperation

from app.src.pattern_builder.pattern_builder import IBuildPatterns
from app.src.update_processor.update_processor import IProcessUpdates
from app.src.operations.parameter_refiner import ParameterRefiner

class ContractUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.contract = ISymboleoContract()

        self.pattern_builder = IBuildPatterns()
        fake_pattern = Pattern()
        self.pattern_builder.build = MagicMock(return_value=fake_pattern)

        self.update_processor = IProcessUpdates()
        fake_update = ContractUpdateObj()
        self.update_processor.process = MagicMock(return_value=fake_update)

        self.sut = ParameterRefiner(self.pattern_builder, self.update_processor)

    def test_refine_parm(self):
        contract = ISymboleoContract()
        contract.get_norms_by_key = MagicMock(return_value=[INorm(), INorm()])
        contract.run_updates = MagicMock(return_value=None)
        contract.update_nl = MagicMock(return_value=None)

        op = ParameterOperation('test', 'test_parm', [])
        
        self.sut.refine(contract, op)

        self.assertEqual(self.pattern_builder.build.call_count, 1)
        self.assertEqual(self.update_processor.process.call_count, 2)
        self.assertEqual(contract.run_updates.call_count, 2)
        self.assertEqual(contract.update_nl.call_count, 1)


if __name__ == '__main__':
    unittest.main()