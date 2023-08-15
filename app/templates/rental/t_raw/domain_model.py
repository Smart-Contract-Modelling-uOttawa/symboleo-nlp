from app.classes.spec.symboleo_contract import DomainModel
from app.classes.spec.domain_object import DomainEvent, DomainProp, Role, Asset, DomainEnum

def get_domain_model():
    domain_model = DomainModel(
        'rentalDomain',
        roles = {
            'Landlord': Role(
                name = 'Landlord',
                props = []
            ),
            'Renter': Role(
                name = 'Renter',
                props = []
            )
        },
        enums = [
            DomainEnum('Currency', ['CAD', 'USD', 'EUR'])
        ],

        events = {
            'PayDeposit': DomainEvent(
                name = 'PayDeposit',
                props = [
                    DomainProp('deposit', 'SecurityDeposit'),
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                ]
            ),
            'PayAmount': DomainEvent(
                name = 'PayAmount',
                props = [
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency'),
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                ]
            ),
            'OccupyProperty': DomainEvent(
                name = 'OccupyProperty',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('property', 'RentalProperty')
                ]
            ),
            'KeepPet': DomainEvent(
                name = 'KeepPet',
                props = [
                    DomainProp('agent', 'Role')
                ]
            ),
            'AllowPets': DomainEvent(
                name = 'AllowPets',
                props = [
                    DomainProp('grantor', 'Role')
                ]
            )
        },
        assets = {
            'RentalProperty': Asset(
                name = 'RentalProperty',
                props = [
                    DomainProp('address', 'String')
                ]
            ),
            'SecurityDeposit': Asset(
                name = 'SecurityDeposit',
                props = [
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency')
                ]
            ),
        }   
    )
    
    # Add aliases
    # ...

    return domain_model