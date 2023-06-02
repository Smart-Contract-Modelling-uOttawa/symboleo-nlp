from typing import List
from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent,ContractEvent,ContractEventName
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBefore

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# The Buyer shall open an irrevocable letter of credit with the bank [PARAMETER]
## Original: within 30 days after signing the contract
## Mine: within 30 days of buyer signing the contract


letter_test_case = TestCase(
    'letter',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'letter_dm',
            roles = {
                'Buyer': Role('Buyer', []),
                'Bank': Role('Bank', [])
            },
            assets = {
            },
            events = {'OpenLetter': DomainEvent('OpenLetter', [
                DomainProp('opener', 'Role'),
                DomainProp('partner', 'Role'),
            ])},
            enums=[]
        ),
        ContractSpec(
            id = 'letter_cs',
            declarations = {
                'buyer': Declaration('buyer', 'Buyer', 'roles', []),
                'bank': Declaration('bank', 'Bank', 'roles', []),
                'evt_open_letter': Declaration('evt_open_letter', 'OpenLetter', 'events', [
                    DeclarationProp('opener', 'buyer', 'Role'),
                    DeclarationProp('partner', 'bank', 'Role'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_open_letter': Obligation('ob_open_letter', None, 'buyer', 'bank', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_open_letter')))
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
                    'The Buyer shall open an irrevocable letter of credit with the bank [PARAMETER]', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_open_letter', 'consequent')]})
            }
        )
    ),
    op_code = OpCode.UPDATE_PARM,
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '30 days'),
            #TODO:Need the 'of'/'after'
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Activated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='nl_key',
        parm_key='PARAMETER'
    ),
    exp_sym = SymboleoContract(
        DomainModel(
            id = 'letter_dm',
            roles = {
                'Buyer': Role('Buyer', []),
                'Bank': Role('Bank', [])
            },
            assets = {
            },
            events = {'OpenLetter': DomainEvent('OpenLetter', [
                DomainProp('opener', 'Role'),
                DomainProp('partner', 'Role'),
            ])},
            enums=[]
        ),
        ContractSpec(
            id = 'letter_cs',
            declarations = {
                'buyer': Declaration('buyer', 'Buyer', 'roles', []),
                'bank': Declaration('bank', 'Bank', 'roles', []),
                'evt_open_letter': Declaration('evt_open_letter', 'OpenLetter', 'events', [
                    DeclarationProp('opener', 'buyer', 'Role'),
                    DeclarationProp('partner', 'bank', 'Role'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_open_letter': Obligation('ob_open_letter', None, 'buyer', 'bank', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionWHappensBefore(
                        VariableEvent('evt_open_letter'),
                        Point(PointFunction(ContractEvent(ContractEventName.Activated), '30', TimeUnit.Days))
                    ))
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
                    'The Buyer shall open an irrevocable letter of credit with the bank within 30 days of contract activating', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_open_letter', 'consequent')]})
            }
        )
    )
)



