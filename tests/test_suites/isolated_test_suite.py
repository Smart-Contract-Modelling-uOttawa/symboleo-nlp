import unittest
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder
from app.src.operations.dependency_builder import DependencyBuilder

from tests.test_suites.nl_summary_builder import NLSummaryBuilder
from tests.test_suites.isolated_test_cases.within_timespan_event import test_case as within_timespan_event_test
from tests.test_suites.isolated_test_cases.cond_a_event import test_case as cond_a_event_test
from tests.test_suites.isolated_test_cases.before_date import test_case as before_date_test
from tests.test_suites.isolated_test_cases.before_event import test_case as before_event_test
from tests.test_suites.isolated_test_cases.timespan_after_event import test_case as timespan_after_event_test
from tests.test_suites.isolated_test_cases.timespan_before_event import test_case as timespan_before_event_test
from tests.test_suites.isolated_test_cases.until_event import test_case as until_event_test
from tests.test_suites.isolated_test_cases.after_timespan_after_event import test_case as after_timespan_after_event_test
from tests.test_suites.isolated_test_cases.after_date import test_case as after_date_test
from tests.test_suites.isolated_test_cases.during_time_period import test_case as during_time_period_test
from tests.test_suites.isolated_test_cases.for_timespan import test_case as for_timespan_test
from tests.test_suites.isolated_test_cases.between_interval import test_case as between_interval_test
from tests.test_suites.isolated_test_cases.cond_t_event import test_case as cond_t_event_test
from tests.test_suites.isolated_test_cases.except_event import test_case as except_event_test
from tests.test_suites.isolated_test_cases.until_date import test_case as until_date_test

test_suite = [
    after_date_test,
    after_timespan_after_event_test,
    before_date_test,
    before_event_test,
    between_interval_test,
    cond_a_event_test,
    cond_t_event_test,
    during_time_period_test,
    except_event_test,
    for_timespan_test,
    timespan_after_event_test,
    timespan_before_event_test,
    until_date_test,
    until_event_test,
    within_timespan_event_test,
]

# test_suite = [
#     until_date_test
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