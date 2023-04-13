import unittest
from unittest.mock import MagicMock

from tests.helpers.test_contract import get_test_contract

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import INorm
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.frames.frame import Frame

from app.src.operations.refine_parameter.parm_configs import ParmOpCode
from app.src.operations.refine_parameter.operation_runner import RefinementOperationRunner, RefinementOperation

class RefinementOperationRunnerTests(unittest.TestCase):
    def setUp(self):
        self.contract = ISymboleoContract()
        self.frame = Frame()
        self.frame.to_text = MagicMock(return_value='test')
        self.sut = RefinementOperationRunner()

    def test_runner_add_norm(self):
        self.contract.add_norm = MagicMock(return_value=None)
        fake_norm = INorm()
        self.frame.op_code = ParmOpCode.ADD_NORM

        op = RefinementOperation(
            key = 'x',
            frame = self.frame,
            contract = self.contract,
            update_obj = fake_norm
        )
        self.sut.run(op)
        self.assertEqual(self.contract.add_norm.call_count, 1)
    

    def test_runner_add_trigger(self):
        fake_norm = INorm()
        self.contract.update_norm = MagicMock(return_value=None)
        fake_pred = PredicateFunction()

        self.frame.op_code = ParmOpCode.ADD_TRIGGER
        op = RefinementOperation(
            key = 'x',
            frame = self.frame,
            contract = self.contract,
            norm = fake_norm,
            update_obj = fake_pred
        )
        self.sut.run(op)
        self.assertEqual(self.contract.update_norm.call_count, 1)
    

    def test_runner_refine_predicate(self):
        fake_norm = INorm()
        self.contract.update_norm = MagicMock(return_value=None)
        fake_pred = PredicateFunction()
        self.frame.op_code = ParmOpCode.REFINE_PREDICATE

        op = RefinementOperation(
            key = 'x',
            frame = self.frame,
            contract = self.contract,
            norm = fake_norm,
            norm_component = 'X',
            update_obj = fake_pred
        )
        self.sut.run(op) 
        self.assertEqual(self.contract.update_norm.call_count, 1)


    def test_fail(self):
        self.frame.op_code = None
        op = RefinementOperation(
            'x',
            self.frame,
        )
        with self.assertRaises(Exception) as context:
            self.sut.run(op)
        
        self.assertTrue('Invalid operation' in str(context.exception))


if __name__ == '__main__':
    unittest.main()