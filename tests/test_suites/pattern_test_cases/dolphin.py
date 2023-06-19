from typing import List
from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

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

dolphin_test_case = TestCase(
    'dolphin',
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
                'Dolphin': Declaration('Dolphin', 'Contractor', 'roles', []),
                'client': Declaration('client', 'Client', 'roles', []),
                'evt_complete_services': Declaration('evt_complete_services', 'CompleteServices', 'events', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_complete': Obligation('ob_complete', None, 'Dolphin', 'client', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_complete_services')))
                )
            },
            surviving_obligations={},
            powers = {},
            constraints=[],
            parameters=[]
        ),
        NLTemplate(
            {   
                'parm': TemplateObj(
                    'Dolphin agrees to complete its photo-editing services [PARM]', 
                    {'PARM': [ParameterConfig('obligations', 'ob_complete', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            # This will be the list of user inputs...
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '14 days'),
            UserInput(UnitType.OF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'Dolphin'),
            UserInput(UnitType.TRANSITIVE_VERB, 'receiving'),
            UserInput(UnitType.DOBJ, 'the original digital photo files')
        ],
        nl_key='parm',
        parm_key='PARM'
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
                'Receive': DomainEvent('Receive', [
                    DomainProp('receiving_agent', 'Role'),
                    DomainProp('received_object', 'Files')
                ]),    
            }, 
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'Dolphin': Declaration('Dolphin', 'Contractor', 'roles', []),
                'client': Declaration('client', 'Client', 'roles', []),
                'evt_complete_services': Declaration('evt_complete_services', 'CompleteServices', 'events', []),
                
                'photo_files': Declaration('photo_files', 'Files', 'assets', []),
                'evt_receive_files': Declaration('evt_receive_files', 'Receive', 'events', [
                    DeclarationProp('receiving_agent', 'Dolphin', 'Role'),
                    DeclarationProp('received_object', 'photo_files', 'Files')
                ]),
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_complete': Obligation('ob_complete', None, 'Dolphin', 'client', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionWHappensBefore(
                        VariableEvent('evt_complete_services'),
                        Point(PointFunction(PointVDE('evt_receive_files'), 14, TimeUnit.Days))
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
                'parm': TemplateObj(
                    'Dolphin agrees to complete its photo-editing services within 14 days of Dolphin receiving the original digital photo files', 
                    {'PARM': [ParameterConfig('obligations', 'ob_complete', 'consequent')]})
            }
        )
    ),
)



