import unittest
from unittest.mock import MagicMock

from app.src.operations.norm_adder import NormAdder

from tests.helpers.sample_norm_lib import SampleNorms
from tests.helpers.test_contract import get_test_contract


class NormAdderTests(unittest.TestCase):
    def setUp(self):
        self.sut = NormAdder()


    def test_norm_adder(self):
        contract = get_test_contract()
        new_norm = SampleNorms.get_sample_obligation('my_new_ob')

        result = self.sut.add(contract, new_norm)

        found_norm = result.contract_spec.obligations['my_new_ob']

        self.assertEqual(new_norm.to_sym(), found_norm.to_sym())




  
if __name__ == '__main__':
    unittest.main()