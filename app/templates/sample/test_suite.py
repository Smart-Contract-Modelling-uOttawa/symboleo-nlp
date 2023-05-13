# Want to have a test where we convert the sample_t into sample_raw
# Eventually I want a NL -> Node list generator... Will replace this with that..
from app.classes.operations.user_input import UserInput, NodeType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.BEFORE),
            UserInput(NodeType.DATE, 'March 18, 2024'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='delivery',
        parm_key='P2'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.BEFORE),
            UserInput(NodeType.DATE, 'March 30, 2024'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='payment',
        parm_key='P2'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.NORM_EVENT),
            UserInput(NodeType.OBLIGATION_SUBJECT, 'ob_payment'),
            UserInput(NodeType.OBLIGATION_ACTION, 'Violated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='latePayment',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.UNTIL),
            UserInput(NodeType.TIMESPAN, '6 months'),
            UserInput(NodeType.AFTER),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='disclosure',
        parm_key='P2'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.NORM_EVENT),
            UserInput(NodeType.OBLIGATION_SUBJECT, 'ob_payment'),
            UserInput(NodeType.OBLIGATION_ACTION, 'Violated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='suspendDelivery',
        parm_key='P1'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.UNTIL),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.NORM_EVENT),
            UserInput(NodeType.OBLIGATION_SUBJECT, 'ob_late_payment'),
            UserInput(NodeType.OBLIGATION_ACTION, 'Fulfilled'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='suspendDelivery',
        parm_key = 'P2'
    ),
    
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.NORM_EVENT),
            UserInput(NodeType.OBLIGATION_SUBJECT, 'ob_delivery'),
            UserInput(NodeType.OBLIGATION_ACTION, 'Violated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        norm_id = 'pow_terminate_contract',
        debtor = 'buyer',
        creditor = 'seller'
    )
]