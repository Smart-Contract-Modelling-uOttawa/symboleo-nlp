from app.classes.selection.all_nodes import *
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.domain_object import DomainEvent, DomainProp
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode
from app.src.operations.refine_parameter2.parm_configs import ParameterConfig

from app.classes.other.user_input import UserInput, NodeType

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
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.NEW_EVENT),
            UserInput(NodeType.SUBJECT, 'legal proceedings'),
            UserInput(NodeType.VERB, 'become'),
            UserInput(NodeType.PREDICATE, 'necessary'),
        ],
        parm_key='legal_proceedings'
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
        parm_key='disburse_termination'
    ),

    ## Temporal refinements
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.WITHIN),
            UserInput(NodeType.TIMESPAN, '3 days'),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT, 'contract'),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
        ],
        parm_key='disburse_termination'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.WITHIN),
            UserInput(NodeType.TIMESPAN, '10 days'),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.STANDARD_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT, 'contract'),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
        ],
        parm_key='reimburse_termination'
    ),

    ## Termination power
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.NEW_EVENT),
            UserInput(NodeType.SUBJECT, 'manager'),
            UserInput(NodeType.VERB, 'provides'),
            UserInput(NodeType.DOBJ, 'termination notice'),
            UserInput(NodeType.ADVERB, 'x days in advance'),
        ],
        #parm_config = ParameterConfig('powers', 'pow_terminate_notice_manager', 'trigger'),
        norm_id = 'pow_terminate_notice_manager',
        debtor = 'manager',
        creditor = 'owner'
    ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.NEW_EVENT),
            UserInput(NodeType.SUBJECT, 'owner'),
            UserInput(NodeType.VERB, 'provides'),
            UserInput(NodeType.DOBJ, 'termination notice'),
            UserInput(NodeType.ADVERB, 'x days in advance'),
        ],
        #parm_config = ParameterConfig('powers', 'pow_terminate_notice_owner', 'trigger'),
        norm_id = 'pow_terminate_notice_owner',
        debtor = 'owner',
        creditor = 'manager'
    ),
]