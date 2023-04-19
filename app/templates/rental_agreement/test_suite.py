from app.classes.selection.all_nodes import *
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode
#from app.src.operations.refine_parameter.parm_configs import ParameterConfig

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            IfNode(),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value='ob_pay_rent obligation'),
            ContractActionNode(value = 'Violated')
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
            RootNode(),
            BeforeNode(),
            EventNode(),
            NewEventNode(),
            SubjectNode(value='renter'),
            VerbNode(value='occupies'),
            DobjNode(value='the_property')
        ],
        parm_key='pay_security_deposit'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            IfNode(),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value='contract'),
            ContractActionNode(value='Terminated')
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
            RootNode(),
            UntilNode(), # TODO: Need an Unless node
            EventNode(),
            NewEventNode(),
            SubjectNode(value='landlor'),
            VerbNode(value='allows'),
            DobjNode(value='pets')
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
            RootNode(),
            IfNode(),
            EventNode(),
            NewEventNode(), # This may be a standard event..
            SubjectNode(value='landlord'),
            VerbNode(value='provides'),
            DobjNode(value='termination notice'),
            AdverbNode(value='3 days in advance') ## Need to figure this one out
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
            RootNode(),
            IfNode(),
            EventNode(),
            NewEventNode(),
            SubjectNode(value='renter'),
            VerbNode(value='abandons'),
            DobjNode(value='the_property')
        ],
        #parm_config = ParameterConfig('powers', 'pow_termination_abandon', 'trigger'),
        norm_id = 'pow_termination_abandon',
        debtor = 'landlord',
        creditor = 'renter'
    ),
]