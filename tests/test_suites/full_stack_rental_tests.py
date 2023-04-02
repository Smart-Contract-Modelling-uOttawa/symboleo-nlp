import unittest
from typing import List
from app.src.helpers.template_getter import get_template
from app.src.grammar.selection import Selection, SelectedNode
from app.classes.grammar.selected_nodes.all_nodes import *
from app.src.operations.contract_updater import OpCode
from tests.test_suites.test_runner import TestConfig, TestRunner

from app.classes.spec.domain_model import DomainEvent, DomainProp
from app.classes.spec.declaration import Declaration, DeclarationProp

from app.src.operations.parm_operations.configs import ParameterConfig

from app.templates.rental_agreement.t.nl_template import parameters

all_ops = [
    TestConfig(
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
    TestConfig(
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
    TestConfig(
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
    TestConfig(
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
    TestConfig(
        OpCode.ADD_DOMAIN_OBJECT,
        dm_obj_type = 'events',
        domain_object = DomainEvent('AllowPets', [
            DomainProp('grantor', 'Role')
        ]),
        declaration = Declaration('evt_allowPets', 'AllowPets', 'events', [
            DeclarationProp('grantor', 'landlord', 'Role')
        ])
    ),
    TestConfig(
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

    TestConfig(
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
    TestConfig(
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

    TestConfig(
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
    TestConfig(
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
        self.runner = TestRunner()

    #@unittest.skip('skip when measuring coverage')
    def test_full_stack(self):
        contract = get_template('rental_t')
        expected_contract = get_template('rental_raw')
        expected_sym = expected_contract.to_sym()

        for test_config in all_ops:
            contract = self.runner.update_contract(contract, test_config)

        result = contract.to_sym()
        
        self.assertEqual(result, expected_sym)
        

if __name__ == '__main__':
    unittest.main()