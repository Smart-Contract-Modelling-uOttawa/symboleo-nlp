from app.classes.symboleo_contract import DomainModel
from app.classes.spec.domain_model import DomainEvent, DomainProp, Role, Asset, DomainEnum

def get_domain_model():
    domain_model = DomainModel(
        'propertyRentalDomain',
        roles = {
            'Landlord': Role(
                name = 'Landlord',
                props = [
                    DomainProp('name', '', 'String'),
                ]
            ),
            'Renter': Role(
                name = 'Renter',
                props = [
                    DomainProp('name', '', 'String')
                ]
            )
        },
        enums = [
            DomainEnum('Currency', ['CAD', 'USD', 'EUR']),
            DomainEnum('PaymentMethod', ['Cash', 'Cheque', 'ETransfer'])
        ],

        events = {
            'Paid': DomainEvent(
                name = 'Paid',
                props = [
                    DomainProp('amount', '', 'Number'),
                    DomainProp('currency', '', 'Currency'),
                    DomainProp('paymentMethod', '', 'PaymentMethod'),
                    DomainProp('from', '', 'Role'),
                    DomainProp('to', '', 'Role'),
                ]
            ),
            'TakeOccupancy': DomainEvent(
                name = 'TakeOccupancy',
                props = [
                    DomainProp('agent', '', 'Role')
                ]
            ),
            'BreachAgreement': DomainEvent(
                name = 'BreachAgreement',
                props = [
                    DomainProp('agent', '', 'Role')
                ]
            ),
            'ProvideWrittenNotice': DomainEvent(
                name = 'ProvideWrittenNotice',
                props = [
                    DomainProp('agent', '', 'Role'),
                    DomainProp('daysInAdvance', '', 'Number')
                ]
            ),
            'Abandons': DomainEvent(
                name = 'Abandons',
                props = [
                    DomainProp('agent', '', 'Role'),
                    DomainProp('property', '', 'Property')
                ]
            ),
            'Enters': DomainEvent(
                name = 'Enters',
                props = [
                    DomainProp('agent', '', 'Role'),
                    DomainProp('property', '', 'Property')
                ]
            ),
            'KeepPets': DomainEvent(
                name = 'KeepPets',
                props = [
                    DomainProp('agent', '', 'Role')
                ]
            ),
            'ProvidePetPermission': DomainEvent(
                name = 'ProvidePetPermission',
                props = [
                    DomainProp('grantor', '', 'Role')
                ]
            )
        },
        assets = {
            'RentalProperty': Asset(
                name = 'RentalProperty',
                props = [
                    DomainProp('address', '', 'String')
                ]
            )
        }   
    )
    
    # Add aliases
    # perishableGood = domain_model.assets['PerishableGood']
    # domain_model.assets['Meat'] = Asset('Meat', [], perishableGood)

    return domain_model