from app.classes.spec.domain_model import DomainModel
from app.classes.spec.domain_object import DomainEvent, DomainProp, Role, Asset, DomainEnum

def get_domain_model():
    domain_model = DomainModel(
        'transactiveEnergyDomain',
        roles = {
            'Prosumer': Role(
                name = 'Prosumer',
                props = []
            ),
            'Buyer': Role(
                name = 'Buyer',
                props = []
            )
        },
        enums = [
            DomainEnum('Currency', ['CAD', 'USD', 'EUR'])
        ],
        events = {
            'DispatchEnergy': DomainEvent(
                name = 'DispatchEnergy',
                props = [
                    DomainProp('energy', 'Energy'),
                    DomainProp('dispatcher', 'Role'),
                    DomainProp('recipient', 'Role'),
                    DomainProp('voltage', 'Number')
                ]
            ),
            'Pay': DomainEvent(
                name = 'Pay',
                props = [
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency'),
                    DomainProp('from', 'Role'),
                    DomainProp('to', 'Role')
                ]
            ),
            'PayInterest': DomainEvent(
                name = 'PayInterest',
                props = [
                    DomainProp('amount', 'Number'),
                    DomainProp('currency', 'Currency'),
                    DomainProp('from', 'Buyer'),
                    DomainProp('to', 'Prosumer')
                ]
            )
        },
        assets = {
            'Energy': Asset(
                name = 'Energy',
                props = [
                    DomainProp('amount_kw', 'Number'),
                ]
            )
        }   
    )

    return domain_model