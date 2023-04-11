from app.classes.spec.symboleo_contract import DomainModel
from app.classes.spec.domain_object import DomainEvent, DomainProp, Role, Asset, DomainEnum

def get_domain_model():
    domain_model = DomainModel(
        'propertyRentalDomain',
        roles = {
            'Landlord': Role(
                name = 'Landlord',
                props = [
                    DomainProp('name', 'String'),
                ]
            ),
            'Renter': Role(
                name = 'Renter',
                props = [
                    DomainProp('name', 'String')
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
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency'),
                    DomainProp('paymentMethod', 'PaymentMethod'),
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                ]
            ),
            'Occupy': DomainEvent(
                name = 'Occupy',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('property', 'RentalProperty')
                ]
            ),
            'ProvideTerminationNotice': DomainEvent(
                name = 'ProvideTerminationNotice',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('daysInAdvance', 'Number')
                ]
            ),
            'Abandon': DomainEvent(
                name = 'Abandon',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('property', 'RentalProperty')
                ]
            ),
            'KeepPets': DomainEvent(
                name = 'KeepPets',
                props = [
                    DomainProp('agent', 'Role')
                ]
            ),
            'AllowPets': DomainEvent(
                name = 'AllowPets',
                props = [
                    DomainProp('grantor', 'Role')
                ]
            ),
            # Placeholder until I figure out frequency...
            'DatePasses': DomainEvent(
                name = 'DatePasses',
                props = [
                    DomainProp('date', 'Date')
                ]
            )
        },
        assets = {
            'RentalProperty': Asset(
                name = 'RentalProperty',
                props = [
                    DomainProp('address', 'String')
                ]
            )
        }   
    )
    
    # Add aliases
    # ...

    return domain_model