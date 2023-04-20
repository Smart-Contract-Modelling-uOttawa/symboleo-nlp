# Want to have a test where we convert the sample_t into sample_raw
# Eventually I want a NL -> Node list generator... Will replace this with that..
from app.classes.other.user_input import UserInput, NodeType
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.BEFORE),
            UserInput(NodeType.TIMEPOINT),
            UserInput(NodeType.DOMAIN_TIMEPOINT, 'evt_delivered.delDueDate')
        ],
        parm_key='delivery'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.BEFORE),
            UserInput(NodeType.TIMEPOINT),
            UserInput(NodeType.DOMAIN_TIMEPOINT, 'evt_paid.payDueDate')
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
            UserInput(NodeType.CONTRACT_SUBJECT, 'ob_payment obligation'),
            UserInput(NodeType.CONTRACT_ACTION, 'Violated'),
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
            UserInput(NodeType.CONTRACT_SUBJECT, 'contract'),
            UserInput(NodeType.CONTRACT_ACTION, 'Activated'),
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
            UserInput(NodeType.CONTRACT_SUBJECT, 'ob_payment obligation'),
            UserInput(NodeType.CONTRACT_ACTION, 'Violated')
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
            UserInput(NodeType.CONTRACT_SUBJECT, 'ob_late_payment obligation'),
            UserInput(NodeType.CONTRACT_ACTION, 'Fulfilled')
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
            UserInput(NodeType.CONTRACT_SUBJECT, 'ob_delivery obligation'),
            UserInput(NodeType.CONTRACT_ACTION, 'Violated')
        ],
        norm_id = 'pow_terminate_contract',
        debtor = 'buyer',
        creditor = 'seller'
    )
]