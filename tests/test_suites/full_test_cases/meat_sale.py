from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.BEFORE, 'before'),
            UserInput(UnitType.DATE, 'March 18, 2024')
        ],
        nl_key='delivery',
        parm_key='P1'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.BY, 'by'),
            UserInput(UnitType.DATE, 'March 30, 2024')
        ],
        nl_key='payment',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.IF, 'if'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'buyer'),
            UserInput(UnitType.TRANSITIVE_VERB, 'misses'),
            UserInput(UnitType.DOBJ, 'payment')
        ],
        nl_key='pay_interest',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.FOR, 'for'),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '6'),
            UserInput(UnitType.TIME_UNIT, 'months'),
            UserInput(UnitType.AFTER, 'after'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
            UserInput(UnitType.CONTRACT_ACTION, 'terminated')
        ],
        nl_key='disclosure',
        parm_key='P1'
    ),
]