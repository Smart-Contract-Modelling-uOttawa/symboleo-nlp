from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.WHEN, 'when'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'contractor'),
            UserInput(UnitType.TRANSITIVE_VERB, 'completes'),
            UserInput(UnitType.DOBJ, 'services')
        ],
        nl_key='send_invoice',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.WITHIN, 'within'),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '10'),
            UserInput(UnitType.TIME_UNIT, 'days'),
            UserInput(UnitType.OF, 'of'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'contractor'),
            UserInput(UnitType.TRANSITIVE_VERB, 'sending'),
            UserInput(UnitType.DOBJ, 'invoice')
        ],
        nl_key='pay_invoice',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.IF, 'if'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'contractor'),
            UserInput(UnitType.TRANSITIVE_VERB, 'breaches'),
            UserInput(UnitType.DOBJ, 'contract')
        ],
        nl_key='partial_completion',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.UNLESS, 'unless'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'client'),
            UserInput(UnitType.TRANSITIVE_VERB, 'authorizes'),
            UserInput(UnitType.DOBJ, 'disclosure')
        ],
        nl_key='disclose',
        parm_key = 'P1'
    ),
]