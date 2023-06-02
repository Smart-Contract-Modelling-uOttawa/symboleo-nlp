from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    # upon contract activation 
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Activated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='payment',
        parm_key='P1'
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
            UserInput(UnitType.OBLIGATION_ACTION, 'Fulfilled'),

            # TODO: Want to be able to say 'completes payment'
            UserInput(UnitType.SUBJECT, 'Gridiron'),
            UserInput(UnitType.VERB, 'completes'),
            UserInput(UnitType.DOBJ, 'payment'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='quarantine',
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
            UserInput(UnitType.OBLIGATION_SUBJECT, 'ob_delivery_processor'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Fulfilled'),

            UserInput(UnitType.SUBJECT, 'Shi Farms'),
            UserInput(UnitType.VERB, 'completes'),
            UserInput(UnitType.DOBJ, 'delivery'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='quarantine',
        parm_key='P2'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.WHEN),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='return_disclose_info',
        parm_key='P1'
    )
]

# TODO: Add the determines analysis one here.. It will be choppy...