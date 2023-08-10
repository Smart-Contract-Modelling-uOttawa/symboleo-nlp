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
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensAfter

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# In no case may any pin code be redeemed later than March 31, 2010
# In no case may any pin code be redeemed [P1]
## Original: later than March 31, 2010
## CNL: later than March 31, 2010
## P_AFTER DATE => HappensAfter

test_case = TestCase(
    'pincode',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'RedeemPin': DomainEvent('RedeemPin', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'partyA': RoleDeclaration('partyA', 'PartyA', []),
                'partyB': RoleDeclaration('partyB', 'PartyB', []),
                'evt_redeem_pin': EventDeclaration('evt_redeem_pin', 'RedeemPin', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_redeem_pin': Obligation(
                    'ob_redeem_pin', 
                    None, 
                    'partyA', 
                    'partyB', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_redeem_pin')), negation=True)
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
                    'In no case may any pin code be redeemed [P1]', 
                    {'P1': [ParameterConfig('obligations', 'ob_redeem_pin', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.LATER_THAN, 'later than'),
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
            events = {'RedeemPin': DomainEvent('RedeemPin', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'partyA': RoleDeclaration('partyA', 'PartyA', []),
                'partyB': RoleDeclaration('partyB', 'PartyB', []),
                'evt_redeem_pin': EventDeclaration('evt_redeem_pin', 'RedeemPin', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_redeem_pin': Obligation(
                    'ob_redeem_pin', 
                    None, 
                    'partyA', 
                    'partyB', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionHappensAfter(
                            VariableEvent('evt_redeem_pin'),
                            Point(PointVDE('"March 31, 2010"'))
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
                    'In no case may any pin code be redeemed later than March 31, 2010', 
                    {'P1': [ParameterConfig('obligations', 'ob_redeem_pin', 'consequent')]})
            }
        )
    ),
)



