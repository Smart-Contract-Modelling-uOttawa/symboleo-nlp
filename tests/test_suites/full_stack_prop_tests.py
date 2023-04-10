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

from app.templates.prop_mgmt.t.nl_template import parameters

all_ops = [
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
        parm_config = parameters['CONDITION_A'].configs[0]
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
        parm_config = parameters['CONDITION_B'].configs[0]
    ),

    ## Temporal refinements
    UpdateConfig(
        OpCode.UPDATE_PARM,
        selection = Selection.from_nodes([
            RootNode('', 0),
            WithinNode('', 0),
            TimespanNode('', 0, '3 days'),
            EventNode('', 0),
            ContractEventNode('',0),
            ContractEventActionNode('', 0, 'Terminated')
        ]),
        parm_config = parameters['REFINEMENT_A'].configs[0]
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
        parm_config = parameters['REFINEMENT_B'].configs[0]
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

class FullStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ContractUpdaterBuilder.build()

    #@unittest.skip('skip when measuring coverage')
    def test_full_stack(self):
        contract = get_template('prop_t')
        expected_contract = get_template('prop_raw')
        expected_sym = expected_contract.to_sym()

        for test_config in all_ops:
            self.sut.update(contract, test_config.op_code, test_config)

        result = contract.to_sym()
        # with open('tests/test_suites/sample_target.txt', 'w') as f:
        #     f.write(result)
        
        self.assertEqual(result, expected_sym)
        

if __name__ == '__main__':
    unittest.main()