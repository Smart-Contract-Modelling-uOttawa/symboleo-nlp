from typing import List
from tests.full_tests.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import RoleDeclaration, EventDeclaration, AssetDeclaration, DeclarationProp
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

# the Franchise Fee shall be paid to Grantor [PARAMETER]
## Original: on or before March 31, 2017
## CNL: before March 31, 2017
## BEFORE DATE => SHappensBefore


test_case = TestCase(
    'before_date',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'franchise_dm',
            roles = {
                'Grantor': Role('Grantor', []),
                'Grantee': Role('Grantee', [])
            },
            assets = {},
            events = {'PayFee': DomainEvent('PayFee', [
                DomainProp('payer', 'Role'),
                DomainProp('payee', 'Role'),
            ])},
            enums=[]
        ),
        ContractSpec(
            id = 'franchise_cs',
            declarations = {
                'grantor': RoleDeclaration('grantor', 'Grantor'),
                'grantee': RoleDeclaration('grantee', 'Grantee'),
                'evt_pay_fee': EventDeclaration('evt_pay_fee', 'PayFee', [
                    DeclarationProp('payer', 'grantee', 'Role'),
                    DeclarationProp('payee', 'grantor', 'Role'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_fee': Obligation('ob_pay_fee', None, 'grantee', 'grantor', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_pay_fee')))
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
                    'the Franchise Fee shall be paid to Grantor [PARAMETER]', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_pay_fee', 'consequent')]})
            }
        )
    ),
    op_code = OpCode.UPDATE_PARM,
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.BEFORE, 'before'),
            UserInput(UnitType.DATE, 'March 31, 2017')
        ],
        nl_key='nl_key',
        parm_key='PARAMETER'
    ),
    exp_sym = SymboleoContract(
        DomainModel(
            id = 'franchise_dm',
            roles = {
                'Grantor': Role('Grantor', []),
                'Grantee': Role('Grantee', [])
            },
            assets = {},
            events = {'PayFee': DomainEvent('PayFee', [
                DomainProp('payer', 'Role'),
                DomainProp('payee', 'Role'),
            ])},
            enums=[]
        ),
        ContractSpec(
            id = 'franchise_cs',
            parameters=[ContractSpecParameter('ob_pay_fee_date', 'Date')],
            declarations = {
                'grantor': RoleDeclaration('grantor', 'Grantor'),
                'grantee': RoleDeclaration('grantee', 'Grantee'),
                'evt_pay_fee': EventDeclaration('evt_pay_fee', 'PayFee', [
                    DeclarationProp('payer', 'grantee', 'Role'),
                    DeclarationProp('payee', 'grantor', 'Role'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_fee': Obligation('ob_pay_fee', None, 'grantee', 'grantor', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionSHappensBefore(VariableEvent('evt_pay_fee'), Point(PointVDE('ob_pay_fee_date'))))
                )
            },
            surviving_obligations={},
            powers = {},
            constraints=[]
        ),
        NLTemplate(
            {   
                'nl_key': TemplateObj(
                    'the Franchise Fee shall be paid to Grantor before March 31, 2017', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_pay_fee', 'consequent')]})
            }
        )
    )
)



