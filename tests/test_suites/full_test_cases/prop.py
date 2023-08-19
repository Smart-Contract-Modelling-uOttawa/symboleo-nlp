from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.IF, 'if'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'legal proceedings'),
            UserInput(UnitType.LINKING_VERB, 'become'),
            UserInput(UnitType.PREDICATE, 'necessary')
        ],
        nl_key='legal_proceedings',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.IF, 'if'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
            UserInput(UnitType.CONTRACT_ACTION, 'terminated')
        ],
        nl_key='disburse_termination',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '3'),
            UserInput(UnitType.TIME_UNIT, 'days'),
            UserInput(UnitType.OF, 'of'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
            UserInput(UnitType.CONTRACT_ACTION, 'terminated')
        ],
        nl_key='disburse_termination',
        parm_key='P2'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '10'),
            UserInput(UnitType.TIME_UNIT, 'days'),
            UserInput(UnitType.OF, 'of'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
            UserInput(UnitType.CONTRACT_ACTION, 'terminated')
        ],
        nl_key='reimburse_termination',
        parm_key='P2'
    ),
]