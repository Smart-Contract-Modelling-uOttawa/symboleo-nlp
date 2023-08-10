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
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# For 24 months following termination of this agreement, licensee shall specify on all public-facing materials that licensee is no longer operating under the licensed mark.
# [P1], licensee shall specify on all public-facing materials that licensee is no longer operating under the licensed mark.
## Original: For 24 months following termination of this agreement
## CNL: For 24 months after contract terminates
## FOR TIMESPAN AFTER EVENT => HappensWithin

## Need to negate the event

test_case = TestCase(
    'materials',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'CeaseSpecifyingMark': DomainEvent('CeaseSpecifyingMark', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'licensee': RoleDeclaration('licensee', 'PartyA', []),
                'licensor': RoleDeclaration('licensor', 'PartyB', []),
                'evt_cease_specifying_mark': EventDeclaration('evt_cease_specifying_mark', 'CeaseSpecifyingMark', [])
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
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_cease_specifying_mark')), negation=True)
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
                    '[P1] licensee shall specify on all public-facing materials that licensee is no longer operating under the licensed mark.', 
                    {'P1': [ParameterConfig('obligations', 'ob_keep_using_mark', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.FOR, 'for'),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '24'),
            UserInput(UnitType.TIME_UNIT, 'months'),
            UserInput(UnitType.AFTER, 'after'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
            UserInput(UnitType.CONTRACT_ACTION, 'terminated'),
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
            events = {'CeaseSpecifyingMark': DomainEvent('CeaseSpecifyingMark', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'licensee': RoleDeclaration('licensee', 'PartyA', []),
                'licensor': RoleDeclaration('licensor', 'PartyB', []),
                'evt_cease_specifying_mark': EventDeclaration('evt_cease_specifying_mark', 'CeaseSpecifyingMark', [])
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
                            VariableEvent('evt_cease_specifying_mark'),
                            Interval(
                                IntervalFunction(
                                    PointVDE('self.end'),
                                    PointFunction(
                                        PointVDE('self.end'),
                                        '24',
                                        TimeUnit.Months
                                    )
                                ))
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
                    'for 24 months after contract terminates licensee shall specify on all public-facing materials that licensee is no longer operating under the licensed mark.', 
                    {'P1': [ParameterConfig('obligations', 'ob_keep_using_mark', 'consequent')]})
            }
        )
    ),
)



