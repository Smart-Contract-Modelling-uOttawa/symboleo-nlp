# Want to have a test where we convert the sample_t into sample_raw
# Eventually I want a NL -> Node list generator... Will replace this with that..

from app.classes.selection.all_nodes import *
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode


test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            BeforeNode(),
            TimepointNode(),
            DomainTimepointNode(value='evt_delivered.delDueDate')
        ],
        parm_key='delivery'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            BeforeNode(),
            TimepointNode(),
            DomainTimepointNode(value='evt_paid.payDueDate')
        ],
        parm_key='payment'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            IfNode(),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value='ob_payment obligation'),
            ContractActionNode(value='Violated')
        ],
        parm_key='latePayment'
    ),


    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            WithinNode(),
            TimespanNode(value = '6 months'),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value='contract'),
            ContractActionNode(value='Activated')
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
            RootNode(),
            IfNode(),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value='ob_payment obligation'),
            ContractActionNode(value='Violated')
        ],
        parm_key='suspendDelivery'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            UntilNode(),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value = 'ob_late_payment obligation'),
            ContractActionNode(value = 'Fulfilled')
        ],
        parm_key='suspendDelivery'
    ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            RootNode(),
            IfNode(),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value = 'ob_delivery obligation'),
            ContractActionNode(value = 'Violated')
        ],
        norm_id = 'pow_terminate_contract',
        debtor = 'buyer',
        creditor = 'seller'
    )
]