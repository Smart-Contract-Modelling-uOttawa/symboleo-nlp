from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, DomainEvent, Asset, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import RoleDeclaration, EventDeclaration, AssetDeclaration, DeclarationProp
from app.classes.spec.norm import Obligation, Power
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig
from app.classes.spec.power_function import PFObligation, PFObligationName

# Unless approved by party a, party b shall pay liquidated damages to party a
# [P1] party b shall pay liquidated damages to party a
## Original: Unless approved by party a
## CNL: unless partyA provides approval
## P_EXCEPT EVENT => New power

test_case = TestCase(
    'except_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'PayDamages': DomainEvent('PayDamages', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'partyA': RoleDeclaration('partyA', 'PartyA', []),
                'partyB': RoleDeclaration('partyB', 'PartyB', []),
                'evt_pay_damages': EventDeclaration('evt_pay_damages', 'PayDamages', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_damages': Obligation(
                    'ob_pay_damages', 
                    None, 
                    'partyA', 
                    'partyB', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_pay_damages')))
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
                    'partyB shall pay liquidated damages to partyA [P1]', 
                    {'P1': [ParameterConfig('obligations', 'ob_pay_damages', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.UNLESS, 'unless'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'partyA'),
            UserInput(UnitType.TRANSITIVE_VERB, 'provides'),
            UserInput(UnitType.DOBJ, 'approval')
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
                'Approval': Asset('Approval', [])
            },
            events = {
                'PayDamages': DomainEvent('PayDamages', []),
                'ProvideApproval': DomainEvent('ProvideApproval', [
                    DomainProp('providing_agent', 'Role'),
                    DomainProp('provided_object', 'Approval')
                ]),
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'partyA': RoleDeclaration('partyA', 'PartyA', []),
                'partyB': RoleDeclaration('partyB', 'PartyB', []),
                'approval': AssetDeclaration('approval', 'Approval', []),
                'evt_pay_damages': EventDeclaration('evt_pay_damages', 'PayDamages', []),
                'evt_provide_approval': EventDeclaration('evt_provide_approval', 'ProvideApproval', [
                    DeclarationProp('providing_agent', 'partyA', 'Role'),
                    DeclarationProp('provided_object', 'approval', 'Approval')
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_pay_damages': Obligation(
                    'ob_pay_damages', 
                    None, 
                    'partyA', 
                    'partyB', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_pay_damages')))
                )
            },
            surviving_obligations={},
            powers = {
                'pow_terminate_ob_pay_damages': Power(
                    'pow_terminate_ob_pay_damages', 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_provide_approval'))), 
                    'partyB', 
                    'partyA', 
                    PropMaker.make_default(), 
                    PFObligation(PFObligationName.Terminated, 'ob_pay_damages')
                )
            },
            constraints=[],
            parameters=[]
        ),
        NLTemplate(
            {   
                'nl_key': TemplateObj(
                    'partyB shall pay liquidated damages to partyA unless partyA provides approval', 
                    {'P1': [ParameterConfig('obligations', 'ob_pay_damages', 'consequent')]})
            }
        )
    ),
)



