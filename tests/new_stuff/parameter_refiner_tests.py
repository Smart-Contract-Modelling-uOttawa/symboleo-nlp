import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import INorm
from app.classes.frames.frame import Frame
from app.classes.operations.contract_update_obj import ContractUpdateObj

from app.src.frames.frame_checker import ICheckFrames
from app.src.sym_updaters.update_extractor import IExtractUpdates
from app.src.operations.refine_parameter.parameter_refiner import ParameterRefiner, ParameterOperation

class ParameterRefinerTests(unittest.TestCase):
    def setUp(self):
        self.frame_checker = ICheckFrames()
        self.frame_checker.get_frame = MagicMock(return_value=Frame)

        self.update_extractor = IExtractUpdates()
        self.update_extractor.extract = MagicMock(return_value=ContractUpdateObj())

        self.sut = ParameterRefiner(self.frame_checker, self.update_extractor)

    def test_parameter_refiner(self):
        # Set up contract
        contract = ISymboleoContract()
        contract.get_norm_by_key = MagicMock(return_value = INorm())
        contract.update_nl = MagicMock(return_value = None)
        contract.run_updates = MagicMock(return_value = None)


        # Run refinement
        node_list = []
        op = ParameterOperation(node_list, '')
        self.sut.refine(contract, op)

        self.assertEqual(contract.get_norm_by_key.call_count, 1)
        self.assertEqual(contract.run_updates.call_count, 1)
        self.assertEqual(contract.update_nl.call_count, 1)
        self.assertEqual(self.update_extractor.extract.call_count, 1)
        self.assertEqual(self.frame_checker.get_frame.call_count, 1)


if __name__ == '__main__':
    unittest.main()