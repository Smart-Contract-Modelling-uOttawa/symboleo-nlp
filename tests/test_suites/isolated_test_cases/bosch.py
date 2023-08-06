from typing import List
from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import AssetDeclaration, RoleDeclaration, EventDeclaration, DeclarationProp
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

## TODO: Kill/replace this... not dealing with rights...
# BOSCH reserves the right to share rights given unless it disrupts and/or interferes with CLIENTS business and/or productivity
# BOSCH reserves the right to share rights given [PARAMETER]
## Original: unless it disrupts and/or interferes with CLIENTS business and/or productivity
## CNL: unless BOSCH disrupts productivity of CLIENT
## Operation: UNLESS EVENT => Power to 

bosch_test_case = TestCase(
    'bosch',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'Customer': Role('Customer', []),
                'Client': Role('Client', [])
            },
            assets = {},
            events = {'ShareRights': DomainEvent('ShareRights', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'BOSCH': RoleDeclaration('BOSCH', 'Customer'),
                'CLIENT': RoleDeclaration('CLIENT', 'Client'),
                'evt_share_rights': EventDeclaration('evt_share_rights', 'ShareRights')
            },
            parameters=[],
            obligations = {
                'ob_not_share': Obligation(
                    'ob_not_share', 
                    PropMaker.make_default(False), 
                    'BOSCH', 
                    'CLIENT', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionHappens(VariableEvent('evt_share_rights')),
                        negation=True
                    )
                )
            },
            powers={}
        ),
        NLTemplate(
            {   
                'parm': TemplateObj(
                    'BOSCH reserves the right to share rights given [PARM]', 
                    {'PARM': [ParameterConfig('obligations', 'ob_not_share', 'trigger')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    # unless BOSCH disrupts productivity of CLIENT
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.UNLESS, 'unless'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'BOSCH'),
            UserInput(UnitType.TRANSITIVE_VERB, 'disrupts'),
            UserInput(UnitType.DOBJ, 'productivity'),
            UserInput(UnitType.PREP_PHRASE, 'of CLIENT')
        ],
        nl_key='parm',
        parm_key='PARM'
    ),
    
    exp_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'Customer': Role('Customer', []),
                'Client': Role('Client', [])
            },
            assets = {
                'Productivity': Asset('Productivity', [])
            },
            events = {
                'ShareRights': DomainEvent('ShareRights', []),
                'Disrupt': DomainEvent('Disrupt', [
                    DomainProp('disrupting_agent', 'Role'),
                    DomainProp('disrupted_object', 'Productivity'),
                    DomainProp('disrupting_target', 'Role'),
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'BOSCH': RoleDeclaration('BOSCH', 'Customer'),
                'CLIENT': RoleDeclaration('CLIENT', 'Client'),
                'productivity': AssetDeclaration('productivity', 'Productivity'),
                'evt_share_rights': EventDeclaration('evt_share_rights', 'ShareRights'),
                'evt_disrupt': EventDeclaration('evt_disrupt', 'Disrupt', [
                    DeclarationProp('disrupting_agent', 'BOSCH', 'Role'),
                    DeclarationProp('disrupted_object', 'productivity', 'Productivity'),
                    DeclarationProp('disrupting_target', 'CLIENT', 'Role'),
                ])
            },
            parameters=[],
            obligations = {
                'ob_not_share': Obligation(
                    'ob_not_share', 
                    PropMaker.make(
                        PredicateFunctionHappens(VariableEvent('evt_disrupt'))
                    ), 
                    'BOSCH', 
                    'CLIENT', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionHappens(VariableEvent('evt_share_rights')),
                        negation=True
                    )
                )
            },
            powers={}
        ),
        NLTemplate(
            {   
                'parm': TemplateObj(
                    'BOSCH reserves the right to share rights given unless BOSCH disrupts productivity of CLIENT', 
                    {'PARM': [ParameterConfig('obligations', 'ob_not_share', 'trigger')]})
            }
        )
    ),
)



