import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import INorm
from app.classes.spec.predicate_function import PredicateFunction

from app.src.operations.refine_parameter.parm_configs import ParmOpCode
from app.src.operations.refine_parameter.operation_runner import RefinementOperationRunner, RefinementOperation

class RefinementOperationRunnerTests(unittest.TestCase):
    def setUp(self):
        self.contract = ISymboleoContract()
        self.sut = RefinementOperationRunner()

    def test_runner_add_norm(self):
        self.contract.add_norm = MagicMock(return_value=None)
        fake_norm = INorm()
        op = RefinementOperation(
            ParmOpCode.ADD_NORM,
            contract = self.contract,
            update_obj = fake_norm
        )
        self.sut.run(op)
        self.assertEqual(self.contract.add_norm.call_count, 1)
    

    def test_runner_add_trigger(self):
        fake_norm = INorm()
        fake_norm.update = MagicMock(return_value=None)
        fake_pred = PredicateFunction()
        op = RefinementOperation(
            ParmOpCode.ADD_TRIGGER,
            norm=fake_norm,
            update_obj = fake_pred
        )
        self.sut.run(op)
        self.assertEqual(fake_norm.update.call_count, 1)
    

    def test_runner_refine_predicate(self):
        fake_norm = INorm()
        fake_norm.update = MagicMock(return_value=None)
        fake_pred = PredicateFunction()

        op = RefinementOperation(
            ParmOpCode.REFINE_PREDICATE,
            norm = fake_norm,
            norm_component = 'X',
            update_obj = fake_pred
        )
        self.sut.run(op) 
        self.assertEqual(fake_norm.update.call_count, 1)

    def test_fail(self):
        op = RefinementOperation(
            None,
        )
        with self.assertRaises(Exception) as context:
            self.sut.run(op)
        
        self.assertTrue('Invalid operation' in str(context.exception))


if __name__ == '__main__':
    unittest.main()