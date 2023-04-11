# Want to have a test where we convert the sample_t into sample_raw
# Eventually I want a NL -> Node list generator... Will replace this with that..

from app.classes.selection.all_nodes import BeforeNode, ContractEventActionNode, ContractEventNode, DomainTimepointNode, EventNode, IfNode, ObligationEventActionNode, ObligationEventNode, ObligationEventVarNode, RootNode, TimepointNode, TimespanNode, UntilNode, WithinNode
from app.src.grammar.selection import Selection
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode
from app.src.operations.parm_configs import ParameterConfig

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            BeforeNode('', 0),
            TimepointNode('', 0),
            DomainTimepointNode('', 0, 'evt_delivered.delDueDate')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_delivery')
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            BeforeNode('', 0),
            TimepointNode('', 0),
            DomainTimepointNode('', 0, 'evt_paid.payDueDate')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_payment')
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'ob_payment'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_late_payment')
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
        parm_config = ParameterConfig('surviving_obligations', 'so1')
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
        parm_config = ParameterConfig('surviving_obligations', 'so2')
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'ob_payment'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = ParameterConfig('powers', 'pow_suspend_delivery')
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            UntilNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'ob_late_payment'),
            ObligationEventActionNode('', 0, 'Fulfilled')
        ]),
        parm_config = ParameterConfig('powers', 'pow_suspend_delivery')
    ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'ob_delivery'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = ParameterConfig('powers', 'pow_terminate_contract', 'trigger'),
        norm_id = 'pow_terminate_contract',
        debtor = 'buyer',
        creditor = 'seller'
    )
]