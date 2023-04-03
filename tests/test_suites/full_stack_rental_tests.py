import unittest
from typing import List
from app.src.helpers.template_getter import get_template
from app.src.grammar.selection import Selection, SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.operations.contract_updater import OpCode

from app.classes.spec.domain_model import DomainEvent, DomainProp
from app.classes.spec.declaration import Declaration, DeclarationProp

from app.src.operations.parm_configs import ParameterConfig

from app.src.operations.contract_updater_builder import ContractUpdaterBuilder
from app.src.operations.contract_updater_config import UpdateConfig

from app.templates.rental_agreement.t.nl_template import parameters

all_ops = [
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            IfNode('', 0),
            EventNode('', 0),
            ObligationEventNode('',0),
            ObligationEventVarNode('', 0, 'pay_rent'),
            ObligationEventActionNode('', 0, 'Violated')
        ]),
        parm_config = parameters['LATE_PAYMENT_CONDITION'].configs[0]
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
        parm_config = parameters['SECURITY_DEPOSIT_REFINEMENT'].configs[0]
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
        parm_config = parameters['RETURN_DEPOSIT_REFINEMENT'].configs[0]
    ),
    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('AllowPets', [
            DomainProp('grantor', 'Role')
        ]),
        declaration = Declaration('evt_allowPets', 'AllowPets', 'events', [
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
            DomainEventNameNode('', 0, 'evt_allowPets')
        ]),
        parm_config = parameters['PETS_UNLESS_CONDITION'].configs[0]
    ),

    UpdateConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('ProvideTerminationNotice', [
            DomainProp('agent', 'Role'),
            DomainProp('daysInAdvance', 'Number')
        ]),
        declaration = Declaration('evt_provideTerminationNotice', 'ProvideTerminationNotice', 'events', [
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
            DomainEventNameNode('', 0, 'evt_provideTerminationNotice')
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

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ContractUpdaterBuilder.build()

    @unittest.skip('skip when measuring coverage')
    def test_full_stack(self):
        contract = get_template('rental_t')
        expected_contract = get_template('rental_raw')
        expected_sym = expected_contract.to_sym()

        for test_config in all_ops:
            self.sut.update(contract, test_config.op_code, test_config)

        result = contract.to_sym()
        
        self.assertEqual(result, expected_sym)
        

if __name__ == '__main__':
    unittest.main()