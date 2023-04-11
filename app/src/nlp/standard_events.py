from typing import Dict
from app.classes.spec.domain_object import DomainEvent, DomainProp

class StandardEvent: 
    def __init__(self, domain_event:DomainEvent, description:str):
        self.domain_event = domain_event
        self.description = description


# To build up this list, should do a verb search on the cuad set to find the most common verbs
standard_event_dict: Dict[str, StandardEvent] = {
    'breach_agreement': StandardEvent(
        DomainEvent('BreachAgreement', [
            DomainProp('breacher', 'Role')
        ]),
        'Event when one party (breacher) fails to complete any obligation.'
    ),

    # TODO: args should use a timespan: time_unit and time_value
    'provide_termination_notice': StandardEvent(
        DomainEvent('ProvideTerminationNotice', [
            DomainProp('agent', 'Role'),
            DomainProp('daysInAdvance', 'Number')
        ]),
        'One party (agent) provides notice a certain number of days in advance to terminate a contract'
    )
    
}
