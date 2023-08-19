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
            )
        },
        enums=[],
                assets = {
            'Services': Asset(
                name = 'Services',
                props = []
            ),
            'Invoice': Asset(
                name = 'Invoice',
                props = []
            ),
            'Expenses': Asset(
                name = 'Expenses',
                props = []
            )
        },
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
                    DomainProp('completing_agent', 'Role'),
                    DomainProp('completed_object', 'Services')
                ]
            ),
            'SendInvoice': DomainEvent(
                name = 'SendInvoice',
                props = [
                    DomainProp('sending_agent', 'Role'),
                    DomainProp('sent_object', 'Invoice')
                ]
            ),
            'PayInvoice': DomainEvent(
                name = 'PayInvoice',
                props = [
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role'),
                    DomainProp('invoice', 'Invoice')
                ]
            ),
            'PayProRata': DomainEvent(
                name = 'PayProRata',
                props = [
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role')
                ]
            ),
            # 'BreachContract': DomainEvent(
            #     name = 'BreachContract',
            #     props = [
            #         DomainProp('agent', 'Role')
            #     ]
            # ),
            'ReimburseExpenses': DomainEvent(
                name = 'ReimburseExpenses',
                props = [
                    DomainProp('to', 'Role'),
                    DomainProp('from', 'Role'),
                    DomainProp('expenses', 'Expenses'),
                ]
            ),
            'Disclose': DomainEvent(
                name = 'Disclose',
                props = [
                    DomainProp('agent', 'Role')
                ]
            ),
            # 'AuthorizeDisclosure': DomainEvent(
            #     name = 'AuthorizeDisclosure',
            #     props = [
            #         DomainProp('agent', 'Role')
            #     ]
            # ),
        }  
    )
    
    # Add aliases

    return domain_model