import unittest
from typing import List
from app.src.helpers.template_getter import get_template
from app.src.grammar.selection import Selection, SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.operations.contract_updater import OpCode
from tests.test_suites.test_runner import TestConfig, TestRunner

from app.templates.rental_agreement.t.nl_template import parameters

all_ops = [
    TestConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'pay_rent'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = parameters['LATE_PAYMENT_CONDITION'].configs[0]
    )
]

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = TestRunner()

    @unittest.skip('In progress')
    def test_full_stack(self):
        contract = get_template('rental_t')
        expected_contract = get_template('rental_raw')
        expected_sym = expected_contract.to_sym()

        for test_config in all_ops:
            contract = self.runner.update_contract(contract, test_config)

        result = contract.to_sym()
        self.assertEqual(result, expected_sym)
        

if __name__ == '__main__':
    unittest.main()