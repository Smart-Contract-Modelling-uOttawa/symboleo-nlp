import unittest
from app.templates.template_getter import get_template, get_test_suite
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.updater = ContractUpdaterBuilder.build()

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

            for i, test_config in enumerate(all_ops):
                print(i)
                self.updater.update(contract, test_config.op_code, test_config)

            result = contract.to_sym()
            result_nl = contract.nl_template.stringify()
            
            with open(f'tests/sample_target_{k}.txt', 'w') as f:
                f.write(result)


            nl_summary = f'==ACTUAL==\n{result_nl}\n\n==EXPECTED==\n{expected_nl}\n'

            with open(f'tests/sample_target_nl_{k}.txt', 'w') as f:
                f.write(nl_summary)

            # Verify Symboleo
            self.assertEqual(result, expected_sym)

            # Verify NL
            self.assertEqual(result_nl, expected_nl)

        

if __name__ == '__main__':
    unittest.main()