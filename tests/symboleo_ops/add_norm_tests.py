import unittest
from unittest.mock import MagicMock

from tests.helpers.sample_norm_lib import SampleNorms
from tests.helpers.test_contract import get_test_contract


class NormAdderTests(unittest.TestCase):
    def test_norm_adder(self):
        contract = get_test_contract()
        new_norm = SampleNorms.get_sample_obligation('my_new_ob')

        contract.add_norm(new_norm, 'new_norm', 'this is a new norm')

        found_norm = contract.contract_spec.obligations['my_new_ob']
        found_nl = contract.nl_template.template_dict['new_norm']

        self.assertEqual(new_norm.to_sym(), found_norm.to_sym())
        self.assertEqual(found_nl.str_val, 'this is a new norm')
        self.assertEqual(found_nl.mapping[0], 'obligations.my_new_ob')




  
if __name__ == '__main__':
    unittest.main()