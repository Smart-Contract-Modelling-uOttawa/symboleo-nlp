from typing import List
from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

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

# During the term of this agreement, licensee shall use the licensed mark only to the extent permitted under this license territory.
# [P1] licensee shall use the licensed mark only to the extent permitted under this license territory
## Original: During the term of this agreement
## CNL: during the contract period
## P_DURING TIME_PERIOD => HappensWithin

## Need to negate the event

test_case = TestCase(
    'licensee',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'CeaseUsingMark': DomainEvent('CeaseUsingMark', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'licensee': RoleDeclaration('licensee', 'PartyA', []),
                'licensor': RoleDeclaration('licensor', 'PartyB', []),
                'evt_cease_using_mark': EventDeclaration('evt_cease_using_mark', 'CeaseUsingMark', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_keep_using_mark': Obligation(
                    'ob_keep_using_mark', 
                    None, 
                    'licensee', 
                    'licensor', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_cease_using_mark')), negation=True)
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
                    '[P1] licensee shall use the licensed mark only to the extent permitted under this license territory', 
                    {'P1': [ParameterConfig('obligations', 'ob_keep_using_mark', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.DURING, 'during'),
            UserInput(UnitType.TIME_PERIOD, 'the contract period')
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
            events = {'CeaseUsingMark': DomainEvent('CeaseUsingMark', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'licensee': RoleDeclaration('licensee', 'PartyA', []),
                'licensor': RoleDeclaration('licensor', 'PartyB', []),
                'evt_cease_using_mark': EventDeclaration('evt_cease_using_mark', 'CeaseUsingMark', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_keep_using_mark': Obligation(
                    'ob_keep_using_mark', 
                    None, 
                    'licensee', 
                    'licensor', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionHappensWithin(
                            VariableEvent('evt_cease_using_mark'),
                            Interval(
                                IntervalFunction(
                                    PointVDE('self.start'),
                                    PointVDE('self.end'),
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
                    'during the contract period licensee shall use the licensed mark only to the extent permitted under this license territory', 
                    {'P1': [ParameterConfig('obligations', 'ob_keep_using_mark', 'consequent')]})
            }
        )
    ),
)



