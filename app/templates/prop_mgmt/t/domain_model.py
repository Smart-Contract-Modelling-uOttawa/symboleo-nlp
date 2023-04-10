from app.classes.symboleo_contract import DomainModel
from app.classes.spec.domain_model import DomainEvent, DomainProp, Role, Asset, DomainEnum

def get_domain_model():
    domain_model = DomainModel(
        'propMgmtDomain',
        roles = {
            'Owner': Role(
                name = 'Owner',
                props = [
                    DomainProp('name','String'),
                ]
            ),
            'Manager': Role(
                name = 'Manager',
                props = [
                    DomainProp('name','String'),
                ]
            )
        },
        enums = [
        ],
        events = {
            'Advertise': DomainEvent(
                name = 'Advertise',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('property', 'Property')
                ]
            ),
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
            'Notify': DomainEvent(
                name = 'Notify',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('target', 'Role'),
                    DomainProp('message', 'String')
                ]
            ),
            'CollectRent': DomainEvent(
                name = 'CollectRent',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('property', 'Property')
                ]
            ),
            'Accounting': DomainEvent(
                name = 'Accounting',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('target', 'Role'),
                    DomainProp('object', 'String')
                ]
            ),
            'Repair': DomainEvent(
                name = 'Repair',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('property', 'Property')
                ]
            ),
            'ProvideInvoice': DomainEvent(
                name = 'ProvideInvoice',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('target', 'Role'),
                    DomainProp('object', 'String')
                ]
            ),
            # 'LegalProceedingsNecessary': DomainEvent(
            #     name = 'LegalProceedingsNecessary',
            #     props = [
            #         DomainProp('property', 'Property')
            #     ]
            # ),
            'HandleLegalProceedings': DomainEvent(
                name = 'HandleLegalProceedings',
                props = [
                    DomainProp('agent', 'Role'),    
                    DomainProp('property', 'Property')
                ]
            ),
            # 'ProvideTerminationNotice': DomainEvent(
            #     name = 'ProvideTerminationNotice',
            #     props = [
            #         DomainProp('agent', 'Role'),
            #         DomainProp('numDays', 'Number')
            #     ]
            # ),
        },
        assets = {
            'Property': Asset(
                name = 'Property',
                props = [
                ]
            )
        }   
    )
    
    # Add aliases

    return domain_model