from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, DomainEvent
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import RoleDeclaration, EventDeclaration
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.sym_point import PointVDE
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin
from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# During the period beginning October 1, 2009 and ending March 31, 2010, charity tunes shall not enable another program sponsorship
# [P1] charity tunes shall not enable another program sponsorship
## Original: During the period beginning October 1, 2009 and ending March 31, 2010
## CNL: between October 1, 2009 and March 31, 2010
## BETWEEN DATE AND DATE => HappensWithin

## Need to negate the event

test_case = TestCase(
    'between_interval',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'EnableSponsorship': DomainEvent('EnableSponsorship', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'charity': RoleDeclaration('charity', 'PartyA', []),
                'sponsor': RoleDeclaration('sponsor', 'PartyB', []),
                'evt_enable_sponsorship': EventDeclaration('evt_enable_sponsorship', 'EnableSponsorship', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_no_sponsorship': Obligation(
                    'ob_no_sponsorship', 
                    None, 
                    'charity', 
                    'sponsor', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_enable_sponsorship')), negation=True)
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
                    '[P1] charity tunes shall not enable another program sponsorship', 
                    {'P1': [ParameterConfig('obligations', 'ob_no_sponsorship', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.BETWEEN, 'between'),
            UserInput(UnitType.DATE, 'October 1, 2009'),
            UserInput(UnitType.AND, 'and'),
            UserInput(UnitType.DATE, 'March 31, 2010')
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
            events = {'EnableSponsorship': DomainEvent('EnableSponsorship', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'charity': RoleDeclaration('charity', 'PartyA', []),
                'sponsor': RoleDeclaration('sponsor', 'PartyB', []),
                'evt_enable_sponsorship': EventDeclaration('evt_enable_sponsorship', 'EnableSponsorship', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_no_sponsorship': Obligation(
                    'ob_no_sponsorship', 
                    None, 
                    'charity', 
                    'sponsor', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionHappensWithin(
                            VariableEvent('evt_enable_sponsorship'),
                            Interval(
                                IntervalFunction(
                                    PointVDE('October 1, 2009'),
                                    PointVDE('March 31, 2010')
                                )
                            )
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
                    'between October 1, 2009 and March 31, 2010 charity tunes shall not enable another program sponsorship', 
                    {'P1': [ParameterConfig('obligations', 'ob_no_sponsorship', 'consequent')]})
            }
        )
    ),
)



