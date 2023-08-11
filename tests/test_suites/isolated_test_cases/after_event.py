from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, DomainEvent, DomainProp, Asset
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import RoleDeclaration, EventDeclaration, AssetDeclaration, DeclarationProp
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBeforeEvent

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# If dividends are credited after premiums can no longer be paid under this contract, dividends will be paid in cash
# If dividends are credited [P1], dividends will be paid in cash
## Original: after premiums can no longer be paid under this contract
## CNL: after partyA becomes insolvent
## P_AFTER_E EVENT => HappensAfter (conditional)


test_case = TestCase(
    'after_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {
                'PayDividends': DomainEvent('PayDividends', [
                    DomainProp('payment_method', 'String'),
                    DomainProp('paying_agent', 'Role'),
                    DomainProp('paying_target', 'Role')
                ]),
                'CreditDividends': DomainEvent('CreditDividends', [
                    DomainProp('crediting_agent', 'Role')
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'partyA': RoleDeclaration('partyA', 'PartyA', []),
                'partyB': RoleDeclaration('partyB', 'PartyB', []),
                'evt_pay_dividends': EventDeclaration('evt_pay_dividends', 'PayDividends', [
                    DeclarationProp('paying_agent', 'partyA', 'Role'),
                    DeclarationProp('paying_target', 'partyB', 'Role'),
                    DeclarationProp('payment_method', 'cash', 'String'),
                ]),
                'evt_credit_dividends': EventDeclaration('evt_credit_dividends', 'CreditDividends', [
                    DeclarationProp('crediting_agent', 'partyB', 'Role')
                ])

            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_dividends': Obligation(
                    'ob_pay_dividends', 
                    None, 
                    'partyA', 
                    'partyB', 
                    PropMaker.make(
                        PredicateFunctionHappens(VariableEvent('evt_credit_dividends'))
                    ), 
                    PropMaker.make(
                        PredicateFunctionHappens(VariableEvent('evt_pay_dividends'))
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
                    'If dividends are credited [P1] dividends will be paid in cash', 
                    {'P1': [ParameterConfig('obligations', 'ob_pay_dividends', 'antecedent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.AFTER, 'after'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'partyA'),
            UserInput(UnitType.LINKING_VERB, 'becomes'),
            UserInput(UnitType.PREDICATE, 'insolvent')
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
            events = {
                'PayDividends': DomainEvent('PayDividends', [
                    DomainProp('payment_method', 'String'),
                    DomainProp('paying_agent', 'Role'),
                    DomainProp('paying_target', 'Role')
                ]),
                'CreditDividends': DomainEvent('CreditDividends', [
                    DomainProp('crediting_agent', 'Role')
                ]),
                'AgentInsolvent': DomainEvent('AgentInsolvent', [
                    DomainProp('agent', 'Role')
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'partyA': RoleDeclaration('partyA', 'PartyA', []),
                'partyB': RoleDeclaration('partyB', 'PartyB', []),
                'evt_pay_dividends': EventDeclaration('evt_pay_dividends', 'PayDividends', [
                    DeclarationProp('paying_agent', 'partyA', 'Role'),
                    DeclarationProp('paying_target', 'partyB', 'Role'),
                    DeclarationProp('payment_method', 'cash', 'String'),
                ]),
                'evt_credit_dividends': EventDeclaration('evt_credit_dividends', 'CreditDividends', [
                    DeclarationProp('crediting_agent', 'partyB', 'Role')
                ]),
                'evt_agent_insolvent': EventDeclaration('evt_agent_insolvent', 'AgentInsolvent', [
                    DeclarationProp('agent', 'partyA', 'Role')
                ]),


            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_dividends': Obligation(
                    'ob_pay_dividends', 
                    None, 
                    'partyA', 
                    'partyB', 
                    PropMaker.make(
                        PredicateFunctionWHappensBeforeEvent(
                            VariableEvent('evt_agent_insolvent'),
                            VariableEvent('evt_credit_dividends')
                        )
                    ), 
                    PropMaker.make(
                        PredicateFunctionHappens(VariableEvent('evt_pay_dividends'))
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
                    'If dividends are credited after partyA becomes insolvent dividends will be paid in cash', 
                    {'P1': [ParameterConfig('obligations', 'ob_pay_dividends', 'antecedent')]})
            }
        )
    ),
)



