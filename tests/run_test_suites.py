import unittest
from app.templates.template_getter import get_template, get_test_suite
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ContractUpdaterBuilder.build()

    def test_full_stack(self):
        target_keys = [
            #'sample',
            #'rental',
            'prop',
        ]
        for k in target_keys:
            contract = get_template(f'{k}_t')
            expected_contract = get_template(f'{k}_raw')
            all_ops = get_test_suite(k)
            expected_sym = expected_contract.to_sym()
            expected_nl = expected_contract.nl_template.stringify()

            for i,test_config in enumerate(all_ops):
                print(i)
                self.sut.update(contract, test_config.op_code, test_config)

            result = contract.to_sym()
            result_nl = contract.nl_template.stringify()
            
            with open('tests/sample_target.txt', 'w') as f:
                f.write(result)

            with open('tests/sample_target_nl.txt', 'w') as f:
                f.write(result_nl)

            # Verify Symboleo
            self.assertEqual(result, expected_sym)

            # Verify NL
            self.assertEqual(result_nl, expected_nl)

        

if __name__ == '__main__':
    unittest.main()