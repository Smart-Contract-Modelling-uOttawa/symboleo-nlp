from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration, DeclarationProp, RoleDeclaration, EventDeclaration, AssetDeclaration
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


# Dolphin agrees to complete its photo-editing services [PARAMETER]
## Original: within 14 days of receiving the original digital photo files
## CNL: within 14 days of Dolphin receiving the original digital photo files
## WITHIN TIMESPAN OF EVENT => WHappensBefore

test_case = TestCase(
    'within_timespan_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'Contractor': Role('Contractor', []),
                'Client': Role('Client', [])
            },
            assets = {},
            events = {'CompleteServices': DomainEvent('CompleteServices', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'dolphin': RoleDeclaration('Dolphin', 'Contractor', id='dolphin'),
                'client': RoleDeclaration('client', 'Client'),
                'evt_complete_services': EventDeclaration('evt_complete_services', 'CompleteServices', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_complete': Obligation('ob_complete', None, 'dolphin', 'client', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_complete_services')))
                )
            },
            surviving_obligations={},
            powers = {},
            constraints=[],
            parameters=[
            ]
        ),
        NLTemplate(
            {   
                'nl_key': TemplateObj(
                    'Dolphin agrees to complete its photo-editing services [P1]', 
                    {'P1': [ParameterConfig('obligations', 'ob_complete', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.WITHIN, 'within'),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '14'),
            UserInput(UnitType.TIME_UNIT, 'days'),
            UserInput(UnitType.OF, 'of'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'Dolphin'),
            UserInput(UnitType.TRANSITIVE_VERB, 'receiving'),
            UserInput(UnitType.DOBJ, 'the original digital photo files')
        ],
        nl_key='nl_key',
        parm_key='P1'
    ),
    
    exp_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'Contractor': Role('Contractor', []),
                'Client': Role('Client', [])
            },
            assets = {
                'Files': Asset('Files', [])
            }, 
            events = {
                'CompleteServices': DomainEvent('CompleteServices', []),
                'ReceiveFiles': DomainEvent('ReceiveFiles', [
                    DomainProp('receiving_agent', 'Role'),
                    DomainProp('received_object', 'Files')
                ]),    
            }, 
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'dolphin': RoleDeclaration('Dolphin', 'Contractor', id='dolphin'),
                'client': RoleDeclaration('client', 'Client'),
                'evt_complete_services': EventDeclaration('evt_complete_services', 'CompleteServices', []),
                
                'photo_files': AssetDeclaration('photo_files', 'Files', []),
                
                'evt_receive_files': EventDeclaration('evt_receive_files', 'ReceiveFiles', [
                    DeclarationProp('receiving_agent', 'dolphin', 'Role'),
                    DeclarationProp('received_object', 'photo_files', 'Files')
                ]),
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_complete': Obligation('ob_complete', None, 'dolphin', 'client', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionWHappensBefore(
                        VariableEvent('evt_complete_services'),
                        Point(PointFunction(PointVDE('evt_receive_files'), '14', TimeUnit.Days))
                    ))
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
                    'Dolphin agrees to complete its photo-editing services within 14 days of Dolphin receiving the original digital photo files', 
                    {'P1': [ParameterConfig('obligations', 'ob_complete', 'consequent')]})
            }
        )
    ),
)



