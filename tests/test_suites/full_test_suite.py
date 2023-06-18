import unittest
from app.classes.spec.symboleo_contract import SymboleoContract
from app.templates.template_getter import get_template
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder
from app.src.operations.dependency_builder import DependencyBuilder

from tests.test_suites.nl_summary_builder import NLSummaryBuilder
from tests.test_suites.full_test_cases.meat_sale import test_suite as meat_sale
from tests.test_suites.full_test_cases.rental import test_suite as rental
from tests.test_suites.full_test_cases.prop import test_suite as prop
from tests.test_suites.full_test_cases.biomass import test_suite as biomass
from tests.test_suites.full_test_cases.indep import test_suite as indep
from tests.test_suites.full_test_cases.sample import test_suite as sample

test_dict = {
    'meat_sale': meat_sale,
    'rental': rental,
    'prop': prop,
    'biomass': biomass,
    'indep': indep,
    'sample': sample
}

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        deps = DependencyBuilder.build(fake=True)
        self.updater = ContractUpdaterBuilder.build(deps)

    def test_full_stack(self):
        filepath = 'tests/test_suites/full_results'

        target_keys = [
            # 'meat_sale',
            # 'rental',
            # 'prop',
            # 'biomass',
            # 'indep',
            'sample'
        ]

        for k in target_keys:
            contract = get_template(f'{k}')
            expected_contract = get_template(f'{k}_raw')
            all_updates = test_dict[k]

            # Run all updates in test suite
            for i, test_config in enumerate(all_updates):
                self.updater.update(contract, test_config.op_code, test_config)

            # Print the actual contract
            with open(f'{filepath}/{k}_sym_actual.txt', 'w') as f:
                f.write(contract.to_sym())
            
            # Print the expected contract
            with open(f'{filepath}/{k}_sym_expected.txt', 'w') as f:
                f.write(expected_contract.to_sym())

            # Summarize NL
            nl_summary = NLSummaryBuilder.build(contract, expected_contract)
            with open(f'{filepath}/{k}_nl.txt', 'w') as f:
                f.write(nl_summary)



if __name__ == '__main__':
    unittest.main()