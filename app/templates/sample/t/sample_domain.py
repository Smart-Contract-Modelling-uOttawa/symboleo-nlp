from app.classes.spec.symboleo_contract import DomainModel
from app.classes.spec.domain_object import DomainEvent, DomainProp, Role, Asset, DomainEnum

def get_domain_model():
    domain_model = DomainModel(
        'meatSaleDomain',
        roles = {
            'Seller': Role(
                name = 'Seller',
                props = [
                    DomainProp('returnAddress', 'String'),
                    DomainProp('name', 'String'),
                ]
            ),
            'Buyer': Role(
                name = 'Buyer',
                props = [
                    DomainProp('warehouse', 'String')
                ]
            )
        },
        enums = [
            DomainEnum('Currency', ['CAD', 'USD', 'EUR']),
            DomainEnum('MeatQuality', ['PRIME', 'AAA', 'AA', 'A'])
        ],
        events = {
            'Delivered': DomainEvent(
                name = 'Delivered',
                props = [
                    DomainProp('item', 'Meat'),
                    DomainProp('deliveryAddress', 'String'),
                    DomainProp('delDueDate', 'Date')
                ]
            ),
            'Paid': DomainEvent(
                name = 'Paid',
                props = [
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency'),
                    DomainProp('from', 'Buyer'),
                    DomainProp('to', 'Seller'),
                    DomainProp('payDueDate', 'Date')
                ]
            ),
            'PaidLate': DomainEvent(
                name = 'PaidLate',
                props = [
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency'),
                    DomainProp('from', 'Buyer'),
                    DomainProp('to', 'Seller')
                ]
            ),
            'Disclosed': DomainEvent(
                name = 'Disclosed',
                props = []
            )
        },
        assets = {
            'PerishableGood': Asset(
                name = 'PerishableGood',
                props = [
                    DomainProp('quantity', 'Number'),
                    DomainProp('quality', 'MeatQuality')
                ]
            )
        }   
    )
    
    # Add aliases
    perishableGood = domain_model.assets['PerishableGood']
    domain_model.assets['Meat'] = Asset('Meat', [], perishableGood)

    return domain_model