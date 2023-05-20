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
            ## We assume this will be generated when user selects ob_payment + Violated
            ## Will need to handle that separately. Falls under input tree management
            #UserInput(NodeType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(NodeType.SUBJECT, 'buyer'),
            UserInput(NodeType.FAILS_TO),
            UserInput(NodeType.VERB, 'pay'),
            UserInput(NodeType.DOBJ, '$100'),
            UserInput(NodeType.PREP_PHRASE, 'in CAD'),
            UserInput(NodeType.PREP_PHRASE, 'to seller'),
            UserInput(NodeType.PREP_PHRASE, 'by March 30, 2024'),
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

            #UserInput(NodeType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(NodeType.SUBJECT, 'buyer'),
            UserInput(NodeType.FAILS_TO),
            UserInput(NodeType.VERB, 'pay'),
            UserInput(NodeType.DOBJ, '$100'),
            UserInput(NodeType.PREP_PHRASE, 'in CAD'),
            UserInput(NodeType.PREP_PHRASE, 'to seller'),
            UserInput(NodeType.PREP_PHRASE, 'by March 30, 2024'),
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

            #UserInput(NodeType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(NodeType.SUBJECT, 'buyer'),
            UserInput(NodeType.VERB, 'pay'),
            UserInput(NodeType.DOBJ, '(interest amount)'),
            UserInput(NodeType.PREP_PHRASE, 'in CAD'),
            UserInput(NodeType.PREP_PHRASE, 'to seller'),
            UserInput(NodeType.PREP_PHRASE, 'by March 30, 2024'), # late payment due date?
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

            #UserInput(NodeType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(NodeType.SUBJECT, 'buyer'),
            UserInput(NodeType.FAILS_TO),
            UserInput(NodeType.VERB, 'deliver'),
            UserInput(NodeType.DOBJ, 'goods'),
            UserInput(NodeType.PREP_PHRASE, 'to delAdd'),
            UserInput(NodeType.PREP_PHRASE, 'by delDueDate'), 
            UserInput(NodeType.FINAL_NODE)
        ],
        norm_id = 'pow_terminate_contract',
        debtor = 'buyer',
        creditor = 'seller'
    )
]