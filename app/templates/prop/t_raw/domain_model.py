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
        assets = {
            'RentalProperty': Asset(
                name = 'RentalProperty',
                props = [
                    DomainProp('address', 'String')
                ]
            ),
            'LegalProceedings': Asset(name='LegalProceedings', props=[])
        },
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
            'LegalProceedingsNecessary': DomainEvent(
                name = 'LegalProceedingsNecessary',
                props = [
                    DomainProp('necessary_thing', 'LegalProceedings')
                ]
            ),
            'HandleLegalProceedings': DomainEvent(
                name = 'HandleLegalProceedings',
                props = [
                    DomainProp('agent', 'Role'),    
                    DomainProp('handled_object', 'LegalProceedings')
                ]
            )
        } 
    )
    
    # Add aliases

    return domain_model