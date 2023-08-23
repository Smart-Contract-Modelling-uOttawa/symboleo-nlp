from typing import List
from tests.full_tests.isolated_test_cases.TestSymboleoContract import TestInfo, TestCase

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

# Display materials from the sponsor must be delivered to the Tian-He stadium at least two days prior to the event.
# Display materials from the sponsor must be delivered to the Tian-He stadium [P1]
## Original: at least two days prior to the event.
## CNL: 2 days prior to the event happening
## TIMESPAN P_BEFORE_T EVENT => WHappensBefore

test_case = TestCase(
    'timespan_before_event',
    init_sym = SymboleoContract(
        DomainModel(
            id = 'test_dm',
            roles = {
                'PartyA': Role('PartyA', []),
                'PartyB': Role('PartyB', [])
            },
            assets = {},
            events = {'DeliverMaterials': DomainEvent('DeliverMaterials', [])},
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'stadium': RoleDeclaration('Stadium', 'PartyA', id='stadium'),
                'sponsor': RoleDeclaration('Sponsor', 'PartyB', id='sponsor'),
                'evt_deliver_materials': EventDeclaration('evt_deliver_materials', 'DeliverMaterials', [])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_deliver_materials': Obligation(
                    'ob_deliver_materials', 
                    None, 
                    'sponsor', 
                    'stadium', 
                    PropMaker.make_default(), 
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_deliver_materials')))
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
                    'Display materials from the sponsor must be delivered to the Tian-He stadium [P1]', 
                    {'P1': [ParameterConfig('obligations', 'ob_deliver_materials', 'consequent')]})
            }
        )
    ),

    op_code = OpCode.UPDATE_PARM,
    
    update_config = UpdateConfig(
        user_inputs = [
            UserInput(UnitType.AT_LEAST, 'at least'),
            UserInput(UnitType.TIMESPAN),
            UserInput(UnitType.TIME_VALUE, '2'),
            UserInput(UnitType.TIME_UNIT, 'days'),
            UserInput(UnitType.PRIOR_TO, 'prior to'),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'the party'),
            UserInput(UnitType.INTRANSITIVE_VERB, 'happening'),
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
                'Party': Asset('Party', []),
            },
            events = {
                'DeliverMaterials': DomainEvent('DeliverMaterials', []),
                'PartyHappen': DomainEvent('PartyHappen', [
                    DomainProp('happening_subject', 'Party')
                ])
            },
            enums=[]
        ),
        ContractSpec(
            id = 'test_cs',
            declarations = {
                'stadium': RoleDeclaration('Stadium', 'PartyA', id='stadium'),
                'sponsor': RoleDeclaration('Sponsor', 'PartyB', id='sponsor'),
                'party': AssetDeclaration('party', 'Party', []),
                'evt_deliver_materials': EventDeclaration('evt_deliver_materials', 'DeliverMaterials', []),
                'evt_party_happen': EventDeclaration('evt_party_happen', 'PartyHappen', [
                    DeclarationProp('happening_subject', 'party', 'Party')
                ])
            },
            preconditions=[],
            postconditions=[],
            obligations = {
                'ob_deliver_materials': Obligation(
                    'ob_deliver_materials', 
                    None, 
                    'sponsor', 
                    'stadium', 
                    PropMaker.make_default(), 
                    PropMaker.make(
                        PredicateFunctionWHappensBefore(
                            VariableEvent('evt_deliver_materials'),
                            Point(PointFunction(PointVDE('evt_party_happen'), '-2', TimeUnit.Days))
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
                    'Display materials from the sponsor must be delivered to the Tian-He stadium at least 2 days prior to the party happening', 
                    {'P1': [ParameterConfig('obligations', 'ob_deliver_materials', 'consequent')]})
            }
        )
    ),
)



