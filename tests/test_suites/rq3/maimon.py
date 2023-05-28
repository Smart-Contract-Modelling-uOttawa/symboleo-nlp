from typing import List
from tests.test_suites.rq3.TestSymboleoContract import TestInfo, TestCase

from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.domain_object import Role, Asset, DomainEvent, DomainProp
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.norm import Obligation
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBefore

from app.classes.spec.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# Upon termination of this Agreement, Maimon agrees to return immediately to the Company all written Confidential Information
# [PARAMETER] Maimon agrees to return immediately to the Company all written Confidential Information
## Original: Upon termination of this Agreement
## Mine: If the contract terminates

# TODO: Should change the antecedent...
maimon_test_case = TestCase(
    'maimon',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'maimon_dm',
            roles = {
                'Contractor': Role('Contractor', []),
                'Company': Role('Company', [])
            },
            assets = {},
            events = {
                'ReturnInfo': DomainEvent('ReturnInfo', [
                    DomainProp('agent', 'Role'),
                    DomainProp('receiver', 'Role')
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'maimon_cs',
            declarations = {
                'Maimon': Declaration('Maimon', 'Contractor', 'roles', []),
                'company': Declaration('company', 'Company', 'roles', []),
                'evt_return_info': Declaration('evt_return_info', 'ReturnInfo', 'events', [
                    DeclarationProp('agent', 'Maimon', 'Role'),
                    DeclarationProp('receiver', 'company', 'Role')
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_return_info': Obligation('ob_return_info', None, 'Maimon', 'company', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_return_info')))
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
                    '[PARAMETER] Maimon agrees to return immediately to the Company all written Confidential Information', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_return_info', 'antecedent')]})
            }
        )
    ),
    op_code = OpCode.UPDATE_PARM,
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.IF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.STANDARD_EVENT),
            UserInput(UnitType.CONTRACT_EVENT),
            UserInput(UnitType.CONTRACT_SUBJECT),
            UserInput(UnitType.CONTRACT_ACTION, 'Terminated'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='nl_key',
        parm_key='PARAMETER'
    ),
    exp_sym = SymboleoContract(
        DomainModel(
            id = 'maimon_dm',
            roles = {
                'Contractor': Role('Contractor', []),
                'Company': Role('Company', [])
            },
            assets = {},
            events = {
                'ReturnInfo': DomainEvent('ReturnInfo', [
                    DomainProp('agent', 'Role'),
                    DomainProp('receiver', 'Role')
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'maimon_cs',
            declarations = {
                'Maimon': Declaration('Maimon', 'Contractor', 'roles', []),
                'company': Declaration('company', 'Company', 'roles', []),
                'evt_return_info': Declaration('evt_return_info', 'ReturnInfo', 'events', [
                    DeclarationProp('agent', 'Maimon', 'Role'),
                    DeclarationProp('receiver', 'company', 'Role')
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_return_info': Obligation(
                    'ob_return_info', 
                    None,
                    'Maimon', 
                    'company', 
                    PropMaker.make(PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))),
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_return_info')))
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
                    'If contract terminates, Maimon agrees to return immediately to the Company all written Confidential Information', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_return_info', 'antecedent')]})
            }
        )
    )
)



