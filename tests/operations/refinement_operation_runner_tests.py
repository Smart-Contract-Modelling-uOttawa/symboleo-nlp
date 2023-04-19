import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import INorm

from app.src.operations.refine_parameter.predicate_updater import IUpdatePredicate
from app.src.operations.refine_parameter.trigger_adder import IAddTrigger
from app.src.operations.refine_parameter.norm_adder import IAddNorm
from app.src.operations.refine_parameter.refinement_operation_runner import RefinementOperationRunner
from app.classes.other.update_obj import *

class RefinementOperationRunnerTests(unittest.TestCase):
    def setUp(self):
        self.predicate_updater = IUpdatePredicate()
        self.trigger_adder = IAddTrigger()
        self.norm_adder = IAddNorm()

        self.contract = ISymboleoContract()
        self.norm = INorm()
        
        self.sut = RefinementOperationRunner(self.predicate_updater, self.trigger_adder, self.norm_adder)


    def test_predicate_update(self):
        self.predicate_updater.update = MagicMock(return_value=None)

        update_obj = PredicateRefinementObj(None, None)
        self.sut.run(self.contract, update_obj, self.norm, '')
                
        self.assertEqual(self.predicate_updater.update.call_count, 1)
    

    def test_add_trigger(self):
        self.trigger_adder.add = MagicMock(return_value=None)

        update_obj = AddTriggerObj(None, None)
        self.sut.run(self.contract, update_obj, self.norm, '')
                
        self.assertEqual(self.trigger_adder.add.call_count, 1)
    

    def test_add_norm(self):
        self.norm_adder.add = MagicMock(return_value=None)

        update_obj = AddNormObj(None)
        self.sut.run(self.contract, update_obj, self.norm, '')
                
        self.assertEqual(self.norm_adder.add.call_count, 1)

if __name__ == '__main__':
    unittest.main()