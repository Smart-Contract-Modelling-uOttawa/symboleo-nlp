import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract

from app.src.grammar.selection import ISelection
from app.src.operations.add_power.termination_updater import TerminationUpdater, TerminationOperation
from app.src.operations.refine_parameter.parameter_refiner import IRefineParameter

class TerminationUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.parm_refiner = IRefineParameter()
        self.parm_refiner.refine = MagicMock(return_value=None)
        self.sut = TerminationUpdater(self.parm_refiner)

    def test_termination_upater(self):
        contract = ISymboleoContract()
        contract.add_norm = MagicMock(return_value = None)

        selection = ISelection()
        op = TerminationOperation('a', 'b', 'c', selection)    

        self.sut.update(contract, op)
        
        self.assertEqual(contract.add_norm.call_count, 1)
        self.assertEqual(self.parm_refiner.refine.call_count, 1)


if __name__ == '__main__':
    unittest.main()