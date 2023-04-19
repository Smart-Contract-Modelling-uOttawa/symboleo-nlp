import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import INorm
from app.classes.frames.frame import Frame
from app.src.operations.refine_parameter.parm_configs import ParameterConfig
from app.src.grammar.selection import ISelection

from app.src.operations.refine_parameter.parameter_refiner import ParameterRefiner, ParameterOperation

from app.src.operations.refine_parameter.update_obj_creator import ICreateUpdateObj
from app.src.operations.refine_parameter.refinement_operation_runner import IRunRefinementOperation
from app.classes.other.update_obj import RefinementObj

class ParameterRefinerTests(unittest.TestCase):
    def setUp(self):
        self.operation_runner = IRunRefinementOperation()
        self.operation_runner.run = MagicMock(return_value=None)

        self.obj_creator = ICreateUpdateObj()
        self.obj_creator.create = MagicMock(return_value=RefinementObj())

        self.sut = ParameterRefiner(self.operation_runner, self.obj_creator)

    def test_parameter_refiner(self):
        # Set up contract
        contract = ISymboleoContract()
        fake_norm = INorm()
        fake_norm.get_default_event = MagicMock(return_value=None)
        contract.get_norm = MagicMock(return_value = fake_norm)
        selection = ISelection()
        
        # Run refinement
        op = ParameterOperation(ParameterConfig('a', 'b'), selection, '')
        self.sut.refine(contract, op)

        self.assertEqual(contract.get_norm.call_count, 1)
        self.assertEqual(self.obj_creator.create.call_count, 1)
        self.assertEqual(self.operation_runner.run.call_count, 1)
    

    def test_parameter_refiner_except(self):
        contract = ISymboleoContract()
        contract.get_norm = MagicMock(return_value = None)
        selection = ISelection()
        selection.get_update_obj = MagicMock(return_value = RefinementObj())
        
        op = ParameterOperation(ParameterConfig('a', 'b'), selection, '')
        self.sut.refine(contract, op)

        self.assertEqual(contract.get_norm.call_count, 1)
        self.assertEqual(self.obj_creator.create.call_count, 1)
        self.assertEqual(self.operation_runner.run.call_count, 1)


if __name__ == '__main__':
    unittest.main()