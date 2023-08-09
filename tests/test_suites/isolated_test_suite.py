import unittest
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder
from app.src.operations.dependency_builder import DependencyBuilder

from tests.test_suites.nl_summary_builder import NLSummaryBuilder
from tests.test_suites.isolated_test_cases.dolphin import test_case as dolphin_test
from tests.test_suites.isolated_test_cases.maimon import test_case as maimon_test
from tests.test_suites.isolated_test_cases.franchise import test_case as franchise_test
from tests.test_suites.isolated_test_cases.cisco import test_case as cisco_test
from tests.test_suites.isolated_test_cases.porex import test_case as porex_test
from tests.test_suites.isolated_test_cases.tianhe import test_case as tianhe_test
from tests.test_suites.isolated_test_cases.prime import test_case as prime_test

test_suite = [
    dolphin_test,
    maimon_test,
    franchise_test,
    cisco_test,
    porex_test,
    tianhe_test,
    prime_test
]

# test_suite = [
#     prime_test
# ]

class IsolatedTests(unittest.TestCase):
    def setUp(self) -> None:
        deps = DependencyBuilder.build(fake=True)
        self.updater = ContractUpdaterBuilder.build(deps)


    def test_isolated(self):
        filepath = 'tests/test_suites/isolated_results'
        for test_case in test_suite:
            k = test_case.case_id
            contract = test_case.init_sym
            
            # Print initial symboleo
            with open(f'{filepath}/{k}_sym_init.txt', 'w') as f:
                f.write(contract.to_sym())
            
            # Perform update
            self.updater.update(
                contract, 
                test_case.op_code,
                test_case.update_config
            )

            # Print the actual and expected            
            with open(f'{filepath}/{k}_sym_actual.txt', 'w') as f:
                f.write(contract.to_sym())
            
            with open(f'{filepath}/{k}_sym_expected.txt', 'w') as f:
                f.write(test_case.exp_sym.to_sym())

            # Print the NL Summary
            nl_summary = NLSummaryBuilder.build(contract, test_case.exp_sym)
            with open(f'{filepath}/{k}_nl.txt', 'w') as f:
                f.write(nl_summary)

            # Verify Symboleo
            self.assertEqual(contract, test_case.exp_sym)


if __name__ == '__main__':
    unittest.main()