from app.classes.operations.user_input import UserInput, NodeType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

test_suite = [
    # upon execution of this agreement
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Activated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='payment',
        parm_key='P1'
    ),

    # if Gridiron determines that third party analysis of the Biomass is required for processing
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.CUSTOM_EVENT),
            UserInput(NodeType.SUBJECT, 'buyer'),
            UserInput(NodeType.VERB, 'determines'),
            UserInput(NodeType.DOBJ, 'that third party analysis of the Biomass is required for processing'), # Improve...
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='delivery_location',
        parm_key='P1'
    ),

    # If any claim or legal proceeding is filed by a third party
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.CUSTOM_EVENT),
            UserInput(NodeType.SUBJECT, 'third party'),
            UserInput(NodeType.VERB, 'files'),
            UserInput(NodeType.DOBJ, 'claim'),
            # Prep phrase: Against buyer/seller?
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='legal_proceeding',
        parm_key='P1'
    ),

    # When the Agreement ends
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF), # Want a "When" (indicates trigger)
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='return_disclose_info',
        parm_key='P1'
    )
]