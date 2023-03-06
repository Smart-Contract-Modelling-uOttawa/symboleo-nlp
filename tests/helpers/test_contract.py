from app.classes.symboleo_contract import SymboleoContract, ContractSpec, DomainModel
from app.classes.spec.domain_model import Role, DomainEvent, Asset
from app.classes.spec.contract_spec import Obligation, Power
from app.classes.spec.prop_maker import PropMaker

class FakeSym:
    def to_sym(self):
        return ''

def get_test_contract():
    # TODO: Can make this more realistic
    return SymboleoContract(
        
        DomainModel(
            roles = {
                'test_role': Role('test_role')
            },
            events = {
                'test_event': DomainEvent('test_event')
            },
            assets = {
                'test_asset': Asset('test_asset')
            }
        ),
        
        ContractSpec(
            obligations = {
                'test_obligation': Obligation(
                    'test_obligation', 
                    PropMaker.make_default(), 
                    'debtor',
                    'creditor',
                    PropMaker.make_default(),
                    FakeSym()
                )
            },
            powers = {
                'test_power': Power(
                    'test_power', 
                    PropMaker.make_default(),
                    'debtor',
                    'creditor', 
                    PropMaker.make_default(),
                    FakeSym()
                )
            }
        ),
        
        None # Template strings...
    )