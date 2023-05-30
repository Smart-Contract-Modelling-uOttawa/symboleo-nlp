from app.classes.spec.symboleo_contract import DomainModel
from app.classes.spec.domain_object import DomainEvent, DomainProp, Role, Asset

def get_domain_model():
    domain_model = DomainModel(
        'propMgmtDomain',
        roles = {
            'Owner': Role(
                name = 'Owner',
                props = []
            ),
            'Manager': Role(
                name = 'Manager',
                props = []
            )
        },
        enums=[],
        events = {
            'Disburse': DomainEvent(
                name = 'Disburse',
                props = [
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                    DomainProp('amount', 'String')
                ]
            ),
            'Reimburse': DomainEvent(
                name = 'Reimburse',
                props = [
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                    DomainProp('amount', 'String')
                ]
            ),
            'HandleLegalProceedings': DomainEvent(
                name = 'HandleLegalProceedings',
                props = [
                    DomainProp('agent', 'Role'),    
                    DomainProp('property', 'RentalProperty')
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

    return domain_model