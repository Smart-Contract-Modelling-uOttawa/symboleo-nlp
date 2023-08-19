from typing import List
from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import DeclarationProp, EventDeclaration, AssetDeclaration, RoleDeclaration
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionSHappensBefore

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# Shi farms will use its best efforts to quarantine product until delivery date as agreed by the parties.
# Shi farms will use its best efforts to quarantine product [P1]
## Original: until delivery date as agreed by the parties.
## CNL: until [DELIVERY_DATE]
## UNTIL DATE => SHappensBefore

## Must be negated event

test_case = TestCase(
    'until_date',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {
                'Product': Asset('Product', [])
            },
            events = {'UnquarantineProduct': DomainEvent('UnquarantineProduct', [
                DomainProp('agent', 'Role'),
                DomainProp('product', 'Product'),
            ])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'shi_farms': RoleDeclaration('Shi Farms', 'PartyA', id='shi_farms'),
                'partyB': RoleDeclaration('partyB', 'PartyB'),
                'product': AssetDeclaration('the product', 'Product', id='product'),
                'evt_unquarantine_product': EventDeclaration('evt_unquarantine_product', 'UnquarantineProduct', [
                    DeclarationProp('agent', 'shi_farms', 'Role'),
                    DeclarationProp('product', 'product', 'Product'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_keep_quarantine': Obligation('ob_keep_quarantine', None, 'shi_farms', 'partyB', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_unquarantine_product')), negation = True)
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
                    'Shi farms will use its best efforts to quarantine product [P1]', 
                    {'P1': [ParameterConfig('obligations', 'ob_keep_quarantine', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.UNTIL, 'until'),
            UserInput(UnitType.DATE, '[DELIVERY_DATE]')
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
                'Product': Asset('Product', [])
            },
            events = {'UnquarantineProduct': DomainEvent('UnquarantineProduct', [
                DomainProp('agent', 'Role'),
                DomainProp('product', 'Product'),
            ])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            parameters=[
                ContractSpecParameter('delivery_date', 'Date')
            ],
            declarations = {
                'shi_farms': RoleDeclaration('Shi Farms', 'PartyA', id='shi_farms'),
                'partyB': RoleDeclaration('partyB', 'PartyB'),
                'product': AssetDeclaration('the product', 'Product', id='product'),
                'evt_unquarantine_product': EventDeclaration('evt_unquarantine_product', 'UnquarantineProduct', [
                    DeclarationProp('agent', 'shi_farms', 'Role'),
                    DeclarationProp('product', 'product', 'Product'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_keep_quarantine': Obligation('ob_keep_quarantine', None, 'shi_farms', 'partyB', PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionSHappensBefore(
                            VariableEvent('evt_unquarantine_product'),
                            Point(PointVDE('delivery_date'))
                        ), 
                        negation = True
                    )
                )
            },
            surviving_obligations={},
            powers = {},
            constraints=[],
        ),
        NLTemplate(
            {   
                'nl_key': TemplateObj(
                    'Shi farms will use its best efforts to quarantine product until [DELIVERY_DATE]', 
                    {'P1': [ParameterConfig('obligations', 'ob_keep_quarantine', 'consequent')]})
            }
        )
    ),
)



