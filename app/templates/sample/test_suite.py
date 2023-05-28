# Want to have a test where we convert the sample_t into sample_raw
# Eventually I want a NL -> Node list generator... Will replace this with that..
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.BEFORE),
            UserInput(UnitType.DATE, 'March 18, 2024'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='delivery',
        parm_key='P2'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.BEFORE),
            UserInput(UnitType.DATE, 'March 30, 2024'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='payment',
        parm_key='P2'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.NORM_EVENT),
            UserInput(UnitType.OBLIGATION_SUBJECT, 'ob_payment'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Violated'),
            ## We assume this will be generated when user selects ob_payment + Violated
            ## Will need to handle that separately. Falls under input tree management
            #UserInput(UnitType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(UnitType.SUBJECT, 'buyer'),
            UserInput(UnitType.FAILS_TO),
            UserInput(UnitType.VERB, 'pay'),
            UserInput(UnitType.DOBJ, '$100'),
            UserInput(UnitType.PREP_PHRASE, 'in CAD'),
            UserInput(UnitType.PREP_PHRASE, 'to seller'),
            UserInput(UnitType.PREP_PHRASE, 'by March 30, 2024'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='latePayment',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.UNTIL),
            UserInput(UnitType.TIMESPAN, '6 months'),
            UserInput(UnitType.AFTER),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='disclosure',
        parm_key='P2'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.NORM_EVENT),
            UserInput(UnitType.OBLIGATION_SUBJECT, 'ob_payment'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Violated'),

            #UserInput(UnitType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(UnitType.SUBJECT, 'buyer'),
            UserInput(UnitType.FAILS_TO),
            UserInput(UnitType.VERB, 'pay'),
            UserInput(UnitType.DOBJ, '$100'),
            UserInput(UnitType.PREP_PHRASE, 'in CAD'),
            UserInput(UnitType.PREP_PHRASE, 'to seller'),
            UserInput(UnitType.PREP_PHRASE, 'by March 30, 2024'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='suspendDelivery',
        parm_key='P1'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.UNTIL),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.NORM_EVENT),
            UserInput(UnitType.OBLIGATION_SUBJECT, 'ob_late_payment'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Fulfilled'),

            #UserInput(UnitType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(UnitType.SUBJECT, 'buyer'),
            UserInput(UnitType.VERB, 'pay'),
            UserInput(UnitType.DOBJ, '(interest amount)'),
            UserInput(UnitType.PREP_PHRASE, 'in CAD'),
            UserInput(UnitType.PREP_PHRASE, 'to seller'),
            UserInput(UnitType.PREP_PHRASE, 'by March 30, 2024'), # late payment due date?
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='suspendDelivery',
        parm_key = 'P2'
    ),
    
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.NORM_EVENT),
            UserInput(UnitType.OBLIGATION_SUBJECT, 'ob_delivery'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Violated'),

            #UserInput(UnitType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(UnitType.SUBJECT, 'buyer'),
            UserInput(UnitType.FAILS_TO),
            UserInput(UnitType.VERB, 'deliver'),
            UserInput(UnitType.DOBJ, 'goods'),
            UserInput(UnitType.PREP_PHRASE, 'to delAdd'),
            UserInput(UnitType.PREP_PHRASE, 'by delDueDate'), 
            UserInput(UnitType.FINAL_NODE)
        ],
        norm_id = 'pow_terminate_contract',
        debtor = 'buyer',
        creditor = 'seller'
    )
]