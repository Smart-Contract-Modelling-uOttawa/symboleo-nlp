import unittest
from typing import List
from app.src.helpers.template_getter import get_template
from app.src.grammar.selection import Selection, SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.operations.contract_updater import OpCode

from app.src.operations.contract_updater_builder import ContractUpdaterBuilder
from app.src.operations.contract_updater_config import UpdateConfig

from app.templates.sample.t.nl_template import parameters

# Want to have a test where we convert the sample_t into sample_raw
# Eventually I want a NL -> Node list generator... Will replace this with that..

all_ops = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            BeforeNode('', 0),
            TimepointNode('', 0),
            DomainTimepointNode('', 0, 'delivered.delDueDate')
        ]),
        parm_config = parameters['DELIVERY_REFINEMENT'].configs[0]
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            BeforeNode('', 0),
            TimepointNode('', 0),
            DomainTimepointNode('', 0, 'paid.payDueDate')
        ]),
        parm_config = parameters['PAYMENT_REFINEMENT'].configs[0]
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'payment'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = parameters['LATE_PAYMENT_CONDITION'].configs[0]
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            WithinNode('', 0),
            TimespanNode('', 0, '6 months'),
            EventNode('', 0),
            ContractEventNode('',0),
            ContractEventActionNode('', 0, 'Activated')
        ]),
        parm_config = parameters['CONFIDENTIALITY_REFINEMENT'].configs[0]
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            WithinNode('', 0),
            TimespanNode('', 0, '6 months'),
            EventNode('', 0),
            ContractEventNode('',0),
            ContractEventActionNode('', 0, 'Activated')
        ]),
        parm_config = parameters['CONFIDENTIALITY_REFINEMENT'].configs[1]
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'payment'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = parameters['DELIVERY_SUSPENSION_CONDITION'].configs[0]
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'delivery'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = parameters['TERMINATION_EXCEPTION'].configs[0]
    )
]

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ContractUpdaterBuilder.build()

    @unittest.skip('skip when measuring coverage')
    def test_full_stack(self):
        contract = get_template('sample_t')
        expected_contract = get_template('sample_raw')
        expected_sym = expected_contract.to_sym()

        for test_config in all_ops:
            self.sut.update(contract, test_config.op_code, test_config)

        result = contract.to_sym()
        self.assertEqual(result, expected_sym)
        

if __name__ == '__main__':
    unittest.main()