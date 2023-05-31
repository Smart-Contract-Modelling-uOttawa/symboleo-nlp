from app.classes.spec.symboleo_contract import DomainModel
from app.classes.spec.domain_object import DomainEvent, DomainProp, Role, Asset

def get_domain_model():
    domain_model = DomainModel(
        'IndependentContractorDomain',
        roles = {
            'Client': Role(
                name = 'Client',
                props = []
            ),
            'Contractor': Role(
                name = 'Contractor',
                props = []
            ),
            'Subcontractor': Role(
                name = 'Subcontractor',
                props = []
            )
        },
        enums=[],
        events = {
            'StartServices': DomainEvent(
                name = 'StartServices',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('services', 'Services')
                ]
            ),
            'CompleteServices': DomainEvent(
                name = 'CompleteServices',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('services', 'Services')
                ]
            ),
            'Invoice': DomainEvent(
                name = 'Invoice',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('target', 'Role')
                ]
            ),
            'Pay': DomainEvent(
                name = 'Pay',
                props = [
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                    DomainProp('payment', 'String')
                ]
            ),
            'Disclose': DomainEvent(
                name = 'Disclose',
                props = [
                    DomainProp('agent', 'Role')
                ]
            ),
            'AuthorizeDisclosure': DomainEvent(
                name = 'AuthorizeDisclosure',
                props = [
                    DomainProp('agent', 'Role')
                ]
            ),
            'Breach': DomainEvent(
                name = 'Breach',
                props = [
                    DomainProp('agent', 'Role')
                ]
            ),
            'HireSubcontractor': DomainEvent(
                name = 'HireSubcontractor',
                props = [
                    DomainProp('agent', 'Role'),
                    DomainProp('subcontractor', 'Role')
                ]
            )
        },
        assets = {
            'Services': Asset(
                name = 'Services',
                props = []
            )
        }   
    )
    
    # Add aliases

    return domain_model