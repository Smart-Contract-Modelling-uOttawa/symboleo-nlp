from app.classes.selection.all_nodes import ContractEventActionNode, ContractEventNode, DomainEventNameNode, DomainEventNode, EventNode, IfNode, RootNode, TimespanNode, WithinNode
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.domain_object import DomainEvent, DomainProp
from app.src.grammar.selection import Selection
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode
from app.src.operations.refine_parameter.parm_configs import ParameterConfig

test_suite = [
    # Add events
    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('LegalProceedingsNecessary', [
            DomainProp('property', 'Property'),
        ]),
        declaration = Declaration('evt_legal_proceedings_necessary', 'LegalProceedingsNecessary', 'events', [
            DeclarationProp('property', 'the_property', 'Property'),
        ])
    ),
    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('ProvideTerminationNotice', [
            DomainProp('agent', 'Role'),
            DomainProp('numDays', 'Number')
        ]),
        declaration = Declaration('evt_provide_termination_notice_manager', 'ProvideTerminationNotice', 'events', [
            DeclarationProp('agent', 'manager', 'Role'),
            DeclarationProp('numDays', 'var_days_notice', 'Number'),
        ])
    ),
    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('ProvideTerminationNotice', [
            DomainProp('agent', 'Role'),
            DomainProp('numDays', 'Number')
        ]),
        declaration = Declaration('evt_provide_termination_notice_owner', 'ProvideTerminationNotice', 'events', [
            DeclarationProp('agent', 'owner', 'Role'),
            DeclarationProp('numDays', 'var_days_notice', 'Number'),
        ])
    ),

    ## Add conditions
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            DomainEventNode('',0),
            DomainEventNameNode('', 0, 'evt_legal_proceedings_necessary')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_legal_proceedings')
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ContractEventNode('',0),
            ContractEventActionNode('', 0, 'Terminated')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_disburse_termination')
    ),

    ## Temporal refinements
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            WithinNode('', 0),
            TimespanNode('', 0, '3 days'),
            EventNode('', 0),
            ContractEventNode('', 0),
            ContractEventActionNode('', 0, 'Terminated')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_disburse_termination')
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            WithinNode('', 0),
            TimespanNode('', 0, '10 days'),
            EventNode('', 0),
            ContractEventNode('',0),
            ContractEventActionNode('', 0, 'Terminated')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_reimburse_termination')
    ),

    ## Termination power
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            DomainEventNode('', 0),
            DomainEventNameNode('', 0, 'evt_provide_termination_notice_manager')
        ]),
        parm_config = ParameterConfig('powers', 'pow_terminate_notice_manager', 'trigger'),
        norm_id = 'pow_terminate_notice_manager',
        debtor = 'manager',
        creditor = 'owner'
    ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            DomainEventNode('', 0),
            DomainEventNameNode('', 0, 'evt_provide_termination_notice_owner')
        ]),
        parm_config = ParameterConfig('powers', 'pow_terminate_notice_owner', 'trigger'),
        norm_id = 'pow_terminate_notice_owner',
        debtor = 'owner',
        creditor = 'manager'
    ),
]