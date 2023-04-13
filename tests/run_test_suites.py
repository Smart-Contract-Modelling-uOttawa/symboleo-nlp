import unittest
from app.templates.template_getter import get_template, get_test_suite
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ContractUpdaterBuilder.build()

    def test_full_stack(self):
        target_keys = [
            'sample',
            'rental',
            'prop',
        ]
        for k in target_keys:
            contract = get_template(f'{k}_t')
            expected_contract = get_template(f'{k}_raw')
            all_ops = get_test_suite(k)
            expected_sym = expected_contract.to_sym()

            for i,test_config in enumerate(all_ops):
                self.sut.update(contract, test_config.op_code, test_config)

            result = contract.to_sym()
            
            with open('tests/sample_target.txt', 'w') as f:
                f.write(result)
        
            self.assertEqual(result, expected_sym)
        

if __name__ == '__main__':
    unittest.main()