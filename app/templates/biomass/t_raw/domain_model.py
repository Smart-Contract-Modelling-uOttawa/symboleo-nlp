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
            'LegalThirdParty': Role(
                name = 'ThirdParty',
                props = [
                    DomainProp('name','String'),
                ]
            )
        },
        assets = {
            'Biomass': Asset(
                name = 'Biomass',
                props = [
                    DomainProp('quantity_lbs', 'Number'),
                    #DomainProp('cannabidiol_percent', 'Number'),
                    #DomainProp('thc_percent', 'Number'),
                    # Contaminants...?
                ]
            ),
            'Location': Asset(
                name = 'Location',
                props = [
                    DomainProp('name', 'String')
                ]
            )
        },
        enums = [
            DomainEnum('Currency', ['CAD', 'USD']),
        ],
        events = {
            'Pay': DomainEvent(
                name = 'Pay',
                props = [
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency')
                ]
            ),
            'Quarantine': DomainEvent(
                name = 'Quarantine',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('product', 'Biomass')
                ]
            ),
            'RemoveQuarantine': DomainEvent(
                name = 'RemoveQuarantine',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('product', 'Biomass')
                ]
            ),
            'DeterminesAnalysisRequired': DomainEvent(
                name = 'DeterminesAnalysisRequired',
                props = [
                    DomainProp('agent', 'Role'),
                ]
            ),
            'Delivery': DomainEvent(
                name = 'Delivery',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('product', 'Biomass'),
                    DomainProp('location', 'Location'),
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
                    DomainProp('target', 'Role')
                ]
            ),
            'ReturnInfo': DomainEvent(
                name = 'ReturnInfo',
                props = [
                    DomainProp('agent', 'Role')
                ]
            ),
            'DiscloseInfo': DomainEvent(
                name = 'DiscloseInfo',
                props = [
                    DomainProp('agent', 'Role')
                ]
            )
        }
    )
    
    # Add aliases

    return domain_model