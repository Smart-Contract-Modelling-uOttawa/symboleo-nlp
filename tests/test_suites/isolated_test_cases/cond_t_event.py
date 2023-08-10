from typing import List
from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBefore

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *
 
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# When the agreement ends, each party shall return all copies of information to the other
# [P1] each party shall return all copies of information to the other
## Original: When the agreement ends
## CNL: When the contract terminates
## COND_T EVENT => Trigger

test_case = TestCase(
    'cond_t_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {
                'ReturnInfo': DomainEvent('ReturnInfo', [
                    DomainProp('agent', 'Role'),
                    DomainProp('receiver', 'Role')
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'partyA': Declaration('partyA', 'PartyA', 'roles', []),
                'partyB': Declaration('partyB', 'PartyB', 'roles', []),
                'evt_return_info_a': Declaration('evt_return_info_a', 'ReturnInfo', 'events', [
                    DeclarationProp('agent', 'partyA', 'Role'),
                    DeclarationProp('receiver', 'partyB', 'Role')
                ]),
                'evt_return_info_b': Declaration('evt_return_info_b', 'ReturnInfo', 'events', [
                    DeclarationProp('agent', 'partyB', 'Role'),
                    DeclarationProp('receiver', 'partyA', 'Role')
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_return_info_a': Obligation('ob_return_info_a', None, 'partyA', 'partyB', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_return_info_a')))
                ),
                'ob_return_info_b': Obligation('ob_return_info_b', None, 'partyB', 'partyA', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_return_info_b')))
                )
            },
            surviving_obligations={},
            powers = {},
            constraints=[],
            parameters=[]
        ),

        NLTemplate(
            {   
                'nl_key': TemplateObj(
                    '[P1] each party shall return all copies of information to the other', 
                    {
                        'P1': [
                            ParameterConfig('obligations', 'ob_return_info_a', 'antecedent'),
                            ParameterConfig('obligations', 'ob_return_info_b', 'antecedent')
                        ]
                    }
                )
            }
        )
    ),
    op_code = OpCode.UPDATE_PARM,
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.WHEN, 'when'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
            UserInput(UnitType.CONTRACT_ACTION, 'terminated')
        ],
        nl_key='nl_key',
        parm_key='P1'
    ),
    exp_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {
                'ReturnInfo': DomainEvent('ReturnInfo', [
                    DomainProp('agent', 'Role'),
                    DomainProp('receiver', 'Role')
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'partyA': Declaration('partyA', 'PartyA', 'roles', []),
                'partyB': Declaration('partyB', 'PartyB', 'roles', []),
                'evt_return_info_a': Declaration('evt_return_info_a', 'ReturnInfo', 'events', [
                    DeclarationProp('agent', 'partyA', 'Role'),
                    DeclarationProp('receiver', 'partyB', 'Role')
                ]),
                'evt_return_info_b': Declaration('evt_return_info_b', 'ReturnInfo', 'events', [
                    DeclarationProp('agent', 'partyB', 'Role'),
                    DeclarationProp('receiver', 'partyA', 'Role')
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_return_info_a': Obligation(
                    'ob_return_info_a', 
                    PropMaker.make(PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))),
                    'partyA', 
                    'partyB', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_return_info_a')))
                ),
                'ob_return_info_b': Obligation(
                    'ob_return_info_b', 
                    PropMaker.make(PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))),
                    'partyB', 
                    'partyA', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_return_info_b')))
                )
            },
            surviving_obligations={},
            powers = {},
            constraints=[],
            parameters=[]
        ),
        
        NLTemplate(
            {   
                'nl_key': TemplateObj(
                    'when contract terminates each party shall return all copies of information to the other', 
                    {
                        'P1': [
                            ParameterConfig('obligations', 'ob_return_info_a', 'antecedent'),
                            ParameterConfig('obligations', 'ob_return_info_b', 'antecedent')
                        ]
                    }
                )
            }
        )
    ),
)



