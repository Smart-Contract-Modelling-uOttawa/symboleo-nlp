from typing import List
from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration, DeclarationProp, RoleDeclaration,AssetDeclaration, EventDeclaration
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBeforeEvent

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# Prime agrees to fund additional shareholder loans equal to the amount repayed by the shareholder until each component of project completion is satisfied.
# Prime agrees to fund additional shareholder loans equal to the amount repayed by the shareholder [P1]
## Original: until each component of project completion is satisfied
## CNL: until Prime completes all project components
## UNTIL EVENT => WHappensBeforeEvent

# Since its 'until', we are dealing with a situation - need to negate the event

test_case = TestCase(
    'until_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'StopFundingLoans': DomainEvent('StopFundingLoans', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'prime': RoleDeclaration('Prime', 'PartyA', id='prime'),
                'shareholder': RoleDeclaration('Shareholder', 'PartyB', id='shareholder'),
                'evt_stop_funding_loans': EventDeclaration('evt_stop_funding_loans', 'StopFundingLoans', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_keep_funding_loans': Obligation(
                    'ob_keep_funding_loans', 
                    None, 
                    'prime', 
                    'shareholder', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_stop_funding_loans')), negation=True)
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
                    'Prime agrees to fund additional shareholder loans equal to the amount repaid by the shareholder [P1]', 
                    {'P1': [ParameterConfig('obligations', 'ob_keep_funding_loans', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.UNTIL, 'until'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'Prime'),
            UserInput(UnitType.TRANSITIVE_VERB, 'completes'),
            UserInput(UnitType.DOBJ, 'all project components'),

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
            assets = {
                'Components': Asset('Components', [])
            },
            events = {
                'StopFundingLoans': DomainEvent('StopFundingLoans', []),
                'CompleteComponents': DomainEvent('CompleteComponents', [
                    DomainProp('completing_agent', 'Role'),
                    DomainProp('completed_object', 'Components')
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'prime': RoleDeclaration('Prime', 'PartyA', id='prime'),
                'shareholder': RoleDeclaration('Shareholder', 'PartyB', id='shareholder'),
                'project_components': AssetDeclaration('project_components', 'Components', []),
                'evt_stop_funding_loans': EventDeclaration('evt_stop_funding_loans', 'StopFundingLoans', []),
                'evt_complete_components': EventDeclaration('evt_complete_components', 'CompleteComponents', [
                    DeclarationProp('completing_agent', 'prime', 'Role'),
                    DeclarationProp('completed_object', 'project_components', 'Components'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_keep_funding_loans': Obligation(
                    'ob_keep_funding_loans', 
                    None, 
                    'prime', 
                    'shareholder', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionWHappensBeforeEvent(
                            VariableEvent('evt_stop_funding_loans'),
                            VariableEvent('evt_complete_components')
                        ), 
                        negation=True
                    )
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
                    'Prime agrees to fund additional shareholder loans equal to the amount repaid by the shareholder until Prime completes all project components', 
                    {'P1': [ParameterConfig('obligations', 'ob_keep_funding_loans', 'consequent')]})
            }
        )
    ),
)



