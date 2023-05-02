from app.classes.spec.symboleo_contract import DomainModel
from app.classes.spec.domain_object import DomainEvent, DomainProp, Role, Asset, DomainEnum

def get_domain_model():
    domain_model = DomainModel(
        'gridironDomain',
        roles = {
            'Seller': Role(
                name = 'Seller',
                props = [
                    DomainProp('name','String'),
                ]
            ),
            'Buyer': Role(
                name = 'Buyer',
                props = [
                    DomainProp('name','String'),
                ]
            ),
            'ThirdParty': Role(
                name = 'ThirdParty',
                props = [
                    DomainProp('name','String'),
                ]
            )
        },
        enums = [
        ],
        events = {
            'Payment': DomainEvent(
                name = 'Payment',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('receiver', 'Role'),
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency')

                ]
            ),
            'Quarantine': DomainEvent(
                name = 'Quarantine',
                props = [
                    DomainProp('product', 'Biomass')
                ]
            ),
            # This one is the challenge:  determines that third party analysis of the Biomass is required for processing
            # Can we reference another event?? 
            # Or maybe add generic relative clause... as following a certain type of verb
            'DeterminesAnalysis': DomainEvent(
                name = 'DeterminesAnalysis',
                props = [
                    DomainProp('agent', 'Role'),
                ]
            ),
            'Delivery': DomainEvent(
                name = 'Delivery',
                props = [
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                    DomainProp('product', 'Biomass'),
                    DomainProp('location', 'String'),
                ]
            ),
            'LegalClaim': DomainEvent(
                name = 'LegalClaim',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('target', 'Role')
                ]
            ),
            'LegalNotice': DomainEvent(
                name = 'LegalNotice',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('receiver', 'Role')
                ]
            ),
            'ReturnInfo': DomainEvent(
                name = 'ReturnInfo',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('receiver', 'Role')
                ]
            ),
            'DiscloseInfo': DomainEvent(
                name = 'DiscloseInfo',
                props = [
                    DomainProp('agent', 'Role')
                ]
            )
        },
        assets = {
            'Biomass': Asset(
                name = 'Biomass',
                props = [
                    DomainProp('quantity', 'Number'),
                    DomainProp('cannabidiol_percent', 'Number'),
                    DomainProp('thc_percent', 'Number'),
                    # Contaminants...?
                ]
            )
        }   
    )
    
    # Add aliases

    return domain_model