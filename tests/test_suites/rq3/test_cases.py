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
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBefore

from app.classes.spec.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, NodeType
from app.classes.tokens.all_nodes import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# Input:
## Original Symboleo contract
## user input
## Parameter info

# Output
## Expected Symboleo... Maybe should do an expected UpdateObj...

test_suite = [
    TestCase(
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
            node_list = [
                # This will be the list of user inputs...
                UserInput(NodeType.ROOT),
                UserInput(NodeType.WITHIN),
                UserInput(NodeType.TIMESPAN, '14 days'),
                #UserInput(NodeType.OF)
                UserInput(NodeType.EVENT),
                UserInput(NodeType.CUSTOM_EVENT),
                UserInput(NodeType.SUBJECT, 'Dolphin'),
                UserInput(NodeType.VERB, 'receiving'),
                UserInput(NodeType.DOBJ, 'the original digital photo files'),
                UserInput(NodeType.FINAL_NODE)
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
                    'evt_receive': Declaration('evt_receive', 'Receive', 'events', [
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
                            Point(PointFunction(PointVDE('evt_receive'), '14', TimeUnit.Days))
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
                        'Dolphin agrees to complete its photo-editing services within 14 days of receiving the original digital photo files', 
                        {'PARM': [ParameterConfig('obligations', 'ob_complete', 'consequent')]})
                }
            )
        ),

    )
]



# within 14 days of receiving the original digital photo files



#expected_sym = SymboleoContract()

# test_suite: List[TestInfo] = [
#     TestInfo(
#         'Dolphin agrees to complete its photo-editing services [PARAMETER]',
        
#         'within 14 days of receiving the original digital photo files',


#         Obligation('test_id', None, 'BOSCH')
#         [
#             Declaration('evt_disrupts_interferes', 'DisruptsOrInterferes', 'events', [
#                 DeclarationProp('disruption_obj', 'CLIENTS business', 'String')
#             ])
#         ],

#     )
# ]

# Plan
## Have original NL
## Have the intended Symboleo
## Have a list of UserInputs correspondig to it
## Generate the Symboleo
## Compare the Symboleo and the NL

# Need a SymboleoTest

