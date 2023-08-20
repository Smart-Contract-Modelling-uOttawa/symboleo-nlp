from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.UPON, 'upon'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
            UserInput(UnitType.CONTRACT_ACTION, 'activated')
        ],
        nl_key='payment',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ONCE, 'once'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'GridIron'),
            UserInput(UnitType.TRANSITIVE_VERB, 'pays'),
            UserInput(UnitType.DOBJ, 'Shi Farms'),
        ],
        nl_key='quarantine',
        parm_key='P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.UNTIL, 'until'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'Shi Farms'),
            UserInput(UnitType.TRANSITIVE_VERB, 'delivers'),
            UserInput(UnitType.DOBJ, 'biomass')
        ],
        nl_key='quarantine',
        parm_key='P2'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.IF, 'if'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'GridIron'),
            UserInput(UnitType.TRANSITIVE_VERB, 'mandates'),
            UserInput(UnitType.DOBJ, 'third-party analysis')
        ],
        nl_key='delivery_location',
        parm_key='P1'
    )
]
