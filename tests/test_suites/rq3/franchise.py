from typing import List
from tests.test_suites.rq3.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionSHappensBefore

from app.classes.spec.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# the Franchise Fee shall be paid to Grantor [PARAMETER]
## Original: on or before March 31, 2017
## Mine: before March 31, 2017

franchise_test_case = TestCase(
    'franchise',
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
                'grantor': Declaration('grantor', 'Grantor', 'roles', []),
                'grantee': Declaration('grantee', 'Grantee', 'roles', []),
                'evt_pay_fee': Declaration('evt_pay_fee', 'PayFee', 'events', [
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
            UserInput(UnitType.ROOT),
            UserInput(UnitType.BEFORE), # TODO: "on or before?"
            UserInput(UnitType.DATE, 'March 31, 2017'),
            UserInput(UnitType.FINAL_NODE)
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
            declarations = {
                'grantor': Declaration('grantor', 'Grantor', 'roles', []),
                'grantee': Declaration('grantee', 'Grantee', 'roles', []),
                'evt_pay_fee': Declaration('evt_pay_fee', 'PayFee', 'events', [
                    DeclarationProp('payer', 'grantee', 'Role'),
                    DeclarationProp('payee', 'grantor', 'Role'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_fee': Obligation('ob_pay_fee', None, 'grantee', 'grantor', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionSHappensBefore(VariableEvent('evt_pay_fee'), Point(PointVDE('March 31, 2017'))))
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
                    'the Franchise Fee shall be paid to Grantor before March 31, 2017.', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_pay_fee', 'consequent')]})
            }
        )
    )
)



