from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.operations.user_input import UserInput, UnitType

test_suite = [

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '2'),
            UserInput(UnitType.TIME_UNIT, 'weeks'),
            UserInput(UnitType.OF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'renter'),
            UserInput(UnitType.TRANSITIVE_VERB, 'occupying'),
            UserInput(UnitType.DOBJ, 'property')
        ],
        nl_key='pay_deposit',
        parm_key = 'P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.UNLESS),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'landlord'),
            UserInput(UnitType.TRANSITIVE_VERB, 'provides'),
            UserInput(UnitType.DOBJ, 'authorization'),
            UserInput(UnitType.PREP_PHRASE, 'for pets'),
        ],
        nl_key= 'no_pets',
        parm_key = 'P2'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.IN_EVENT, 'in the event that'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'renter'),
            UserInput(UnitType.TRANSITIVE_VERB, 'pays'),
            UserInput(UnitType.DOBJ, 'security deposit'),
            UserInput(UnitType.ADVERB, 'late'),
        ],
        nl_key='pay_extra',
        parm_key = 'P3'
    ),

]