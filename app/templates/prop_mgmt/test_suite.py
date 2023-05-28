from app.classes.elements.all_nodes import *
from app.classes.operations.user_input import UserInput, UnitType
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
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'legal proceedings'),
            UserInput(UnitType.VERB, 'become'),
            UserInput(UnitType.PREDICATE, 'necessary'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='legal_proceedings',
        parm_key='P1'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='disburse_termination',
        parm_key='P1'
    ),

    ## Temporal refinements
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '3 days'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='disburse_termination',
        parm_key='P2'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        node_list = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '10 days'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='reimburse_termination',
        parm_key='P2'
    ),

    ## Termination power
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        node_list = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'manager'),
            UserInput(UnitType.VERB, 'provides'),
            UserInput(UnitType.DOBJ, 'termination notice'),
            UserInput(UnitType.ADVERB, 'x days in advance'),
            UserInput(UnitType.FINAL_NODE)
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
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'owner'),
            UserInput(UnitType.VERB, 'provides'),
            UserInput(UnitType.DOBJ, 'termination notice'),
            UserInput(UnitType.ADVERB, 'x days in advance'),
            UserInput(UnitType.FINAL_NODE)
        ],
        #parm_config = ParameterConfig('powers', 'pow_terminate_notice_owner', 'trigger'),
        norm_id = 'pow_terminate_notice_owner',
        debtor = 'owner',
        creditor = 'manager'
    ),
]