import unittest
from app.classes.spec.symboleo_contract import SymboleoContract
from app.templates.template_getter import get_template
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder


from tests.test_suites.full_test_cases.meat_sale import test_suite as meat_sale
from tests.test_suites.full_test_cases.rental import test_suite as rental
from tests.test_suites.full_test_cases.prop import test_suite as prop
from tests.test_suites.full_test_cases.biomass import test_suite as biomass
from tests.test_suites.full_test_cases.indep import test_suite as indep

test_dict = {
    'meat_sale': meat_sale,
    'rental': rental,
    'prop': prop,
    'biomass': biomass,
    'indep': indep
}

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.updater = ContractUpdaterBuilder.build()

    def test_full_stack(self):
        filepath = 'tests/test_suites/full_results'

        target_keys = [
            'meat_sale',
            'rental',
            'prop',
            'biomass',
            'indep'
        ]
        for k in target_keys:
            contract = get_template(f'{k}')
            expected_contract = get_template(f'{k}_raw')
            all_ops = test_dict[k]
            expected_sym = expected_contract.to_sym()
            expected_nl = expected_contract.nl_template.stringify()

            for i, test_config in enumerate(all_ops):
                self.updater.update(contract, test_config.op_code, test_config)

            result = contract.to_sym()
            result_nl = contract.nl_template.stringify()
            
            with open(f'{filepath}/{k}_sym_actual.txt', 'w') as f:
                f.write(result)
            
            with open(f'{filepath}/{k}_sym_expected.txt', 'w') as f:
                f.write(expected_sym)

            nl_summary = self._build_nl_summary(contract, expected_contract)
            with open(f'{filepath}/{k}_nl.txt', 'w') as f:
                f.write(nl_summary)

            # Verify Symboleo
            #self.assertEqual(result, expected_sym)

            # Verify NL
            #self.assertEqual(result_nl, expected_nl)


    # Pull out into a helper..
    def _build_nl_summary(self, contract: SymboleoContract, expected_contract: SymboleoContract):
        nl_summary = ''
        #nl_summary = f'==ACTUAL==\n{result_nl}\n\n==EXPECTED==\n{expected_nl}\n'
        for xk in contract.nl_template.template_dict:
            act_x = contract.nl_template.template_dict[xk].str_val
            
            if xk in expected_contract.nl_template.template_dict:
                exp_x = expected_contract.nl_template.template_dict[xk].str_val
            else:
                exp_x = ''
            nl_summary += f'A - {xk}: {act_x}\nE - {xk}: {exp_x}\n\n'
        
        for xk in expected_contract.nl_template.template_dict:
            act_x = ''
            if xk not in contract.nl_template.template_dict:
                exp_x = expected_contract.nl_template.template_dict[xk].str_val
                nl_summary += f'A - {xk}: {act_x}\nE - {xk}: {exp_x}\n\n'
            
        return nl_summary

if __name__ == '__main__':
    unittest.main()