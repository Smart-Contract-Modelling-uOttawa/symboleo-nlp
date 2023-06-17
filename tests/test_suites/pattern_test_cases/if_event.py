from typing import List
from tests.test_suites.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName
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


if_event_test_case = TestCase(
    'if_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'Contractor': Role('Contractor', []),
                'Client': Role('Client', [])
            },
            assets = {},
            events = {
                'CompleteServices': DomainEvent('CompleteServices', []),
                'Pay': DomainEvent('Pay', [])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'buyer': Declaration('buyer', 'Buyer', 'roles', []),
                'seller': Declaration('seller', 'Seller', 'roles', []),
                'evt_pay': Declaration('buyer', 'seller', 'events', []),
                'evt_complete_services': Declaration('evt_complete_services', 'CompleteServices', 'events', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_payment': Obligation('ob_payment', None, 'buyer', 'seller', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_pay')))
                ),
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
                    '[PARM] Seller agrees to complete the services', 
                    {'PARM': [ParameterConfig('obligations', 'ob_complete', 'antecedent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.NORM_EVENT),
            UserInput(UnitType.OBLIGATION_SUBJECT, 'ob_payment'),
            UserInput(UnitType.OBLIGATION_ACTION, 'Violated'),
            ## We assume this will be generated when user selects ob_payment + Violated
            ## Will need to handle that separately. Falls under input tree management
            #UserInput(UnitType.CUSTOM_EVENT), # May use a different node type here...?
            UserInput(UnitType.SUBJECT, 'buyer'),
            UserInput(UnitType.FAILS_TO),
            UserInput(UnitType.TRANSITIVE_VERB, 'complete'),
            UserInput(UnitType.DOBJ, 'payment'),
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
            assets = {},
            events = {
                'CompleteServices': DomainEvent('CompleteServices', []),
                'Pay': DomainEvent('Pay', [])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'buyer': Declaration('buyer', 'Buyer', 'roles', []),
                'seller': Declaration('seller', 'Seller', 'roles', []),
                'evt_pay': Declaration('buyer', 'seller', 'events', []),
                'evt_complete_services': Declaration('evt_complete_services', 'CompleteServices', 'events', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_payment': Obligation('ob_payment', None, 'buyer', 'seller', 
                    PropMaker.make_default(),
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_pay')))
                ),
                'ob_complete': Obligation('ob_complete', None, 'Dolphin', 'client', 
                    PropMaker.make(PredicateFunctionHappens(ObligationEvent(ObligationEventName.Violated, 'ob_payment'))),
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
                    'if buyer fails to complete payment Seller agrees to complete the services', 
                    {'PARM': [ParameterConfig('obligations', 'ob_complete', 'antecedent')]})
            }
        )
    ),
)


