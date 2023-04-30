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
            UserInput(NodeType.TIMEPOINT),
            UserInput(NodeType.DOMAIN_TIMEPOINT, 'evt_delivered.delDueDate'),
            UserInput(NodeType.FINAL_NODE)
        ],
        parm_key='delivery'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.BEFORE),
            UserInput(NodeType.TIMEPOINT),
            UserInput(NodeType.DOMAIN_TIMEPOINT, 'evt_paid.payDueDate'),
            UserInput(NodeType.FINAL_NODE)
        ],
        parm_key='payment'
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
        parm_key='latePayment'
    ),


    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.WITHIN),
            UserInput(NodeType.TIMESPAN, '6 months'),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Activated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        parm_key='disclosure'
    ),


    # UpdateConfig(
    #     OpCode.UPDATE_PARM,
    #     node_list = [
    #         RootNode(),
    #         WithinNode(),
    #         TimespanNode(value = '6 months'),
    #         EventNode(),
    #         StandardEventNode(),
    #         ContractSubjectNode(value='contract'),
    #         ContractActionNode(value='Activated')
    #     ],
    #     parm_key='disclosure'
    # ),


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
        parm_key='suspendDelivery'
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
        parm_key='suspendDelivery'
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