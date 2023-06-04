import unittest
from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

from tests.test_suites.nl_summary_builder import NLSummaryBuilder
from tests.test_suites.isolated_test_cases.dolphin import dolphin_test_case
from tests.test_suites.isolated_test_cases.maimon import maimon_test_case
from tests.test_suites.isolated_test_cases.franchise import franchise_test_case
from tests.test_suites.isolated_test_cases.fox import fox_test_case
from tests.test_suites.isolated_test_cases.letter import letter_test_case
from tests.test_suites.isolated_test_cases.bosch import bosch_test_case

test_suite = [
    dolphin_test_case,
    maimon_test_case,
    franchise_test_case,
    fox_test_case,
    letter_test_case,
    bosch_test_case
]


class IsolatedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.updater = ContractUpdaterBuilder.build()

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
                test_case.update_config)

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