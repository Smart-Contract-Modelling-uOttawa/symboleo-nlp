import unittest
from unittest.mock import MagicMock

from app.src.operations.helpers.predicate_processor import IProcessPredicates
from app.src.operations.parm_operations.predicate_refiner import PredicateRefiner

from tests.helpers.test_contract import get_test_contract


class PredicateRefinerTests(unittest.TestCase):
    def setUp(self):
        self.fake_predicate_processor = IProcessPredicates()
        self.fake_contract = get_test_contract()
        self.fake_predicate_processor.process = MagicMock(return_value=self.fake_contract)
        self.sut = PredicateRefiner(self.fake_predicate_processor)


    def test_predicate_refiner(self):
        result = self.sut.refine(None, None, None)
        self.assertEqual(result.to_sym(), self.fake_contract.to_sym())

        self.assertEqual(self.fake_predicate_processor.process.call_count, 1)



  
if __name__ == '__main__':
    unittest.main()