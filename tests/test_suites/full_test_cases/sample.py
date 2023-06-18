from app.classes.elements.all_elements import *
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.operations.user_input import UserInput, UnitType

test_suite = [

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '2 weeks'),
            UserInput(UnitType.OF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'renter'),
            UserInput(UnitType.TRANSITIVE_VERB, 'occupying'),
            UserInput(UnitType.DOBJ, 'the property')
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
            UserInput(UnitType.TRANSITIVE_VERB, 'allows'),
            UserInput(UnitType.DOBJ, 'pets'),
        ],
        nl_key= 'no_pets',
        parm_key = 'P2'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.NORM_EVENT),
            UserInput(UnitType.OBLIGATION_SUBJECT, 'pay_deposit.ob_pay_deposit'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Violated'),
        ],
        nl_key='late_payment',
        parm_key = 'P3'
    ),

]