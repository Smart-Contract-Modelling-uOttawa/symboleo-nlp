from app.classes.selection.all_nodes import *
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.operations.user_input import UserInput, NodeType

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.NORM_EVENT),
            UserInput(NodeType.OBLIGATION_SUBJECT, 'ob_pay_rent'),
            UserInput(NodeType.OBLIGATION_ACTION, 'Violated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='late_payment',
        parm_key = 'P1'
    ),

    # UpdateConfig(
    #     OpCode.ADD_DOMAIN_OBJECT,
    #     dm_obj_type = 'events',
    #     domain_object = DomainEvent('Occupy', [
    #         DomainProp('agent', 'Role'),
    #         DomainProp('property', 'RentalProperty')
    #     ]),
    #     declaration = Declaration('evt_occupy', 'Occupy', 'events', [
    #         DeclarationProp('agent', 'renter', 'Role'),
    #         DeclarationProp('property', 'the_property', 'RentalProperty'),
    #     ])
    # ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.BEFORE),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.CUSTOM_EVENT),
            UserInput(NodeType.SUBJECT, 'renter'),
            UserInput(NodeType.VERB, 'occupies'),
            UserInput(NodeType.DOBJ, 'the_property'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='pay_security_deposit',
        parm_key = 'P2'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key='return_deposit',
        parm_key = 'P1'
    ),
    # UpdateConfig(
    #     OpCode.ADD_DOMAIN_OBJECT,
    #     dm_obj_type = 'events',
    #     domain_object = DomainEvent('AllowPets', [
    #         DomainProp('grantor', 'Role')
    #     ]),
    #     declaration = Declaration('evt_allow_pets', 'AllowPets', 'events', [
    #         DeclarationProp('grantor', 'landlord', 'Role')
    #     ])
    # ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.UNTIL), # Need unless
            UserInput(NodeType.EVENT),
            UserInput(NodeType.CUSTOM_EVENT),
            UserInput(NodeType.SUBJECT, 'landlord'),
            UserInput(NodeType.VERB, 'allows'),
            UserInput(NodeType.DOBJ, 'pets'),
            UserInput(NodeType.FINAL_NODE)
        ],
        nl_key= 'no_pets',
        parm_key = 'P2'
    ),

    # UpdateConfig(
    #     OpCode.ADD_DOMAIN_OBJECT,
    #     dm_obj_type = 'events',
    #     domain_object = DomainEvent('ProvideTerminationNotice', [
    #         DomainProp('agent', 'Role'),
    #         DomainProp('daysInAdvance', 'Number')
    #     ]),
    #     declaration = Declaration('evt_provide_termination_notice', 'ProvideTerminationNotice', 'events', [
    #         DeclarationProp('agent', 'landlord', 'Role'),
    #         DeclarationProp('daysInAdvance', 'var_daysInAdvance', 'Number')
    #     ])
    # ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.CUSTOM_EVENT),# might be a standard event
            UserInput(NodeType.SUBJECT, 'landlord'),
            UserInput(NodeType.VERB, 'provides'),
            UserInput(NodeType.DOBJ, 'termination notice'),
            UserInput(NodeType.ADVERB, '3 days in advance'), # Improve this
            UserInput(NodeType.FINAL_NODE)
        ],
        #parm_config = ParameterConfig('powers', 'pow_termination_written', 'trigger'),
        norm_id = 'pow_termination_written',
        debtor = 'renter',
        creditor = 'landlord'
    ),

    # UpdateConfig(
    #     OpCode.ADD_DOMAIN_OBJECT,
    #     dm_obj_type = 'events',
    #     domain_object = DomainEvent('Abandon', [
    #         DomainProp('agent', 'Role'),
    #         DomainProp('property', 'RentalProperty')
    #     ]),
    #     declaration = Declaration('evt_abandon', 'Abandon', 'events', [
    #         DeclarationProp('agent', 'renter', 'Role'),
    #         DeclarationProp('property', 'the_property', 'RentalProperty')
    #     ])
    # ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.CUSTOM_EVENT),
            UserInput(NodeType.SUBJECT, 'renter'),
            UserInput(NodeType.VERB, 'abandons'),
            UserInput(NodeType.DOBJ, 'the_property'),
            UserInput(NodeType.FINAL_NODE)
        ],
        #parm_config = ParameterConfig('powers', 'pow_termination_abandon', 'trigger'),
        norm_id = 'pow_termination_abandon',
        debtor = 'landlord',
        creditor = 'renter'
    ),
]