from app.classes.selection.all_nodes import BeforeNode, ContractEventActionNode, ContractEventNode, DomainEventNameNode, DomainEventNode, EventNode, IfNode, ObligationEventActionNode, ObligationEventNode, ObligationEventVarNode, RootNode, UntilNode
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.domain_object import DomainEvent, DomainProp
from app.src.grammar.selection import Selection
from app.src.operations.contract_updater_config import UpdateConfig
from app.src.operations.op_code import OpCode
from app.src.operations.refine_parameter.parm_configs import ParameterConfig

test_suite = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'ob_pay_rent'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_late_payment'),
        parm_key='late_payment'
    ),
    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('Occupy', [
            DomainProp('agent', 'Role'),
            DomainProp('property', 'RentalProperty')
        ]),
        declaration = Declaration('evt_occupy', 'Occupy', 'events', [
            DeclarationProp('agent', 'renter', 'Role'),
            DeclarationProp('property', 'the_property', 'RentalProperty'),
        ])
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            BeforeNode('', 0),
            EventNode('', 0),
            DomainEventNode('',0),
            DomainEventNameNode('', 0, 'evt_occupy')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_pay_security_deposit'),
        parm_key='pay_security_deposit'
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ContractEventNode('', 0),
            ContractEventActionNode('', 0, 'Terminated')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_return_deposit'),
        parm_key='return_deposit'
    ),
    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('AllowPets', [
            DomainProp('grantor', 'Role')
        ]),
        declaration = Declaration('evt_allow_pets', 'AllowPets', 'events', [
            DeclarationProp('grantor', 'landlord', 'Role')
        ])
    ),
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            UntilNode('', 0), # TODO: Need an Unless node
            EventNode('', 0),
            DomainEventNode('', 0),
            DomainEventNameNode('', 0, 'evt_allow_pets')
        ]),
        parm_config = ParameterConfig('obligations', 'ob_no_pets'),
        parm_key= 'no_pets'
    ),

    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('ProvideTerminationNotice', [
            DomainProp('agent', 'Role'),
            DomainProp('daysInAdvance', 'Number')
        ]),
        declaration = Declaration('evt_provide_termination_notice', 'ProvideTerminationNotice', 'events', [
            DeclarationProp('agent', 'landlord', 'Role'),
            DeclarationProp('daysInAdvance', 'var_daysInAdvance', 'Number')
        ])
    ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            DomainEventNode('', 0),
            DomainEventNameNode('', 0, 'evt_provide_termination_notice')
        ]),
        parm_config = ParameterConfig('powers', 'pow_termination_written', 'trigger'),
        norm_id = 'pow_termination_written',
        debtor = 'renter',
        creditor = 'landlord'
    ),

    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('Abandon', [
            DomainProp('agent', 'Role'),
            DomainProp('property', 'RentalProperty')
        ]),
        declaration = Declaration('evt_abandon', 'Abandon', 'events', [
            DeclarationProp('agent', 'renter', 'Role'),
            DeclarationProp('property', 'the_property', 'RentalProperty')
        ])
    ),
    UpdateConfig(
        OpCode.ADD_TERMINATION_POWER,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            DomainEventNode('', 0),
            DomainEventNameNode('', 0, 'evt_abandon')
        ]),
        parm_config = ParameterConfig('powers', 'pow_termination_abandon', 'trigger'),
        norm_id = 'pow_termination_abandon',
        debtor = 'landlord',
        creditor = 'renter'
    ),
]