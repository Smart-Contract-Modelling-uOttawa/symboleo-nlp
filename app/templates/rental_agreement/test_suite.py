from app.classes.selection.all_nodes import *
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode
#from app.src.operations.refine_parameter.parm_configs import ParameterConfig
from app.classes.other.user_input import UserInput, NodeType

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT, 'ob_pay_rent obligation'),
            UserInput(NodeType.CONTRACT_ACTION, 'Violated'),
        ],
        parm_key='late_payment'
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
            UserInput(NodeType.NEW_EVENT),
            UserInput(NodeType.SUBJECT, 'renter'),
            UserInput(NodeType.VERB, 'occupies'),
            UserInput(NodeType.DOBJ, 'the_property'),
        ],
        parm_key='pay_security_deposit'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT, 'contract'),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
        ],
        parm_key='return_deposit'
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
            UserInput(NodeType.NEW_EVENT),
            UserInput(NodeType.SUBJECT, 'landlord'),
            UserInput(NodeType.VERB, 'allows'),
            UserInput(NodeType.DOBJ, 'pets'),
        ],
        parm_key= 'no_pets'
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
            UserInput(NodeType.NEW_EVENT),# might be a standard event
            UserInput(NodeType.SUBJECT, 'landlord'),
            UserInput(NodeType.VERB, 'provides'),
            UserInput(NodeType.DOBJ, 'termination notice'),
            UserInput(NodeType.ADVERB, '3 days in advance'), # Improve this
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
            UserInput(NodeType.NEW_EVENT),
            UserInput(NodeType.SUBJECT, 'renter'),
            UserInput(NodeType.VERB, 'abandons'),
            UserInput(NodeType.DOBJ, 'the_property')
        ],
        #parm_config = ParameterConfig('powers', 'pow_termination_abandon', 'trigger'),
        norm_id = 'pow_termination_abandon',
        debtor = 'landlord',
        creditor = 'renter'
    ),
]