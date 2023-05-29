from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.domain_model import DomainModel, DomainEnum
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import Role, DomainEvent, Asset
from app.classes.spec.norm import Obligation, Power
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.nl_template import NLTemplate

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
                    'property': Declaration('property', 'Property', 'assets', []),
                },
                obligations={},
                powers={}
            ),
            nl_template=None
        )


def get_test_contract():
    # TODO: Can make this more realistic
    return SymboleoContract(
        
        DomainModel(
            id = 'test',
            roles = {
                'test_role': Role('test_role', [])
            },
            enums = {},
            events = {
                'test_event': DomainEvent('test_event', [])
            },
            assets = {
                'test_asset': Asset('test_asset', [])
            },
        ),
        
        ContractSpec(
            id = 'test',
            obligations = {
                'test_obligation': Obligation(
                    'test_obligation', 
                    PropMaker.make_default(), 
                    'debtor',
                    'creditor',
                    PropMaker.make_default(),
                    PropMaker.make(PredicateFunctionHappens('event_x'))
                ),
                
            },
            powers = {
                'test_power': Power(
                    'test_power', 
                    PropMaker.make_default(),
                    'debtor',
                    'creditor', 
                    PropMaker.make_default(),
                    PropMaker.make(PredicateFunctionHappens('event_y'))
                )
            },
            declarations={},
            preconditions=[],
            postconditions=[],
            surviving_obligations={},
            constraints=[],
            parameters=[]
        ),
        nl_template = NLTemplate({})
    )