import unittest
from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

from tests.test_suites.rq3.dolphin import dolphin_test_case
from tests.test_suites.rq3.maimon import maimon_test_case
from tests.test_suites.rq3.franchise import franchise_test_case
from tests.test_suites.rq3.fox import fox_test_case
from tests.test_suites.rq3.letter import letter_test_case


test_suite = [
    dolphin_test_case,
    maimon_test_case,
    franchise_test_case,
    fox_test_case,
    letter_test_case
]


class IsolatedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.updater = ContractUpdaterBuilder.build()

    def test_isolated(self):
        
        for test_case in test_suite:
            contract = test_case.init_sym
            self.updater.update(
                contract, 
                test_case.op_code,
                test_case.update_config)


            #print(contract.to_sym())

            #self.assertEqual(contract, test_case.exp_sym)

            result = contract.to_sym()
            result_nl = contract.nl_template.stringify()
            k = test_case.case_id
            with open(f'tests/test_results/{k}_sym_actual.txt', 'w') as f:
                f.write(result)
            
            with open(f'tests/test_results/{k}_sym_expected.txt', 'w') as f:
                f.write(test_case.exp_sym.to_sym())

            nl_summary = self._build_nl_summary(contract, test_case.exp_sym)
            with open(f'tests/test_results/{k}_nl.txt', 'w') as f:
                f.write(nl_summary)

            # Verify Symboleo
            self.assertEqual(contract, test_case.exp_sym)

            # Verify NL
            #self.assertEqual(result_nl, expected_nl)

    
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