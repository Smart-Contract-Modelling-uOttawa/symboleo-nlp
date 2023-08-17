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
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBefore

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig


# Payment to Porex of undisputed fees shall be due [P1]
## Original: 10 days following Cerus' receipt of the invoice submitted by Porex
## CNL: 10 days after Porex submits invoice receipt to Cerus
## TIMESPAN P_AFTER_T EVENT => WHappensBefore

test_case = TestCase(
    'timespan_after_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'PayFees': DomainEvent('PayFees', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'Porex': RoleDeclaration('Porex', 'PartyA', []),
                'Cerus': RoleDeclaration('Cerus', 'PartyB', []),
                'evt_pay_fees': EventDeclaration('evt_pay_fees', 'PayFees', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_fees': Obligation(
                    'ob_pay_fees', 
                    None, 
                    'Cerus', 
                    'Porex', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_pay_fees')))
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
                    'Payment to Porex of undisputed fees shall be due [P1]', 
                    {'P1': [ParameterConfig('obligations', 'ob_pay_fees', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.AT_LEAST, 'at least'),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '10'),
            UserInput(UnitType.TIME_UNIT, 'days'),
            UserInput(UnitType.AFTER, 'after'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'Porex'),
            UserInput(UnitType.TRANSITIVE_VERB, 'submits'),
            UserInput(UnitType.DOBJ, 'invoice receipt'),
            UserInput(UnitType.PREP_PHRASE, 'to Cerus'),
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
                'Receipt': Asset('Receipt', []),
            },
            events = {
                'PayFees': DomainEvent('PayFees', []),
                'SubmitReceipt': DomainEvent('SubmitReceipt', [
                    DomainProp('submitting_agent', 'Role'),
                    DomainProp('submitting_target', 'Role'),
                    DomainProp('submitted_object', 'Receipt')
                ])
                },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'Porex': RoleDeclaration('Porex', 'PartyA', []),
                'Cerus': RoleDeclaration('Cerus', 'PartyB', []),
                'invoice_receipt': AssetDeclaration('invoice_receipt', 'Receipt', []),
                'evt_pay_fees': EventDeclaration('evt_pay_fees', 'PayFees', []),
                'evt_submit_receipt': EventDeclaration('evt_submit_receipt', 'SubmitReceipt', [
                    DeclarationProp('submitting_agent', 'Porex', 'Role'),
                    DeclarationProp('submitting_target', 'Cerus', 'Role'),
                    DeclarationProp('submitted_object', 'invoice_receipt', 'Receipt'),
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_fees': Obligation(
                    'ob_pay_fees', 
                    None, 
                    'Cerus', 
                    'Porex', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionWHappensBefore(
                            VariableEvent('evt_pay_fees'),
                            Point(PointFunction(PointVDE('evt_submit_receipt'), '10', TimeUnit.Days))
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
                    'Payment to Porex of undisputed fees shall be due at least 10 days after Porex submits invoice receipt to Cerus', 
                    {'P1': [ParameterConfig('obligations', 'ob_pay_fees', 'consequent')]})
            }
        )
    ),
)



