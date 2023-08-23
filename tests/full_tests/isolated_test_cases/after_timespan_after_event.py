from tests.full_tests.isolated_test_cases.TestSymboleoContract import TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, DomainEvent
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import RoleDeclaration, EventDeclaration
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensAfter

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# Following the expiration of 90 days from the termination or expiration of this agreement, the company shall cease usage of all advertising materials which contain the professional's image
# [P1], the company shall cease usage of all advertising materials which contain the professional's image
## Original: Following the expiration of 90 days from the termination or expiration of this agreement
## CNL: after 90 days following contract termination
## P_AFTER_PF TIMESPAN P_AFTER_T EVENT => HappensAfter


test_case = TestCase(
    'after_timespan_after_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'CeaseAdvertising': DomainEvent('CeaseAdvertising', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'company': RoleDeclaration('Company', 'PartyA', id='company'),
                'professional': RoleDeclaration('Professional', 'PartyB', id='professional'),
                'evt_cease_advertising': EventDeclaration('evt_cease_advertising', 'CeaseAdvertising', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_cease_advertising': Obligation(
                    'ob_cease_advertising', 
                    None, 
                    'company', 
                    'professional', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_cease_advertising')))
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
                    '[P1] the company shall cease usage of all advertising materials which contain the professional\'s image', 
                    {'P1': [ParameterConfig('obligations', 'ob_cease_advertising', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.FOLLOWING, 'following'),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '90'),
            UserInput(UnitType.TIME_UNIT, 'days'),
            UserInput(UnitType.AFTER, 'after'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
            UserInput(UnitType.CONTRACT_ACTION, 'terminates')
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
            events = {'CeaseAdvertising': DomainEvent('CeaseAdvertising', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'company': RoleDeclaration('Company', 'PartyA', id='company'),
                'professional': RoleDeclaration('Professional', 'PartyB', id='professional'),
                'evt_cease_advertising': EventDeclaration('evt_cease_advertising', 'CeaseAdvertising', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_cease_advertising': Obligation(
                    'ob_cease_advertising', 
                    None, 
                    'company', 
                    'professional', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionHappensAfter(
                            VariableEvent('evt_cease_advertising'),
                            Point(
                                PointFunction(
                                    ContractEvent(ContractEventName.Terminated),
                                    '90', 
                                    TimeUnit.Days
                                )
                            )
                        )
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
                    'following 90 days after contract terminates the company shall cease usage of all advertising materials which contain the professional\'s image', 
                    {'P1': [ParameterConfig('obligations', 'ob_cease_advertising', 'consequent')]})
            }
        )
    ),
)



