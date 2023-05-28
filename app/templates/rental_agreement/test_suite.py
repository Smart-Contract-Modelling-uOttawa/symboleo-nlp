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
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='return_deposit',
        parm_key = 'P1'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.UNTIL), # Need unless
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
            UserInput(UnitType.CUSTOM_EVENT),# might be a standard event
            UserInput(UnitType.SUBJECT, 'landlord'),
            UserInput(UnitType.VERB, 'provides'),
            UserInput(UnitType.DOBJ, 'termination notice'),
            UserInput(UnitType.ADVERB, '3 days in advance'), # Improve this
            UserInput(UnitType.FINAL_NODE)
        ],
        #parm_config = ParameterConfig('powers', 'pow_termination_written', 'trigger'),
        norm_id = 'pow_termination_written',
        debtor = 'renter',
        creditor = 'landlord'
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
        #parm_config = ParameterConfig('powers', 'pow_termination_abandon', 'trigger'),
        norm_id = 'pow_termination_abandon',
        debtor = 'landlord',
        creditor = 'renter'
    ),
]