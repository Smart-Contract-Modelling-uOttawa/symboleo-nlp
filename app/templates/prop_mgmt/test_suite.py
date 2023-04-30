from app.classes.selection.all_nodes import *
from app.classes.operations.user_input import UserInput, NodeType
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

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
            UserInput(NodeType.CUSTOM_EVENT),
            UserInput(NodeType.SUBJECT, 'legal proceedings'),
            UserInput(NodeType.VERB, 'become'),
            UserInput(NodeType.PREDICATE, 'necessary'),
            UserInput(NodeType.FINAL_NODE)
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
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
            UserInput(NodeType.FINAL_NODE)
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
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
            UserInput(NodeType.FINAL_NODE)
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
            UserInput(NodeType.CONTRACT_EVENT),
            UserInput(NodeType.CONTRACT_SUBJECT),
            UserInput(NodeType.CONTRACT_ACTION, 'Terminated'),
            UserInput(NodeType.FINAL_NODE)
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
            UserInput(NodeType.CUSTOM_EVENT),
            UserInput(NodeType.SUBJECT, 'manager'),
            UserInput(NodeType.VERB, 'provides'),
            UserInput(NodeType.DOBJ, 'termination notice'),
            UserInput(NodeType.ADVERB, 'x days in advance'),
            UserInput(NodeType.FINAL_NODE)
        ],
        #parm_config = ParameterConfig('powers', 'pow_terminate_notice_manager', 'trigger'),
        norm_id = 'pow_terminate_notice_manager',
        debtor = 'manager',
        creditor = 'owner'
    ),
    #TODO: Make this use a CommonEvent... Start from a TDD approach. What should this suite look like?
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            UserInput(NodeType.ROOT),
            UserInput(NodeType.IF),
            UserInput(NodeType.EVENT),
            UserInput(NodeType.CUSTOM_EVENT),
            UserInput(NodeType.SUBJECT, 'owner'),
            UserInput(NodeType.VERB, 'provides'),
            UserInput(NodeType.DOBJ, 'termination notice'),
            UserInput(NodeType.ADVERB, 'x days in advance'),
            UserInput(NodeType.FINAL_NODE)
        ],
        #parm_config = ParameterConfig('powers', 'pow_terminate_notice_owner', 'trigger'),
        norm_id = 'pow_terminate_notice_owner',
        debtor = 'owner',
        creditor = 'manager'
    ),
]