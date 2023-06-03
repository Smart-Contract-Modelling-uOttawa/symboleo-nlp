from app.classes.elements.all_elements import *
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.WHEN),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'client'),
            UserInput(UnitType.VERB, 'completes'),
            UserInput(UnitType.DOBJ, 'services'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='invoice',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '10 days'),
            UserInput(UnitType.OF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.NORM_EVENT),
            UserInput(UnitType.OBLIGATION_SUBJECT, 'ob_invoice'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Fulfilled'),

            UserInput(UnitType.SUBJECT, 'contractor'),
            UserInput(UnitType.VERB, 'sending'),
            UserInput(UnitType.DOBJ, 'invoice'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='invoice_due',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'contractor'),
            UserInput(UnitType.VERB, 'starts'),
            UserInput(UnitType.DOBJ, 'services'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='partial_completion',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.UNLESS),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'client'),
            UserInput(UnitType.VERB, 'authorizes'),
            UserInput(UnitType.DOBJ, 'disclosure'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='disclose',
        parm_key = 'P1'
    ),
]