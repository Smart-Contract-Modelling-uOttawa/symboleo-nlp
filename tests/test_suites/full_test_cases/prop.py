from app.classes.elements.all_elements import *
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'legal proceedings'),
            UserInput(UnitType.VERB, 'become'),
            UserInput(UnitType.PREDICATE, 'necessary'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='legal_proceedings',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='disburse_termination',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '3 days'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='disburse_termination',
        parm_key='P2'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '10 days'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='reimburse_termination',
        parm_key='P2'
    ),
]