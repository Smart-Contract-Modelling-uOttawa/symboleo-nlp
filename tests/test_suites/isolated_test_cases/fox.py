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
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionSHappensBefore

from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.units.all_units import *

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.spec.parameter_config import ParameterConfig

# In no event will Fox develop, publish and/or distribute games derived from the Property "ICE AGE 2" [PARAMETER]
## Original: prior to January 1, 2007
## Mine: prior to January 1, 2007

# TODO: F2 - Need prior to. Change the exp value in nl_tempalte as well
fox_test_case = TestCase(
    'fox',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'fox_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {
            },
            events = {'DistributeGames': DomainEvent('DistributeGames', [
                DomainProp('distributor', 'Role')
            ])},
            enums=[]
        ),
        ContractSpec(
            id = 'fox_cs',
            declarations = {
                'fox': Declaration('fox', 'PartyA', 'roles', []),
                'partyB': Declaration('partyB', 'PartyB', 'roles', []),
                'evt_distribute_games': Declaration('evt_distribute_games', 'DistributeGames', 'events', [
                    DeclarationProp('distributor', 'fox', 'Role')
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_not_distribute_games': Obligation('ob_not_distribute_games', None, 'fox', 'partyB', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_distribute_games')), negation=True)
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
                    'In no event will Fox develop, publish and/or distribute games derived from the Property "ICE AGE 2" [PARAMETER]', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_not_distribute_games', 'consequent')]})
            }
        )
    ),
    op_code = OpCode.UPDATE_PARM,
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.ROOT),
            UserInput(UnitType.BEFORE),
            UserInput(UnitType.DATE, 'January 1, 2007'),
            UserInput(UnitType.FINAL_NODE)
        ],
        nl_key='nl_key',
        parm_key='PARAMETER'
    ),
    exp_sym = SymboleoContract(
        DomainModel(
            id = 'fox_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {
            },
            events = {'DistributeGames': DomainEvent('DistributeGames', [
                DomainProp('distributor', 'Role')
            ])},
            enums=[]
        ),
        ContractSpec(
            id = 'fox_cs',
            declarations = {
                'fox': Declaration('fox', 'PartyA', 'roles', []),
                'partyB': Declaration('partyB', 'PartyB', 'roles', []),
                'evt_distribute_games': Declaration('evt_distribute_games', 'DistributeGames', 'events', [
                    DeclarationProp('distributor', 'fox', 'Role')
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_not_distribute_games': Obligation('ob_not_distribute_games', None, 'fox', 'partyB', PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionSHappensBefore(VariableEvent('evt_distribute_games'), Point(PointVDE('"January 1, 2007"'))), negation=True)
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
                    'In no event will Fox develop, publish and/or distribute games derived from the Property "ICE AGE 2" before January 1, 2007', 
                    {'PARAMETER': [ParameterConfig('obligations', 'ob_not_distribute_games', 'consequent')]})
            }
        )
    )
)



