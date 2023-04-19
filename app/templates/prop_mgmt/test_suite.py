from app.classes.selection.all_nodes import *
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.domain_object import DomainEvent, DomainProp
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode
from app.src.operations.refine_parameter2.parm_configs import ParameterConfig

test_suite = [
    # Add events
    # UpdateConfig(
    #     OpCode.ADD_DOMAIN_OBJECT,
    #     dm_obj_type = 'events',
    #     domain_object = DomainEvent('LegalProceedingsNecessary', [
    #         DomainProp('property', 'Property'),
    #     ]),
    #     declaration = Declaration('evt_legal_proceedings_necessary', 'LegalProceedingsNecessary', 'events', [
    #         DeclarationProp('property', 'the_property', 'Property'),
    #     ])
    # ),
    
    # UpdateConfig(
    #     OpCode.ADD_DOMAIN_OBJECT,
    #     dm_obj_type = 'events',
    #     domain_object = DomainEvent('ProvideTerminationNotice', [
    #         DomainProp('agent', 'Role'),
    #         DomainProp('numDays', 'Number')
    #     ]),
    #     declaration = Declaration('evt_provide_termination_notice_manager', 'ProvideTerminationNotice', 'events', [
    #         DeclarationProp('agent', 'manager', 'Role'),
    #         DeclarationProp('numDays', 'var_days_notice', 'Number'),
    #     ])
    # ),

    # UpdateConfig(
    #     OpCode.ADD_DOMAIN_OBJECT,
    #     dm_obj_type = 'events',
    #     domain_object = DomainEvent('ProvideTerminationNotice', [
    #         DomainProp('agent', 'Role'),
    #         DomainProp('numDays', 'Number')
    #     ]),
    #     declaration = Declaration('evt_provide_termination_notice_owner', 'ProvideTerminationNotice', 'events', [
    #         DeclarationProp('agent', 'owner', 'Role'),
    #         DeclarationProp('numDays', 'var_days_notice', 'Number'),
    #     ])
    # ),

    ## Add conditions
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            IfNode(),
            EventNode(),
            NewEventNode(),
            SubjectNode(value='legal proceedings'),
            VerbNode(value='become'),
            PredicateNode(value='necessary')
        ],
        parm_key='legal_proceedings'
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
        parm_key='disburse_termination'
    ),

    ## Temporal refinements
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            WithinNode(),
            TimespanNode(value = '3 days'),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value='contract'),
            ContractActionNode(value='Terminated')
        ],
        parm_key='disburse_termination'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            RootNode(),
            WithinNode(),
            TimespanNode(value='10 days'),
            EventNode(),
            StandardEventNode(),
            ContractSubjectNode(value='contract'),
            ContractActionNode(value='Terminated')
        ],
        parm_key='reimburse_termination'
    ),

    ## Termination power
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            RootNode(),
            IfNode(),
            EventNode(),
            NewEventNode(),
            SubjectNode(value='manager'),
            VerbNode(value='provides'),
            DobjNode(value='termination notice'),
            AdverbNode(value='x days in advance')
        ],
        #parm_config = ParameterConfig('powers', 'pow_terminate_notice_manager', 'trigger'),
        norm_id = 'pow_terminate_notice_manager',
        debtor = 'manager',
        creditor = 'owner'
    ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            RootNode(),
            IfNode(),
            EventNode(),
            NewEventNode(),
            SubjectNode(value='owner'),
            VerbNode(value='provides'),
            DobjNode(value='termination notice'),
            AdverbNode(value='x days in advance')
        ],
        #parm_config = ParameterConfig('powers', 'pow_terminate_notice_owner', 'trigger'),
        norm_id = 'pow_terminate_notice_owner',
        debtor = 'owner',
        creditor = 'manager'
    ),
]