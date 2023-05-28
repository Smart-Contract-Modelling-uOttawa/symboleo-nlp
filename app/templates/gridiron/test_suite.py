from app.classes.operations.user_input import UserInput, UnitType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    # upon execution of this agreement
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Activated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='payment',
        parm_key='P1'
    ),

    # if Gridiron determines that third party analysis of the Biomass is required for processing
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'buyer'),
            UserInput(UnitType.VERB, 'determines'),
            UserInput(UnitType.DOBJ, 'that third party analysis of the Biomass is required for processing'), # Improve...
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='delivery_location',
        parm_key='P1'
    ),

    # If any claim or legal proceeding is filed by a third party
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'third party'),
            UserInput(UnitType.VERB, 'files'),
            UserInput(UnitType.DOBJ, 'claim'),
            # Prep phrase: Against buyer/seller?
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='legal_proceeding',
        parm_key='P1'
    ),

    # When the Agreement ends
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF), # Want a "When" (indicates trigger)
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='return_disclose_info',
        parm_key='P1'
    )
]