from app.classes.symboleo_contract import DomainModel
from app.classes.spec.domain_model import DomainEvent, DomainProp, Role, Asset, DomainEnum

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
            'KeepPets': DomainEvent(
                name = 'KeepPets',
                props = [
                    DomainProp('agent', 'Role')
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
    
    # Add aliases...

    return domain_model