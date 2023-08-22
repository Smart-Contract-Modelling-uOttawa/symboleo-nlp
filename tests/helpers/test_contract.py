from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.domain_model import DomainModel, DomainEnum
from app.classes.spec.declaration import Declaration, EventDeclaration, RoleDeclaration, AssetDeclaration, DeclarationProp
from app.classes.spec.domain_object import Role, DomainEvent, Asset, DomainProp
from app.classes.spec.norm import Obligation, Power, SurvivingObligation
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.nl_template import NLTemplate, TemplateObj, ParameterConfig

from tests.helpers.test_objects import CustomEvents

class FakeSym:
    def to_sym(self):
        return ''

def get_test_contract_for_assets():
    return SymboleoContract(
            domain_model = DomainModel(
                'test',
                roles={},
                events={},
                assets={},
                enums=[
                    DomainEnum('Currency', ['CAD', 'USD'])
                ] ),
            contract_spec=ContractSpec(
                'test',
                parameters=[],
                declarations = {
                    'buyer': Declaration('buyer', 'Buyer', 'roles', []),
                    'renter': Declaration('renter', 'Renter', 'roles', []),
                    'Dolphin': Declaration('Dolphin', 'Contractor', 'roles', []),
                    'client': Declaration('client', 'Client', 'roles', []),
                    'contractor': Declaration('contractor', 'Contractor', 'roles', []),

                    'BOSCH': Declaration('BOSCH', 'Company', 'roles', []),
                    'CLIENT': Declaration('CLIENT', 'Client', 'roles', []),

                    'property': Declaration('property', 'RentalProperty', 'assets', []),
                    'services': Declaration('services', 'Services', 'assets', []),
                },
                obligations={},
                powers={}
            ),
            nl_template=None
        )


def get_test_contract():
    dm = DomainModel(
        id = 'test',
        roles = {
            'TestRole': Role('TestRole', [
                DomainProp('name', 'String')
            ])
        },
        enums = [
            DomainEnum('Currency', ['CAD', 'USD'])
        ],
        events = {
            'TestEvent': DomainEvent('TestEvent', []),
        },
        assets = {
            'TestAsset': Asset('TestAsset', [])
        },
    )
    p_asset = dm.assets['TestAsset']
    dm.assets['SubAsset'] = Asset('SubAsset', [], p_asset)

    return SymboleoContract(
        domain_model = dm,
        contract_spec = ContractSpec(
            id = 'test',
            obligations = {
                'test_obligation': Obligation(
                    'test_obligation', 
                    PropMaker.make_default(), 
                    'debtor',
                    'creditor',
                    PropMaker.make_default(),
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('test_event')))
                ),
                
            },
            surviving_obligations={
                'test_so': SurvivingObligation(
                    'test_so', 
                    PropMaker.make_default(), 
                    'debtor',
                    'creditor',
                    PropMaker.make_default(),
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('test_event')))
                ),
            },
            powers = {
                'test_power': Power(
                    'test_power', 
                    PropMaker.make_default(),
                    'debtor',
                    'creditor', 
                    PropMaker.make_default(),
                    PropMaker.make(PredicateFunctionHappens(VariableEvent('event_y')))
                )
            },
            declarations={
                'test_event': EventDeclaration('test_event', 'TestEvent', []),
                'test_asset': AssetDeclaration('test_asset', 'TestAsset', []),
                'test_role': RoleDeclaration('test_role', 'TestRole', [
                    DeclarationProp('name', 'test', 'String')
                ]),
            },
            parameters=[
                ContractSpecParameter('x', 'String')
            ],
            preconditions=[],
            postconditions=[],
            constraints=[],
        ),
        nl_template = NLTemplate({
            'test_nl_key': TemplateObj(
                str_val = 'Event X happens [P1]', 
                parameters = {
                    'P1': [
                        ParameterConfig('obligations', 'test_obligation', 'consequent')
                    ]
            })
        })
    )