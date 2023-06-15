import unittest
from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.update_processor2.operation_mapper_builder import OperationMapperBuilder
from app.src.update_processor2.contract_updater import ContractUpdater
from app.src.update_processor2.nl_creator import NLCreator
from app.src.update_processor2.nl_fillers.nl_unit_filler_dict import NLUnitFillerDictConstructor

from app.src.operations.dependency_builder import DependencyBuilder
from tests.test_suites.nl_summary_builder import NLSummaryBuilder

from tests.test_suites.pattern_test_cases.dolphin import dolphin_test_case
from tests.test_suites.pattern_test_cases.if_event import if_event_test_case

test_suite = [
    dolphin_test_case,
    if_event_test_case
]


class PatternTests(unittest.TestCase):
    def setUp(self) -> None:
        deps = DependencyBuilder.build(fake=True)
        mapper = OperationMapperBuilder.build(deps)
        nl_filler_dict = NLUnitFillerDictConstructor.build()
        nl_creator = NLCreator(nl_filler_dict)
        self.contract_updater = ContractUpdater(mapper, nl_creator) 

    def test_isolated(self):
        filepath = 'tests/test_suites/pattern_results'
        for test_case in test_suite:
            k = test_case.case_id
            contract = test_case.init_sym
            
            # Print initial symboleo
            with open(f'{filepath}/{k}_sym_init.txt', 'w') as f:
                f.write(contract.to_sym())
            
            # Perform update
            self.contract_updater.update(
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