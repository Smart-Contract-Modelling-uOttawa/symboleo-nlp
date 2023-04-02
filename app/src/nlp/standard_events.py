from typing import Dict
from app.classes.spec.domain_model import DomainEvent, DomainProp

class StandardEvent: 
    def __init__(self, domain_event:DomainEvent, description:str):
        self.domain_event = domain_event
        self.description = description


standard_event_dict: Dict[str, StandardEvent] = {
    'breach_agreement': StandardEvent(
        DomainEvent('BreachAgreement', [
            DomainProp('breacher', 'Role')
        ]),
        'Event when one party (breacher) fails to complete any obligation.'
    ),

    'provide_termination_notice': StandardEvent(
        DomainEvent('ProvideTerminationNotice', [
            DomainProp('agent', 'Role'),
            DomainProp('daysInAdvance', 'Number')
        ]),
        'One party (agent) provides notice a certain number of days in advance to terminate a contract'
    )
    
}
