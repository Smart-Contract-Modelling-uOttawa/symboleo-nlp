import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import INorm
from app.classes.frames.frame import Frame
from app.src.operations.parm_configs import ParmOpCode, ParameterConfig
from app.src.grammar.selection import ISelection

from app.src.frames.frame_checker import ICheckFrames
from app.src.operations.refine_parameter.parameter_refiner import ParameterRefiner, ParameterOperation
from app.src.operations.refine_parameter.operation_runner import IRunRefinementOperation, RefinementOperation

class ParameterRefinerTests(unittest.TestCase):
    def setUp(self):
        self.frame_checker = ICheckFrames()
        fake_frame = Frame()
        fake_frame.op_code = ParmOpCode.REFINE_PREDICATE
        self.frame_checker.check_all_frames = MagicMock(return_value=[fake_frame])

        self.runner = IRunRefinementOperation()
        self.runner.run = MagicMock(return_value=None)

        self.sut = ParameterRefiner(self.frame_checker, self.runner)


    def test_parameter_refiner(self):
        contract = ISymboleoContract()
        fake_norm = INorm()
        fake_norm.get_default_event = MagicMock(return_value=None)
        contract.get_norm = MagicMock(return_value = fake_norm)

        selection = ISelection()
        selection.to_obj = MagicMock(return_value = None)
        selection.get_nodes = MagicMock(return_value=[])
        parm_config = ParameterConfig('a', 'b')
        op = ParameterOperation(parm_config, selection)
        
        self.sut.refine(contract, op)
        
        self.assertEqual(self.frame_checker.check_all_frames.call_count, 1)
        self.assertEqual(contract.get_norm.call_count, 1)
        self.assertEqual(fake_norm.get_default_event.call_count, 1)
        self.assertEqual(selection.to_obj.call_count, 1)
        self.assertEqual(self.runner.run.call_count, 1)
    
    def test_parameter_refiner_except(self):
        contract = ISymboleoContract()
        contract.get_norm = MagicMock(return_value = None)

        selection = ISelection()
        selection.to_obj = MagicMock(return_value = None)
        selection.get_nodes = MagicMock(return_value=[])
        parm_config = ParameterConfig('a', 'b')
        op = ParameterOperation(parm_config, selection)
        
        self.sut.refine(contract, op)
        
        self.assertEqual(self.frame_checker.check_all_frames.call_count, 1)
        self.assertEqual(contract.get_norm.call_count, 1)
        self.assertEqual(selection.to_obj.call_count, 1)
        self.assertEqual(self.runner.run.call_count, 1)


if __name__ == '__main__':
    unittest.main()