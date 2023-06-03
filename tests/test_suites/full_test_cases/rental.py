from app.classes.elements.all_elements import *
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.operations.user_input import UserInput, UnitType

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.NORM_EVENT),
            UserInput(UnitType.OBLIGATION_SUBJECT, 'ob_pay_rent'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Violated'),

            UserInput(UnitType.SUBJECT, 'renter'),
            UserInput(UnitType.FAILS_TO),
            UserInput(UnitType.VERB, 'pay'),
            UserInput(UnitType.DOBJ, 'rent'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='late_payment',
        parm_key = 'P1'
    ),
   
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.BEFORE),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'renter'),
            UserInput(UnitType.VERB, 'occupies'),
            UserInput(UnitType.DOBJ, 'the property'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='pay_security_deposit',
        parm_key = 'P2'
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
            UserInput(UnitType.CONTRACT_ACTION, 'terminates'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='return_deposit',
        parm_key = 'P1'
    ),

    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.UNLESS),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'landlord'),
            UserInput(UnitType.VERB, 'allows'),
            UserInput(UnitType.DOBJ, 'pets'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key= 'no_pets',
        parm_key = 'P2'
    ),

    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'renter'),
            UserInput(UnitType.VERB, 'abandons'),
            UserInput(UnitType.DOBJ, 'the property'),
            UserInput(UnitType.FINAL_NODE)
        ],
        norm_id = 'pow_termination_abandon',
        debtor = 'landlord',
        creditor = 'renter'
    ),
]