from app.classes.spec.domain_model import DomainModel
from app.classes.spec.domain_object import DomainEvent, DomainProp, Role, Asset, DomainEnum

def get_domain_model():
    domain_model = DomainModel(
        'meatSaleDomain',
        roles = {
            'Seller': Role(
                name = 'Seller',
                props = []
            ),
            'Buyer': Role(
                name = 'Buyer',
                props = []
            )
        },
        enums = [
            DomainEnum('Currency', ['CAD', 'USD', 'EUR']),
            DomainEnum('MeatQuality', ['PRIME', 'AAA', 'AA', 'A'])
        ],
        events = {
            'Deliver': DomainEvent(
                name = 'Deliver',
                props = [
                    DomainProp('item', 'Meat'),
                    DomainProp('deliverer', 'Role'),
                    DomainProp('recipient', 'Role')
                ]
            ),
            'Pay': DomainEvent(
                name = 'Pay',
                props = [
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency'),
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role')
                ]
            ),
            'PayInterest': DomainEvent(
                name = 'PayInterest',
                props = [
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency'),
                    DomainProp('from', 'Buyer'),
                    DomainProp('to', 'Seller')
                ]
            ),
            'Disclose': DomainEvent(
                name = 'Disclose',
                props = []
            )
        },
        assets = {
            'PerishableGood': Asset(
                name = 'PerishableGood',
                props = [
                    DomainProp('quantity_kg', 'Number')
                ]
            )
        }   
    )
        
    # # Add aliases
    perishableGood = domain_model.assets['PerishableGood']
    domain_model.assets['Meat'] = Asset(
        'Meat', 
        [
            DomainProp('quality', 'MeatQuality')
        ], 
        perishableGood
    )

    return domain_model