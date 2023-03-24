import unittest
from unittest.mock import MagicMock

from app.src.operations.parm_operations.configs import ParameterConfig
from app.src.operations.helpers.predicate_processor import IProcessPredicates
from app.src.operations.parm_operations.trigger_adder import TriggerAdder

from tests.helpers.test_contract import get_test_contract


class TriggerAdderTests(unittest.TestCase):
    def setUp(self):
        self.fake_predicate_processor = IProcessPredicates()
        self.fake_contract = get_test_contract()
        self.fake_predicate_processor.process = MagicMock(return_value=self.fake_contract)
        self.sut = TriggerAdder(self.fake_predicate_processor)


    def test_trigger_adder(self):
        config = ParameterConfig('', '', '')
        result = self.sut.update(None, config, None)
        self.assertEqual(result.to_sym(), self.fake_contract.to_sym())
        self.assertEqual(self.fake_predicate_processor.process.call_count, 1)



  
if __name__ == '__main__':
    unittest.main()